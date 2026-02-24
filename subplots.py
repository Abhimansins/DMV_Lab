import matplotlib.pyplot as plt

x = [1,2,3,4]
y1 = [10,20,30,40]
y2 = [40,30,20,10]

fig, ax = plt.subplots(1, 2)

ax[0].plot(x, y1)
ax[0].set_title("Increasing")

ax[1].plot(x, y2)
ax[1].set_title("Decreasing")

plt.show()
