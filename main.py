from re import sub


def reverse_string(string):
    tempString = ""
    for s in string:
        tempString = s + tempString
    return tempString


def reverse_string_2(my_string):
    my_string = list(my_string)
    
    i = 0
    j = len(my_string) - 1
    
    while (i < j):
        temp = my_string[j]
        my_string[j] = my_string[i]
        my_string[i] = temp
        i += 1
        j -= 1 
        
    return str(my_string)

def find_substring(string, substring):
    j = 0
    for i in range(len(string)):
        if string[i] == substring[j]:
            for j in range(len(substring)):
                if string[i] == substring[j]:
                    if (j+1) == len(substring):
                        if (i - j) < 0:
                            return None
                        return i - j
                    

 
            



def main():
    print(reverse_string("Hello World"))
    
    print(reverse_string_2("Hello World"))
    
    print(find_substring("Hello World", "orld"))


if __name__ == "__main__":
    main()


    
