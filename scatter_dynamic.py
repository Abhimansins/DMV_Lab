import matplotlib.pyplot as plt

n = int(input("Enter number of points: "))

x = []
y = []

print("Enter X values:")
for i in range(n):
    val=int(input("Enter value: "))
    x.append(val)
print("Enter Y values:")
for i in range(n):
    val=int(input("Enter value: "))
    y.append(val)
plt.scatter(x, y)

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Scatter Plot from User Input")

plt.show()
