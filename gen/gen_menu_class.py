import os

f=None
#open(menu_file_name,'w')
oc="<!--"
cc="-->"

# Constants
HOME                = 0
CUSTOMER            = 1
TABLES              = 2
PROCESSES           = 3
REPORTS             = 4
OPTIONS             = 5
HELP                = 6
ACCOUNT             = 7

ROLE_CUSTOMER       = 1
ROLE_REPORTER       = 2
ROLE_CHARGER        = 3
ROLE_ADMINISTRATOR  = 4
ROLE_AUDITOR        = 5
ROLE_GOD            = 6

class Generate_Collector_Menu():

    # General folder definitions
    app_name                =   "Collector"
    home_folder             =   "~"
    suite_folder            =   "~/GIT/EG-Suite-Tools/Collector"
    tools_folder            =   "~/GIT/EG-Collector-Tools"
    collector_folder        =   "~/GIT/EG-Collector"

    def __init__(self,jsonfile=None):
        if jsonfile is not None:
            with open(jsonfile, 'r') as f:
                json_data = json.load(f)
            
            self.app_name                =   json_data['app_name']
            self.home_folder             =   json_data['home_folder']
            self.suite_folder            =   json_data['suite_folder']+ self.app_name
            self.tools_folder            =   json_data['tools_folder']
            self.collector_folder        =   json_data['collector_folder']
        self.suite_code_folder       =   self.suite_folder        + "/code"
        self.code_folder             =   self.tools_folder        + "/code"

        # Auto Code main folders
        self.suite_auto_folder       =   self.suite_code_folder   + "/auto"
        self.suite_auto_views        =   self.suite_auto_folder         + "/views"
        self.suite_auto_templates    =   self.suite_auto_folder         + "/templates"
        self.suite_auto_models       =   self.suite_auto_folder         + "/models"
        self.suite_auto_forms        =   self.suite_auto_folder         + "/forms"
        self.suite_auto_includes     =   self.suite_auto_folder         + "/includes"

        # Source Folders
        self.auto_folder             =   self.code_folder         + "/auto"
        self.auto_templates          =   self.auto_folder         + "/templates"
        self.source_folder           =   self.code_folder         + "/src"
        self.source_includes         =   self.source_folder       + "/include"

        # Output Final versions
        self.output_folder           =   self.code_folder         + "/output"

        self.style_file_name         =   self.source_includes+"/collector_style.css"
        self.navbar_file_name        =   self.source_includes+"/html/collector_navbar.html" 
        self.menu_file_name          =   self.source_includes+"/menu.html"
        self.base_file_name          =   self.auto_templates+"/base.html"
        
    def Include_File(self,file_name,f):
        with open(file_name,'r') as fp:
            line = fp.readline()
            cnt=1
            while line:
                f.write(line)
                line = fp.readline()
                cnt += 1
        print('\tInclude_File():',file_name,"included.")   

    def Delete_File(self,file_name):
        os.remove(file_name)
        print('\tDelete_File():',file_name,"removed.")   

    def Comment(self,comment,f):
        c="%s %-*s %s"%(oc,72,comment,cc)
        print(c)
        f.write("%s\n"%(c))

    def Gen_SubOption(self,suboption,f):
        f.write(    '                      <!-- gen_menu_functions - Gen_SubOption -->\n')
        if suboption['header'] is not None:
            f.write('                      <b>%s</b>\n'%(suboption['header']))
        f.write(    '                      <a class="dropdown-item" href="%s">%s</a>\n'%(suboption['url'],suboption['name']))
        if suboption['hr']:
            f.write('                      <hr>\n')
        f.write(    '                      <!-- -------------------------------gso -->\n')

    def Gen_Option(self,option,f):

        f.write(    '          {%- if current_user.is_authenticated -%}\n')
        f.write(    '            {%%- if current_user.role.id in %s -%%}\n'%str(option['roles']))
        f.write(    '              <!-- ------------------------------- -->\n')
        f.write(    '              <!-- gen_menu_functions - Gen_Option -->\n')
        f.write(    '              <!-- ------------------------------- -->\n')    

        if len(option['options']) == 0:
            f.write('                <a class="dropdown-item" href="%s">%s</a>\n'%(option['url'],option['name']))
        else:
            f.write('                <!-- Dropdown -->\n')
            f.write('                  <li class="nav-item dropdown">\n')
            f.write('                    <a class="nav-link dropdown-toggle" href="/" id="navbardrop" data-toggle="dropdown">%s</a>\n'%(option['name']))
            f.write('                    <div class="dropdown-menu">\n')
            c=0
            for suboption in option['options']:
                Gen_SubOption(suboption,f)
            f.write('                    </div>\n')
            f.write('                  </li>\n')
        f.write(    '              <!-- -----------------------------go -->\n')
        f.write(    '            {%- endif -%}\n')
        f.write(    '          {%- endif -%}\n')
        
    def Gen_Menu(self,Menu,ACCOUNT,filename=None):
        if filename is None:
            filename=navbar_file_name
        f=open(filename,'w')
        print("%s: Gen_Menu() is writing file '%s' ..."%(__name__,filename))
        f.write('    <!-- ----------------------------- -->\n')
        f.write('    <!-- gen_menu_functions - Gen_Menu -->\n')
        f.write('    <!-- ----------------------------- -->\n')
        f.write('    <nav class="navbar navbar-expand-sm bg-dark navbar-dark navbar-fixed-top" data-spy="affix" data-offset-top="197" style="position: fixed;top: 0;width: 100%;">\n')
        f.write('      <div class="container-fluid">\n')
        
        #GV 20190408
        f.write('      <div id="navbarCollapse" class="collapse navbar-collapse">\n')
        
        
        f.write('        <!-- Brand -->\n')
        f.write('        <a class="navbar-brand" href="http://www.emtecgroup.net"><img src="/static/img/logo_emtec.jpg" title="" alt="Emtec Group" ></a>\n')
        f.write('        <!-- Links -->\n')
        f.write('        <ul class="navbar-nav">\n')
        for option in Menu:
            Gen_Option(option,f)
        f.write('        </ul>\n')
        
        
        # GV 20181123 Include Login call in Nav Bar -->
        #f.write('        <ul class="navbar navbar-nav navbar-right">\n')
        f.write('        <ul class="navbar navbar-nav">\n')
        f.write('          {%- if current_user.is_authenticated -%}\n')
        
        # Account Sub-Menu depends on authentication state so it's added only when needed
        Menu.append(Option('<h3>Account</h3>'))
        
        Menu[ACCOUNT]['roles']=(ROLE_CUSTOMER,ROLE_REPORTER,ROLE_CHARGER,ROLE_ADMINISTRATOR,ROLE_AUDITOR,ROLE_GOD)
        
        Menu[ACCOUNT]['options'].append(Sub_Option('Register User',     url='/auth/register',hr=True))
        Menu[ACCOUNT]['options'].append(Sub_Option('Change Password',   url='/auth/change-password'))
        Menu[ACCOUNT]['options'].append(Sub_Option('Change Email',      url='/auth/change-email'))
        Menu[ACCOUNT]['options'].append(Sub_Option('Log Out',           url='/auth/logout'))
        
        Gen_Option(Menu[ACCOUNT],f)

        # GV 20181123 Include Login call in Nav Bar -->
        f.write('          {%- else -%}\n')
        f.write('          <li><a href="{{ url_for(\'auth.login\') }}"><h3>Log In</h3></a></li>\n')
        f.write('          {%- endif -%}\n')
        f.write('        </ul>\n')

        # GV 20190408
        f.write('      </div>\n')

        f.write('      </div>\n')
        f.write('    </nav>\n')
        f.write('    <!-- ----------------------------- -->\n')
        f.close()

    def Doc_bottom(self,f):
        f.write('</html>\n')
        
    def Doc_head(self,f):
        f.write('<!DOCTYPE html>\n')
        f.write('<html>\n')

    def Style(self):
        f=open(style_file_name,'w')

        f.write('.navbar {\n')
        f.write('    overflow: hidden;\n')
        f.write('    background-color: #333;\n')
        f.write('    font-family: Arial, Helvetica, sans-serif;\n')
        f.write('}\n')

        f.write('.navbar a {\n')
        f.write('    float: left;\n')
        f.write('    font-size: 16px;\n')
        f.write('    color: white;\n')
        f.write('    text-align: center;\n')
        f.write('    padding: 14px 16px;\n')
        f.write('    text-decoration: none;\n')
        f.write('}\n')

        f.write('.dropdown {\n')
        f.write('    float: left;\n')
        f.write('    overflow: hidden;\n')
        f.write('}\n')

        f.write('.dropdown .dropbtn {\n')
        f.write('    font-size: 16px;\n')
        f.write('    border: none;\n')
        f.write('    outline: none;\n')
        f.write('    color: white;\n')
        f.write('    padding: 14px 16px;\n')
        f.write('    background-color: inherit;\n')
        f.write('    font-family: inherit;\n')
        f.write('    margin: 0;\n')
        f.write('}\n')

        f.write('.navbar a:hover, .dropdown:hover .dropbtn {\n')
        f.write('    background-color: red;\n')
        f.write('}\n')

        f.write('.dropdown-content {\n')
        f.write('    display: none;\n')
        f.write('    position: absolute;\n')
        f.write('    background-color: #f9f9f9;\n')
        f.write('    min-width: 160px;\n')
        f.write('    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);\n')
        f.write('    z-index: 1;\n')
        f.write('}\n')

        f.write('.dropdown-content a {\n')
        f.write('    float: none;\n')
        f.write('    color: black;\n')
        f.write('    padding: 12px 16px;\n')
        f.write('    text-decoration: none;\n')
        f.write('    display: block;\n')
        f.write('    text-align: left;\n')
        f.write('}\n')

        f.write('.dropdown-content a:hover {\n')
        f.write('    background-color: #ddd;\n')
        f.write('}\n')

        f.write('.dropdown:hover .dropdown-content {\n')
        f.write('    display: block;\n')
        f.write('}\n')
        
        f.close()
       
    def Header(self,f):
        f.write('<head>\n')
        f.write('  <meta name="viewport" content="width=device-width, initial-scale=1">\n')
        f.write('  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">\n')
        f.write('<style>\n')
        f.write('body{ margin-top: 129px; }')    
        Include_File(style_file_name,f)
        f.write('\n</style>\n')    
        f.write('</head>\n')
        
    def Gen_Doc(self):
        f=open(menu_file_name,'w')
        Doc_head(f)
        Header(f)
        f.write('<body>\n')
        Include_File(navbar_file_name,f)
        f.write('\n')
        f.write('<h3>Dropdown Menu inside a Navigation Bar</h3>\n')
        f.write('<p>Hover over the "Dropdown" link to see the dropdown menu.</p>\n')
        f.write('</body>\n')
        Doc_bottom(f)
        f.close()

    def Option(self,name,url='/'):
        return {'name':name,'url':url,'options':[],'roles':()}    
        
    def Sub_Option(self,name,url='/under_construction',hr=False,header=None):
        return {'name':name,'url':url,'hr':hr,'header':header}    

