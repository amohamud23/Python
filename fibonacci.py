temp1 = 1
temp2 = 0
result = 1
for i in range(20):
    if i > 1:
        result = temp2 + temp1
        print(result)
        temp1=temp2
        temp2= result
    
    else:
        print(result)
        
        result = temp1 + temp2
        temp2 = temp1


    
