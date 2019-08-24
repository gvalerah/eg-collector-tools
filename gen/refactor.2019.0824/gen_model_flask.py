import os
from sqlalchemy import text
# General variables
from gen.gen_functions          import Dash,Do_not_modify,Dash_Jinja,Do_not_modify_Jinja,print_log
from gen.gen_menu_functions     import auto_models
from gen.gen_menu_functions     import auto_forms
from gen.gen_menu_functions     import source_includes
from gen.gen_menu_functions     import Include_File
from gen.gen_menu_functions     import Delete_File


def Gen_Model_Schema(tables):
    # ------------------------------------------------------------------
    # Create Class SQL Alchemy for direct non Flask DB Handling
    # ------------------------------------------------------------------
    list_files=[]
    for table in tables:
        list_files.append("orm_%s_table.py"%table.lower())

    file_name = auto_models+"/ORM_model_schema.py"
    print_log("Creating '%s'..."%(file_name))


    f= open(file_name,"w")
    

    f.write(Dash)
    f.write(Do_not_modify)
    f.write(Dash)
    f.write('\n')
    f.write("from sqlalchemy                 import Table, Column, MetaData, ForeignKey\n")
    f.write("from sqlalchemy                 import Integer, String, Date, Time, Numeric, DateTime, Boolean\n\n")
    f.write("Meta = MetaData()\n")
    f.write('\n')
    f.write('def Create_Tables(engine):\n')
    
    for filename in list_files:
        file_name = auto_models+"/"+filename
        try:
            Include_File(file_name,f)
            Delete_File(file_name)
        except Exception as e:
            print("EXCEPTION: ",e,"!!!!")
    f.write('    try:\n')
    f.write('        Meta.create_all(engine)\n')
    f.write('    except Exception as e:\n')
    f.write('        print("EXCEPTION: on Meta.create_all(engine=%s)"%engine,e,"!!!!")\n')
    f.write('\n')
    # Creates load function here
    file_name="%s/models/orm_function_load_table.py"%source_includes
    Include_File(file_name,f)
    f.write('\n')
    f.close()
    
