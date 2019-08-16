# Import create_engine function
from sqlalchemy import create_engine
from sqlalchemy import text

# Create an engine to the census database
engine = create_engine('mysql+pymysql://root:Zj1245//$$@127.0.0.1:3306/collector')

# Print the table names
print(engine.table_names())
T=engine.table_names()
    

# Get Table Names using text SQL Command
query = text('SHOW TABLES')

TABLES = engine.execute(query).fetchall()

map_folder="map"
model_folder="model"

model_name='%s/map_functions.py'%(model_folder)
m=open(model_name,'w')

    
for t in range(len(TABLES)):
    file_name='%s/map_%s.json'%(map_folder,TABLES[t][0])
    model_name='%s/map_%s.py'%(model_folder,TABLES[t][0])
    print('Creating %s ...'%file_name)
    f=open(file_name,'w')
    f.write('{\n')
    f.write('  "metadata":{\n')
    f.write('             "name":"%s full map",\n'%TABLES[t][0])
    f.write('             "table_name":"%s"\n'%TABLES[t][0])
    f.write('             },\n')
    f.write('  "fields":[\n')
    
    query = text('SHOW COLUMNS FROM '+TABLES[t][0])
    COLUMNS = engine.execute(query).fetchall()
    row_sep=' '
    
    id_field=None
    code_field=None
    description_field=None
    
    for c in range(len(COLUMNS)):
        f.write('    %s{'%row_sep,)
        f.write(              '"name":"%s",'%COLUMNS[c][0])
        f.write(              '"type":"%s",'%COLUMNS[c][1])
        f.write(              '"null":"%s",'%COLUMNS[c][2])
        f.write(              '"key":"%s",'%COLUMNS[c][3])
        f.write(              '"default":"%s",'%COLUMNS[c][4])
        f.write(              '"extra":"%s",'%COLUMNS[c][5])
        f.write(              '"output":"True",')
        f.write(              '"export_name":"%s",'%COLUMNS[c][0])
        
        type=COLUMNS[c][1]

        quote='False'
        isid='False'
        iscode='False'
        isdescription='False'
        
        if ('id' == COLUMNS[c][0]):
            isid = 'True'
        if ('_Id' in COLUMNS[c][0]):
            isid = 'True'
        if ('_Code' in COLUMNS[c][0]):
            iscode = 'True'
        if ('_Name' in COLUMNS[c][0]):
            isdescription = 'True'
        if ('_Description' in COLUMNS[c][0]):
            isdescription = 'True'
        
        if isid=='True':
            id_field=COLUMNS[c][0]
        
        if (iscode=='True' and code_field==None):
            code_field=COLUMNS[c][0]
        
        if isdescription=='True':
            description_field_field=COLUMNS[c][0]
        
        
        
        if      ('tinyint' in type):
            format = '%d'
            length=1
            precision=0
        elif    ('int' in type):
            format = type.replace('int','%0')+'d'
            length=11
            precision=0
        elif    ('varchar' in type):
            format = type.replace('varchar','%-')+'s'
            xtype=type.split('(')
            xtype=xtype[1].split(')')
            length=int(xtype[0])
            precision=0
            quote='True'
        elif    ('date' in type):
            format = '%Y-%m-%d'
            length=10
            precision=0
            quote='True'
        elif    ('time' in type):
            format = '%H:%M:%S'
            length=8
            precision=0
            quote='True'
        elif    ('datetime' in type):
            format = '%Y-%m-%d %H:%M:%S'
            length=9
            precision=0
            quote='True'
        elif    ('float' in type):
            xtype=type.split('(')
            xtype=xtype[1].split(')')
            xtype=xtype[0].replace(',','.')
            format = '%%0%sf'%xtype
            xtype=xtype.split('.')
            length=int(xtype[0])
            precision=int(xtype[1])            
        elif    ('decimal' in type):
            xtype=type.split('(')
            xtype=xtype[1].split(')')
            xtype=xtype[0].replace(',','.')
            format = '%%0%sf'%xtype
            xtype=xtype.split('.')
            length=int(xtype[0])
            precision=int(xtype[1])            

        format = format.replace('(','')
        format = format.replace(')','')
        
        f.write(              '"length":"%d",'%length)
        f.write(              '"precision":"%d",'%precision)
        f.write(              '"quote":"%s",'%quote)
        f.write(              '"format":"%s",'%format)
        f.write(              '"isid":"%s",'%isid)
        f.write(              '"iscode":"%s",'%iscode)
        f.write(              '"isdescription":"%s"'%isdescription)
        f.write(              '}\n')
        
        row_sep=','

    T=TABLES[t][0]

    m.write('    """ Functions for %s """\n'%T)

    if ((id_field is not None) and (code_field is not None)):
        m.write('    def get_%s_id_from_code(code):\n'%T)
        m.write('       id=session.query(%s.%s).filter(%s.%s==code).one_or_None()\n'%(T,id_field,T,code_field))
        m.write('       return id\n\n')
        m.write('    def get_%s_code_from_id(id):\n'%T)
        m.write('       code=session.query(%s.%s).filter(%s.%s==id).one_or_None()\n'%(T,code_field,T,id_field))
        m.write('       return code\n\n)')
        
    if ((id_field is not None) and (description_field is not None)):
        m.write('    def get_%s_id_from_description(description):\n'%T)
        m.write('       id=session.query(%s.%s).filter(%s==description).one_or_None()\n'%(T,id_field,T,description_field))
        m.write('       return id\n\n')
        m.write('    def get_%s_description_from_id(id):\n'%T)
        m.write('       description=session.query(%s.%s).filter(%s==id).one_or_None()\n'%(T,id_description,T,id_field))
        m.write('       return id\n\n')

    if ((code_field is not None) and (description_field is not None)):
        m.write('    def get_%s_code_from_description(description):\n'%T)
        m.write('       code=session.query(%s.%s).filter(%s==description).one_or_None()\n'%(T,code_field,T,description_field))
        m.write('       return code\n\n')
        m.write('    def get_%s_description_from_code(code):\n'%T)
        m.write('       description=session.query(%s.%s).filter(%s==code).one_or_None()\n'%(T,id_description,T,code_field))
        m.write('       return code\n\n')


       
    f.write(' ]\n')
    f.write('}\n')
    f.close()
m.close()
