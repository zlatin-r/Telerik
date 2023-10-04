input_list = input().split(",")
unique_list = []

for item in input_list:
    if item not in unique_list:  
        unique_list.append(item)  

print(",".join(unique_list))