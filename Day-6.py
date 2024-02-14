#pattern programs
# rows = 6
# for i in range(rows):
#   for j in range(i):
#     print(i,end='')
#   print('') 

    #pyramid numbers
# rows = 5
# for i in range(1,rows+1):
#   for j in range(1,i+1):
#     print(j, end=' ')
#   print(' ')  

# rows = 5
# reverse_rows = 0
# for i in range(rows, 0, -1):
#   reverse_rows += 1
#   for j in range(1,i+1):
#     print(reverse_rows, end= ' ')
#   print(' ')  

# rows = 10
# same_rows = rows
# for i in range(rows,0,-1):
#   for j in range(0,i):
#     print(same_rows, end=' ')
#   print('')


#half pyramid

rows = 5
for i in range(rows,0,-1):
  for j in range(0,1,i+1):
    print()