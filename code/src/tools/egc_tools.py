import  sys
import  warnings
import  math
import  pandas as pd
import  argparse
import  re
import  random
from    collections                     import namedtuple
from    getpass                         import getpass
from    pprint                          import pprint,pformat
from    time                            import strptime

from    sqlalchemy                      import create_engine
from    sqlalchemy.orm                  import sessionmaker
from    sqlalchemy                      import func

import  simplejson  as json
import  collections

from    emtec                           import *
from    emtec.collector.db.orm_model    import *
from    emtec.common.stats_functions    import *
# Tool specific functions
# Candidate to go to emtec.collector.db.orm_model.py
# parameter is a binded session
# returns the list of sharding tables for base table
def get_tables_list(session,sharded_table_name=None):
    tables_list=[]
    if session is not None:
        # Get list of tables in binded schema
        sentence="SHOW TABLES"
        result=session.execute(sentence)
        # Get List of tables matching shardedctable name
        for row in result:
            table_name=row[0]
            if sharded_table_name is not None:
                pattern="^%s_.*$"%sharded_table_name
                if re.match(pattern,table_name) is not None:
                    records_count=session.execute("SELECT COUNT(*) FROM %s"%table_name).scalar()
                    tables_list.append(
                        (   table_name[len(sharded_table_name)+1:],
                            table_name,
                            records_count
                        )
                    )
            else:
                    records_count=session.execute("SELECT COUNT(*) FROM %s"%table_name).scalar()
                    tables_list.append(
                        (   table_name,
                            records_count
                        )
                    )
    return tables_list

def get_table_shards_list(session,sharded_table_name='Charge_Items'):
    table_shards_list=[]
    if session is not None:
        # Get list of tables in binded schema
        sentence="SHOW TABLES"
        result=session.execute(sentence)
        # Get List of tables matching shardedctable name
        for row in result:
            table_name=row[0]
            pattern="^%s_.*$"%sharded_table_name
            if re.match(pattern,table_name) is not None:
                records_count=session.execute("SELECT COUNT(*) FROM %s"%table_name).scalar()
                table_shards_list.append(
                    (   table_name[len(sharded_table_name)+1:],
                        table_name,
                        records_count
                    )
                )
    return table_shards_list

# Module internal functions
def create_cit_shards(session,args):
    try:
        sentence="SELECT YEAR(CIT_DateTime) AS YY,MONTH(CIT_DateTime) AS MM,COUNT(*) AS COUNT FROM Charge_Items GROUP BY YY,MM ORDER BY YY,MM"
        # Get List of required periods
        result=session.execute(sentence)
        for YY,MM,CC in result:
            shard_table="Charge_Items_%04d%02d"%(YY,MM)
            if args.drop:
                drop_sentence="DROP TABLE IF EXISTS %s"%shard_table
                print("dropping shard table '%s' ..."%shard_table)
                session.execute(drop_sentence)        
            create_sentence="CREATE TABLE IF NOT EXISTS %s AS SELECT * FROM Charge_Items WHERE YEAR(CIT_DateTime)=%s AND MONTH(CIT_DateTime)=%s"%(shard_table,YY,MM)
            print("creating shard table '%s' ..."%shard_table,end='')
            result=session.execute(create_sentence)
            count=session.execute("SELECT COUNT(*) FROM %s"%shard_table).scalar()
            print("{:12,d} records.".format(count))
        session.flush() #20210630 GV session. close()
    except exception as e:
            print(str(e))

def create_shard(session,args):
    if args.table is None:
        args.table = input("Base table name to shard ? ")
    if args.suffix is None:
        args.suffix = input("Sharding suffix         ? ")
    if args.table is not None:
        try:
            print("base table     : ",args.table)
            print("shard suffix   : ",args.suffix)
            shard_table="%s_%s"%(args.table,args.suffix)
            print("shard table    : ",shard_table)
            print("drop if exists : ",args.drop)
            if args.drop:
                drop_sentence="DROP TABLE IF EXISTS %s"%shard_table
                print("dropping shard table '%s' ..."%shard_table)
                session.execute(drop_sentence)
            create_sentence="CREATE TABLE IF NOT EXISTS %s LIKE %s"%(shard_table,args.table)
            print("Executing %s ..."%create_sentence)
            result=session.execute(create_sentence)
            session.flush() #20210630 GV session. close()
        except Exception as e:
            print(str(e))

