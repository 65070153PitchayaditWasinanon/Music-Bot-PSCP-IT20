"""#9 - Sorting"""

# ♠ ♦ ♥ ♣

# def insertionSort(my_list, last):
#     """Insertion Sort"""
#     current = 1
#     compare = 0
#     while (current <= last):
#         hold = my_list[current]
#         walker = current-1
#         compare += 1
#         while (walker >= 0 and hold < my_list[walker]):
#             my_list[walker+1] = my_list[walker]
#             walker -= 1
#             compare += 1
#         my_list[walker+1] = hold
#         current += 1
#         if (walker < 0):
#             compare -= 1
#         print(my_list)
#     print("Comparsion times: "+str(compare))

# def selectionSort(my_list, last):
#     """Selection Sort"""
#     current = 0
#     compare = 0
#     while (current <= last):
#         smallest = current
#         walker = current + 1
#         while (walker <= last):
#             if my_list[walker] < my_list[smallest]:
#                 smallest = walker
#             walker += 1
#             compare += 1
#         my_list[current], my_list[smallest] = my_list[smallest], my_list[current]
#         current += 1
#         print(my_list)
#     print("Comparsion times: "+str(compare))

# def bubbleSort(my_list, last):
#     """Bubble Sort"""
#     current = 0
#     sorted_0 = False
#     compare = 0
#     while (current <= last) and (sorted_0 is False):
#         walker = last
#         sorted_0 = True
#         while (walker > current):
#             if my_list[walker] < my_list[walker-1]:
#                 sorted_0 = False
#                 walkers = walker - 1
#                 my_list[walker], my_list[walkers] = my_list[walkers], my_list[walker]
#             compare += 1
#             walker -= 1
#         current += 1
#         print(my_list)
#     print("Comparsion times: "+str(compare))

# insertionSort([23, 78, 45, 8, 32, 56], 5)
# selectionSort([23, 78, 45, 8, 32, 56], 5)
# bubbleSort([23, 78, 45, 8, 32, 56], 5)

#---------------------------------------------------------------------------------------------------------------

number = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
symbol = ["♣", "♦", "♥", "♠"]

def insertionSort(my_list, last):
    """Insertion Sort"""
    my_list0 = []
    for i in my_list:
        if "♣" in i:
            num = ""
            for j in i:
                if j == "J":
                    num = 11
                elif j == "Q":
                    num = 12
                elif j == "K":
                    num = 13
                elif j == "A":
                    num = 14
                elif j.isnumeric():
                    num += j
            my_list0.append(int(num)+0.1)
        elif "♦" in i:
            num = ""
            for j in i:
                if j == "J":
                    num = 11
                elif j == "Q":
                    num = 12
                elif j == "K":
                    num = 13
                elif j == "A":
                    num = 14
                elif j.isnumeric():
                    num += j
            my_list0.append(int(num)+0.2)
        elif "♥" in i:
            num = ""
            for j in i:
                if j == "J":
                    num = 11
                elif j == "Q":
                    num = 12
                elif j == "K":
                    num = 13
                elif j == "A":
                    num = 14
                elif j.isnumeric():
                    num += j
            my_list0.append(int(num)+0.3)
        elif "♠" in i:
            num = ""
            for j in i:
                if j == "J":
                    num = 11
                elif j == "Q":
                    num = 12
                elif j == "K":
                    num = 13
                elif j == "A":
                    num = 14
                elif j.isnumeric():
                    num += j
            my_list0.append(int(num)+0.4)
    current = 1
    compare = 0
    while (current <= last):
        my_list_final = []
        hold = my_list0[current]
        walker = current-1
        compare += 1
        while (walker >= 0 and hold < my_list0[walker]):
            my_list0[walker+1] = my_list0[walker]
            walker -= 1
            compare += 1
        my_list0[walker+1] = hold
        current += 1
        if (walker < 0):
            compare -= 1
        for k in my_list0:
            total = str(k).split(".")
            if int(total[0]) <= 10:
                if total[1] == "1":
                    my_list_final.append(str(total[0])+"♣")
                elif total[1] == "2":
                    my_list_final.append(str(total[0])+"♦")
                elif total[1] == "3":
                    my_list_final.append(str(total[0])+"♥")
                elif total[1] == "4":
                    my_list_final.append(str(total[0])+"♠")
            elif int(total[0]) == 11:
                if total[1] == "1":
                    my_list_final.append("J"+"♣")
                elif total[1] == "2":
                    my_list_final.append("J"+"♦")
                elif total[1] == "3":
                    my_list_final.append("J"+"♥")
                elif total[1] == "4":
                    my_list_final.append("J"+"♠")
            elif int(total[0]) == 12:
                if total[1] == "1":
                    my_list_final.append("Q"+"♣")
                elif total[1] == "2":
                    my_list_final.append("Q"+"♦")
                elif total[1] == "3":
                    my_list_final.append("Q"+"♥")
                elif total[1] == "4":
                    my_list_final.append("Q"+"♠")
            elif int(total[0]) == 13:
                if total[1] == "1":
                    my_list_final.append("K"+"♣")
                elif total[1] == "2":
                    my_list_final.append("K"+"♦")
                elif total[1] == "3":
                    my_list_final.append("K"+"♥")
                elif total[1] == "4":
                    my_list_final.append("K"+"♠")
            elif int(total[0]) == 14:
                if total[1] == "1":
                    my_list_final.append("A"+"♣")
                elif total[1] == "2":
                    my_list_final.append("A"+"♦")
                elif total[1] == "3":
                    my_list_final.append("A"+"♥")
                elif total[1] == "4":
                    my_list_final.append("A"+"♠")
        print(my_list_final)
    print("Comparsion times: "+str(compare))

