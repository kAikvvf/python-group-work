import sys
import importlib

class codeDebugger:
    def debug(prog):
        makedebugFile = open("debugFile.py","w")
        makedebugFile.writelines(prog)
        makedebugFile.close()
        sys.stdout = open("debugDirectory.txt","w")
        try: #引数に実行するプログラムを文字列で入力
            debugProg = importlib.import_module("debugFile")
            importlib.reload(debugProg)
            debugProg.run()

#-------------以下でほぼ全てのエラーに対応し判別----------------
        except AssertionError as error:
            print(f"AssertionError : {error}")
        
        except AttributeError as error:
            print(f"AttributeError : {error}")
        
        except EOFError as error:
            print(f"EOFError : {error}")
        
        except GeneratorExit as error:
            print(f"GeneratorExit : {error}")
        
        except ModuleNotFoundError as error:
            print(f"ModuleNotFoundError : {error}")
        
        except IndexError as error:
            print(f"IndexError : {error}")
        
        except KeyError as error:
            print(f"KeyError : {error}")
        
        except KeyboardInterrupt as error:
            print(f"KerboardInterrupt : {error}")
        
        except MemoryError as error:
            print(f"MemoryError : {error}")
        
        except NotImplementedError as error:
            print(f"NotImplentedError : {error}")
        
        except OverflowError as error:
            print(f"OverflowError : {error}")
        
        except PythonFinalizationError as error:
            print(f"PythonFinalizationError : {error}")
        
        except RecursionError as error:
            print(f"RecursionError : {error}")
        
        except ReferenceError as error:
            print(f"ReferencError: {error}")
        
        except RuntimeError as error:
            print(f"RuntimeError : {error}")
        
        except StopIteration as error:
            print(f"StopIteration : {error}")
        
        except StopAsyncIteration as error:
            print(f"StopAsyncIteration : {error}")

        except SyntaxError as error:
            print(f"SyntaxError : {error}")
        
        except IndentationError as error:
            print(f"IndentationError : {error}")
        
        except TabError as error:
            print(f"TabError : {error}")
        
        except SystemError as error:
            print(f"SystemError : {error}")
        
        except SystemExit as error:
            print(f"SystemExit : {error}")
        
        except TypeError as error:
            print(f"TypeError : {error}")
        
        except UnboundLocalError as error:
            print(f"UnboundLocalError : {error}")
        
        except UnicodeError as error:
            print(f"UnicodeError : {error}")
        
        except UnicodeEncodeError as error:
            print(f"UnicodeEncodeError : {error}")
        
        except UnicodeDecodeError as error:
            print(f"UnicodeDecodeError : {error}")
        
        except UnicodeTranslateError as error:
            print(f"UnicodeTranslateError : {error}")
        
        except ZeroDivisionError as error:
            print(f"ZeroDivisionError : {error}")
        
        except EnvironmentError as error:
            print(f"EnvironmentError : {error}")
        
        except IOError as error:
            print(f"TOError : {error}")
        
        except WindowsError as error:
            print(f"WindowsError : {error}")
        
        except BlockingIOError as error:
            print(f"BlockingIOError : {error}")
        
        except ChildProcessError as error:
            print(f"ChildProcessError : {error}")
        
        except ConnectionError as error:
            print(f"ConnentionError : {error}")
        
        except BrokenPipeError as error:
            print(f"BrokenPipeError : {error}")
        
        except ConnectionAbortedError as error:
            print(f"ConnectionAbortedError : {error}")
        
        except ConnectionRefusedError as error:
            print(f"ConnectionRefusedError : {error}")
        
        except ConnectionResetError as error:
            print(f"ConnectionResetError : {error}")
        
        except FileExistsError as error:
            print(f"FileExistsError : {error}")
        
        except FileNotFoundError as error:
            print(f"FileNotFoundError : {error}")
        
        except InterruptedError as error:
            print(f"InterruptedError : {error}")
        
        except IsADirectoryError as error:
            print(f"IsADirectoryError : {error}")
        
        except NotADirectoryError as error:
            print(f"NotADirtectoryError : {error}")
        
        except PermissionError as error:
            print(f"PermissionError : {error}")
        
        except ProcessLookupError as error:
            print(f"ProcessLookupError : {error}")
        
        except TimeoutError as error:
            print(f"TimeoutError : {error}")
                
        except UserWarning as warning:
            print(f"UserWarning : {warning}")
        
        except DeprecationWarning as warning:
            print(f"DeprecationWarning : {warning}")
        
        except PendingDeprecationWarning as warning:
            print(f"PendingDeprecationWarning : {warning}")
        
        except SyntaxWarning as warning:
            print(f"SyntaxWarning : {warning}")
        
        except RuntimeWarning as warning:
            print(f"RuntimeWarning : {warning}")
        
        except FutureWarning as warning:
            print(f"FututeWarning : {warning}")
        
        except ImportWarning as warning:
            print(f"ImportWarning : {warning}")
        
        except UnicodeWarning as warning:
            print(f"UnicodeWarning : {warning}")
        
        except EncodingWarning as warning:
            print(f"EndcodingWarning : {warning}")
        
        except BytesWarning as warning:
            print(f"BytesWarning : {warning}")
        
        except ResourceWarning as warning:
            print(f"ResourceWarning : {warning}")

        except Exception as error:
            print(f"予期しないエラーが発生しました:{error}")

        finally:
            sys.stdout.close()
            sys.stdout = sys.__stdout__
            return(open("debugDirectory.txt","r").read())