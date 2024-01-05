try:
    with open("sample.csv") as f:
        pk_list = f.readlines()
        for elem in pk_list[1:]:
            print(elem.split(",")[0])
except FileNotFoundError as e:
   print(e)