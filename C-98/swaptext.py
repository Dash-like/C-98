


def swaptext():
    # file1  = open("test.txt")
    # file2  = open("test2.txt")

    with open("test.txt", 'r') as a:
       data_a = a.read()

    with open("test2.txt", 'r') as b:
       data_b = b.read()

    with open("test.txt", 'w') as a:
       a.write(data_b)

    with open("test2.txt", 'w') as b:
       b.write(data_a)  
swaptext()


