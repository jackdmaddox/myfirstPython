
#list_of_numbers = [-34, -23, 10, 51, 204, 12, 50, 37]

#Sum the Numbers 
#print(sum(list_of_numbers))

#Largest Number
#print(max(list_of_numbers))

#Smallest Number
#print(min(list_of_numbers))

#Even Numbers
#for number in list_of_numbers:
#    if number % 2 == 0:
#        print(number)

#Positive Numbers
#for number in list_of_numbers:
#   if number > 0:
#       print(number)

#Positive Numbers II
#second_number_list = []

#for number in list_of_numbers:
#    if number > 0:
#        second_number_list.append(number)
#print(second_number_list)

#Multiply a list
#multiplied_numbers =[]
#single_factor = 2
#for number in list_of_numbers:
#    multiplied_numbers.append(number * single_factor)
#print(multiplied_numbers)

#Multiply Vectors
# list_of_numbers = [-34, -23, 10, 51, 204, 12, 50, 37]
# multiply_vector_list = [1, 2, 3, 4, 5, 6, 7, 8]
# vector_results = []
# for number in range(0, len(list_of_numbers)):
#     vector_results.append(list_of_numbers[number] * multiply_vector_list[number])
# print(vector_results)

#Matrix Addition
# matrix_one = [[1,3], [2,4]]
# matrix_two = [[5,2], [1,0]]
# matrix_result = []
# for outerlist in range(len(matrix_one)):
#     for innernumber in range(len(matrix_one)):
#         matrix_result.append(matrix_one[outerlist][innernumber] + matrix_two[outerlist][innernumber])
# print(matrix_result)

#Matrix Addition II
# matrix_one = [[1,3, 4], [2,4, 5], [3,3, 3]]
# matrix_two = [[5,2, 4], [1,0, 5], [3,3, 3]]
# matrix_result = []
# for outerlist in range(len(matrix_one)):
#     for innernumber in range(len(matrix_one[0])):
#         matrix_result.append(matrix_one[outerlist][innernumber] + matrix_two[outerlist][innernumber])
# print(matrix_result)

#De-Dup
first_list = [1, 2, 2, 2, 3, 3, 4]
deduped_list = []
for number in first_list:
    if number not in deduped_list:
        deduped_list.append(number)
print(deduped_list)