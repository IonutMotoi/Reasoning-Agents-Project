import matplotlib.pyplot as plt

axis = [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000]

data2 = [0.028, 0.198, 0.619, 1.424, 2.731, 4.594, 7.305, 10.728, 15.482, 21.974]

data3 = [0.028, 0.189, 0.594, 1.362, 2.590, 4.424, 6.999, 10.356, 14.837, 20.806]

data5 = [0.027, 0.185, 0.581, 1.341, 2.526, 4.307, 6.746, 9.961, 14.248, 19.695]

fig = plt.figure()
plt.grid()
plt.xlabel('Number of nodes')
plt.ylabel('Time (s)')
plt.plot(axis, data2, '-o', label="Priority 2")
plt.plot(axis, data3, '-o', label="Priority 3")
plt.plot(axis, data5, '-o', label="Priority 5")
plt.legend()
plt.show()

