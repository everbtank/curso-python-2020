
i=0
numbers=[]

while i<9:
    print(f"at top i is: {i}")
    numbers.append(i)
    i=i+1
    print("Number now:", numbers)
    print(f"at the botton i is {i}")

print("los numeros:")
for nums in numbers:
    print(nums)