def Gen_Model_Flask(Metadata,Tab,session,Forms,app_folder):
    table_name = Tab['table']
    class_name = Tab['class']
    
    # Flask Model File
    file_name = auto_models+"/flask_"+Tab['table'].lower()+".py"
    print_log("Creating '%s'..."%(file_name))
    
    file_flask_properties = source_includes+"/models/flask_"+Tab['table'].lower()+"_properties.py"
    file_flask_methods    = source_includes+"/models/flask_"+Tab['table'].lower()+"_methods.py"
    file_orm_properties   = source_includes+"/models/orm_"+Tab['table'].lower()+"_properties.py"
    file_orm_methods      = source_includes+"/models/orm_"+Tab['table'].lower()+"_methods.py"
    
    f = open(file_name,"w")
    f.write(Dash)
    f.write(Do_not_modify)
    f.write(Dash)
    f.write('\n')
    
    # For Users table there is an exception because inherits from UserMixin Class too
    if Tab['table'] in ['Users']:
        Mixin='UserMixin, '
    else:
        Mixin=''
        
    #print("class %s(%sdb.Model):"%(class_name,Mixin))
    f.write("class %s(%sdb.Model):\n"%(class_name,Mixin))
    f.write("    __tablename__ = '%s'\n"%(table_name))
    
    
    # Creates Column Definitions for Table's Class
    for c in Tab['columns']:
        
        xkey=", primary_key=True" if c['key'] == "PRI" else "" 
        xrel= ""

        for rel in Metadata['relations']:
            if rel['table_name'] == table_name and rel['column_name'] == c['field']:
                try:
                    form_field = session.query(Forms).filter(Forms.Table==table_name,Forms.Field==c['field']).one()
                except Exception as e:
                    print()
                    print("---------------------------------------------------------------")
                    print("WARNING: Exception creating column definitions in model")
                    print("Check if %s and %s exists in Dev_Forms"%(table_name,c['field']))
                    print("form_field=",form_field)
                    print("gen model flask creating xrel Exception")
                    print("table_name",table_name,"c['field']",c['field'])
                    print("e=",e)
                    print("---------------------------------------------------------------")
                    print()
                    break
                # Get Related Data
                try:
                    Rel=Metadata['tables'][rel['referenced_table_name']]
                    xrel=str(", db.ForeignKey('%s.%s')"%(rel['referenced_table_name'],\
                        rel['referenced_column_name']))   # Referenced Table and field
                    Tab['code']['my_relations'].append((rel['referenced_table_name'],rel['referenced_column_name']))
                    Tab['code']['my_joins'] = Tab['code']['my_joins'] + \
                        "               .join(%s,%s.%s == %s.%s).add_columns(%s.%s)\\\n"%\
                        (Rel['class'], Tab['class'], c['field'], Rel['class'], c['field'], Rel['class'],\
                        form_field.Foreign_Value)                    
                except Exception as e:
                    print()
                    print("---------------------------------------------------------------")
                    print("WARNING: Exception creating column definitions in model")
                    print("Check if %s and %s exists in Dev_Forms"%(table_name,c['field']))
                    print("rel=",rel)
                    print("Rel=",Rel)
                    print("table_name",table_name,"c['field']",c['field'])
                    print("e=",e)
                    print("---------------------------------------------------------------")
                    print()
                    break
                break
            else:
                xrel =""
               
        if (c['extra'].find('auto_increment') != -1):
            xextra=", autoincrement=True"
        else:
            xextra=""

        if c['default'] is not None and len(c['default'])>0:
            if 'int' in c['type'] or 'float' in c['type'] or 'decimal' in c['type'] :
                xdefault=", default=%s"%c['default']
            else:
                xdefault=", default='%s'"%c['default']
        else:
            xdefault=""
   
        f.write(str("    %-*s = db.Column( %s%s%s%s%s )\n"%(Tab['max_column_name_length'],c['field'],c['type_flask'],xrel,xkey,xextra,xdefault)))

    f.write("\n")

    # Look for BACK REFERENCES
    for R in Tab['relations']:
        # 20181216 GV ACTUALLY AVOIDING AUTO-REFERENCES NEED TO BE REVIEWED
        if R['class'] == R['backref']:
            pass
        else:
            f.write("    %-*s = db.relationship('%s',backref='%s')\n"%\
                (Tab['max_column_name_length'],R['name'],R['class'],R['backref'].lower())) # backref= lowercase as a convention
            Tab['has_references'] = True
    f.write("\n")
   
    # ------------------------------------------------------------------
    # Conditional include properties
    # ------------------------------------------------------------------
    if os.path.isfile(file_flask_properties):
        Include_File(file_flask_properties,f)
        
    # ------------------------------------------------------------------
    # Class Methods
    # ------------------------------------------------------------------
    if Tab['gen_flask_methods']:                
        # Create Initialization method
        f.write(    "    def __init__(self,%s):\n"          % ( Tab['code']['default_fields'] ) )
        f.write(            "%s\n"                          % ( Tab['code']['init_fields']    ) )
         
        # Create Representation method
        f.write(    "    def __repr__(self):\n")
        f.write(    '        return "<%s('                  % ( table_name) )
        f.write('%s)>" %% \\\n                (%s)\n\n'     % ( Tab['code']['parameters'], \
                                                                Tab['code']['self_fields']    ) )
    
    # ------------------------------------------------------------------
    # Conditional include methods
    # ------------------------------------------------------------------
    if os.path.isfile(file_flask_methods):
        Include_File(file_flask_methods,f)

    #f.write(Dash)
    f.close()

    # ------------------------------------------------------------------
    # Create Class Form
    # ------------------------------------------------------------------
    
    file_name = auto_forms+"/frm_"+Tab['table'].lower()+".py"
    print_log("Creating '%s'..."%(file_name))

    f = open(file_name,"w")
    f.write(Dash)
    f.write(Do_not_modify)
    f.write(Dash)
    f.write('\n')
       
    f.write(    "from decimal import ROUND_HALF_UP\n\n")        
    f.write(    "class frm_%s(Form):\n"%(class_name))

    s=''
    xchoices = []
    
    for c in Tab['columns']:
        x=''
        xchoices.append("")
        try:
            form_field = session.query(Forms).filter(Forms.Table==table_name,Forms.Field==c['field']).one()
        except Exception as e:
            print("Table : ",Tab['table'])
            print("Processing column: ",c)
            print("EXCEPCION:",e)
            continue
            
        if form_field is not None:
            
            # Check for Foreign Keys
            if form_field.Foreign_Key is not None:
                if form_field.Foreign_Key != 'NULL':
                    c['form_type']='SelectField'
                    try:
                        Tab['code']['get_choices'] = Tab['code']['get_choices'] + "        form.%s.choices = db.session.query(%s.%s,%s.%s).order_by(%s.%s).all()\n"%(
                                form_field.Field,
                                Metadata['tables'][form_field.Referenced_Table]['class'],form_field.Foreign_Key,
                                Metadata['tables'][form_field.Referenced_Table]['class'],form_field.Foreign_Value,
                                Metadata['tables'][form_field.Referenced_Table]['class'],form_field.Foreign_Value
                                )
                    except Exception as e:
                        print("ERROR: form_field = ",form_field)
                        print("ERROR: Generating choices for class=%s field=%s"%(class_name,c['field']))
                        print("1",form_field.Field)
                        print("2",Metadata['tables'][form_field.Referenced_Table]['class'])
                        print("3",form_field.Foreign_Key)
                        print("4",Metadata['tables'][form_field.Referenced_Table]['class'])
                        print("5",form_field.Foreign_Field)
                        print("5",form_field.Foreign_Value)
                        print("EXCEPTION:",e)
                        
                                                
            # Check for validators
            validators = ''
            if form_field.Validation:               # Incluir aqui codigo si se necesita mas de una validacion, incluyendo FKs
                validators = ", validators=[%s]"%form_field.Validation_String
                if    form_field.Validation_Type == "RF":
                    # Field will be a selection of the valid values only , depends on Valid Options 
                    c['form_type']='RadioField'

           # Check for DATE,TIME,DATETIME formats
            format = ''
            coerce = ''
            parameters = ''
            if   c['form_type'] == "DateField":               
                format=', format=\'%Y-%m-%d\''                    
            elif c['form_type'] == "TimeField":               
                format=', format=\'%H-%M-%S\''                    
            elif c['form_type'] == "DateTimeField":               
                format=', format=\'%Y-%m-%d %H:%M:%S\''                    
            elif c['form_type'] == "DecimalField":               
                parameters=', places=6, rounding=ROUND_HALF_UP'                    

            # Creating form field depending on Field Type
            if c['form_type'] == "SelectField" or c['form_type'] == "RadioField":
                if c['type_flask'] == "db.Integer":
                    coerce = ", coerce=int"
            # Avoid Generation of Primary Key fields edition field       
            if form_field.Key=='PRI' and form_field.Extra=='auto_increment':
                Tab['primary_key_auto_increment']=form_field.Field
            else:
                if c['is_form_editable']:
                    f.write("    %-*s = %s(\"%s?\"%s%s%s%s)\n"%( Tab['max_column_name_length']+8,c['field'], 
                        c['form_type'], 
                        form_field.Caption_String,
                        coerce,
                        validators,
                        format,
                        parameters)
                        )
                
            c.update({'header':form_field.Caption_String})
        else:
            c.update({'header':COLUMNS[c][0]})
            
    f.write(    "\n" )
    f.write(    "    %-*s = SubmitField  ('Save')\n"%(Tab['max_column_name_length']+8,"submit_Save"))
    f.write(    "    %-*s = SubmitField  ('New')\n"%(Tab['max_column_name_length']+8,"submit_New"))
    
    f.write(    "    %-*s = SubmitField  ('Cancel')\n\n"%(Tab['max_column_name_length']+8,"submit_Cancel"))
    f.write(    "    %-*s = %s\n\n"%(Tab['max_column_name_length']+8,"has_FKs",Tab['has_fks']))

    #f.write(Dash)

    # ------------------------------------------------------------------
    # Create Class Form Delete
    # ------------------------------------------------------------------

    f.write(    "class frm_%s_delete(Form):\n"              % (class_name) )
    f.write(    "    %-*s = SubmitField  ('Delete')\n"      % (Tab['max_column_name_length']+8,"submit_Delete") )
    f.write(    "    %-*s = SubmitField  ('Cancel')\n\n"    % (Tab['max_column_name_length']+8,"submit_Cancel") )

    f.write(Dash)
    f.close()

    # ------------------------------------------------------------------
    # Create Class SQL Alchemy for direct non Flask DB Handling
    # ------------------------------------------------------------------

    file_name = auto_models+"/orm_"+Tab['table'].lower()+".py"
    file_name2= auto_models+"/orm_"+Tab['table'].lower()+"_table.py"
    print_log("Creating '%s'..."%(file_name))

    f = open(file_name,"w")
    f.write(Dash)
    f.write(Do_not_modify)
    f.write(Dash)
    f.write('\n')

    
    f.write("class %s(Base):\n"%(table_name))
    f.write("    __tablename__ = '%s'\n"%(table_name))
    f.write("    engine        = None\n")

    f2= open(file_name2,"w")
     
    f2.write( "    try:\n")
    f2.write( "        %s = Table(\n"%Tab['table'])
    f2.write( "                '%s',Meta,\n"%Tab['table'])
        
    for c in Tab['columns']:
    
        if (c['key'] == "PRI"):
            xkey=", primary_key=True"
        else:
            xkey=""
    
        for rel in Metadata['relations']:
            if rel['table_name'] == table_name and rel['column_name'] == c['field']:
                # GV 20190731 xrel=str(", ForeignKey('%s.%s')"%(rel['referenced_table_name'],rel['column_name']))   # rel[4] = Referenced Table rel[2] = FK field
                xrel=str(", ForeignKey('%s.%s')"%(rel['referenced_table_name'],rel['referenced_column_name']))   # rel[4] = Referenced Table rel[2] = FK field
                break
            else:
                xrel =""

        if (c['extra'].find('auto_increment') != -1):
            xextra=", autoincrement=True"
        else:
            xextra=""
    
        f.write(str("    %-*s = Column( %s%s%s%s )\n"%(Tab['max_column_name_length'],c['field'],c['type_sqlalchemy'],xrel,xkey,xextra)))
        f2.write(str("                Column( '%s',%s%s%s%s ),\n"%(c['field'],c['type_sqlalchemy'],xrel,xkey,xextra)))

    # ------------------------------------------------------------------
    # Conditional include properties
    # ------------------------------------------------------------------
    if os.path.isfile(file_orm_properties):
        Include_File(file_orm_properties,f)


    # Create Initialization method (Set to empty initialization now, just create instance)
    # 20190116 f.write(    "    def __init__(self,%s):\n"%Tab['code']['fields'])
    f.write(    "    \n")
    f.write(    "    def __init__(self,%s):\n"%Tab['code']['default_fields'])
    #f.write("%s\n"%none_fields)
    #f.write(    "        self.set(%s)\n\n"%Tab['code']['fields'])
    f.write(            "%s\n"                          % ( Tab['code']['init_fields']    ) )
    
    # Create Representation method
    f.write(    "    def __repr__(self):\n")
    f.write(str('        return "<%s('%(table_name)))

    f.write('%s)>" %% \\\n                (%s)\n\n'%(Tab['code']['parameters'],Tab['code']['self_fields']))

    # ------------------------------------------------------------------
    # Conditional include methods
    # ------------------------------------------------------------------
    if os.path.isfile(file_orm_methods):
        Include_File(file_orm_methods,f)

    #f.write(Dash)
    f.write('\n')
    
    f.close()
    f2.write("        )\n")
    f2.write("    except Exception as e:\n")
    f2.write("        print('EXCEPTION:',e)\n")
    f2.close()
    

