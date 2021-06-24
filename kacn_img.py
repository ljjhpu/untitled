import matplotlib.pyplot as plt

x_data = [1, 2, 3, 4, 5]
x_index = ['4', '8', '16', '32', '64']
y_data = [0.902, 0.910, 0.900, 0.858, 0.840]


plt.plot(x_data, y_data, marker='*')

plt.xticks(x_data, x_index)
plt.yticks([0.800, 0.825, 0.850,0.875, 0.900,0.925])

plt.xlabel('neighbor_sample_size')
plt.ylabel('test_auc')

plt.show()
