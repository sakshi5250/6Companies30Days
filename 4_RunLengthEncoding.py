def RunLenthEncoding(Input_String):

    n = len(Input_String)
    i = 0
    while i < n - 1:

        count = 1
        while (i < n - 1 and
               Input_String[i] == Input_String[i + 1]):
            count += 1
            i += 1
        i += 1

        print(Input_String[i - 1] +
              str(count),
              end="")


if __name__ == "__main__":

    Input_string = input("Enter String:")
    RunLenthEncoding(Input_string)
