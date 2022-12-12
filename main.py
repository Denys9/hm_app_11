def denyskaa():
    try:
        with open("task.txt", "w") as file:
            file.write("When you picture mountain climbers scaling Mount Everest,"
                       " what probably comes to mind are teams of climbers with Sherpa"
                       " guides leading them to the summit, equipped with oxygen masks,"
                       " supplies and tents. And in most cases you'd be right, as 97 per"
                       " cent of climbers use oxygen to ascend to Everest's summit at 8,850"
                       " metres above sea level.")

        with open("task.txt", "r") as file:
            for line in file:
                print("Full text: ", line, end=" ")
        print()
        lst = []
        k = line.split(' ')
        for item in k:
            l = len(item)
            if l > 7:
                lst.append(item)
                with open("7+letters.txt", "w") as fle:
                    print(f"words which have 7+ letters: {lst}", file=fle)
                    print(f"words which have 7+ letters: {item}")
    except Exception as ex:
        print(f"Error: {ex}")


denyskaa()