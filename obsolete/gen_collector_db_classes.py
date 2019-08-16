# Import system modules
import sys

# Import create_engine function
from sqlalchemy import create_engine
from sqlalchemy import text

# Import logging functions
import logging
# Import time formatter fuctions
from time import strftime

# Import App Modules
from common.log import Log
from db.FORMS import Forms



# Setup DB connection parameters
driver = "mysql+pymysql"
user =  "root"
password = "Zj1245//$$"
host = "127.0.0.1"
port = 3306
schema = "collector"
schema_dev = "collector_development"
app_folder = "/home/gvalera/CODE/Python/collector"
log_folder = "/home/gvalera/CODE/Python/collector/log"
log_format = "col_%Y-%m-%d.log"
charset="utf8mb4"

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
if (len(sys.argv) > 1):
    schema = sys.argv[1]
    
print ('Generating code for schema: [%s]'%schema)


logger = Log('gen_collector_db_classes',log_folder,log_format,logging.DEBUG).logger

# 'application' code

logger.info("Start Execution")

# Connect to DB
engine_string       =   str("%s://%s:%s@%s:%s/%s?charset=%s"%(driver,user,password,host,port,schema,charset))
engine              =   create_engine(engine_string)
engine_string_dev   =   str("%s://%s:%s@%s:%s/%s?charset=%s"%(driver,user,password,host,port,schema_dev,charset))
engine_dev          =   create_engine(engine_string_dev)

# General variables
Dash = "# "+"="*77+"\n"
Do_not_modify="# Auto-Generated code. do not modify\n# (c) Sertechno 2018\n# GLVH @ %s\n"%strftime("%Y-%m-%d %H:%M:%S")

Dash_Jinja = "{# "+"="*77+" #}\n"
Do_not_modify_Jinja ="{# Auto-Generated code. do not modify #}\n{# (c) Sertechno 2018 #}\n{# GLVH @ %s #}\n"%strftime("%Y-%m-%d %H:%M:%S")

    
# Creating Base Connection module    
file_name=app_folder+"/db/base.py"

logger.debug("Creating '%s'..."%(file_name))

f=open(file_name,'w')

f.write(Dash)
f.write(Do_not_modify)
f.write(Dash)
f.write("from sqlalchemy import create_engine\n")
f.write("from sqlalchemy.ext.declarative import declarative_base\n")
f.write("from sqlalchemy.orm import sessionmaker\n\n")

f.write("Base = declarative_base()\n\n")

f.close()

# Get Table Names using text SQL Command
logger.info("Getting Schema Tables ...")
query = text("SHOW TABLES")

TABLES = engine.execute(query).fetchall()
logger.info("{} Tables in schema ...".format(len(TABLES)))

# Get Schema relationships
logger.info("Getting Schema Relationships ...")
query = text("SELECT " 
               "`TABLE_SCHEMA`,"                           # -- Foreign key schema
               "`TABLE_NAME`,"                             # -- Foreign key table
               "`COLUMN_NAME`,"                            # -- Foreign key column
               "`REFERENCED_TABLE_SCHEMA`,"                # -- Origin key schema
               "`REFERENCED_TABLE_NAME`,"                  # -- Origin key table
               "`REFERENCED_COLUMN_NAME` "                 # -- Origin key column
             "FROM"
               "`INFORMATION_SCHEMA`.`KEY_COLUMN_USAGE` "  # -- Will fail if user don't have privilege
             "WHERE"
                   "`TABLE_SCHEMA` = SCHEMA() "            # -- Detect current schema in USE 
               "AND `REFERENCED_TABLE_NAME` IS NOT NULL;") # -- Only tables with foreign keys

logger.debug("Query = %s"%(query))

RELATIONS = engine.execute(query).fetchall()

logger.debug("Query = %s executed"%(query))

logger.info("{} Schema Relationships ...".format(len(RELATIONS)))
        
