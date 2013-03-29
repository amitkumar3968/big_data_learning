def printStuff(*args):
    for arg in args:
        if isinstance(arg,  dict) == True:
            print "Dictionary"
            for items in arg:
                print items,  arg[items]
        else:
            print arg

value = dict()
value = {'jack': 4098, 'sape': 4139}

printStuff(1, 2, "Hello World",  [1, 2, 3, 4, 5, 6, 7, 8, 9],  1,{'jack': 4098, 'sape': 4139},  "Ok I am done !!")
