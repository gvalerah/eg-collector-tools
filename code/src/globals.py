""" Application Globals """

C = None

class NameForm(Form):
    name = StringField('What is your name?', validators=[DataRequired()])
    password = StringField('What is your password?', validators=[DataRequired()])
    submit = SubmitField('Submit')


""" Creates Application Objects """

app         = Flask(__name__)

# GV Global Object Instances are defined here

basedir     = os.path.abspath(os.path.dirname(__file__))
manager     = Manager   (app)
bootstrap   = Bootstrap (app)
moment      = Moment    (app)
db          = SQLAlchemy(app)

# GV Configuration Defaults

app.config['SECRET_KEY'] = 'Hard to guess string'   # GV Check chapter 7 for more secure method of Key generation instead of hard codding
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, '%s.sqlite'%(__name__))
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

# GV Should be moved to app_functions.py
def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}
            