for t in range(len(TABLES)):
    table_name = TABLES[t][0]
    file_name = app_folder+"/db/"+table_name+".py"
    logger.debug("Creating '%s'..."%(file_name))
    f = open(file_name,"w")
    f.write(Dash)
    f.write(Do_not_modify)
    f.write(Dash)
    f.write('\n')
    f.write("from sqlalchemy            import Column, String, Integer, Numeric, Date, Time, Boolean\n")
    f.write("from sqlalchemy            import ForeignKey\n")
    f.write("from sqlalchemy.orm        import exc\n")
    f.write("from sqlalchemy.orm        import sessionmaker\n")
    f.write("from copy                  import copy, deepcopy\n")
    f.write("# Flask required modules\n")
    f.write("from flask_wtf             import Form\n")
    f.write("from wtforms               import Field\n")
    f.write("from wtforms               import StringField, IntegerField, DecimalField, DateField, DateTimeField, TimeField\n")
    f.write("from wtforms               import BooleanField, SelectField, SubmitField, RadioField\n")
    f.write("from wtforms.validators    import Required, AnyOf, DataRequired, Email, EqualTo, HostnameValidation\n")
    f.write("from wtforms.validators    import IPAddress, InputRequired, Length, MacAddress, NoneOf, NumberRange, Optional\n")
    f.write("from wtforms.validators    import Regexp, Required\n")
    f.write("\n")
    
    f.write("from db.base import Base\n\n")
    
    f.write("class %s(Base):\n"%(table_name))
    f.write("    __tablename__ = '%s'\n"%(table_name))
    f.write("    engine        = None\n\n")
    
    # Here needs to be replaced by parameter use, next test
    query = text("SHOW COLUMNS FROM "+table_name)
    COLUMNS = engine.execute(query).fetchall()
    max_column_name = 0
    for c in range(len(COLUMNS)):
        if (len(COLUMNS[c][0]) > max_column_name):
            max_column_name = len(COLUMNS[c][0])
            
    key_fields = ''        
    key_params = ''        
    key_redirs = ''        
    non_key_fields = ''        
    key_filter = ''        
    row_keys = ''

    has_relations = False
    my_relations = []
    my_joins = ''
    type = []
    is_time =[]
    
    num_key_fields = 0
    
    for c in range(len(COLUMNS)):
        field   = COLUMNS[c][0]        
        type.append(COLUMNS[c][1])
        null    = COLUMNS[c][2]
        key     = COLUMNS[c][3]
        default = COLUMNS[c][4]
        extra   = COLUMNS[c][5]
        
        if  type[c] == 'time':
            is_time.append(True)
        else:
            is_time.append(False)
            
      
        #if (type[c] == "int(11)"):
        #    type[c] = "Integer"
        #if (type[c] == "tinyint(4)"):
        #    type[c] = "Boolean"
            
        type[c]=type[c].replace("int(11)","Integer")
        type[c]=type[c].replace("tinyint(4)","Boolean")
        type[c]=type[c].replace("varchar","String")
        type[c]=type[c].replace("date","Date")
        type[c]=type[c].replace("time","String(10)")        # Necesary to avoid problem with Time Field in Forms
        type[c]=type[c].replace("float","Numeric")
        type[c]=type[c].replace("decimal","Numeric")
        
        if (key == "PRI"):
            xkey=", primary_key=True"
            if (len(key_fields) == 0):
                key_fields = key_fields + "%s"%(field)
                key_filter = key_filter + "%s.%s == %s"%(table_name,field,field)
                key_params = key_params + "<%s>"%(field)
                key_redirs = key_redirs + "%s=session['data']['%s']"%(field,field)
                row_keys   = row_keys   + "{{ row.%s }}"%(field)
            else:
                key_fields = key_fields + ",%s"%(field)
                key_filter = key_filter + ",%s.%s == %s"%(table_name,field,field)
                key_params = key_params + "&<%s>"%(field)
                key_redirs = key_redirs + ",%s=session['data']['%s']"%(field,field)
                row_keys   = row_keys   + "&{{ row.%s }}"%(field)
            num_key_fields += 1
        else:
            xkey=""
            if (len(non_key_fields) == 0):
                non_key_fields = non_key_fields + "%s.%s : %s"%(table_name,field,field)
            else:
                non_key_fields = non_key_fields + ",%s.%s : %s"%(table_name,field,field)
        
        xrel= ""
            
        for r in range(len(RELATIONS)):
            rel=RELATIONS[r]
            if rel[1] == table_name and rel[2] == field:
                xrel=str(", ForeignKey('%s.%s')"%(rel[4],rel[2]))   # rel[4] = Referenced Table rel[2] = FK field
                my_relations.append((rel[4],rel[2]))
                my_joins = my_joins + ".join(%s)"%rel[4]
                break
            else:
                xrel =""

        if (extra.find('auto_increment') != -1):
            xextra=", autoincrement=True"
        else:
            xextra=""
    
        f.write(str("    %-*s = Column( %s%s%s%s )\n"%(max_column_name,field,type[c],xrel,xkey,xextra)))
    f.write("\n")
    
    # Define fields loop variables
    fields          = ''
    init_fields     = ''
    none_fields     = ''
    dict_fields     = ''
    dict_nones      = ''
    self_fields     = ''
    deep_fields     = ''
    parameters      = ''
    self_parameters = ''
    nones           = ''

    for c in range(len(COLUMNS)):
        colum = COLUMNS[c][0]
        if (c):
            s=','
        else:
            s=''
        parameters      = parameters        + str("%s %s='%%s'"          %(s,colum))
        fields          = fields            + str("%s %s"                %(s,colum))
        if is_time[c]:
            dict_fields     = dict_fields       + str("%s '%s':str(row.%s)"       %(s,colum,colum))
        else:
            dict_fields     = dict_fields       + str("%s '%s':row.%s"       %(s,colum,colum))
        
        dict_nones      = dict_nones        + str("%s '%s':None"         %(s,colum))
        nones           = nones             + str("%s None"              %(s,))
        init_fields     = init_fields       + str("%sself.%-*s = %s\n"  %(' '*8,max_column_name,colum,colum))
        none_fields     = none_fields       + str("%sself.%-*s = None\n"  %(' '*8,max_column_name,colum))
        self_fields     = self_fields       + str("%s self.%s"           %(s,colum))
        self_parameters = self_parameters   + str("%s %s='%%s'"          %(s,colum))
        deep_fields     = deep_fields       + str("%s%sdeepcopy(self.%-*s , memo)\n"  %(' '*16,s,max_column_name,colum))
    
    # Create Initialization method (Set to empty initialization now, just create instance)
    f.write(    "    def __init__(self,%s):\n"%fields)
    #f.write("%s\n"%none_fields)
    f.write(    "        self.set(%s)\n"%fields)
    
    # Create Representation method
    f.write(    "    def __repr__(self):\n")
    f.write(str('        return "<%s('%(table_name)))

    f.write('%s)>" %% \\\n                (%s)\n\n'%(parameters,self_fields))
            
    # Create copy method
    f.write(    "    def __copy__(self):\n")
    f.write(    "        return type(self)(%s)\n\n"%(self_fields))            

    # Create deepcopy method
    f.write(    "    def __deepcopy__(self, memo): # memo is a dict of id's to copies\n")
    f.write(    "        id_self = id(self)        # memoization avoids unnecesary recursion\n")
    f.write(    "        _copy = memo.get(id_self)\n")
    f.write(    "        if _copy is None:\n")
    f.write(    "            _copy = type(self)(\n%s"%(deep_fields))
    f.write(    "                )\n")
    f.write(    "            memo[id_self] = _copy\n")
    f.write(    "        return _copy\n\n")
                        
    # Create set method
    f.write(    "    def set(self,%s):\n"%(fields))
    f.write(    "%s\n"%init_fields)
    
    # Create insert method
    f.write(    "    def insert(self,%s):\n"%(fields))

    f.write(    '        self.set(%s)\n'%(fields))
    f.write(    '        Session = sessionmaker(bind=self.engine)\n')
    f.write(    '        session = Session()\n')
    f.write(    '        X = copy(self)\n')
    f.write(    '        session.add(X)\n')
    f.write(    '        session.commit()\n')
    f.write(    '        session.close()\n\n')

    # Create merge method
    f.write(    "    def merge(self,%s):\n"%(fields))

    f.write(    '        self.set(%s)\n'%(fields))
    f.write(    '        Session = sessionmaker(bind=self.engine)\n')
    f.write(    '        session = Session()\n')
    f.write(    '        session.merge()\n')
    f.write(    '        session.commit()\n')
    f.write(    '        session.close()\n\n')

    # Create update method
    f.write(    "    def update(self,%s):\n"%(fields))

    f.write(    '        self.set(%s)\n'%(fields))
    f.write(    '        Session = sessionmaker(bind=self.engine)\n')
    f.write(    '        session = Session()\n')
    f.write(    '        session.query(%s).filter(%s).update({%s})\n'%(table_name,key_filter,non_key_fields))
    f.write(    '        session.commit()\n')
    f.write(    '        session.close()\n\n')
                
     # Create delete method
    f.write(    '    def delete(self,%s):\n'%(key_fields))
    f.write(    '        Session = sessionmaker(bind=self.engine)\n')
    f.write(    '        session = Session()\n')
    f.write(    '        session.query(%s).filter(%s).delete()\n'%(table_name,key_filter))
    f.write(    '        session.commit()\n')
    f.write(    '        session.close()\n\n')

    # Create query method
    f.write(    '    def queryall(self):\n')
    f.write(    '        Session = sessionmaker(bind=self.engine)\n')
    f.write(    '        session = Session()\n')
    f.write(    '        try:\n')
    f.write(    '            results = session.query(%s).all()\n'%(table_name))
    f.write(    '        except exc.NoResultFound:\n')
    f.write(    '            results = None\n')
    f.write(    '        return results\n\n')

    # Create queryone method
    f.write(    '    def queryone(self,%s):\n'%(key_fields))
    f.write(    '        Session = sessionmaker(bind=self.engine)\n')
    f.write(    '        session = Session()\n')
    f.write(    '        try:\n')
    f.write(    '            results = session.query(%s).filter(%s).one()\n'%(table_name,key_filter))
    f.write(    '        except exc.NoResultFound:\n')
    f.write(    '            results = None\n')
    f.write(    '        return results\n\n')

    # Create queryjoin method
    f.write(    '    def queryjoin(self,%s):\n'%(key_fields))
    f.write(    '        Session = sessionmaker(bind=self.engine)\n')
    f.write(    '        session = Session()\n')
    f.write(    '        try:\n')
    f.write(    '            results = session.query(%s)%s.filter(%s).one()\n'%(table_name,my_joins,key_filter))
    f.write(    '        except exc.NoResultFound:\n')
    f.write(    '            results = None\n')
    f.write(    '        return results\n\n')


           
    # Create inject_list method
    f.write(    '    def inject_list(self,rows):\n')
    f.write(    '        Session = sessionmaker(bind=self.engine)\n')
    f.write(    '        session = Session()\n')
    f.write(    '        for row in (rows):\n')
    f.write(    '            X = copy(self)\n')
    f.write(    '            for f in range(len(row)):\n')
    for c in range(len(COLUMNS)):
        f.write('                X.%-*s = row[%d]\n'%(max_column_name,COLUMNS[c][0],c))
    f.write(    '            session.add(X)\n')
    f.write(    '        session.commit()\n')
    f.write(    '        session.close()\n\n') 
    
    # Create inject_dict method
    f.write(    '    def inject_dict(self,rows):\n')
    f.write(    '        Session = sessionmaker(bind=self.engine)\n')
    f.write(    '        session = Session()\n')
    f.write(    '        for row in (rows):\n')
    f.write(    '            X = copy(self)\n')
    f.write(    '            for f in range(len(row)):\n')
    for c in range(len(COLUMNS)):
        f.write('                X.%-*s = row[\'%s\']\n'%(max_column_name,COLUMNS[c][0],COLUMNS[c][0]))
    f.write(    '            session.add(X)\n')
    f.write(    '        session.commit()\n')
    f.write(    '        session.close()\n\n')    
        
    # Create Class Form
    f.write(Dash)
    
    F           =   Forms(None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None)
    F.engine    =   engine_dev
    
    HEADERS = []
    
  
    #K_Fields = ''
    FK_List = ''
    FK_Choi = ''
    FK_dict = ''
    
    has_fks = False
    
    f.write(    "class frm_%s(Form):\n"%(table_name))

    s=''
    xchoices = []
    for c in range(len(COLUMNS)):
        x=''
        xchoices.append("")
