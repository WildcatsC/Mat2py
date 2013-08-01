from lexer import *
from token import *

def main():
    source = "test.m"
    lexer = Lexer(source)
    while True:
        token = lexer.getToken()
        if  token.tokenValue:
            print "<",token.tokenValue,",",token.tokenType,">"
        else:
            break

if __name__ == "__main__":
    main()
