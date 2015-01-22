def run_collections():
    a = [1,2,3,4]
    a.append(7)
    a.append(20)

    print(a)

    b = [2,4,6]

    c = a + b
    print(c)

    a.extend(b)
    print(a)

    print("First: {}, Last: {}".format(
        a[0], a[ -1 ]
    ))

    a[0] = 100

    # a.push = a.append
    # a.push()

    print(a)
    del a[2]
    print(a)

    print("Dictionaries....")
    d = {}
    d = dict()
    # d = { 'id':7, 'name': "Ted" }
    # print(d)
    # d = dict(name="Ted", id="7")
    # print(d)

    # print( d["name"] )
    # print( d["id"] )

    products = [
        "cheese",
        "tacos",
        "cheeseburger"
    ]

    for i, p in enumerate(products):
        d[i] = p


    print(d[1])

    values = list(d.values())
    print(values.index("tacos"))

    #t = 40,
    t = (40, 2, 40.213, "Happy cats")

    n1, n2, f, pet = t
    print(n1)
    print(pet)

    print(t[2])

    num = [7, 11, 13, 17, 19]

    # [2, 4)
    print(num[2:4])  # [13, 17]
    print(num[::3])
    print(num[0:5:3])
    num[-1]

    num[4:]