#        form_field = F.queryone(table_name,COLUMNS[c][0]).one()
        form_field = F.queryone(COLUMNS[c][0])
        if form_field is not None:
            # Checking for Basic Form Field Type
            if      type[c].find('Integer') != -1:
                field_type='IntegerField'
            elif    type[c].find('String') != -1:
                field_type='StringField'
            elif    type[c].find('Boolean') != -1:
                field_type='BooleanField'
            elif    type[c].find('Date') != -1:
                field_type='DateField'
            elif    type[c].find('Time') != -1:
                field_type='TimeField'
            elif    type[c].find('DateTime') != -1:
                field_type='DateTimeField'
            elif    type[c].find('Numeric') != -1:
                field_type='DecimalField'
        
            # Check for Foreign Keys
            if form_field.Foreign_Key is not None:
                has_fks = True
                # Field will be a selection of the valid values only , depends on Referenced Table
                field_type='SelectField'
                #FK_Fields = FK_Fields + "    fk%s = []\n"%(COLUMNS[c][0])
                FK_dict = "{ 'Referenced_Table':'%s', 'Foreign_Key':'%s', 'Foreign_Field':'%s', 'Value': '' }" % \
                            (form_field.Referenced_Table, form_field.Foreign_Key, form_field.Foreign_Field)
                FK_List = FK_List + "        self.FK_List['%s'] = %s\n"%(COLUMNS[c][0],FK_dict)
                
                FK_Choi = FK_Choi + "        self.FK_List['%s']['Choices'] = self.Get_Choices('%s')\n" % (form_field.Field, form_field.Field)
                FK_Choi = FK_Choi + "        self.%s.choices = self.FK_List['%s']['Choices']\n"        % (form_field.Field, form_field.Field)
                
                
                
                x ="%s ref: %s->%s=%s"%(COLUMNS[c][0], form_field.Referenced_Table, form_field.Foreign_Key, form_field.Foreign_Field)    
                #session['data']['Rat_Id']
                s = s + "        form.FK_List['%s']['Value'] = sess.query(%s.%s).filter(%s.%s == session['data']['%s']).first()\n" % \
                        (form_field.Field, \
                            form_field.Referenced_Table, form_field.Foreign_Field,form_field.Referenced_Table, \
                            form_field.Foreign_Key, form_field.Field)
                #s = s + "    print('fk_%s = ',fk_%s)\n" % (form_field.Field, form_field.Field)

                        
           # Check for validators
            validators = ''
            if form_field.Validation:               # Incluir aqui codigo si se necesita mas de una validacion, incluyendo FKs
                validators = ", validators=[%s]"%form_field.Validation_String
                # Check for Optipns Fields
                if      form_field.Validation_Type == "OP":
                    # Field will be a selection of the valid values only , depends on Valid Options 
                    field_type='SelectField'
                elif    form_field.Validation_Type == "RF":
                    # Field will be a selection of the valid values only , depends on Valid Options 
                    field_type='RadioField'
            
            # Creating form field depending on Field Type
            if field_type == "SelectField":
                if type[c] == "Integer":
                    coerce = ", coerce=int"
                else:
                    coerce = ""
                if      form_field.Validation_Type == "OP":
                    #choices = ", choices = %s" % form_field.Options_String
                    choices = ""
                elif    form_field.Validation_Type == "FK":
                    choices = ", choices = %s_choices" % form_field.Field    
                    f.write("    %-*s = []\n"%(max_column_name+8,form_field.Field+"_choices") )                
                f.write("    %-*s = %s(\"%s?\"%s%s%s)\n"%( max_column_name+8,COLUMNS[c][0], field_type, form_field.Caption_String, choices, coerce,validators))
            elif field_type == "RadioField":
                choices = ", choices = %s" % form_field.Options_String
                f.write("    %-*s = %s(\"%s?\"%s%s)\n"%( max_column_name+8,COLUMNS[c][0], field_type, form_field.Caption_String, choices, validators))
            else:
                f.write("    %-*s = %s(\"%s?\"%s)\n"%( max_column_name+8,COLUMNS[c][0], field_type, form_field.Caption_String, validators))

            if      form_field.Validation_Type == "OP":
                f.write("    %-*s = %s\n"%(max_column_name+8,COLUMNS[c][0]+".choices", form_field.Options_String))
                xchoices[c] = xchoices[c] + form_field.Options_String

            HEADERS.append(form_field.Caption_String)
        else:
            HEADERS.append(COLUMNS[c][0])
    f.write(    "    %-*s = SubmitField('Save')\n\n"%(max_column_name+8,"submit"))
    f.write(    "    %-*s = %s\n"%(max_column_name+8,"has_FKs",has_fks))
    f.write(    "    %-*s = {}\n"%(max_column_name+8,"FK_List"))
    f.write(    "    %-*s = None\n\n"%(max_column_name+8,"engine"))
        
    if len(FK_List)>0:
        f.write("    def set_FK_list(self):\n")
        f.write(        "%s\n"%(FK_List))
        f.write(        "%s\n"%(FK_Choi))

        f.write("    def Get_Choices(self,Field):\n")
        f.write("        FK_Table   = self.FK_List[Field]['Referenced_Table']\n"  )
        f.write("        FK_Key     = self.FK_List[Field]['Foreign_Key']\n"       )
        f.write("        FK_Field   = self.FK_List[Field]['Foreign_Field']\n"     )
        f.write("        #logger.debug('Get_Choices: %s -> %s (%s)'%(FK_Key,FK_Table,FK_Field))\n")
        f.write("        Q='SELECT %s,%s from %s' % (FK_Key,FK_Field,FK_Table)\n")
        f.write("        rows       = self.engine.execute(Q).fetchall()\n")
        f.write("        #logger.debug('Get_Choices(\\'%s\\') %d rows found using [%s]'%(Field,len(rows),Q))\n")      
        f.write("        return rows\n")
        
        f.write(Dash)
    
    # ------------------------------------------------------------------------
    # Create Flask decorator code
    # ------------------------------------------------------------------------
    
    file_name = app_folder+"/tools/decorators/decorator_"+table_name+".py"
    logger.debug("Creating '%s'..."%(file_name))
    f = open(file_name,"w")

    f.write(Dash)
    f.write(Do_not_modify)
    f.write(Dash)

    f.write(    "from db.%s import %s,frm_%s\n\n"%(table_name,table_name,table_name))
    
    f.write(    "@app.route('/forms/%s/%s', methods=['GET', 'POST'])\n"%(table_name,key_params))
    f.write(    "def forms_%s(%s):\n"%(table_name,key_fields))
    f.write(    "    logger.debug('Enter: forms_%s(%s)'%%(%s))\n" % (table_name,"%s,"*num_key_fields,key_fields) )
    f.write(    "    %s =  %s(%s)\n"                        % (table_name.lower(),table_name,nones) )
    f.write(    "    %s.engine =  C.db\n"                   % (table_name.lower()) )
    f.write(    "    row =  %s.queryone(%s)\n"              % (table_name.lower(),key_fields) )    
    
    f.write(    "    if row is not None:\n")
    f.write(    "        session['data'] =  {%s}\n"         % (dict_fields) )
    f.write(    "    else:\n")
    f.write(    "        session['data'] =  {%s}\n"         % (dict_nones) )
                       
    f.write(    "    form = frm_%s()\n\n"                   % (table_name) )
    f.write(    "    form.engine = C.db\n\n" )
    f.write(    "    if form.has_FKs:\n")
    f.write(    "        form.set_FK_list()\n\n")
    
    
    # Debug Code Begins here
    

    #f.write(    "        logger.debug( 'form: %s'%form )\n")
    #f.write(    "        px=pprint.pformat(form.FK_List)\n")        
    #f.write(    "        logger.debug( 'FK_List:\\n%s\\n'%px)\n")
    #f.write(    "        for k in form._fields.keys():\n")
    #f.write(    "           logger.debug( 'key = %s'%k )\n")
    #f.write(    "           logger.debug(dir(form._fields[k]))\n")
    #f.write(    "           px=pprint.pformat(form._fields[k].__dict__)\n")        
    #f.write(    "           logger.debug(px)\n")   
    
    # Debug Code ends here
    
    # Code for Foreign key data gathering
    f.write(    "        Session=sessionmaker(bind=C.db)\n")
    f.write(    "        sess=Session()\n")
    f.write(            "%s\n" % (s))

    for c in range(len(COLUMNS)):
        if len(xchoices[c]) > 0:
            f.write("    %-*s = %s\n"%( max_column_name+13,"form."+COLUMNS[c][0]+".choices", xchoices[c]))
            
    # Actual Form activation here
    f.write(    "    if form.validate_on_submit():\n")
    for c in range(len(COLUMNS)):
        f.write("        session['data']['%s'] = form.%s.data\n"%(COLUMNS[c][0],COLUMNS[c][0]))
    f.write(    "        return redirect(url_for('forms_%s',%s))\n\n"%(table_name,key_redirs))    
    for c in range(len(COLUMNS)):        
        f.write("    form.%s.data = session['data']['%s']\n"%(COLUMNS[c][0],COLUMNS[c][0]))            

    f.write(    "\n")    

    f.write(    "    return render_template('%s.html',C=C, form=form, data=session.get('data'),row=row)\n\n"%(table_name))    
    
    # ------------------------------------------------------------------------    
    f.write(    "@app.route('/select/%s', methods=['GET'])\n"       %(table_name))
    f.write(    "def select_%s():\n"                                %(table_name))
    f.write(    "    logger.debug('Enter: select_%s()')\n"          % (table_name) )
    f.write(    "    %s =  %s(%s)\n"                                %(table_name.lower(),table_name,nones))
    f.write(    "    %s.engine =  C.db\n"                           %(table_name.lower()))
    f.write(    "    result =  %s.queryall()\n"                     %(table_name.lower()))
    f.write(    "    rows = []\n")
    f.write(    "    for r in result:\n")
    f.write(    "	    row = object_as_dict(r)\n")
    f.write(    "	    rows.append(row)\n")
    f.write(    "    return render_template('%s_All.html',C=C,rows=rows)\n"%(table_name))
    
    f.write(Dash)
    f.close()

    # ------------------------------------------------------------------------
    # Create HTML Templates
    # ------------------------------------------------------------------------
    
    file_name = "./xtemplates/"+table_name+".html"
    logger.debug("Creating '%s'..."%(file_name))
    f = open(file_name,"w")
    
    f.write(Dash_Jinja)
    f.write(Do_not_modify_Jinja)
    f.write(Dash_Jinja)    
    f.write('{% extends "base.html" %}\n')
    f.write('{% import "bootstrap/wtf.html" as wtf %}\n')

    f.write('{% block title %}Collector{% endblock %}\n')

    f.write('{% block head %}\n')
    f.write('{{ super() }}\n')
    f.write('<link rel="shortcut icon" href="{{ url_for(\'static\', filename = \'favicon.ico\') }}"\n')
    f.write('type="image/x-icon">\n')
    f.write('<link rel="icon" href="{{ url_for(\'static\', filename = \'img/favicon.ico\') }}"\n')
    f.write('type="image/x-icon">\n')
    f.write('{% endblock %}\n')

    f.write('{% block page_content %}\n')
    f.write('<div class="page-header">\n')
    
    f.write('    <h2>%s Form:</h2>\n'%table_name)
    #f.write('    <p>{{row}}</p>\n')
    #f.write('    <p>{{data}}</p>\n')
    
    f.write('</div>\n')
    f.write('{{ wtf.quick_form(form) }}\n')
    f.write('{% endblock %}\n')
    f.write(Dash_Jinja)       
    f.close()          

    # ------------------------------------------------------------------------

    file_name = "./xtemplates/"+table_name+"_All.html"
    logger.debug("Creating '%s'..."%(file_name))
    f = open(file_name,"w")
    
    f.write(Dash_Jinja)
    f.write(Do_not_modify_Jinja)
    f.write(Dash_Jinja)    

    f.write(    '{% extends "base.html" %}\n\n')
    f.write(    '{% import "bootstrap/wtf.html" as wtf %}\n\n')
    f.write(    '{% block title %}Collector{% endblock %}\n\n')
    f.write(    '{% block head %}\n')
    f.write(    '   {{ super() }}\n')
    f.write(    '   <link rel="shortcut icon" href="{{ url_for(\'static\', filename = \'favicon.ico\') }}"\n')
    f.write(    '   type="image/x-icon">\n')
    f.write(    '   <link rel="icon" href="{{ url_for(\'static\', filename = \'img/favicon.ico\') }}"\n')
    f.write(    '   type="image/x-icon">\n')
    f.write(    '{% endblock %}\n\n')
    f.write(    '{% block page_content %}\n')
    f.write(    '<div class="page-header">\n')
    f.write(    '    <h2>%s:<h2> <p>{{ rows.__len__() }} records found.</p>\n'%(table_name))
    f.write(    '</div>\n')
    f.write(    '<table>\n')
    f.write(    '    <tr id="header">\n')
    for c in range(len(COLUMNS)):     
        f.write('        <td>%s</td>\n'%(HEADERS[c]))
    f.write('        <td>Edit Link</td>\n')
        
    f.write(    '    </tr>\n')
    f.write(    '    {% for row in rows %}\n')
    f.write(    '       <tr id="{{loop.cycle("even","odd")}}">\n')
    for c in range(len(COLUMNS)):     
        f.write('           <td>{{ row.%s }}</td>\n'%((COLUMNS[c][0])))
            
    #url_for('forms_%s',%s))\n"%(table_name,key_redirs)      
    f.write('           <td><a href="/forms/%s/%s">Edit</a></td>\n'%(table_name,row_keys) )      
    f.write(    '       </tr>\n')
    f.write(    '    {% endfor %}\n')
    f.write(    '</table>\n')
    f.write(    '{% endblock %}\n\n')
    
    f.write(Dash_Jinja)    

    # <a href="/howto/howto_css_dropdown.asp">Dropdowns</a>


    f.close()          