def create_shard_orm(session,args):
    try:
        Table_Class=globals()[args.table]
    except:
        Table_Class=None
    if Table_Class is not None:
        if args.table is None:
            args.table = input("Base table name to shard ? ")
        args.suffix = input("Sharding suffix         ?")
        try:
            print("Table_Class=",Table_Class)
            print("base table  : ",args.table)
            print("shard suffix: ",args.suffix)
            shard_table="%s_%s"%(args.table,args.suffix)
            print("shard table : ",shard_table)
            Table_Class.__tablename__ =shard_table
            Table_Class.__table__.name=shard_table
            if not engine.dialect.has_table(engine, Table_Class.__tablename__):
                print("Table %s does not exist"% Table_Class.__tablename__)
            else:
                print("Table %s exist !!!"% Table_Class.__tablename__)
            if args.drop:
                print("dropping shard table '%s' ..."%shard_table)
                Table_Class.__table__.drop(engine)
            print("creating shard table '%s' if not exist ..."%shard_table)
            metadata=MetaData()
            metadata.bind=engine
            Table_Class.__table__.metadata=metadata    
            Table_Class.__table__.create(checkfirst=True)
            if not engine.dialect.has_table(engine, Table_Class.__tablename__):
                print("Table %s does not exist. creation error?"% Table_Class.__tablename__)
            else:
                print("Table %s exist !!!"% Table_Class.__tablename__)
        except Exception as e:
            print(str(e))
    else:
        print("Invalid table class '%s'."%args.table)

def list_tables(session,args):
    tablesl=get_tables_list(session)
    pprint(tablesl)

def list_shards(session,args):
    if args.table is None:
        args.table = input("Base shard table name to list ? ")
    if args.table is not None:
        citsl=get_table_shards_list(session,args.table)
        citsl=get_tables_list(session,args.table)
        pprint(citsl)
    else:
        print("Table name not specified.")

def drop_table(session,args):
    if args.table is None:
        args.table = input("Table name to delete ? ")
    if args.table is not None:
        try:
            print("dropping table '%s' ..."%args.table)
            sentence="DROP TABLE IF EXISTS %s"%args.table
            session.execute(sentence)
            session.flush() #20210630 GV session. close()
        except Exception as e:
            print(str(e))
    else:
        print("Table name not specified.")

def drop_table_orm(session,args):
    if args.table is None:
        args.table = input("Table name to delete ? ")
    if args.table is not None:
        try:
            Table_Class=globals()[args.table]
        except:
            Table_Class=None
        try:
            if Table_Class is not None:
                if args.suffix is None:
                    table_name=args_table
                else:
                    table_name="%s_%s"%(args.table,args.suffix)
                    Table_Class.__tablename__  = table_name
                    Table_Class.__table__.name = table_name
                count=session.query(Table_Class).count()
                if count:
                    option=input("Table %s has %s records. Drop anyway (y/N)?"%(table_name,count))
                    if option.upper() == 'Y':
                        print("dropping table '%s' ..."%table_name)
                        session.execute('LOCK TABLES %s WRITE'%table_name)
                        Table_Class.__table__.drop(engine,checkfirst=False)
                        session.execute('UNLOCK TABLES')
        except Exception as e:
            print(str(e))
    else:
        print("Table name not specified.")

def dump_ci(session,args):
    print("dentro de dump ci")
    CI_Id=input("Configuration Item Id ? ")
    if CI_Id is not None:
        CI=session.query(Configuration_Items
            ).filter(Configuration_Items.CI_Id==CI_Id).one_or_none()
        if CI is not None:
            print(CI)
            CUs=session.query(Charge_Units
                ).filter(Charge_Units.CI_Id==CI_Id).all()
            print("    Charge Units=",len(CUs))
            
            for CU in CUs:
                print("  ",CU)
                CITs=session.query(Charge_Items
                    ).filter(Charge_Items.CU_Id==CU.CU_Id
                    ).order_by(Charge_Items.CIT_DateTime.desc()
                    )
                print("        Charge Items=",CITs.count())
                c=0
                for CIT in CITs:
                    print("        ",CIT)
                    c+=1
                    if c==12:
                        break
                
