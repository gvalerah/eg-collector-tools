# ----------------------------
# Demo Data Generation
# Objetive is to cover all demo cases needed for an Efective Demonstration
# of Collector's Capabilities
# ----------------------------

from time import strftime

Num_Customers   = 5
CC_Levels       = 3
Num_VM_per_CC   = 3

# Demo Platforms
PLATFORMS = []
PLATFORMS.append({'id':0,'name':'Nutanix Demo','host':'localhost','port':9440,'user':'user','password':'password'})
PLATFORMS.append({'id':0,'name':'VM Ware Demo','host':'localhost','port':1000,'user':'user','password':'password'})
# Demo CCs
CC=[]


# Geografia 1
CC.append({'id':100000,'code':'100000','description':'XYZ Chile'                ,'cur':'USD','parent':'1'})

CC.append({'id':101000,'code':'101000','description':'Banco XYZ Chile'          ,'cur':'USD','parent':'10000'})

CC.append({'id':101001,'code':'101001','description':'Produccion'               ,'cur':'USD','parent':'101000'})
CC.append({'id':101002,'code':'101002','description':'Desarrollo'               ,'cur':'USD','parent':'101000'})
CC.append({'id':101003,'code':'101003','description':'QA'                       ,'cur':'USD','parent':'101000'})

CC.append({'id':102000,'code':'102000','description':'Cia Seguros JKL Chile'    ,'cur':'USD','parent':'10000'})

CC.append({'id':102001,'code':'102010','description':'Produccion'               ,'cur':'USD','parent':'102000'})
CC.append({'id':102002,'code':'102010','description':'Desarrollo'               ,'cur':'USD','parent':'102000'})
CC.append({'id':102003,'code':'102010','description':'Laboratorio'              ,'cur':'USD','parent':'102000'})

CC.append({'id':103000,'code':'103000','description':'Isapre JKL Chile'         ,'cur':'USD','parent':'10000'})

CC.append({'id':103001,'code':'103001','description':'Produccion'               ,'cur':'USD','parent':'103000'})
CC.append({'id':103002,'code':'103002','description':'Desarrollo'               ,'cur':'USD','parent':'103000'})
CC.append({'id':103003,'code':'103003','description':'QA'                       ,'cur':'USD','parent':'103000'})

# Geografia 2
CC.append({'id':200000,'code':'200000','description':'XYZ Peru'                 ,'cur':'USD','parent':'1'})

CC.append({'id':201000,'code':'201000','description':'Banco XYZ Peru'           ,'cur':'USD','parent':'20000'})

CC.append({'id':201001,'code':'201001','description':'Produccion'               ,'cur':'USD','parent':'201000'})
CC.append({'id':201002,'code':'201002','description':'Desarrollo'               ,'cur':'USD','parent':'201000'})
CC.append({'id':201003,'code':'201003','description':'QA'                       ,'cur':'USD','parent':'201000'})

CC.append({'id':202000,'code':'202000','description':'Cia Seguros JKL Peru'     ,'cur':'USD','parent':'20000'})

CC.append({'id':202001,'code':'202010','description':'Produccion'               ,'cur':'USD','parent':'202000'})
CC.append({'id':202002,'code':'202010','description':'Desarrollo'               ,'cur':'USD','parent':'202000'})
CC.append({'id':202003,'code':'202010','description':'Laboratorio'              ,'cur':'USD','parent':'202000'})

CC.append({'id':203000,'code':'203000','description':'Mutual Amigo'             ,'cur':'USD','parent':'20000'})

CC.append({'id':203001,'code':'203001','description':'Produccion'               ,'cur':'USD','parent':'203000'})
CC.append({'id':203002,'code':'203002','description':'Desarrollo'               ,'cur':'USD','parent':'203000'})
CC.append({'id':203003,'code':'203003','description':'QA'                       ,'cur':'USD','parent':'203000'})

         
# Demo Customers
CUSTOMERS = []

CUSTOMERS.append({'id':0,'name':'XYZ Chile', 'cc':100000})
CUSTOMERS.append({'id':0,'name':'XYZ Peru' , 'cc':200000})


for p in range(len(PLATFORMS)):
    print(PLATFORMS[p])
print()
    
for c in range(len(CC)):
    print(CC[c])
print()
    
for cu in range(len(CUSTOMERS)):
    print(CUSTOMERS[cu])
    
print()

# Demo Configuration Items

CI = []
count=0
for p in range(len(PLATFORMS)):
    for c in range(len(CC)):
        for vm in range(Num_VM_per_CC):
            id=count
            name="VM-%s-%d"%(CC[c]['description'],id)
            uuid="ABCD-EFGH-%04d"%id
            plat=p
            cc=CC[c]['id']
            citg=1
            cus=1
            date=strftime("%Y-%m-%d %H:%M:%s")
            CI.append({'id':id,'name':name,'uuid':uuid,'platform':plat,'cc':cc,'citg':citg,'cus':cus,'date':date})
            count+=1
            
for ci in range(len(CI)):
    print(CI[ci])
    
print()            

print("Estadisticas")
print("Plataformas              ="   ,len(PLATFORMS))
print("Centros de Costo         ="   ,len(CC))
print("Clientes                 ="   ,len(CUSTOMERS))
print("Maquinas Virtuales       ="   ,len(CI))
print("Unidades de Cargo        ="   ,len(CI)*3)
print("Items de Cargo por Mes   ="   ,len(CI)*3*720)
print("Items de Cargo por Año   ="   ,len(CI)*3*720*12)

