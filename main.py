def denyska():
    try:
        with open("1stfile.txt", "w") as file1:
            print("Denyska", file= file1)
            print("is", file= file1)
            print("the", file= file1)
            print("best<3", file= file1)
        with open("1stfile.txt", "r") as file3:
            con = file3.readlines()
        with open("2ndfile.txt", "w") as file2:
            for item in con:
                print(item.replace("\n", ""), file=file2)
        print("<><><><><><><><>")
    except Exception as ex:
        print(f"Error: {ex}")


denyska()