def query(session,args):
    if args.query is None:
        args.query = input("SQL Query sentence ? ")

    if args.query is not None:
        result=session.execute(args.query)
        keys_printed=False
        ROWS=[]
        HEADERS=[]
        COLUMNS=collections.OrderedDict()
        for key in result.keys():
            COLUMNS.update({key:None})
            HEADERS.append(key)
        # --------------------------------------------------
        if args.print_result:
            print("is  insert          ? %s"%result.is_insert)
            if result.is_insert:
                print("inserted_primary_key= %s"%result.inserted_primary_key)
            print("returns rows        ? %s"%result.returns_rows)
            print("rows found          = %s"%result.rowcount)
            print("closed              ? %s"%result.closed)
            print("returned_defaults   = %s"%result.returned_defaults)
            print()
        # --------------------------------------------------
        for row in result:
            for column in range(len(row)):
                COLUMNS[HEADERS[column]]=row[column]
            ROWS.append(dict(COLUMNS))
        # --------------------------------------------------
        if args.print_csv:
            print(args.separator.join(list(result.keys())))
            for row in ROWS:
                print(args.separator.join([str(c) for c in row.values() ]))
        # --------------------------------------------------
        if args.print_pprint:
            pprint(ROWS)
        # --------------------------------------------------
        if args.print_json:
            for row in range(len(ROWS)):
                for column in range(len(HEADERS)):
                    ROWS[row][HEADERS[column]]=str(ROWS[row][HEADERS[column]])
            JSON=json.dumps(ROWS)
            print(JSON)
        # --------------------------------------------------
        if args.print_html:
            print("<table border=1>")
            print("  <thead><tr>",end='')
            for header in HEADERS:
                print("<td>%s</td>"%header,end='')
            print("</tr></thead>")
            print("  <tbody>")
            for row in range(len(ROWS)):
                print("    <tr>",end='')
                for column in range(len(HEADERS)):
                    print("<td>%s</td>"%ROWS[row][HEADERS[column]],end='')
                print("</tr>")
            print("  </tbody>")
            print("</table>")
        # --------------------------------------------------
        args.query=None
    else:
        print("Query not specified.")

