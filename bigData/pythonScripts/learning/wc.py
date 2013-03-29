def linecount(filename): 
    count = 0
    wc_count = 0
    for line in open(filename):
        print line
        for item in line:
            print item
            wc_count += 1
        count += 1
    print wc_count
    return count

if __name__ == '__main__':
    print linecount('wc.py')
