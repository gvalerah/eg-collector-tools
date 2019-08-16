# =============================================================================
# View for Get Billing Resume fro DB
# (c) Sertechno 2018
# GLVH @ 2018-11-11
# =============================================================================


from babel.numbers  import format_number, format_decimal, format_percent

@main.route('/reports/DB_Status', methods=['GET'])
@login_required
def reports_DB_Status():
    logger.debug('Enter: reports_DB_Status()'%())


    # Prepare query
    version  = db.engine.execute("SELECT VERSION()").fetchall()
    hostname = db.engine.execute("SELECT @@HOSTNAME").fetchall()
    query=  " SELECT table_schema as `Database`, table_name AS `Table`, round(((data_length + index_length) / 1024 / 1024), 2)" \
            "`Size in MB`  FROM information_schema.TABLES  WHERE table_schema = 'collector' ORDER BY (data_length + index_length) DESC"
    table_usage = db.engine.execute(query).fetchall()
    data={}
    data.update({'version': version[0][0]})
    data.update({'hostname': hostname[0][0]})
    data.update({'table_usage': table_usage})
    data.update({'table_data': {} })
    
    for t in range(len(data['table_usage'])):
        query = "SELECT count(*) FROM %s"%data['table_usage'][t][1]
        count=db.engine.execute(query).fetchall()
        data['table_data'].update({data['table_usage'][t][1]:{}})
        data['table_data'][data['table_usage'][t][1]].update({'count':count[0][0]})
        
    return render_template('report_db_status.html',data=data)

# =============================================================================