def check_ci(session,args):
    print()
    if args.ci is None:
        CI_Id=input("Configuration Item Id ? ")
    else:
        CI_Id=args.ci
    if args.period is None:
        Period=input("Period (YYYYMM) ? ")
    else:
        Period=args.period
    if Period is None:
        Period=strftime("%Y%m")
    period=datetime.strptime(Period+'01',"%Y%m%d")
    print()
    print("period         =",period)
    start,end = Get_Period(period)
    tsstart=int(datetime.timestamp(start))
    tsend=int(datetime.timestamp(end))
    print("start,end      =",start,end)
    slices=[]
    for slice in range(tsstart,tsend,3600):
        slices.append(datetime.fromtimestamp(slice))
    print("Period records =",len(slices))
    print()
    if CI_Id is not None:
        total_verified_records=0
        total_missing_records=0
        CI=session.query(Configuration_Items
            ).filter(Configuration_Items.CI_Id==CI_Id).one_or_none()
        if CI is not None:
            print(CI.CI_Id,CI.CI_Name)
            CUs=session.query(Charge_Units
                ).filter(Charge_Units.CI_Id==CI_Id).all()
            print("    Charge Units=",len(CUs))
            numCUs=len(CUs)
            for CU in CUs:
                # Preparing analitics ...
                rs = RunningStats()
                RLX=[]
                RLY=[]

                verified_records=0
                missing_records=0
                print("  ",CU.CU_Id,CU.CU_Description,CU.CU_UUID)
                for slice in slices:
                    CIT=session.query(Charge_Items
                        ).filter(Charge_Items.CU_Id==CU.CU_Id
                        ).filter(Charge_Items.CIT_DateTime==slice
                        )
                    CIT=CIT.one_or_none()
                    if CIT is not None:
                        verified_records+=1
                        total_verified_records+=1
                        rs.push(CIT.CIT_Quantity)
                        RLX.append(datetime.timestamp(slice))
                        RLY.append(CIT.CIT_Quantity)
                    else:
                        missing_records+=1
                        total_missing_records+=1
                print("        Verified records = %d %6.2f%%"%(verified_records,verified_records/len(slices)*100))
                print("            mean=%s var=%s stdev=%s min=%s max=%s n=%s"%(
                                rs.mean(),
                                rs.variance(),
                                rs.standard_deviation(),
                                rs.min(),
                                rs.max(),
                                rs.n
                                ))
                if rs.standard_deviation() == 0:
                    print("            recomended to fill with mean value '%s'"%(rs.mean()))
                    RL=Regression_Line(y=RLY,x=RLX)
                    for i in range(5):
                        print("            RL estimate",i,slices[i],"=",RL.get_y(datetime.timestamp(slices[i])))
                print("        Missing  records = %d %6.2f%%"%(missing_records,missing_records/len(slices)*100))

            print()
            print("Total Expected records = %d"%(len(slices)*numCUs))
            print("Total Verified records = %d %6.2f%%"%(total_verified_records,total_verified_records/(len(slices)*numCUs)*100))
            print("Total Missing  records = %d %6.2f%%"%(total_missing_records,total_missing_records/(len(slices)*numCUs)*100))

def cis_report(session,args):
    print()
    if args.period is None:
        Period=input("Period (YYYYMM) ? ")
    else:
        Period=args.period
    if Period is None:
        Period=strftime("%Y%m")
    period=datetime.strptime(Period+'01',"%Y%m%d")
    print()
    print("period         =",period)
    start,end = Get_Period(period)
    tsstart=int(datetime.timestamp(start))
    tsend=int(datetime.timestamp(end))
    print("start,end      =",start,end)
    slices=[]
    for slice in range(tsstart,tsend,3600):
        slices.append(datetime.fromtimestamp(slice))
    print("Period records =",len(slices))
    print()
    rows=session.query(Configuration_Items.CI_Id
        ).filter(Configuration_Items.CI_Id>1
        ).all()
    print()
    f=open("CI-CU-revision.dat","w")
    x="CI;CU;NAME;UUID;verrecs;verrecsp;mean;var;stddev;min;max;n;missing;missingp;***"
    print(x)
    f.write("%s\n"%x)
    for row in rows:
        CI_Id=row.CI_Id
        if CI_Id is not None:
            total_verified_records=0
            total_missing_records=0
            CI=session.query(Configuration_Items
                ).filter(Configuration_Items.CI_Id==CI_Id).one_or_none()
            if CI is not None:
                CUs=session.query(Charge_Units
                    ).filter(Charge_Units.CI_Id==CI_Id).all()
                numCUs=len(CUs)
                for CU in CUs:
                    # Preparing analitics ...
                    rs = RunningStats()
                    RLX=[]
                    RLY=[]

                    verified_records=0
                    missing_records=0
                    for slice in slices:
                        CIT=session.query(Charge_Items
                            ).filter(Charge_Items.CU_Id==CU.CU_Id
                            ).filter(Charge_Items.CIT_DateTime==slice
                            )
                        CIT=CIT.one_or_none()
                        if CIT is not None:
                            verified_records+=1
                            total_verified_records+=1
                            rs.push(CIT.CIT_Quantity)
                            RLX.append(datetime.timestamp(slice))
                            RLY.append(CIT.CIT_Quantity)
                        else:
                            missing_records+=1
                            total_missing_records+=1
                    
                    x="%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;***"%(
                        CI.CI_Id,
                        CU.CU_Id,
                        CU.CU_Description,
                        CU.CU_UUID,
                        verified_records,
                        verified_records/len(slices)*100,
                        rs.mean(),
                        rs.variance(),
                        rs.standard_deviation(),
                        rs.min(),
                        rs.max(),
                        rs.n,
                        missing_records,
                        missing_records/len(slices)*100
                        )
                    print(x)
                    f.write("%s\n"%x)
                
    f.close()
    print()

