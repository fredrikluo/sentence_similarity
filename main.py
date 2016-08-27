from sbss import similarity

if __name__ == '__main__':
    st1 = raw_input("sentence1:")
    st2 = raw_input("sentence2:")

    res = similarity(st1, st2)
    print "%s\t%s\t:%f" % (st1, st2, res)


