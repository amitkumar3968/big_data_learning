import os
cmd = 'ls -l'
try:
    fp = os.popen(cmd)
    result = fp.read()
    resp = fp.close()
    print result
    if resp == None:
        print "closed Pipe Normally !! "
except:
    print "something Happend.!!"
