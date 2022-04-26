import numpy as np
import matplotlib.pyplot as plt
with open("settings.txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")]


data_array = np.loadtxt("data.txt", dtype=int)
fig, ax=plt.subplots(figsize=(16,10),dpi=400)
ax.set_title('Процесс заряда и разряда конденсатора в RC-цепочке')
ax.set_xlabel('Время, с')
ax.set_ylabel('Напряжение, В')
ax.plot(data_array, label = 'V(t)')
ax.settle
plt.legend()
plt.grid(True)
plt.show()