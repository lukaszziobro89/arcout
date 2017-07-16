def read_file(file_path):
    arctest = open(file_path, "r+")
    for line in arctest.readlines():
        print("normal text: {}".format(line),end='')
        print("length normal text: {}".format(str(len(line))))
        print(line.split(','))
        print("list length {}".format(len(line.split(','))))
        list_element(line.split(','), 2)
        print("-----------------------------------------------------")


def list_element(list, element_number):
    print(list[element_number])