class codeChecker:
    def debugger(prog):
        try:
            eval(prog) #引数に実行するプログラムを文字列で入力

            
#-------------以下でほぼ全てのエラーに対応し判別----------------
        except AssertionError as error:
            return(f"AssertionError : {error}")
        
        except AttributeError as error:
            return(f"AttributeError : {error}")
        
        except EOFError as error:
            return(f"EOFError : {error}")
        
        except GeneratorExit as error:
            return(f"GeneratorExit : {error}")
        
        except ModuleNotFoundError as error:
            return(f"ModuleNotFoundError : {error}")
        
        except IndexError as error:
            return(f"IndexError : {error}")
        
        except KeyError as error:
            return(f"KeyError : {error}")
        
        except KeyboardInterrupt as error:
            return(f"KerboardInterrupt : {error}")
        
        except MemoryError as error:
            return(f"MemoryError : {error}")
        
        except NotImplementedError as error:
            return(f"NotImplentedError : {error}")
        
        except OverflowError as error:
            return(f"OverflowError : {error}")
        
        except PythonFinalizationError as error:
            return(f"PythonFinalizationError : {error}")
        
        except RecursionError as error:
            return(f"RecursionError : {error}")
        
        except ReferenceError as error:
            return(f"ReferencError: {error}")
        
        except RuntimeError as error:
            return(f"RuntimeError : {error}")
        
        except StopIteration as error:
            return(f"StopIteration : {error}")
        
        except StopAsyncIteration as error:
            return(f"StopAsyncIteration : {error}")

        except SyntaxError as error:
            return(f"SyntaxError : {error}")
        
        except IndentationError as error:
            return(f"IndentationError : {error}")
        
        except TabError as error:
            return(f"TabError : {error}")
        
        except SystemError as error:
            return(f"SystemError : {error}")
        
        except SystemExit as error:
            return(f"SystemExit : {error}")
        
        except TypeError as error:
            return(f"TypeError : {error}")
        
        except UnboundLocalError as error:
            return(f"UnboundLocalError : {error}")
        
        except UnicodeError as error:
            return(f"UnicodeError : {error}")
        
        except UnicodeEncodeError as error:
            return(f"UnicodeEncodeError : {error}")
        
        except UnicodeDecodeError as error:
            return(f"UnicodeDecodeError : {error}")
        
        except UnicodeTranslateError as error:
            return(f"UnicodeTranslateError : {error}")
        
        except ZeroDivisionError as error:
            return(f"ZeroDivisionError : {error}")
        
        except EnvironmentError as error:
            return(f"EnvironmentError : {error}")
        
        except IOError as error:
            return(f"TOError : {error}")
        
        except WindowsError as error:
            return(f"WindowsError : {error}")
        
        except BlockingIOError as error:
            return(f"BlockingIOError : {error}")
        
        except ChildProcessError as error:
            return(f"ChildProcessError : {error}")
        
        except ConnectionError as error:
            return(f"ConnentionError : {error}")
        
        except BrokenPipeError as error:
            return(f"BrokenPipeError : {error}")
        
        except ConnectionAbortedError as error:
            return(f"ConnectionAbortedError : {error}")
        
        except ConnectionRefusedError as error:
            return(f"ConnectionRefusedError : {error}")
        
        except ConnectionResetError as error:
            return(f"ConnectionResetError : {error}")
        
        except FileExistsError as error:
            return(f"FileExistsError : {error}")
        
        except FileNotFoundError as error:
            return(f"FileNotFoundError : {error}")
        
        except InterruptedError as error:
            return(f"InterruptedError : {error}")
        
        except IsADirectoryError as error:
            return(f"IsADirectoryError : {error}")
        
        except NotADirectoryError as error:
            return(f"NotADirtectoryError : {error}")
        
        except PermissionError as error:
            return(f"PermissionError : {error}")
        
        except ProcessLookupError as error:
            return(f"ProcessLookupError : {error}")
        
        except TimeoutError as error:
            return(f"TimeoutError : {error}")
                
        except UserWarning as warning:
            return(f"UserWarning : {warning}")
        
        except DeprecationWarning as warning:
            return(f"DeprecationWarning : {warning}")
        
        except PendingDeprecationWarning as warning:
            return(f"PendingDeprecationWarning : {warning}")
        
        except SyntaxWarning as warning:
            return(f"SyntaxWarning : {warning}")
        
        except RuntimeWarning as warning:
            return(f"RuntimeWarning : {warning}")
        
        except FutureWarning as warning:
            return(f"FututeWarning : {warning}")
        
        except ImportWarning as warning:
            return(f"ImportWarning : {warning}")
        
        except UnicodeWarning as warning:
            return(f"UnicodeWarning : {warning}")
        
        except EncodingWarning as warning:
            return(f"EndcodingWarning : {warning}")
        
        except BytesWarning as warning:
            return(f"BytesWarning : {warning}")
        
        except ResourceWarning as warning:
            return(f"ResourceWarning : {warning}")

        except Exception as error:
            return(f"予期しないエラーが発生しました:{error}")

# もしエラーが見つからなかった場合には、"qualified" と返す
        else:
            return("qualified")