def Build_Iterations(Tab):
    s = ''
    Tab['code']['parameters']       = ''
    Tab['code']['fields']           = ''
    Tab['code']['default_fields']   = ''
    Tab['code']['dict_fields']      = ''
    Tab['code']['dict_nones']       = ''
    Tab['code']['nones']            = ''
    Tab['code']['init_fields']      = ''
    Tab['code']['none_fields']      = ''
    Tab['code']['self_fields']      = ''
    Tab['code']['self_parameters']  = ''
    Tab['code']['deep_fields']      = ''

    Tab['max_column_name_length'] = 0
    for c in Tab['columns']:
        Tab['max_column_name_length'] = max(Tab['max_column_name_length'],len(c['field']))    

    for c in Tab['columns']:
        colum   = c['field']
        if  'int' in c['type']:
            default = c['default']
        elif 'decimal' in c['type']:    
            default = c['default']
        elif 'tinyint' in c['type']:    
            default = "'True'" if c['default']=='TRUE' else "'False'"
        elif 'varchar' in c['type']:    
            default = "'%s'"%c['default']
        else:
            default = c['default']

        if default=='' or default==None:
            default='NULL'
            
        Tab['code']['parameters']             = Tab['code']['parameters']       + str("%s %s='%%s'"                         % (s,colum))
        Tab['code']['fields']                 = Tab['code']['fields']           + str("%s %s"                               % (s,colum))
        
        """
        if c['type'] in "time/date":
            Tab['code']['default_fields']     = Tab['code']['default_fields']   + str("%s %s=%s"                          % (s,colum,'None' if default=='NULL' else "'%s'"%default))
        else:
            if c['is_id']:
                Tab['code']['default_fields'] = Tab['code']['default_fields']   + str("%s %s=0"                             % (s,colum))
            else:
                Tab['code']['default_fields'] = Tab['code']['default_fields']   + str("%s %s=%s"                            % (s,colum,'None' if default=='NULL' else default))
        """
        if c['type'] in "time/date":
            #print("Table=%s Field=%s default=%s -> %s"%(Tab['table'],c['field'],c['default'],default))
            pass
        if c['is_id']:
            Tab['code']['default_fields'] = Tab['code']['default_fields']   + str("%s %s=0"                             % (s,colum))
        else:
            if c['type'] in "time/date":
                Tab['code']['default_fields'] = Tab['code']['default_fields']   + str("%s %s=%s"                            % (s,colum,'None' if default=='NULL' else "'%s'"%default))
            else:
                Tab['code']['default_fields'] = Tab['code']['default_fields']   + str("%s %s=%s"                            % (s,colum,'None' if default=='NULL' else default))
        
        if c['type'] == 'time':
            Tab['code']['dict_fields']        = Tab['code']['dict_fields']      + str("%s '%s':str(row.%s)"                 % (s,colum,colum))
        else:
            Tab['code']['dict_fields']        = Tab['code']['dict_fields']      + str("%s '%s':row.%s"                      % (s,colum,colum))
        
        Tab['code']['dict_nones']             = Tab['code']['dict_nones']       + str("%s '%s':None"                        % (s,colum))
        Tab['code']['nones']                  = Tab['code']['nones']            + str("%s None"                             % (s,))
        Tab['code']['init_fields']            = Tab['code']['init_fields']      + str("%sself.%-*s = %s\n"                  % (' '*8,Tab['max_column_name_length'],colum,colum))
        Tab['code']['none_fields']            = Tab['code']['none_fields']      + str("%sself.%-*s = None\n"                % (' '*8,Tab['max_column_name_length'],colum))
        Tab['code']['self_fields']            = Tab['code']['self_fields']      + str("%s self.%s"                          % (s,colum))
        Tab['code']['self_parameters']        = Tab['code']['self_parameters']  + str("%s %s='%%s'"                         % (s,colum))
        Tab['code']['deep_fields']            = Tab['code']['deep_fields']      + str("%s%sdeepcopy(self.%-*s , memo)\n"    % (' '*16,s,Tab['max_column_name_length'],colum))
        s = ','

