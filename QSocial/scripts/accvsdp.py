import matplotlib.pyplot as plt
import numpy as np

batches = ["Batch 1", "Batch 2", "Bacth 3", "Batch 4"]
acc = [70, 100, 90, 70]

plt.bar(batches, acc, color='green', width=0.4)
plt.xlabel('Batches')
plt.ylabel("Accuracy")
plt.title("Bar plot of accuracy vs data points")
plt.savefig("accvsdp.png")
plt.show()