# Data import functions

# Import sheet data definition goes here
sheets=[
    ('CC'        ,'ID'  ,['PARENT_CHECK','CURRENCY_CHECK'],Cost_Centers),
    ('RATE'      ,'ID'  ,['TYPCHK','CUSCHK','PLACHK','CCCHK','CURCHK','MUCHK','PERCHK'],Rates),
    ('CUSTOMERS' ,'ID'  ,['CC_CHECK'],Customers),
    ('PERIODS'   ,'CODE',[],Rat_Periods),
    ('CURRENCIES','CODE',[],Currencies),
    ('MUNITS'    ,'CODE',[],Measure_Units),
    ('CUTYPES'   ,'CODE',[],CU_Types),
    ('PLATFORMS' ,'ID'  ,[],Platforms),
    ('EXRATES'   ,'ID'  ,['CURCHK'],Exchange_Rates),
    ]

def import_cc(nt):
    CC=session.query(Cost_Centers
        ).filter(Cost_Centers.CC_Code==nt.CODE).one_or_none()
    result=0
    if CC is not None:
        CC.CC_Description = nt.DESCRIPTION
        CC.Cur_Code       = nt.CURRENCY
        CC.CC_Parent_Code = nt.PARENT
        CC.CC_Reg_Exp     = nt.REGEXP
        CC.CC_Reference   = nt.REFERENCE
        session.merge(CC)
        result=1
    else:
        CC=Cost_Centers()
        CC.CC_Id          = nt.ID
        CC.CC_Code        = nt.CODE
        CC.CC_Description = nt.DESCRIPTION
        CC.Cur_Code       = nt.CURRENCY
        CC.CC_Parent_Code = nt.PARENT
        CC.CC_Reg_Exp     = nt.REGEXP
        CC.CC_Reference   = nt.REFERENCE
        session.add(CC)
        result=2
    try:
        session.commit()
    except:
        session.rollback()
        result=3
    return result

def import_data(session,args):
    if args.filename is None:
        filename=input("Input filename?")
    if args.filename is not None:
        if args.data in ['CC',]:
            filename=args.filename
            sheet=args.data
            tups={}
            dfs={}
            print("\tloading ...",flush=True)
            try:
                dfs.update({sheet:pd.read_excel(filename,sheet)})
                print("\tcleaning data ...",flush=True)

                found=False
                for s in range(len(sheets)):
                    name,id,chkcolumns,tablename=sheets[s]
                    if name == sheet:
                        found=True
                        break

                if found:        
                    print("\t\tcleaning %20s ..."%name,flush=True,end='')
                    tups.update({name:namedtuple(name, dfs[name].columns)})
                    # delete non meaningfull records
                    l1=len(dfs[name].index)
                    dfs[name]=dfs[name].dropna(subset=[id])
                    l2=len(dfs[name].index)
                    # delete identified errors
                    for column in chkcolumns:
                        dfs[name][dfs[name][column]!='ERROR']
                    l3=len(dfs[name].index)
                    print("\t\tnans=%6d errors=%6d clean=%6d"%(l2-l1,l3-l2,l3),flush=True)
                print("\tdata is clean.")
                print("\timporting ...")    
                df=dfs[sheet]
                created=updated=errors=0
                for row in df.itertuples(index=False, name='Pandas'):
                        t=tuple(row)        
                        # named tuple from tuple, 
                        # tuple include index so first column should be removed  
                        # is required after convertion to list
                        lt=list(t)
                        for i in range(len(lt)):
                            if type(lt[i]) in [int,float]:
                                if math.isnan(lt[i]):
                                    lt[i]=None
                        nt=tups[sheet]._make(lt)
                        result=0
                        if sheet == 'CC':
                            result=import_cc(nt)
                        elif sheet == 'XX':
                            pass
                        if   result == 1: updated+=1
                        elif result == 2: created+=1
                        elif result == 3: errors+=1
                        
                print('\tcreated=',created,'updated=',updated,'errors=',errors)
            except Exception as e:
                print("load failure: %s"%str(e))
        else:
            print("Invalid data type: '%'"%args.data)
    print()

