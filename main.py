def denyskaa():
    try:
        with open("1file.txt", "w") as file:
            print("Denyskais", file= file)
            print("the best <3", file= file)
            print("goplay", file= file)
            print("dota2", file= file)

        with open("1file.txt", "r") as file1:
            reader = file1.readline()
            counter = reader.count(' ')
            reader1 = file1.readline()
            counter1 = reader1.count(' ')
            reader2 = file1.readline()
            counter2 = reader2.count(' ')
            reader3 = file1.readline()
            counter3 = reader3.count(' ')


            if counter == 0:
                with open("1file.txt", "w") as file:
                    print(reader, file=file)
                    print("------------", file=file)
                    print(reader1, file=file)
                    print(reader2, file=file)
                    print(reader3, file=file)


            if counter1 == 0:
                with open("1file.txt", "w") as file:
                    print(reader, file=file)
                    print(reader1, file=file)
                    print("------------", file=file)
                    print(reader2, file=file)
                    print(reader3, file=file)


            if counter2 == 0:
                with open("1file.txt", "w") as file:
                    print(reader, file=file)
                    print(reader1, file=file)
                    print(reader2, file=file)
                    print("------------", file=file)
                    print(reader3, file=file)


            if counter3 == 0:
                with open("1file.txt", "w") as file:
                    print(reader, file=file)
                    print(reader1, file=file)
                    print(reader2, file=file)
                    print(reader3, file=file)
                    print("------------", file=file)
            print(reader)
            print(f"**{counter}")
    except Exception as ex:
        print(f"Error:{ex}")


denyskaa()