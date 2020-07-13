
#With functions:  Repetitive job is put inside a function, we can reuse the code!
# -------------------------------------------
def count_number_of_odd_numbers(numbers_list):
    ''' This function counts number of odd numbers, 
    input is list of numbers, 
    output is and integer number of odd numbers'''

    count_odd = 0
    count_even = 0
    for i in numbers_list:
        if i%2 == 0:
            pass #does nothing
            count_even = count_even + 1
            #print(i,"is an even number")
        else:
            #print(i,"is an odd number")
            count_odd = count_odd + 1

    return count_odd+1, count_even + 1

input_numbers_list = [24,76,88,13,15,17,97,44,99,22]

def sensor_report(input_numbers_list):
    print("Sensor Report:")
    odd, even = count_number_of_odd_numbers(input_numbers_list)
    print(odd, even)

def security_report(input_numbers_list):
    print("Security Report:")
    odd, even = count_number_of_odd_numbers(input_numbers_list)
    print(odd, even)
    
def principal_report(input_numbers_list):
    print("Principal Report:")
    odd, even = count_number_of_odd_numbers(input_numbers_list)
    print(odd, even)


#----- main function , calling generate reports:
def generte_reports():
    input_numbers_list = [24,76,88,13,15,17,97,44,99,22]
    sensor_report(input_numbers_list)
    security_report(input_numbers_list)
    principal_report(input_numbers_list)

generte_reports()