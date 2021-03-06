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
from flask                              import current_app

# Authorization sub-system
from .                                  import auth
from ..decorators                       import admin_required
from ..decorators                       import permission_required
from flask_login                        import login_user
from flask_login                        import logout_user
from flask_login                        import login_required
from flask_login                        import current_user
from flask_babel                        import gettext
from flask_babel                        import lazy_gettext
# Application context
#from ..                                 import app
from ..                                 import db
from ..                                 import logger

# Actual Application model
from emtec.collector.db.flask_models    import User
from emtec.debug                        import *
from emtec.ldap                         import *

# Interface
from .forms                             import LoginForm
from .forms                             import ChangePasswordForm
from .forms                             import ResetPasswordForm
from .forms                             import ChangeEmailForm
from .forms                             import RegistrationForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    logger.debug(f"{this()}: IN")
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
                logger.debug(f"login: {user}")
                if user.ldap:
                    # LDAP HERE ----------------------------------------------
                    logger.info(f"{this()}:  user {user} requires LDAP authentication")
                    try:
                        # LDAP default methos is SIMPLE, otherwise needs to be specified
                        if user.ldap_method is None:
                            method = 'SIMPLE'
                        else:
                            method = user.ldap_method.strip().upper()
                        if len(method):
                            logger.info(f"{this()}: method = {method}")
                            ldap_user_name = user.ldap_user
                            ldap_common_name = user.ldap_common
                            host   = user.ldap_host   if user.ldap_host   is not None else current_app.config.get('LDAP_HOST')
                            port   = user.ldap_port   if user.ldap_port               else current_app.config.get('LDAP_PORT')
                            domain = user.ldap_domain if user.ldap_domain is not None else current_app.config.get('LDAP_DOMAIN')
                            # Elemental very simple OPEN LDAP Authentication
                            if method == 'SIMPLE': 
                                LDAP_username = ldap_username(username=ldap_user_name,common_name=ldap_common_name,domain=domain)
                                logger.info(f"{this()}: LDAP_username = {LDAP_username}")
                                success = ldap_authentication(LDAP_username, form.password.data,host=host,port=port,logger=logger)
                            # MS Windows Active Directory Authentication
                            elif method in ['MSAD','WINDOWS']:
                                logger.info(f"{this()}: Enter MSAD/WINDOWS authentication")
                                # Gets sure LDAP username format is DOMAIN\USERNAME
                                if ldap_user_name.find("\\")>-1: pass
                                elif ldap_user_name.find("@")>-1: pass
                                else: ldap_user_name = f"{domain.upper()}\\{ldap_user_name}"
                                logger.debug(f"{this()}: ldap_user_name={ldap_user_name}")
                                options = {}
                                # defaults
                                '''
                                protocol = 3
                                options  = [(ldap.OPT_REFERRALS,0)]
                                if len(user.vars):
                                    pairs = user.vars.split(',')
                                    for pair in pairs:
                                        var,value=pair.split('=')
                                        variables.update({var:value})
                                    for variable in variables:
                                        if variable == 'protocol':protocol=int(value)
                                        else:
                                            key = getattr(ldap,key)
                                            if key is not None:
                                                # cast value to int if possible
                                                try:
                                                    value=int(value)
                                                except:
                                                    pass
                                                options.append((key,value))
                                '''
                                try:
                                    vars = json.loads(user.vars)
                                except:
                                    vars = {}
                                logger.debug(f"{this()}: host={host} user={ldap_user_name} vars={vars}")
                                success = ldap_authentication_msad(host, ldap_user_name, form.password.data, logger=logger,**vars)
                            # Legacy NT Lan Manager authentication should be considered obsolete
                            elif method in ['NTLM']: 
                                if ldap_user_name.find("\\")>-1: pass
                                elif ldap_user_name.find("@")>-1:
                                    usr,dom = ldap_user_name.split('@',1)
                                    ldap_user_name = f"{str(dom).upper()}\\{usr}"
                                else: ldap_user_name = f"{domain.upper()}\\{ldap_user_name}"
                                flash(f"host={host} user={ldap_user_name} pwd={form.password.data}")
                                vars = json.loads(user.vars)
                                url = f"http://{domain}/{vars.get('endpoint')}"
                                success = ldap_authentication_ntlm(url, ldap_user_name, form.password.data,logger=logger)
                            logger.info(f"{this()}: success={success}")
                            if success:
                                login_user(user, False)
                                return redirect(request.args.get('next') or url_for('main.index'))
                            else:
                                flash(gettext('Invalid username or password.'),'error')
                        else:
                            flash(gettext('Invalid authentication method required.'),'error')
                    except Exception as e:
                        flash(f"EXCEPTION: {str(e)}",'error')
                    # LDAP HERE ----------------------------------------------
                else:
                    if user is not None and user.verify_password(form.password.data):
                        login_user(user, False)
                        logger.debug(f"{this()}: request.args.get('next') = {request.args.get('next')}")
                        logger.debug(f"{this()}: url_for('main.index')    = {url_for('main.index')}")
                        return redirect(request.args.get('next') or url_for('main.index'))
                    else:
                        logger.error(f"login: user = {user}")
                        if user is not None:
                            logger.error(f"login: user.verify_password() = {user.verify_password(form.password.data)}")
                    flash('Invalid username or password.','error')
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
        flash('You have been logged out.','info')
        #lash('You have been logged out.')
    except Exception as e:
        print       ( f"logout: exception: {str(e)}")
        logger.error( f"logout: exception: {str(e)}")
    return redirect(url_for('main.index'))
    