def random_cc(session,args):
    CCs=session.query(Cost_Centers.CC_Id,Cost_Centers.CC_Description
        ).filter(Cost_Centers.CC_Description.like('%FALABELLA%')
        ).filter(Cost_Centers.CC_Description.like('%CC%')
        )
    list_CCs=[]    
    if CCs is not None:
        for CC in CCs:
            list_CCs.append(CC.CC_Id)
    print("%s CCs found"%len(list_CCs))
    CIs=session.query(Configuration_Items
        ).filter(Configuration_Items.CI_Id>1
        ).all()
    if CIs is not None:
        print("%s CIs found"%len(CIs))
        counter=errors=0
        print("updating ... ")
        for CI in CIs:
            CI.CC_Id=random.choice(list_CCs)
            session.merge(CI)
            try:
                session.commit()
                print(".",end='',flush=True)
                counter+=1
            except:
                errors+=1
                print("e",end='',flush=True)
        print()
        print("updated = %s errors = %s"%(counter,errors))
        for CC in list_CCs:
            count=session.query(func.count(Configuration_Items.CC_Id)
                ).filter(Configuration_Items.CC_Id==CC).scalar()
            x="None assigned" if count==0 else ''
            print(CC,count,x)

# Data Fix Functions
# Update Rate types
RAT_TYPE        =0x01
RAT_PLATFORM    =0x02
RAT_CUSTOMER    =0x04
RAT_CC          =0x08
RAT_CI          =0x10

Rat_Types = [   RAT_TYPE,
                RAT_TYPE|RAT_PLATFORM,
                RAT_TYPE|RAT_PLATFORM|RAT_CUSTOMER,
                RAT_TYPE|RAT_PLATFORM|RAT_CUSTOMER|RAT_CC,
                RAT_TYPE|RAT_PLATFORM|RAT_CUSTOMER|RAT_CC|RAT_CI
                ]
# Check if this function is defined anywhere else 
def Get_Rat_Type(Rate):
    rate_type = 0
    if Rate.Typ_Code != 'NUL'   :   rate_type |= RAT_TYPE    
    if Rate.Pla_Id != 1         :   rate_type |= RAT_PLATFORM
    if Rate.Cus_Id != 1         :   rate_type |= RAT_CUSTOMER
    if Rate.CC_Id  != 1         :   rate_type |= RAT_CC
    if Rate.CI_Id  != 1         :   rate_type |= RAT_CI
    return rate_type

def update_rates_type(session,args):    
    print( 'Fixing Rate Types ...')

    rates=session.query(Rates).all()
    print(f'Fixing ...')
    for rat in rates:
        print(rat,Get_Rat_Type(rat))
        rat.Rat_Type=Get_Rat_Type(rat)
        session.add(rat)
        session.commit()

    rates=session.query(Rates).all()
    print(f'Result:')
    for rat in rates:
        print(rat,Get_Rat_Type(rat))
            
