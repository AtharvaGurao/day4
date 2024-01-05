try:
    with open("sample.txt") as f:
        pk_list = f.readlines()
        for elem in pk_list:
            print(elem.strip("\n"))
except FileNotFoundError as e:
   print(e)