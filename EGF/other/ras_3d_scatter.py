from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X1 = [0, 60, 120, 180, 300, 420]
X2 = [0, 120, 240, 360, 480, 600]
X3 = [0, 120, 240, 360, 480, 600]
X4 = [360, 360, 360, 360, 360, 360]
X5 = [360, 360, 360, 360, 360, 360]

Y1 = [0.165, 0.165, 0.165, 0.165, 0.165, 0.165]
Y2 = [0.165, 0.165, 0.165, 0.165, 0.165, 0.165]
Y3 = [0.165, 0.165, 0.165, 0.165, 0.165, 0.165]
Y4 = [0, 0.00165, 0.005, 0.0165, 0.05, 0.5]
Y5 = [0, 0.0165, 0.05, 0.165, 1.65, 16.5]

Z1 = [1.915, 8.244, 13.019, 24.925, 28, 24.697]
Z2 = [0.735, 12.697, 18.166, 24.266, 28, 24.679]
Z3 = [1.647, 12.188, 28, 19.647, 16.824, 13.882]
Z4 = [2.831, 7.548, 11.193, 17.951, 25.346, 28]
Z5 = [1.631, 12.686, 18.576, 21.113, 28, 16.854]
s = 96
ax.scatter(X1, Y1, Z1, c='red', marker='o', s=s)
ax.scatter(X2, Y2, Z2, c='blue', marker='o', s=s)
ax.scatter(X3, Y3, Z3, c='green', marker='o', s=s)
ax.scatter(X4, Y4, Z4, c='orange', marker='o', s=s)
ax.scatter(X5, Y5, Z5, c='purple', marker='o', s=s)

ax.set_xlabel('Time')
ax.set_ylabel('Dose')
ax.set_zlabel('Response')

plt.show()
