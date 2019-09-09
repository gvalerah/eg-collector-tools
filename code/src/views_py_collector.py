""" Application decorators for routes """
""" Decorators specify main routes to be handled by Collector Solution """

"""
@main.route('/', methods=['GET', 'POST'])
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
"""
       
@main.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

@main.route('/reports/<report>&<customer>&<fromx>&<tox>&<currency>')
def reports(report,customer,fromx,tox,currency):
    logger.debug("reports() IN %s,%s,%s,%s,%s"% (report,customer,fromx,tox,currency))

    r = page_header()
    r+= '<h1>Get \'%s\' for customer %s in period %s to %s cur=%s</h1>' % (report,customer,fromx,tox,currency)
    # SQL Query call here
    #query = text("C*ALL Get_Billing_Resume(%s,'%s','%s',1,'%s')"%(customer,fromx,tox,currency))
    try:
        #result = C.db.execute(query).fetchall()
        result = C.db.Get_Billing_Resume(customer,fromx,tox,1,currency)
    except Exception as e:
        r+="<h2>EXCEPTION:%s</h2>"%e
    r+="<table>"
    sum=0.0
    for row in result:
        r+='<tr>'
        for c in range(len(row)):
            r+="<td>%s</td>"%str(row[c])
        sum+=row[25]
        r+="<td>%.2f</td>"%sum
        r+='</tr>'
    r+="</table>"
    r+="<p>Total in %s = %10.2f<p>"%(currency,sum)
    r+=page_footer()
    logger.debug("reports() OUT %s"% (r))
    return r

@main.route('/table/<name>')
def table(name):
    logger.debug("table() IN %s"% (name))

    r = page_header()
    r+= '<h1>Get \'%s\' data</h1>' % (name)

    # SQL Query call here
    
    try:
        # Build Query
        query = text("SELECT * FROM %s"%(name))

        # Get keys (column names) from Query        
        keys=C.db.execute(query).keys()
        
        r+="<p>Query=%s</p>"%str(query)
        r+="<p>Keys =%s</p>"%str(keys)
        r+="<table>"
        r+='<tr style="border:2px solid blue ; background-color:blue; color:yellow">'
        for key in keys:
           r+="<td><b>%s</b></td>"%key
        r+='</tr>'           
               
        result=None
        result = C.db.execute(query).fetchall()
        rc = 0
        for row in result:
            if (rc%2):
                r+='<tr style="background-color:cyan">'
                #r+='<tr id="tr01">'
            else:
                r+='<tr style="background-color:white">'
                #r+='<tr id="tr02">'
            
            for c in range(len(row)):
                r+="<td>%s</td>"%str(row[c])
            r+='</tr>'
            rc+=1
        r+="</table>"
        if rc:
            r+="<p>Count=%s</p>"%str(rc)
    except Exception as e:
        r+="<h2>EXCEPTION:%s</h2>"%e
    r+=page_footer()
    logger.debug("table() out %s"% (r))
    return r

@main.route('/query/<name>')
def query(name):
    logger.debug("query() IN %s"% (name))

    # SQL Query call here    
    try:
        # Build Query
        query = text("SELECT * FROM %s"%(name))

        # Get keys (column names) from Query        
        keys=C.db.execute(query).keys()

        rows = C.db.execute(query).fetchall()
    except Exception as e:
        msg="EXCEPTION: %s"%e
        logger.error("query() %s"% (msg))
        return "<h2>%s</h2>"%msg
    
    logger.debug("query() out")
    return render_template('query.html',name=name,keys=keys,rows=rows,count=len(rows))

@main.route('/query_orm/<table_name>')
def query_orm(table_name):
    logger.debug("query() IN %s"% (table_name))
    # SQL Query call here    
    try:
        Session = sessionmaker(bind=C.db)  
        session=Session()
        keys = ("ID","NOMBRE","CC")
        rows = session.query(Customers.Cus_Id,Customers.Cus_Name,Customers.CC_Id).all()
    except Exception as e:
        msg="EXCEPTION: %s"%e
        logger.error("query() %s"% (msg))
        return "<h2>%s</h2>"%msg
    
    logger.debug("query() out")
    return render_template('query_orm.html',name=table_name,keys=keys,rows=rows,count=len(rows))
    
