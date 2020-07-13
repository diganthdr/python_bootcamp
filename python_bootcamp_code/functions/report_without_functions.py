numbers_list = [24,76,88,13,15,17,97,44,99,22]
count = 0
count_even = 0

for i in numbers_list:
    if i%2 == 0:
        pass #does nothing
        count_even = count_even + 1
        #print(i,"is an even number")
    else:
        #print(i,"is an odd number")
        count = count + 1

print("Sensor Report: ", count)

for i in numbers_list:
    if i%2 == 0:
        pass #does nothing
        #print(i,"is an even number")
    else:
        #print(i,"is an odd number")
        count = count + 1

print("Principal Report:", count)

for i in numbers_list:
    if i%2 == 0:
        pass #does nothing
        #print(i,"is an even number")
    else:
        #print(i,"is an odd number")
        count = count + 1
print("Sensor Report:", count)


#requirement: add 1 to odd,even counts in the report.

