import math as mt
import random as rand
import matplotlib.pyplot as plt

Lx = (2 * 10 ** (-22)) ** (1 / 3)
Ly = (2 * 10 ** (-22)) ** (1 / 3)
Lz = (2 * 10 ** (-22)) ** (1 / 3)
T0 = 300
K = 1.38 * 10 ** (-23)
R = 5 * 10 ** (-9)
m = 10 ** (-28)
a = -10 ** (-7)
b = 10 ** (-66)
coord = []
Angles = []
dp = 0
V0 = mt.sqrt(2 * K * T0 / (100 * m))
t = Lx/100/V0
Velocity0 = []
Acceleration = []
w = 0
p = 0
q = 0
E = 0
T = []
Time = []
for i in range(100):
    coord1 = [rand.uniform(0, (10 ** (-22)) ** (1 / 3)), rand.uniform(0, (10 ** (-22)) ** (1 / 3)),
              rand.uniform(0, (10 ** (-22)) ** (1 / 3))]
    coord.append(coord1)
    angle = [rand.uniform(0, 180), rand.uniform(0, 360)]
    Angles.append(angle)
    vel = [mt.sin(mt.radians(angle[0])) * mt.cos(mt.radians(angle[1])) * V0,
           mt.sin(mt.radians(angle[0])) * mt.sin(mt.radians(angle[1])) * V0, mt.cos(mt.radians(angle[1])) * V0]
    Velocity0.append(vel)
    acc = [0, 0, 0]
    Acceleration.append(acc)
for z in range(10000):
    for k in range(100):
        for j in range(100):
            if (mt.sqrt((coord[k][0] - coord[j][0]) ** 2 + (coord[k][1] - coord[j][1]) ** 2 + (
                    coord[k][2] - coord[j][2]) ** 2) < R):
                r = mt.sqrt((coord[k][0] - coord[j][0]) ** 2 + (coord[k][1] - coord[j][1]) ** 2 + (
                            coord[k][2] - coord[j][2]) ** 2)
                if (r != 0.0):
                    Acceleration[k][0] = Acceleration[k][0] + (
                                3 * a * (coord[k][0] - coord[j][0]) / (r ** 5) + 5 * b * (coord[k][0] - coord[j][0]) / (
                                    r ** 7)) / m
                    Acceleration[k][1] = Acceleration[k][1] + (
                                3 * a * (coord[k][1] - coord[j][1]) / (r ** 5) + 5 * b * (coord[k][1] - coord[j][1]) / (
                                    r ** 7)) / m
                    Acceleration[k][2] = Acceleration[k][2] + (
                                3 * a * (coord[k][2] - coord[j][2]) / (r ** 5) + 5 * b * (coord[k][2] - coord[j][2]) / (
                                    r ** 7)) / m
    for i in range(100):
        Velocity0[i][0] = Velocity0[i][0] + Acceleration[i][0] * t
        Velocity0[i][1] = Velocity0[i][1] + Acceleration[i][1] * t
        Velocity0[i][2] = Velocity0[i][2] + Acceleration[i][2] * t
    for i in range(100):
        coord[i][0] = coord[i][0] + Velocity0[i][0] * t
        coord[i][1] = coord[i][1] + Velocity0[i][1] * t
        coord[i][2] = coord[i][2] + Velocity0[i][2] * t
        V0 = mt.sqrt(Velocity0[i][0] ** 2 + Velocity0[i][1] ** 2 + Velocity0[i][2] ** 2)
        if (coord[i][0] >= Lx or coord[i][0] <= 0):
            Velocity0[i][0] = -Velocity0[i][0]
            coord[i][0]=coord[i][0]+Velocity0[i][0]*t
            if (z >= 1900):
                dp = dp + 2 * m * Velocity0[i][0]
        if (coord[i][1] >= Ly or coord[i][1] <= 0) :
            Velocity0[i][1] = -Velocity0[i][1]
            coord[i][1] = coord[i][1] + Velocity0[i][1] * t
        if (coord[i][2] >= Lz or coord[i][2] <= 0):
            Velocity0[i][2] = -Velocity0[i][2]
            coord[i][2] = coord[i][2] + Velocity0[i][2] * t
        Acceleration[i][0] = 0
        Acceleration[i][1] = 0
        Acceleration[i][2] = 0
    if (z % 1000 == 0):
        Time.append(t * z)
        for l in range(100):
            E = E + m * (Velocity0[l][0] ** 2 + Velocity0[l][1] ** 2 + Velocity0[l][2] ** 2) / 2

        T.append(2 * E / (100 * 3 * K))
        E = 0
        print(coord[0][0])
P = dp / (100 * Ly * Lx)
print(P)
plt.figure()
plt.plot(Time, T, 'o-r')
plt.xlabel('Время, с')
plt.ylabel('Температура, К')
plt.legend()
plt.grid(True)
plt.show()
