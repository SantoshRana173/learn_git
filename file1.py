#Listing all the digits present in a string
import re
def my_func(data):
    data_list = re.findall('[0-9]+', data)
    return data_list

def main():
    str1 = "My favourite numbers are 19, 29, 8, and 1"
    print(my_func(str1))


if __name__ ==  '__main__': 
    main()


