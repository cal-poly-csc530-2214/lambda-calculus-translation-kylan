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
    head = parsed[0]
    if type(head) == sexpdata.Symbol:
        print(head)

def main():
    for i in testfiles:
        print("========== " + i + " ========")
        parsed = tokenize(i)
        print(parsed)

main()
