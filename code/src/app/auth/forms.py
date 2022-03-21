# GV 20220310 collector/app/auth/forms.py
from flask_wtf                          import FlaskForm
from wtforms                            import StringField, PasswordField, BooleanField, SubmitField, SelectField
# GV 200020310 from wtforms.validators                import Required, Length, Email, Regexp, EqualTo
from wtforms.validators                 import DataRequired, Length, Email, Regexp, EqualTo
from wtforms                            import ValidationError
from emtec.collector.db.flask_models    import User
from flask_babel                        import lazy_gettext

class LoginForm(FlaskForm):
    # GV 20181123 email = StringField('Email', validators=[DataRequired(), Length(1, 64),    Email()])
    #username    = StringField('User Name', validators=[DataRequired(), Length(1, 64)])
    username    = StringField('User Name', validators=[DataRequired()])
    password    = PasswordField('Password', validators=[DataRequired()])
    #remember_me = BooleanField('Keep me logged in')
    submit      = SubmitField('Log In')
    

class RegistrationForm(FlaskForm):
    username    = StringField('Username', validators=[ \
                    DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, \
                    'Usernames must have only letters, ' \
                    'numbers, dots or underscores')])
                    
    role_id     = SelectField('Role', validators=[DataRequired()], choices=[(1,'Customer'),(2,'Reporter'),(3,'Charger'),(4,'Administrator'),(5,'Auditor')], coerce=int)
        
    email       = StringField('Email', validators=[ DataRequired(), Length(1, 64), Email()])
    
    password    = PasswordField('Password', validators=[ \
                    DataRequired(), EqualTo('password2', message='Passwords must match.')])
    
    password2   = PasswordField('Confirm password', validators=[ DataRequired()])
    
    submit = SubmitField('Register')
    
    #def validate_email(self, field):
    #    if User.query.filter_by(email=field.data).first():
    #        raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')
    

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old password', validators=[DataRequired()])
    password = PasswordField('New password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm new password', validators=[DataRequired()])
    submit = SubmitField('Update Password')

class ResetPasswordForm(FlaskForm):
    old_password = PasswordField('Admin password', validators=[DataRequired()])
    username = StringField('Username', validators=[
        DataRequired(), 
        Length(1, 64),
        ])
    #email = StringField('Email', validators=[DataRequired(), Length(1, 64),
    #                                         Email()])
    password = PasswordField('New Password', validators=[
        DataRequired(), 
        EqualTo('password2', message='Passwords must match')
        ])
    password2 = PasswordField('Confirm password', validators=[
        DataRequired()
        ])
    submit = SubmitField('Reset Password')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first() is None:
            raise ValidationError(f"Unknown username '{field.data}'.")

    #def validate_email(self, field):
    #    if User.query.filter_by(email=field.data).first() is None:
    #        raise ValidationError('Unknown email address.')

class PasswordResetRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    submit = SubmitField('Reset Password')


class PasswordResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    password = PasswordField('New Password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Reset Password')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError('Unknown email address.')


class ChangeEmailForm(FlaskForm):
    email = StringField('New Email', validators=[DataRequired(), Length(1, 64),
                                                 Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Update Email Address')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')      

     
     
     
     
        