def menu(session,args):
    opts='abcdefghijklmnopqrstuvwxyz12345678'
    modes_list=[]
    for mode in valid_modes:
        if mode != 'menu':
            modes_list.append(mode)
    args.print_csv=True
    while True:
        o=0
        print()
        print('Collector tools menu')
        args.table=None
        args.suffix=None
        print('table:%s suffix:%s drop:%s ign warsns:%s csv:%s%s pprint:%s json:%s html:%s result:%s'%(
            args.table,args.suffix,args.drop,args.ignore_warnings,
            args.print_csv,args.separator,args.print_pprint,args.print_json,
            args.print_html,args.print_result))
        print('--------------------')
        print()
        for mode in modes_list:
            print(opts[o],valid_modes[modes_list[o]])
            o+=1
        print()
        print("9 Toggle: (c)sv[;, :|] (p)print (j)son (h)tml (w)arnings (d)rop")
        print("0 Quit")
        print()
        option=input('Option? ')
        print()
        if option == '0':
            break
        if len(option) and option[0] == '9':
            if 'c' in option:    args.print_csv=not(args.print_csv)
            if 'p' in option:    args.print_pprint=not(args.print_pprint)
            if 'j' in option:    args.print_json=not(args.print_json)
            if 'h' in option:    args.print_html=not(args.print_html)
            if 'w' in option:    args.ignore_warnings=not(args.ignore_warnings)
            if 'd' in option:    args.drop=not(args.drop)
            if 'r' in option:    args.print_result=not(args.print_result)
            if ';' in option:    args.separator=';'
            if ',' in option:    args.separator=','
            if ' ' in option:    args.separator=' '
            if ':' in option:    args.separator=':'
            if '|' in option:    args.separator='|'
            continue
        if len(option):
            f=opts.find(option)
            if f != -1:
                opc=modes_list[f]
                print('Executing %s ...'%valid_modes[opc])
                print()
                
                if   opc=='create-cit-shards' : create_cit_shards(session,args)
                elif opc=='create-shard'      : create_shard(session,args)
                elif opc=='create-shard-orm'  : create_shard_orm(session,args)
                elif opc=='list-tables'       : list_tables(session,args)
                elif opc=='list-shards'       : list_shards(session,args)
                elif opc=='drop-table'        : drop_table(session,args)
                elif opc=='drop-table-orm'    : drop_table_orm(session,args)
                elif opc=='query'             : query(session,args)
                elif opc=='dump-ci'           : dump_ci(session,args)
                elif opc=='check-ci'          : check_ci(session,args)
                elif opc=='import-data'       : import_data(session,args)
                elif opc=='random-cc'         : random_cc(session,args)
                elif opc=='cis-report'        : cis_report(session,args)
                elif opc=='update-rates-type' : update_rates_type(session,args)
                print()
                print('Execution of %s completed.'%valid_modes[opc])
                print()

        
# Here I can setup multiple Collector Tool Services
valid_modes =   {   'create-cit-shards':'Create CIT shard tables',
                    'create-shard':'Create shard table from base',
                    'list-tables':'List all tables in schema',
                    'list-shards':'List shards of base table',
                    'drop-table':'Deletes a table in schema',                    
                    'create-shard-orm':'Create shard table from ORM base model',
                    'drop-table-orm':'Deletes a table in ORM schema',                    
                    'query':'Arbitrary query to DB',
                    'dump-ci':'Dumps a Configuration Item',
                    'check-ci':'Checks Configuration Item integrity within period',
                    'import-data':'Imports Data',
                    'random-cc':'Assing Random CC to CIs',
                    'cis-report':'CIs integrity report',
                    'update-rates-type':'Updates Rates Type',
                    'menu':'Menu Tools Mode'                    
                }
mode_help = "Any of: [%s]"%'|'.join(valid_modes.keys())

# Argument's parser definitions
parser = argparse.ArgumentParser()
parser.add_argument('-m','--mode'    ,help=mode_help,   required=True,default=None)
parser.add_argument('-R','--rdbms'   ,help='ORM RDBMS',     required=False,default='mysql')
parser.add_argument('-D','--dialect' ,help='ORM Dialect',   required=False,default='pymysql')
parser.add_argument('-H','--host'    ,help='DB Host name or IP',      required=False,default='localhost')
parser.add_argument('-P','--port'    ,help='D Port',      required=False,default=3306)
parser.add_argument('-u','--user'    ,help='DB User',      required=False,default='collector')
parser.add_argument('-p','--password',help='DB Password',  required=False,default=None)
parser.add_argument('-s','--schema'  ,help='DB Schema',    required=False,default='collector')
parser.add_argument('-t','--table'   ,help='mode Table name argument',    required=False,default=None)
parser.add_argument('-x','--suffix'  ,help='Sharding Suffix',    required=False,default=strftime('%Y%m'))
parser.add_argument('-q','--query'   ,help='Query statement',    required=False,default=None)
parser.add_argument("-v",'--verbose' ,help='Increase output verbosity',action='count',required=False,default=0)
parser.add_argument(     '--ignore-warnings'  ,help='Ignore Warnings.',    
                                            required=False,action='store_true',default=False)
