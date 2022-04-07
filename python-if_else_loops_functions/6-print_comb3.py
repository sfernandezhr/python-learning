'''
1. imprimir todas las combinaciones posibles de dos digitos
2. Las cifras deben estar separadas por compas y un espacio
3. los dos digitos deben ser distintos
4. los numeros deben ir ascendiendo

list.append(i)
    for e in list:
        if e not in duplicates:
            duplicates.append(e)

'''


#list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]

#for i in range (1,90):
    #print(().zfill(2),end=", ")
    #print(str(i).zfill(2),end=", ")



'''two_digit_number_list = list() 
for i in range(1, 90): 
	two_digit_number_list.append(i)
  
res = [sub for sub in two_digit_number_list if len(set(str(sub))) == len(str(sub))]
convert= ' '.join([str(item) for item in two_digit_number_list])

#print(convert)
for i in res:
    print(f'{i:02}',end=', ')'''


for i in range(8):
    for j in range(i+1,10):


        print(f'{i}{j}',end=', ')
print('89')        

