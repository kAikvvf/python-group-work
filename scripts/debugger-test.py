from lib.codeChecker import codeChecker

prog = "print(3)"

test = codeChecker.debugger(prog)

if test == "qualified":
    eval(prog)
else:
    print(test)