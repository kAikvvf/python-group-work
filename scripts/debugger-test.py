from libraries.codeDebugger import codeDebugger

prog = "print(1/0)"

test = codeDebugger.debug(prog)

print(test)