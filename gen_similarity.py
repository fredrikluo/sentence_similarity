from sbss import similarity, init
import numpy as np
import sys
import time
from concurrent.futures import ThreadPoolExecutor
import traceback

worker_count = 100

scache = {}

def worker(s0, i, sentences):
    try:
        global scache
        with open('res/' + str(i) + ".txt", 'w') as out_file:
            print "start:", i
            for a in sentences:
                s1 = a[1]
                if s0 == s1:
                    res = 1
                    print "same:", i, s0, s1
                elif s0+s1 in scache:
                    res = scache[s0+s1]
                    print "cache:", i, s0, s1
                else:
                    res = 1 - similarity(s0, s1)
                    scache[s0+s1] = res
                    scache[s1+s0] = res
                    print "cal:", i, s0, s1

                out_file.write(str(res) + ",")
            print "Done", i
    except:
        traceback.print_exc(file=sys.stdout)
        print "Error", i

def main():
    init()
    # build up matrix
    with open (sys.argv[1]) as data_file:
        sentences = [ l.strip().split(";") for l in data_file.readlines()]
        with ThreadPoolExecutor(max_workers=worker_count) as executor:
            for i in range(0, len(sentences)):
                url = sentences[i][0]
                s0  = sentences[i][1]
                executor.submit(worker, s0, i, sentences)

        print "exit"
if __name__ == '__main__':
    main()
