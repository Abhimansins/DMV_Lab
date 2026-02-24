import matplotlib.pyplot as plt

# Data
labels = ["Python", "Java", "C++", "JavaScript"]
sizes = [30, 25, 20, 25]

# Plot
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

plt.title("Programming Language Popularity")
plt.show()
