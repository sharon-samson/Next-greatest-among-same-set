number = 12345
new_number = number
count = 0
while count == 0:
    new_number = new_number + 1
    print(new_number)
    res = [int(x) for x in str(new_number)]
    res1 = [int(x) for x in str(number)]
    length_val = len(res)

    empty_list = []
    for i in range(0, length_val):
        if res[i] in res1:
            if new_number > number:
                if res[i] not in empty_list:
                    empty_list.append(res[i])

    print(empty_list)

    if len(empty_list) == len(res1):
        print("Next largest number is", empty_list)
        count += 1
    else:

        print("Not largest")

