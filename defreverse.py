def reverse_string(string):
    reversed = ""
    length = len(string)
    for i in range(length - 1, -1, -1):
        reversed += string[i]
    return reversed
input= input("Enter a string: ")
reversed_result = reverse_string(input)
print("Reversed string:", reversed_result)
