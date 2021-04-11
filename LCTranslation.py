# Lambda Calculus Translation
# Kylan Stewart
# CSC 530
import sys
import sexpdata

testfiles = ["test1.in",
        "test2.in",
        "test3.in",
        "test4.in",
        "test5.in",
        "test6.in",
        "test7.in",
        "test8.in",
        "test9.in",
        "test10.in"]

def tokenize(i):
    parsed = []
    with open(i, 'r') as infile:
        parsed = sexpdata.loads(infile.read())
    return parsed

def identify(parsed):
    # LC = num -> "<num>"
    if type(parsed) == int:
        return str(parsed)
    # LC = id -> "<id>"
    elif type(parsed) == sexpdata.Symbol:
        return sexpdata.dumps(parsed)

    head = parsed[0]
    print(parsed)
    # LC = (/ id => LC) -> "lambda <id> : LC"
    if head == sexpdata.Symbol('/'):
        return "lambda " + identify(parsed[1]) + ": " + identify(parsed[3])
    # LC = (+ LC LC) -> "(LC1 + LC2)"
    elif head == sexpdata.Symbol('+'):
        return "(" + identify(parsed[1]) + " + " + identify(parsed[2]) + ")"
    # LC = (* LC LC) -> "(LC1 * LC2)"
    elif head == sexpdata.Symbol('*'):
        return "(" + identify(parsed[1]) + " * " + identify(parsed[2]) + ")"
    # LC = (ifleq0 LC LC LC) -> 
    # if (LC1 <= 0):
    #    LC2
    # else:
    #    LC3
    elif head == sexpdata.Symbol('ifleq0'):
        cond = identify(parsed[1])
        c1 = identify(parsed[2])
        c2 = identify(parsed[3])
        return "if (" + cond + " <= 0):\n   " + c1 + "\nelse:\n   " + c2
    # LC = (println LC) -> "print(LC)"
    elif head == sexpdata.Symbol('println'):
        return "print(" + identify(parsed[1]) + ")"
    # LC = (LC LC) -> "(LC1(LC2))"
    else:
        return "(" + identify(head) + "(" + identify(parsed[1]) + "))"

def main():
    for i in testfiles:
        print("========== " + i + " ========")
        parsed = tokenize(i)
        returned = identify(parsed)
        print(returned)

main()
