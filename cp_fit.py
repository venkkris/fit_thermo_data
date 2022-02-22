import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

# Raw data from Nakajima textbook
Cp_data_CF = np.array([0.3175, 0.7363, 2.449, 5.185, 8.468, 14.51, 19.45, 23.70, 27.57]) # [J/K.mol]
T_data_CF = np.array([15, 25, 50, 75, 100, 150, 200, 250, 300]) # [K]

# Raw data from JANAF table for LiF
Cp_data_LiF = np.array([0, 12.816, 32.803, 41.815, 41.936, 46.543, 49.329]) # [J/K.mol]
T_data_LiF = np.array([0, 100, 200, 298.15, 300, 400, 500]) # [K]

T_fit_CF = np.linspace(0, 300, 100)
T_fit_LiF = np.linspace(0, 500, 100)

# Define Cp function
def Cp (T, a, b, c, d):
    return a + b*T + c*T**2 + d*T**3

# Fit data to Cp function
popt_CF, pcov_CF = curve_fit(Cp, T_data_CF, Cp_data_CF)
popt_LiF, pcov_LiF = curve_fit(Cp, T_data_LiF, Cp_data_LiF)
Cp_fit_CF = Cp(T_fit_CF, *popt_CF)
Cp_fit_LiF = Cp(T_fit_LiF, *popt_LiF)

# Plot Cp vs T for CF1.125
plt.plot(T_data_CF, Cp_data_CF, 'o')
plt.plot(T_fit_CF, Cp_fit_CF)
plt.xlim(0, 300)
plt.ylim(0, 30)
plt.xlabel('T [K]')
plt.ylabel('Cp [J/K.mol]')
plt.title('Cp vs. T for $CF_{1.125}$')
plt.savefig('Cp_CF.png')
# plt.show()
plt.close()

# Plot Cp vs T for LiF
plt.plot(T_data_LiF, Cp_data_LiF, 'o')
plt.plot(T_fit_LiF, Cp_fit_LiF)
plt.xlim(0, 500)
plt.ylim(0, 60)
plt.xlabel('T [K]')
plt.ylabel('Cp [J/K.mol]')
plt.title('Cp vs. T for LiF')
plt.savefig('Cp_LiF.png')
# plt.show()
plt.close()

# Compute Delta H between 298 K and 0 K for CF
a = popt_CF[0]
b = popt_CF[1]
c = popt_CF[2]
d = popt_CF[3]
Delta_H = a*(298) + b*(298)**2/2 + c*(298)**3/3 + d*(298)**4/4
print('H_298 - H_0 for CF = {:1.4} kJ/mol'.format(Delta_H/1000))

# Compute Delta H between 298 K and 0 K for LiF
a = popt_LiF[0]
b = popt_LiF[1]
c = popt_LiF[2]
d = popt_LiF[3]
Delta_H = a*(298) + b*(298)**2/2 + c*(298)**3/3 + d*(298)**4/4
print('H_298 - H_0 for LiF = {:1.5} kJ/mol'.format(Delta_H/1000))
