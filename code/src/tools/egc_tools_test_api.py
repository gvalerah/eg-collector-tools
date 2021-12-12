""" 
EG Collector Test API tool
"""
import argparse
import simplejson as json
import requests
import urllib3
from   jinja2 import Environment, BaseLoader
from   emtec                  import *
from   emtec.debug            import *

def get_args():

    # Argument's parser definitions
    parser = argparse.ArgumentParser()
    parser.add_argument('-c','--config'  ,help='Configuration filename',     required=True)
    parser.add_argument('-g','--group'   ,help='Configuration group',   required=True)
    parser.add_argument("-v",'--verbose' ,help='Increase output verbosity',action='count',required=False,default=0)

    args = parser.parse_args()
    return args
    
    
args = get_args()

def get_request(test,username,password,url,connection_timeout=5,read_timeout=20):
        session         = requests.Session()
        session.auth    = (username, password)
        session.verify  = False                                            
        session.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        session.headers.update({'Accept': 'application/json;'})
        # Disable warnings
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)    
        try:
            logger.debug(f"{test.get('method')} url={url}")
            if test.get('method') == 'GET':
                serverResponse = session.get(url,timeout=(connection_timeout,read_timeout))
            elif test.get('method') == 'POST':
                serverResponse = session.post(url,timeout=(connection_timeout,read_timeout),data=json.dumps(test.get('data')))
            else:
                logger.error(f"Invalid method: {test.get('method')}")
        except ConnectionError:
            logger.error("%s: getClusterInformation: Connection Error trying version=%d call=%s URL=%s"     %(this(),version,call_type,vmsURL))            
            return  None,None
        except ConnectTimeout:
            logger.error("%s: getClusterInformation: Connection Timeout trying version=%d call=%s URL=%s"     %(this(),version,call_type,vmsURL))            
            return None,None
        except Exception as e:
            emtec_handle_general_exception(e,logger=logger,module=this())
            return None,None
        if serverResponse is not None and is_json(serverResponse.text):
            return serverResponse.status_code, json.loads(serverResponse.text)
        else:
            return serverResponse.status_code, None


if __name__ == '__main__':
    
    if args.verbose==1:
        logger_level=logging.INFO
    elif args.verbose>=1:
        logger_level=logging.DEBUG
    else:
        logger_level=logging.WARNING
            
    logger = logging.getLogger('egc_tools_test_api')
    logger.setLevel(logger_level)
    formatter = logging.Formatter('%(asctime)s %(levelname)8s (%(lineno)3d): %(message)s')
    ch = logging.StreamHandler()
    try:
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    except:
        logger.exception("creating logger ...")
    logger.debug(f"Process IN: logger={logger}")

    logger.debug(f"args={args}")
    with open(args.config) as fp:
        config=json.load(fp)
    data  = config.get(args.group)
    tests = config.get('tests')
    logger.debug(f"data={data}")
    connection_timeout=5
    read_timeout=30
    counter = 0
    total   = 0
    ok=0
    fail=0
    #PC=data.get('Prism_Central')
    #PE=data.get('Prism_Element')    
    entities={}
    queries=open(f'egc_tools_test_api_{args.group}.txt','w')
    #message = f"{args.group}: PC={PC.get('host')} ({PC.get('version')}) PE={PE.get('host')} ({PE.get('version')})"
    message = f"{args.group}:"
    logger.info(message)
    queries.write(f"{message}\n")
    for test in tests:
        try:
            logger.debug(f"test={test}")
            servers = data.get(test.get('server'))
            for server in servers:
                counter+=1
                
                logger.debug(f"server = {server}")
                protocol = server.get('protocol')
                host     = server.get('host')
                port     = server.get('port')
                username = server.get('username')
                password = server.get('password')
                base_url = server.get('base_url')
                name     = test.get('name')
                method   = test.get('method')
                template = Environment(loader=BaseLoader).from_string(test.get('endpoint'))
                endpoint = test.get('endpoint')
                logger.debug(f"endpoint={endpoint}")
                logger.debug(f"template={template}")
                try:
                    logger.debug(f"rendering endpoint:{endpoint} with {template}")
                    endpoint = template.render(entities=entities)
                except Exception as e:
                    logger.exception('rendering exception')
                    endpoint = test.get('endpoint')
                logger.debug(f"endpoint={endpoint}")
                url = f"{protocol}://{host}:{port}/{base_url}/{endpoint}"
                
                logger.debug(f"url={url}")
                status,text = get_request(test,username,password,url,connection_timeout,read_timeout)
                logger.debug(text.keys())
                matches = 0
                comment = ''
                if text is not None and text.get('message'):
                    comment = text.get('message')
                elif test.get('comment'):
                    comment = test.get('comment')
                if server.get('api_version') == "2":
                    if status == 200:
                        matches = 1
                        if text.get('metadata'): matches = text.get('metadata').get('grand_total_entities')
                        message = f"{host} v{server.get('api_version')}: {counter:3}: {name:20} {status:3} api:{str(text.get('api_version')):6} {matches:4} matches {comment}"
                        logger.info(message)
                        queries.write(f"{message}\n")
                elif server.get('api_version') == "3":
                    if status == 200:
                        matches = 1
                        if text.get('metadata'): matches = text.get('metadata').get('total_matches')
                        message = f"{host} v{server.get('api_version')}: {counter:3}: {name:20} {status:3} api:{str(text.get('api_version')):6} {matches:4} matches {comment}"
                        logger.info(f"{message}")
                        queries.write(f"{message}\n")
                if status == 200:
                    ok+=1
                    if text.get('entities') and len(text.get('entities')):
                            entities.update({name:text.get('entities')[0]})
                    with open(f"{args.group}_{host}_{name}.json","w") as fp:
                        fp.write(json.dumps(text))                    
                else:
                    fail+=1
                    
                    message = f"{host} v{server.get('api_version')}: {counter:3}: {name:20} {status:3} {method} {url} {comment}"
                    logger.error(f"{message}")
                    queries.write(f"{message}\n")
        except Exception as e:
            message = f"test: {host} {server} {server.get('api_version')}: {name:20}"
            #ogger.exception(f"{message}")
            #ogger.exception(f"{e}")
            logger.error(f"{message}")
            logger.error(f"{e}")
            queries.write(f"{message}\n")
    
    message = f"{counter} tests completed. {ok} OK = {ok*100/counter:.2f}%"
    logger.info(message)
    queries.write(f"{message}\n")
    logger.debug(entities.keys())
    logger.debug(entities.get("protection_domains"))

    
