from libraries.codeDebugger import codeDebugger
import sys

prog = "print(2+2)"

test = codeDebugger.debug(prog)

print(test)