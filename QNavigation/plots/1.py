import matplotlib.pyplot as plt

X = [1, 2, 3, 4, 5]
Y10 = [90, 90, 60, 70, 80]
Y20 = [90, 95, 65, 80, 80]
Y30 = [90, 93.33, 70, 76.67, 73.33]
Y40 = [87.5, 92.5, 70, 80, 77.5]
Y50 = [86, 94, 66, 82, 77.5]

plt.plot(X, Y10, marker='o')
plt.plot(X, Y20, marker='o')
plt.plot(X, Y30, marker='o')
plt.plot(X, Y40, marker='o')
plt.plot(X, Y50, marker='o')
plt.title("Plot of accuracy for all data points versus layers")
plt.xlabel("No. of layers")
plt.ylabel("Accuracy for each data points")
plt.legend(['10 data points', '20 data points', '30 data points', '40 data points', '50 data points'])
plt.savefig('plotAllDatapointVsLayers.png')
plt.show()