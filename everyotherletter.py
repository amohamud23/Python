string = "house"
result = ""
for i in range(len(string)):
    if i%2 == 0:
        result += string[i]

print(result)