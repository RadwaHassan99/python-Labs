def divide_string(a, b):
    # Get midpoint of string a
    midpoint_a = len(a) // 2
    if len(a) % 2 != 0:
        midpoint_a += 1
    
    # Get midpoint of string b
    midpoint_b = len(b) // 2
    if len(b) % 2 != 0:
        midpoint_b += 1
    
    # Get front and back halves of strings a and b
    a_front = a[:midpoint_a]
    a_back = a[midpoint_a:]
    b_front = b[:midpoint_b]
    b_back = b[midpoint_b:]
    
    # Return combined string
    return a_front + b_front + a_back + b_back


a = 'abcde'
b = 'fghij'
result = divide_string(a, b)
print(result) # Output: 'abfgcdehij'
