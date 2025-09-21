with open("wtf.py", "w") as f:
    f.write("num = int(input('type a number: '))\n\nif (num == 0):\n\tprint('even')\n")

    for i in range(1,10000):
        if (i % 2 == 0):
            type = "even"
        else:
            type = "odd"
        f.write(f"elif (num == {i}):\n\tprint('{type}')\n")

    f.write("else:\n\tprint('bad input')\n")
