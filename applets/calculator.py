

class calc:
    def __init__(self):
        pass



while True:
    inp = input("| ")

    if inp.lower() == "x":
        break
    print("type x to exit")
    try:
        print(">>",eval(inp))
    except:
        print("Invalid")
