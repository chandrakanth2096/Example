def create_pattern(n): # this is a function
    for i in range(1, n+1):
        print("* " * i)

n = 5
result = create_pattern(n) # function calling (passing n argument)


name = "Karthik"
for i in range(len(name)):
    print(name[i:])

result = ""
for i in name:
    result += i
    print(result)
