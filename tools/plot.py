import matplotlib.pyplot as plt
import numpy as np

axis = [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000]

data2 = [0.028, 0.198, 0.619, 1.424, 2.731, 4.594, 7.305, 10.728, 15.482, 21.974]

data3 = [0.028, 0.189, 0.594, 1.362, 2.590, 4.424, 6.999, 10.356, 14.837, 20.806]

data5 = [0.027, 0.185, 0.581, 1.341, 2.526, 4.307, 6.746, 9.961, 14.248, 19.695]

data10 = [0.027, 0.181, 0.561, 1.286, 2.418, 4.154, 6.540, 9.645, 13.775, 18.860]

data50 = [0.029, 0.178, 0.549, 1.247, 2.369, 4.061, 6.366, 9.381, 13.350, 18.299]

data100 = [0.030, 0.181, 0.559, 1.251, 2.367, 4.027, 6.321, 9.374, 13.247, 18.170]

dataN = [0.031, 0.205, 0.667, 1.469, 2.624, 4.143, 7.138, 10.258, 13.722, 22.316]

fig = plt.figure()
plt.grid()
plt.xlabel('Number of nodes')
plt.ylabel('Time (s)')
plt.xticks(np.arange(0, 2001, 200))
plt.plot(axis, data2, '-o', label="Max priority 2")
# plt.plot(axis, data3, '-o', label="Max priority 3")
# plt.plot(axis, data5, '-o', label="Max priority 5")
# plt.plot(axis, data10, '-o', label="Max priority 10")
# plt.plot(axis, data50, '-o', label="Max priority 50")
plt.plot(axis, data100, '-o', label="Max priority 100")
plt.plot(axis, dataN, '-o', label="Max priority N")
plt.legend()
plt.show()