logger.info("End Execution")

"""
class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    password = StringField('What is your password?', validators=[Required()])
    submit = SubmitField('Submit')    
   
@app.route('/', methods=['GET', 'POST'])
def index():
    # Espera a capitulo 3 para mejorar procedimiento de respuesta, hard coding mucho aqui
    logger.debug("index() IN")

    data =  {   "name":current_app.name,
                "app_name":C.app_name,
                "date_time":strftime('%Y-%m-%d %H:%M:%S'),
                "user_agent":request.headers.get('User-Agent'),
                "current_time":datetime.utcnow()
            }
    name = None
    password = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        form.name.data = ''            
        form.password.data = ''            
    logger.debug("index() OUT")
    return render_template('collector.html',data=data, form=form, name=name,password=password)

HTML

{% extends "base.html" %}
{% import "bootstrap/wtf.html" as wtf %}

{% block title %}Collector{% endblock %}

{% block head %}
{{ super() }}
<link rel="shortcut icon" href="{{ url_for('static', filename = 'favicon.ico') }}"
type="image/x-icon">
<link rel="icon" href="{{ url_for('static', filename = 'img/favicon.ico') }}"
type="image/x-icon">
{% endblock %}

{% block page_content %}
<div class="page-header">
    
    <h1>Collector v 1.0</h1>
    <p>(c) SERTECHNO 2018 GLVH</p>
    <p>Flask Current Application Name is "{{ data["name"] }}"</p>
    <p>Collector local C Context Name is "{{ data["app_name"] }}"</p>
    <p>Your browser is "{{ data["user_agent"] }}"</p>
    <p>Local time is @ {{ data["date_time"] }}</p> 
    <p>The local date and time is {{ moment(data["current_time"]).format('LLL') }}.</p>
    <p>That was {{ moment(data["current_time"]).fromNow(refresh=True) }}</p>    
    <p>Esto esta solo en collector.html y recibio name='{{ name }}'({{password}})</p>
    <h1>H1</h1>    <h1>H2</h1>    <h1>H3</h1>
    <p>p</p>
    <table>Table
        <tr>tr 1
            <td>td 1</td>
            <td>td 2</td>
            <td>td 3</td>
        </tr>
        <tr>tr 2
            <td>td 1</td>
            <td>td 2</td>
            <td>td 3</td>
        </tr>
        <tr>tr 3
            <td>td 1</td>
            <td>td 2</td>
            <td>td 3</td>
        </tr>
    </table>

</div>
{{ wtf.quick_form(form) }}
{% endblock %}
"""

