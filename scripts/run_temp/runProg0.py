def inputMode(inputed_data,message):
    print(message,inputed_data)
    return(inputed_data)
def generateResult():
    import sys
    sys.stdout = open('scripts/debugTerminal.txt','w',encoding='utf-8')
    try:
        x= int(inputMode(3,"かける数"))
        y = int(inputMode(8,"かけられる数"))
        print(x*y)
        
    except Exception as e:
        print(e)
    finally:
        sys.stdout.close()
        sys.stdout = sys.__stdout__
        with open('scripts/debugTerminal.txt','r',encoding='utf-8') as terminal_file:
            return(terminal_file.read())