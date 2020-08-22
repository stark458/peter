

def delete_recurring(x):
    set1 = set()
    outputstring = ''
    for char in x:
        print(char)
        if char not in set1:
            set1.add(char)
            outputstring += char
    print(set1)
          
    return outputstring

x = str(input('Enter a string:'))
y = len(x)

v = delete_recurring(x)

print(f"the string was \t {x} and obtained output is \t {v}")


        