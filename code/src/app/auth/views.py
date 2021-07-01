# Application Autorization system --------------------------------------
# GLVH @ Emtec Group 
# (c) 2018,2019,2020,2021
# 
# 2021-05-02 GLVH refactoring to improve error handling
# ----------------------------------------------------------------------
# Flask Application basic methods    
from flask                              import render_template
from flask                              import redirect
from flask                              import request
from flask                              import url_for
from flask                              import flash

# Authorization sub-system
from .                                  import auth
from ..decorators                       import admin_required
from ..decorators                       import permission_required
from flask_login                        import login_user
from flask_login                        import logout_user
from flask_login                        import login_required
from flask_login                        import current_user

# Application context
#from ..                                 import app
from ..                                 import db
from ..                                 import logger

# Actual Application model
from emtec.collector.db.flask_models    import User

# Interface
from .forms                             import LoginForm
from .forms                             import ChangePasswordForm
from .forms                             import ChangeEmailForm
from .forms                             import RegistrationForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    try:
        logger.debug(f"login: login in course ... viene mas data")
        logger.debug(f"login: User       = {User}")
        logger.debug(f"login: logger     = {logger}")
        logger.debug(f"login: db         = {db}")
        logger.debug(f"login: db.engine  = {db.engine}")
        logger.debug(f"login: db.Session = {db.Session}")
        logger.debug(f"login: db.session = {db.session}")
        # Required to be sure DB connection is Up
        # if not, further request will be reconnected
        try:
            logger.debug(f"login: asuring DB connection is UP ..")
            result = db.engine.execute('SELECT 1')
            for row in result:
                logger.debug(f"login: row = {row}")
        except Exception as e:
            logger.error(f"login: DB connection test exception: {str(e)}")
    except Exception as e:
        print(f"login: exception: {str(e)}")
        print(f"login: logger is not available")
    try:
        form = LoginForm()
        if form.validate_on_submit():
            try:
                logger.debug(f"login: form.validate_on_submit() = True")
                user = User.query.filter_by(username=form.username.data).first()
                #rint(f"login: {user}")
                logger.debug(f"login: {user}")
                if user is not None and user.verify_password(form.password.data):
                    login_user(user, False)
                    #rint(       f"login: 69: request.args.get('next') = {request.args.get('next')}")
                    logger.debug(f"login: 70: request.args.get('next') = {request.args.get('next')}")
                    #rint(       f"login: 71: url_for('main.index')    =",url_for('main.index'))
                    logger.debug(f"login: 72: url_for('main.index')    = {url_for('main.index')}")
                    return redirect(request.args.get('next') or url_for('main.index'))
                else:
                    logger.error(f"login: user = {user}")
                    if user is not None:
                        logger.error(f"login: user.verify_password() = {user.verify_password}")
                print('Invalid username or password.')
                flash('Invalid username or password.')
            except Exception as e:
                print       ( f"login: form validated exception: {str(e)}")
                logger.error( f"login: form validated exception: {str(e)}")
        else:
            #rint(       "login: FORM NOT VALIDATED YET")        
            logger.debug("login: FORM NOT VALIDATED YET")
        try:
            return render_template('auth/login.html', form=form)
        except Exception as e:
            print       ( f"login: render exception: {str(e)}")
            logger.error( f"login: render exception: {str(e)}")
    except Exception as e:
        print       ( f"login: main exception: {str(e)}")
        logger.error( f"login: main exception: {str(e)}")
    return redirect(url_for('main.index'))

@auth.route('/logout')
@login_required
def logout():
    try:
        #rint       ( f"logout: loging out user {current_user} ...")
        logger.debug( f"logout: loging out user {current_user} ...")
        logout_user()
        #rint('You have been logged out.')
        flash('You have been logged out.')
    except Exception as e:
        print       ( f"logout: exception: {str(e)}")
        logger.error( f"logout: exception: {str(e)}")
    return redirect(url_for('main.index'))
    
    