def selectionSort(my_list, last):
    """Selection Sort"""
    my_list0 = []
    for i in my_list:
        if "♣" in i:
            num = ""
            for j in i:
                if j == "J":
                    num = 11
                elif j == "Q":
                    num = 12
                elif j == "K":
                    num = 13
                elif j == "A":
                    num = 14
                elif j.isnumeric():
                    num += j
            my_list0.append(int(num)+0.1)
        elif "♦" in i:
            num = ""
            for j in i:
                if j == "J":
                    num = 11
                elif j == "Q":
                    num = 12
                elif j == "K":
                    num = 13
                elif j == "A":
                    num = 14
                elif j.isnumeric():
                    num += j
            my_list0.append(int(num)+0.2)
        elif "♥" in i:
            num = ""
            for j in i:
                if j == "J":
                    num = 11
                elif j == "Q":
                    num = 12
                elif j == "K":
                    num = 13
                elif j == "A":
                    num = 14
                elif j.isnumeric():
                    num += j
            my_list0.append(int(num)+0.3)
        elif "♠" in i:
            num = ""
            for j in i:
                if j == "J":
                    num = 11
                elif j == "Q":
                    num = 12
                elif j == "K":
                    num = 13
                elif j == "A":
                    num = 14
                elif j.isnumeric():
                    num += j
            my_list0.append(int(num)+0.4)
    current = 0
    compare = 0
    while (current <= last):
        my_list_final = []
        smallest = current
        walker = current + 1
        while (walker <= last):
            if my_list0[walker] < my_list0[smallest]:
                smallest = walker
            walker += 1
            compare += 1
        my_list0[current], my_list0[smallest] = my_list0[smallest], my_list0[current]
        current += 1
        for k in my_list0:
            total = str(k).split(".")
            if int(total[0]) <= 10:
                if total[1] == "1":
                    my_list_final.append(str(total[0])+"♣")
                elif total[1] == "2":
                    my_list_final.append(str(total[0])+"♦")
                elif total[1] == "3":
                    my_list_final.append(str(total[0])+"♥")
                elif total[1] == "4":
                    my_list_final.append(str(total[0])+"♠")
            elif int(total[0]) == 11:
                if total[1] == "1":
                    my_list_final.append("J"+"♣")
                elif total[1] == "2":
                    my_list_final.append("J"+"♦")
                elif total[1] == "3":
                    my_list_final.append("J"+"♥")
                elif total[1] == "4":
                    my_list_final.append("J"+"♠")
            elif int(total[0]) == 12:
                if total[1] == "1":
                    my_list_final.append("Q"+"♣")
                elif total[1] == "2":
                    my_list_final.append("Q"+"♦")
                elif total[1] == "3":
                    my_list_final.append("Q"+"♥")
                elif total[1] == "4":
                    my_list_final.append("Q"+"♠")
            elif int(total[0]) == 13:
                if total[1] == "1":
                    my_list_final.append("K"+"♣")
                elif total[1] == "2":
                    my_list_final.append("K"+"♦")
                elif total[1] == "3":
                    my_list_final.append("K"+"♥")
                elif total[1] == "4":
                    my_list_final.append("K"+"♠")
            elif int(total[0]) == 14:
                if total[1] == "1":
                    my_list_final.append("A"+"♣")
                elif total[1] == "2":
                    my_list_final.append("A"+"♦")
                elif total[1] == "3":
                    my_list_final.append("A"+"♥")
                elif total[1] == "4":
                    my_list_final.append("A"+"♠")
        print(my_list_final)
    print("Comparsion times: "+str(compare))

