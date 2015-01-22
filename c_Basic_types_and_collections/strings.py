def run_strings():
    s = "This is a\t\t'string'"
    print(s)

    pth = r"C:\windows\tests\run.py"
    print(pth)

    pth = r"C:\windows\'tests'\run.py"
    print(pth)

    pth = r'C:\windows\"tests"\run.py'
    print(pth)

    pth = "C:\\\'windows\'\\\"tests\"\\run.py"

    print(pth)

    s = """
    This is a string


    that is wrapped
    and otherwise exactly
    as I typed it.
    """

    print(s)


    # n = input("What is your name?")
    # d = input("How hot is it in degrees today?")

    # print( "Hello {0}, today it's {1} degrees"
    #        .format(n, d) )

    print("Why mathy?")
    products = [
        "cheese",
        "tacos",
        "cheeseburger"
    ]

    for p in products:
        pad_length = 40 - len(p)
        print("."*pad_length + p)