# Only Administrator can register users, include decorator here
@auth.route('/register', methods=['GET', 'POST'])
@login_required
@admin_required
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        #user = User(email=form.email.data,
        #username=form.username.data,
        
        #print("******** role_id = %s *** type=%s ********"%(form.role_id.data,type(form.role_id.data)))
        
        
        user = User(username=form.username.data,
            role_id=form.role_id.data,
            email=form.email.data,
            password=form.password.data)
        try:
            #flash("Trying to register user: '%s'"%user)
            #20210630 GV db.session. close()
            db.session.add(user)
            db.session.commit()
            #20210630 GV db.session. close()
            db.session.flush() #20210630 GV 
            flash('New user "%s" can login now.'%form.username.data)
            return redirect(url_for('main.index'))
        except Exception as e:
            db.session.rollback()
            #20210630 GV db.session. close()
            db.session.flush() #20210630 GV 
            flash('Form Data is: [name=%s,role_id=%s,email=%s,password=%s]'%( form.username.data, form.role_id.data, form.email.data, form.password.data))
            flash('Error creating new user. %s'%(e))
            return redirect(url_for('auth.register'))
            
    return render_template('auth/register.html', form=form)
    
  
@auth.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.old_password.data):
            current_user.password = form.password.data
            db.session.add(current_user)
            flash('Your password has been updated.')
            return redirect(url_for('main.index'))
        else:
            flash('Invalid password.')
    return render_template("auth/change_password.html", form=form)

@auth.route('/change-email', methods=['GET', 'POST'])
@login_required
@admin_required
def change_email_request():
    form = ChangeEmailForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.password.data):
            new_email = form.email.data
            token = current_user.generate_email_change_token(new_email)
            send_email(new_email, 'Confirm your email address',
                       'auth/email/change_email',
                       user=current_user, token=token)
            flash('An email with instructions to confirm your new email '
                  'address has been sent to you.')
            return redirect(url_for('main.index'))
        else:
            flash('Invalid email or password.')
    return render_template("auth/change_email.html", form=form)

    
"""    
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, \
    current_user
from . import auth
from .. import db
from ..models import User
from ..email import send_email
from .forms import LoginForm, RegistrationForm, ChangePasswordForm,\
    PasswordResetRequestForm, PasswordResetForm, ChangeEmailForm


@auth.before_app_request
def before_request():
    if current_user.is_authenticated \
            and not current_user.confirmed \
            and request.endpoint \
            and request.endpoint[:5] != 'auth.' \
            and request.endpoint != 'static':
        return redirect(url_for('auth.unconfirmed'))


@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_email(user.email, 'Confirm Your Account',
                   'auth/email/confirm', user=user, token=token)
        flash('A confirmation email has been sent to you by email.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        flash('You have confirmed your account. Thanks!')
    else:
        flash('The confirmation link is invalid or has expired.')
    return redirect(url_for('main.index'))


@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(current_user.email, 'Confirm Your Account',
               'auth/email/confirm', user=current_user, token=token)
    flash('A new confirmation email has been sent to you by email.')
    return redirect(url_for('main.index'))


@auth.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.old_password.data):
            current_user.password = form.password.data
            db.session.add(current_user)
            flash('Your password has been updated.')
            return redirect(url_for('main.index'))
        else:
            flash('Invalid password.')
    return render_template("auth/change_password.html", form=form)


@auth.route('/reset', methods=['GET', 'POST'])
def password_reset_request():
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))
    form = PasswordResetRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            token = user.generate_reset_token()
            send_email(user.email, 'Reset Your Password',
                       'auth/email/reset_password',
                       user=user, token=token,
                       next=request.args.get('next'))
        flash('An email with instructions to reset your password has been '
              'sent to you.')
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password.html', form=form)


@auth.route('/reset/<token>', methods=['GET', 'POST'])
def password_reset(token):
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))
    form = PasswordResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            return redirect(url_for('main.index'))
        if user.reset_password(token, form.password.data):
            flash('Your password has been updated.')
            return redirect(url_for('auth.login'))
        else:
            return redirect(url_for('main.index'))
    return render_template('auth/reset_password.html', form=form)


@auth.route('/change-email', methods=['GET', 'POST'])
@login_required
def change_email_request():
    form = ChangeEmailForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.password.data):
            new_email = form.email.data
            token = current_user.generate_email_change_token(new_email)
            send_email(new_email, 'Confirm your email address',
                       'auth/email/change_email',
                       user=current_user, token=token)
            flash('An email with instructions to confirm your new email '
                  'address has been sent to you.')
            return redirect(url_for('main.index'))
        else:
            flash('Invalid email or password.')
    return render_template("auth/change_email.html", form=form)


@auth.route('/change-email/<token>')
@login_required
def change_email(token):
    if current_user.change_email(token):
        flash('Your email address has been updated.')
    else:
        flash('Invalid request.')
    return redirect(url_for('main.index'))
    
"""    
    
    