parser.add_argument(     '--drop'    ,help='Force drop shard table if exists',
                                            required=False,action='store_true',default=False)
parser.add_argument(     '--separator'    ,help='Column separator',
                                            required=False,default=';')
parser.add_argument(     '--print-csv'    ,help='CSV output required',
                                            required=False,action='store_true',default=False)
parser.add_argument(     '--print-result'    ,help='DB query result output required',
                                            required=False,action='store_true',default=False)
parser.add_argument(     '--print-pprint'    ,help='Pretty print output required',
                                            required=False,action='store_true',default=False)
parser.add_argument(     '--print-json'    ,help='JSON output required',
                                            required=False,action='store_true',default=False)
parser.add_argument(     '--print-html'    ,help='HTML output required',
                                            required=False,action='store_true',default=False)
parser.add_argument(     '--ci'    ,help='Configuration Item Id',required=False,default=None)
parser.add_argument(     '--period',help='Period YYYYMM',required=False,default=None)
parser.add_argument(     '--filename',help='Input file name',required=False,default=None)
parser.add_argument(     '--data',help='Input data type',required=False,default=None)

args = parser.parse_args()

if args.mode is None or args.mode not in valid_modes.keys():
    print("Invalid mode: %s",args.mode)
    sys.exit(1)

if args.ignore_warnings:
    warnings.filterwarnings("ignore")

if args.verbose > 0:
    print()
    print("---------------------------------------------------------------")
    print("Collector Tools : %s"%valid_modes[args.mode])
    print("Engine          : %s"%args.rdbms)
    print("---------------------------------------------------------------")
    print()

if args.password is None:
    args.password=getpass('Password for %s@%s:%s ? '%(args.user,args.host,args.port))
    print()

connection_string="%s+%s://%s:%s@%s:%s/%s"%(
                    args.rdbms,
                    args.dialect,
                    args.user,
                    args.password,
                    args.host,
                    args.port,
                    args.schema
                    )

try:                    
    engine=create_engine(connection_string)
    connection=None
    Session=None
    session=None
    try:
        if args.verbose > 0: print("connecting to '%s' ..."%engine)
        connection=engine.connect()
        if args.verbose > 0: print("DB connection successful.")
        Session=sessionmaker(bind=engine)
        session=Session()
    except Exception as e:
        print(str(e))
        print("WARNING: DB connection unsuccessful.")
    if args.verbose > 0: print()
    if session is not None:
        if   args.mode == 'create-cit-shards':
            create_cit_shards(session,args)
        elif args.mode == 'create-shard':
            create_shard(session,args)
        elif args.mode == 'create-shard-orm':
            create_shard_orm(session,args)
        elif args.mode == 'list-tables':
            list_tables(session,args)
        elif args.mode == 'list-shards':
            list_shards(session,args)
        elif args.mode == 'drop-table':
            drop_table(session,args)
        elif args.mode == 'drop-table-orm':
            drop_table_orm(session,args)
        elif args.mode == 'query':
            query(session,args)
        elif args.mode == 'dump-ci':
            dump_ci(session,args)
        elif args.mode == 'check-ci':
            check_ci(session,args)
        elif args.mode == 'import-data':
            import_data(session,args)
        elif args.mode == 'random-cc':
            random_cc(session,args)
        elif args.mode == 'cis-report':
            random_cc(session,args)
        elif args.mode == 'update-rates-type':
            update_rates_type(session,args)
        elif args.mode == 'menu':
            menu(session,args)
        else:
            print("Unimplemented mode: %s"%args.mode)
        print()
    else:
        print("DB session couldn't be open.")
except Exception as e:
    print("EXCEPTION: ",str(e))
    raise e
if args.verbose > 0: 
    print()
    print("Execution completed.")
    print()
