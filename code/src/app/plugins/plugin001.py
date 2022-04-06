import os
import jinja2
from emtec.plugins import Plugin

template_main = """
<H1>name={{name}}</H1>
<table border = 1>
    <thead>
        <tr>
            <th>kwarg</th>
            <th>Value</th>
        </tr>
    </thead>
    <tbody>
    <tr><td>name</td>             <td>{{name}}</td></tr>
    <tr><td>title</td>            <td>{{title}}</td></tr>
    <tr><td>short description</td><td>{{short_description}}</td></tr>
    <tr><td>long description</td> <td>{{long_description}}</td></tr>
    <tr><td>app</td>              <td>{{app.name}}</td></tr>
    <tr><td>user</td>             <td>{{user.id}}</td></tr>
    <tr><td>request</td>          <td>{{request.method}}</td></tr>
    <tr><td>db</td>               <td>{{db.engine}}</td></tr>
    <tr><td>logger</td>           <td>{{logger.name}}</td></tr>
    <tr><td>kwargs</td>           <td>{{kwargs}}</td></tr>
    {% for kwarg in kwargs %}
        <tr>
            <td>{{kwarg}}</td>
            <td>{{kwargs[kwarg]}}</td>
        </tr>
    {% endfor %}
    </tbody>
</table>
data={{data}}
"""

class Instance(Plugin):
    name      = 'plugin001'
    version   = '1.0.1'
    templates = {'main':template_main}
    kwargs    = {}
    title     = 'Plugin 001'
    short_description = 'English short description'
    long_description  = 'English long description for Plugin 001'
    format = 'html_body'

    def execute(self,**kwargs):
        print("-----")
        print(f"{self.name}.execute()")
        # will render template here
        # Overrrides predefined data in execute call 
        self.kwargs=kwargs
        # all call arguments will become instance attributes
        # sets up kwargs for expansion oportunities
        for kwarg in kwargs:
            setattr(self,kwarg,kwargs.get(kwarg))
            #print (f"added attribute {kwarg} to instance = {kwargs.get(kwarg)}")
        #self.details()
        # Initialize Instance variables
        result = None
        filesystem_template = f"{self.folder}/{self.name}.html".lower()
        # Plugin logic that calls complex functions tree
        self.data.update({'other':self.func1("execute: module level")})
        # validates is filesystem template available
        if os.path.isfile(filesystem_template):
            # if so overrrides default, if any
            templateLoader = jinja2.FileSystemLoader(searchpath=self.folder)
            templateEnv    = jinja2.Environment(loader=templateLoader)
            tm =  templateEnv.get_template(filesystem_template)
            print(f"{self.name} rendering filesystem template {filesystem_template}")
            result = tm.render(**kwargs)
        elif self.templates.get('main'):
            tm = jinja2.Environment(loader=jinja2.BaseLoader).from_string(self.templates['main'])
            print(f"{self.name} rendering default memory template")
            #result = tm.render(data=self.data,kwargs=kwargs)
            result = tm.render(**kwargs)
        else:
            result = None # abort(500,'??????')
        return result

# Plugin internal functions, all plugin hidden logic need to happen 
# within them
    def func1(self,msg):
        #print(self.func1)
        return self.func2(f"{msg} func1: pass through")

    def func2(self,msg):
        #print(self.func2)
        return self.func3(f"{msg} func2: pass through")

    def func3(self,msg):
        #print(self.func3)
        return f"{msg} func3: last level reached!!!!"

