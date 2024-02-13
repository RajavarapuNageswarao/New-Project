target = int(input("please provide the target number"))
even_num = 0
odd_num = 0
for sum_of_even_odd in range(1,target+1):
    if sum_of_even_odd % 2 == 0:
        even_num += sum_of_even_odd
    else:
        odd_num += sum_of_even_odd
print(f"sum of even number {even_num}")
print(f"sum of odd number {odd_num}")  