def bubbleSort(my_list, last):
    """Bubble Sort"""
    my_list0 = []
    for i in my_list:
        if "♣" in i:
            num = ""
            for j in i:
                if j == "J":
                    num = 11
                elif j == "Q":
                    num = 12
                elif j == "K":
                    num = 13
                elif j == "A":
                    num = 14
                elif j.isnumeric():
                    num += j
            my_list0.append(int(num)+0.1)
        elif "♦" in i:
            num = ""
            for j in i:
                if j == "J":
                    num = 11
                elif j == "Q":
                    num = 12
                elif j == "K":
                    num = 13
                elif j == "A":
                    num = 14
                elif j.isnumeric():
                    num += j
            my_list0.append(int(num)+0.2)
        elif "♥" in i:
            num = ""
            for j in i:
                if j == "J":
                    num = 11
                elif j == "Q":
                    num = 12
                elif j == "K":
                    num = 13
                elif j == "A":
                    num = 14
                elif j.isnumeric():
                    num += j
            my_list0.append(int(num)+0.3)
        elif "♠" in i:
            num = ""
            for j in i:
                if j == "J":
                    num = 11
                elif j == "Q":
                    num = 12
                elif j == "K":
                    num = 13
                elif j == "A":
                    num = 14
                elif j.isnumeric():
                    num += j
            my_list0.append(int(num)+0.4)
    current = 0
    sorted_0 = False
    compare = 0
    while (current <= last) and (sorted_0 is False):
        my_list_final = []
        walker = last
        sorted_0 = True
        while (walker > current):
            if my_list0[walker] < my_list0[walker-1]:
                sorted_0 = False
                walkers = walker - 1
                my_list0[walker], my_list0[walkers] = my_list0[walkers], my_list0[walker]
            compare += 1
            walker -= 1
        current += 1
        for k in my_list0:
            total = str(k).split(".")
            if int(total[0]) <= 10:
                if total[1] == "1":
                    my_list_final.append(str(total[0])+"♣")
                elif total[1] == "2":
                    my_list_final.append(str(total[0])+"♦")
                elif total[1] == "3":
                    my_list_final.append(str(total[0])+"♥")
                elif total[1] == "4":
                    my_list_final.append(str(total[0])+"♠")
            elif int(total[0]) == 11:
                if total[1] == "1":
                    my_list_final.append("J"+"♣")
                elif total[1] == "2":
                    my_list_final.append("J"+"♦")
                elif total[1] == "3":
                    my_list_final.append("J"+"♥")
                elif total[1] == "4":
                    my_list_final.append("J"+"♠")
            elif int(total[0]) == 12:
                if total[1] == "1":
                    my_list_final.append("Q"+"♣")
                elif total[1] == "2":
                    my_list_final.append("Q"+"♦")
                elif total[1] == "3":
                    my_list_final.append("Q"+"♥")
                elif total[1] == "4":
                    my_list_final.append("Q"+"♠")
            elif int(total[0]) == 13:
                if total[1] == "1":
                    my_list_final.append("K"+"♣")
                elif total[1] == "2":
                    my_list_final.append("K"+"♦")
                elif total[1] == "3":
                    my_list_final.append("K"+"♥")
                elif total[1] == "4":
                    my_list_final.append("K"+"♠")
            elif int(total[0]) == 14:
                if total[1] == "1":
                    my_list_final.append("A"+"♣")
                elif total[1] == "2":
                    my_list_final.append("A"+"♦")
                elif total[1] == "3":
                    my_list_final.append("A"+"♥")
                elif total[1] == "4":
                    my_list_final.append("A"+"♠")
        print(my_list_final)
    print("Comparsion times: "+str(compare))

insertionSort(["4♣", "A♣", "10♥", "K♦", "4♠", "10♣", "3♦", "7♥", "4♦"], 8)
selectionSort(["4♣", "A♣", "10♥", "K♦", "4♠", "10♣", "3♦", "7♥", "4♦"], 8)
bubbleSort(["4♣", "A♣", "10♥", "K♦", "4♠", "10♣", "3♦", "7♥", "4♦"], 8)
