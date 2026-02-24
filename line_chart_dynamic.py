import matplotlib.pyplot as plt
n=int(input("Enter the number of points:"))
x=[]
y=[]
print("Enter values of X-Axis")
for i in range(n):
    val=int(input("Enter value"))
    x.append(val)
print("Enter values of Y-Axis")
for i in range(n):
    val=int(input("Enter value"))
    y.append(val)
plt.plot(x,y)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()