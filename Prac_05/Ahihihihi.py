

def main():
    list_name = ['Hung', 'Is', 'One', 'Person', 'Ahihi']
    list_age = [19, 23, 45, 56, 89]

    print(sortList(list_name, list_age))


def sortList(a_list_name, a_list_age):

    stringToPrint = ""
    for i in range(len(a_list_age)):
        if max(a_list_age) == a_list_age[i]:
            stringToPrint = "The oldest person is {} and his/her age is {}".format(a_list_name[i], a_list_age[i])
            return stringToPrint
            break


main()