# Only Administrator can register users, include decorator here
@auth.route('/register', methods=['GET', 'POST'])
@login_required
@admin_required
def register():
    db.session.commit()
    db.session.flush()
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
            role_id=form.role_id.data,
            email=form.email.data,
            password=form.password.data,
            CC_Id = form.CC_Id.data,
            roles = form.roles.data,
            ldap  = form.ldap.data,
            ldap_method = form.ldap_method.data,
            ldap_user   = form.ldap_user.data,
            ldap_common = form.ldap_common.data,
            ldap_host   = form.ldap_host.data,
            ldap_port   = form.ldap_port.data,
            ldap_domain = form.ldap_domain.data,
            vars        = form.vars.data
            )
        try:
            #flash("Trying to register user: '%s'"%user)
            db.session.add(user)
            db.session.commit()
            db.session.flush() #20210630 GV 
            flash('New user "%s" can login now.'%form.username.data,'info')
            #lash('New user "%s" can login now.'%form.username.data)
            return redirect(url_for('main.index'))
        except Exception as e:
            db.session.rollback()
            db.session.flush() #20210630 GV 
            flash('Form Data is: [name=%s,role_id=%s,email=%s,password=%s]'%( form.username.data, form.role_id.data, form.email.data, form.password.data),'warning')
            flash('Error creating new user. %s'%(e),'error')
            #lash('Form Data is: [name=%s,role_id=%s,email=%s,password=%s]'%( form.username.data, form.role_id.data, form.email.data, form.password.data))
            #lash('Error creating new user. %s'%(e))
            return redirect(url_for('auth.register'))
            
    return render_template('auth/register.html', form=form)
    
'''  
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
'''
@auth.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    # 20210609 cambio 
    db.session.flush()
    db.session.commit()
    if current_user.role_id in (4,6):
        form = ResetPasswordForm()
    else:
        form = ChangePasswordForm()
        username = current_user.username
    if form.validate_on_submit():
        #lash('Change Password','message')
        flash('Change Password')
        if current_user.verify_password(form.old_password.data):
            if hasattr(form,'username'):
                user = db.session.query(User
                        ).filter(User.username==form.username.data
                        ).first()
            else:
                user = current_user
            user.password = form.password.data
            db.session.merge(user)
            db.session.flush()
            db.session.commit()
            if user.username == current_user.username:
                flash('Your password has been updated.','info')
                #lash('Your password has been updated.')
            else:
                flash(f"'{user.username}' password has been updated.",'info')
                #lash(f"'{user.username}' password has been updated.")
            return redirect(url_for('main.index'))
        else:
            flash('Invalid password.','error')
            #lash('Invalid password.')
    return render_template("auth/change_password.html", form=form,user=current_user)

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
                  'address has been sent to you.','info')
            #lash('An email with instructions to confirm your new email '
            #     'address has been sent to you.')
            return redirect(url_for('main.index'))
        else:
            flash('Invalid email or password.','error')
            #lash('Invalid email or password.')
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
    
    
