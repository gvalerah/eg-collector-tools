MAX_MESSAGE_LEN=75

def line(message,length,left,right):
    borders_len=len(left)+len(right)        
    print("%s%-*s%s"%(left,(length-borders_len),message,right))

def box(message, max_cols=MAX_MESSAGE_LEN,type='python'):
    if type=='python':
        left='""" '
        right=' """'
    elif type=='c':
        left='# '
        right=' #'
    elif type=='html':
        left='<!-- '
        right=' -->'
    elif type=='jinja':
        left='{# '
        right=' #}'

    borders_len=len(left)+len(right)        
    
    max_len_msg=79-borders_len
    
    if len(message)>max_len_msg:
        max_columns=max_len_msg+borders_len
    else:
        max_columns=len(message)+borders_len
    
    
    line('-'*max_len_msg,max_columns,left,right)
    
    while len(message)>max_len_msg:
        line(message[0:max_len_msg],max_columns,left,right)
        message=message[max_len_msg:]
    if len(message):
        line(message,max_columns,left,right)
    
    line('-'*max_len_msg,max_columns,left,right)
    
box("Mensaje 1")
box("Este es mi mensaje 2 Mensaje 1")
box("Este es mi mensaje 3 mas largo Mensaje 1")
box("Este es mi mensaje 3 mas largo Mensaje 1",type='c')
box("Este es mi mensaje 3 mas largo Mensaje 1",type='html')
box("Este es mi mensaje 3 mas largo Mensaje 1",type='jinja')
box("Este es mi mensaje 4 mas largo  que deberia ocupar mas de una linea del box en cuestion Mensaje 1",type='jinja')

