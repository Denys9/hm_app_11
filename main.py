def denyskaa():
    try:
        with open("4stfile.txt", "w") as file4:
            print("Denyska", file= file4)
            print("is", file= file4)
            print("the", file= file4)
            print("best<3", file= file4)

        with open("4stfile.txt", "r") as file4:
            con = file4.readlines()
        lst = []
        with open("5ndfile.txt", "w") as file5:
            for item in con:
                repl = lst.append(item.replace("\n", ""))
                re = lst[::-1]
                repl = lst[-1]
                l = []
                for i in repl:
                    l.append(i)
                l = l.reverse()
                print(l)
                del lst[0]
        print("****DONE****")
    except Exception as ex:
        print(f"Error: {ex}")


denyskaa()
