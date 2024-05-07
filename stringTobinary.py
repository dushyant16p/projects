def string_to_binary(string):
    binary_result = ""
    for char in string:
        
        binary_char = format(ord(char), '08b')  
        binary_result += binary_char + " "  
    return binary_result.strip()  



text = input("enter text you want to covert into binary:")


binary_code = string_to_binary(text)

print("Binary representation:", binary_code)
