def inputMode(inputed_data,message):
    print(message,inputed_data)
    return(inputed_data)
def run():
    x = int(inputMode(3,"かける数"))
    y = int(inputMode(6,"かけられる数"))
    
    print(x*y)
def generateResult():
    import sys
    sys.stdout = open('scripts/debugTerminal.txt','w',encoding='utf-8')
    try:
        run()
    except Exception as e:
        print(e)
    finally:
        sys.stdout.close()
        sys.stdout = sys.__stdout__