from gen_models.Forms               import Forms
   
def Populate_Table_Columns(Metadata,Tab,session):   
    # Populate table's columns data
    
    #print("        Populating columns for %s"%Tab['table'])
    
    table_name = Tab['table']
    class_name = Tab['class']

    # Populate Relationship & Other column data for Table & Columns
                
    for cc in Tab['columns']:
        try:
            form_field = session.query(Forms).filter(Forms.Table==table_name,Forms.Field==cc['field']).one()
        except Exception as e:
            print("*******************************************************************************************")
            print("Populate_Table_Columns: Error populating '%s'.'%s'"%(table_name,cc['field']))
            print("Populate_Table_Columns: Check Record in Dev_Forms for '%s'.'%s'"%(table_name,cc['field']))
            print("Populate_Table_Columns: WARNING !!! RESULT CODE MAY BE INCOMPLETE !!!")
            print("EXCEPTION:",e)
            print("*******************************************************************************************")
            continue
        cc.update({'is_form_editable': form_field.Form_Editable})
        cc.update({'format': form_field.Field_Format})
        cc.update({'order': form_field.Field_Order})
        for rel in Metadata['relations']:
            if rel['table_name'] == table_name and rel['column_name'] == cc['field']:
                # Get Related Data
                #form_field = session.query(Forms).filter(Forms.Table==table_name,Forms.Field==cc['field']).one()
                Tab['has_relations'] = True
                Tab['has_fks'] = True
                cc.update({'is_fk': True})
                cc.update({'foreign_field':form_field.Foreign_Field})
                break
            else:
                cc.update({'is_fk': False})
                cc.update({'foreign_field':None})
                       
    # ---------------------------------------------------------------------------------------
    # Populate Type & Keys Data               
    for cc in Tab['columns']:

        # Setup SQL-Alchemy Types
        # Setup Flask Column types depending on original Type
        cc['type_sqlalchemy'] = cc['type_sqlalchemy'].replace("int(11)","Integer") 
        cc['type_sqlalchemy'] = cc['type_sqlalchemy'].replace("tinyint(4)","Boolean") 
        cc['type_sqlalchemy'] = cc['type_sqlalchemy'].replace("varchar","String") 
        cc['type_sqlalchemy'] = cc['type_sqlalchemy'].replace("date","Date") 
        # Necesary to avoid problem with Time Field in Forms (DateTime?)
        # GV 20181208 cc['type_sqlalchemy'] = cc['type_sqlalchemy'].replace("time","String(10)")
        cc['type_sqlalchemy'] = cc['type_sqlalchemy'].replace("time","Time")
        cc['type_sqlalchemy'] = cc['type_sqlalchemy'].replace("datetime","DateTime")
        cc['type_sqlalchemy'] = cc['type_sqlalchemy'].replace("float","Numeric") 
        cc['type_sqlalchemy'] = cc['type_sqlalchemy'].replace("decimal","Numeric") 

        # Setup Flask Column types depending on original Type
        cc['type_flask'] = cc['type_flask'].replace("int(11)","db.Integer") 
        cc['type_flask'] = cc['type_flask'].replace("tinyint(4)","db.Boolean") 
        cc['type_flask'] = cc['type_flask'].replace("varchar","db.String") 
        cc['type_flask'] = cc['type_flask'].replace("datetime","db.DateTime")
        cc['type_flask'] = cc['type_flask'].replace("date","db.Date") 
        # Necesary to avoid problem with Time Field in Forms (DateTime?)
        # GV 20181208 cc['type_flask'] = cc['type_flask'].replace("time","db.String(10)")
        cc['type_flask'] = cc['type_flask'].replace("time","db.Time")
        cc['type_flask'] = cc['type_flask'].replace("float","db.Numeric") 
        cc['type_flask'] = cc['type_flask'].replace("decimal","db.Numeric") 
        
        # Checking for Basic Form Field Type depending on Flask DB Column Type
        if      cc['type_flask'].find('db.Integer')     != -1:
                cc['form_type'] = 'IntegerField'
        elif    cc['type_flask'].find('db.String')      != -1:
                cc['form_type'] = 'StringField'
        elif    cc['type_flask'].find('db.Boolean')     != -1:
                cc['form_type'] = 'BooleanField'
        elif    cc['type_flask'].find('db.DateTime')    != -1:
                cc['form_type'] = 'DateTimeField'
        elif    cc['type_flask'].find('db.Date')        != -1:
                cc['form_type'] = 'DateField'
        elif    cc['type_flask'].find('db.Time')        != -1:
                cc['form_type'] = 'TimeField'
        elif    cc['type_flask'].find('db.Numeric')     != -1:
                cc['form_type'] = 'DecimalField'
        
        # Checking for primary key fields and flagging   
                
        if  cc['key'] == 'PRI':
            Tab['keys'].append(cc['field'])
        if  cc['key'] == 'PRI' and cc['extra'] == 'auto_increment':
            cc['is_id']     = True
        else:
            cc['is_id']     = False
        
        # Define default headers    
        cc['header']     = cc['field']
        
        # Calculates max column name length
        if len(cc['field']) > Tab['max_column_name_length']:
            Tab['max_column_name_length'] = len(cc['field'])
        
        # Flag if its a time field
        cc.update({'is_time':True if cc['type'] == 'time' else False})
                
        # Code iterator for primary keys, may be moved to iterator module                
        # --------------------------------------------------------------------------------------------------------------------------------------------------
        if (cc['key'] == "PRI"):
            xkey=", primary_key=True"
            if (len(Tab['code']['key_fields']) == 0):
                Tab['code']['key_fields'] = Tab['code']['key_fields'] + "%s"                        % (cc['field'])
                Tab['code']['key_filter'] = Tab['code']['key_filter'] + "%s.%s == %s"               % (class_name,cc['field'],cc['field'])
                Tab['code']['key_params'] = Tab['code']['key_params'] + "<%s>"                      % (cc['field'])
                Tab['code']['key_redirs'] = Tab['code']['key_redirs'] + "%s=session['data']['%s']"  % (cc['field'],cc['field'])
                if Tab['has_fks']:
                    Tab['code']['row_keys']   = Tab['code']['row_keys']   + "%s={{ row.0.%s }}"              % (cc['field'],cc['field'])
                else:
                    Tab['code']['row_keys']   = Tab['code']['row_keys']   + "%s={{ row.%s }}"              % (cc['field'],cc['field'])
                
            else:
                Tab['code']['key_fields'] = Tab['code']['key_fields'] + ",%s"                       % (cc['field'])
                Tab['code']['key_filter'] = Tab['code']['key_filter'] + ",%s.%s == %s"              % (class_name,cc['field'],cc['field'])
                Tab['code']['key_params'] = Tab['code']['key_params'] + "&<%s>"                     % (cc['field'])
                Tab['code']['key_redirs'] = Tab['code']['key_redirs'] + ",%s=session['data']['%s']" % (cc['field'],cc['field'])
                if Tab['has_fks']:
                    Tab['code']['row_keys']   = Tab['code']['row_keys']   + "&%s={{ row.0.%s }}"             % (cc['field'],cc['field'])
                else:
                    Tab['code']['row_keys']   = Tab['code']['row_keys']   + "&%s={{ row.%s }}"             % (cc['field'],cc['field'])
            Tab['num_key_fields'] += 1
        else:
            xkey=""
            if (len(Tab['code']['non_keys_fields']) == 0):
                Tab['code']['non_keys_fields'] = Tab['code']['non_keys_fields'] + "%s.%s : %s"      % (table_name,cc['field'],cc['field'])
            else:
                Tab['code']['non_keys_fields'] = Tab['code']['non_keys_fields'] + ",%s.%s : %s"     % (table_name,cc['field'],cc['field'])
        # --------------------------------------------------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------



