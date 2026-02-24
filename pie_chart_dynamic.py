import matplotlib.pyplot as plt

n = int(input("Enter number of categories: "))

labels = []
sizes = []

# Input labels
for i in range(n):
    label = input("Enter label: ")
    labels.append(label)

# Input values
for i in range(n):
    value = float(input("Enter value for label: "))
    sizes.append(value)

# Plot
plt.pie(sizes, labels=labels)

plt.title("Pie Chart from User Input")
plt.show()
