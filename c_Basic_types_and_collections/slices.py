def run_slices():
    text = "The quick brown fox jumped over the lazy dog"

    print(text[0])
    print(text[-1])

    print(text[4:15])
    print(text[:15])
    print(text[15:])
    print(text[5::-1])

    l = [1,2,3,4,5,6]

    print( l[2:4] )
    print(l)
    l[2:4] = []
    #l[2:4] = [7,9,11,200]

    print(l)

    # q = "SELECT * FROM USERS WHERE Id > 1000 Order by ..."
    # cursor = db.query(q)
    #
    # top_20 = cursor[:20]
    # for r in top_20:
    #     print(r)
























