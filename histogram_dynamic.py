import matplotlib.pyplot as plt
data=[]
n=int(input("Enter the number of data:"))
print("Enter the data")
for i in range(n):
    val=int(input("Enter value: "))
    data.append(val)
plt.hist(data)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()
