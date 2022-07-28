def reverse_string(string):
    reverse_string = ""
    for s in string:
        reverse_string = s + reverse_string
    return reverse_string


def main():
    print(reverse_string("Hello World"))


if __name__ == "__main__":
    main()
    
