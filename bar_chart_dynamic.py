import matplotlib.pyplot as plt
n=int(input("Entet the number of categories:"))
categories=[]
values=[]
print("Enter the categories")
for i in range(n):
    val=input("Enter the category:")
    categories.append(val)
print("Enter the values:")
for i in range(n):
    val=int(input("Enter the values:"))
    values.append(val)
plt.bar(categories, values)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()