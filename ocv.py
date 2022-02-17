import matplotlib.pyplot as plt
import numpy as np

###################################################################
# Raw data
H = np.array([-25.43, -101.74, -195.73]) # kJ/mol
S = np.array([11.22, 14.71, 23.64]) # J/mol-K
x = np.array([0.237, 0.597, 1.125])
xprime = np.arange(0, 1.25, 0.01)
T = 298 # K

# Other thermochemical data
Delta_G_LiF = -588.660 # kJ/mol
Delta_G_Li = 0
Delta_G_C = 0

###################################################################
# Linear regression to raw data
mH, bH = np.polyfit(x, H, 1)
mS, bS = np.polyfit(x, S, 1)

# Print fit parameters
print('m = {}, b= {}'.format(mH, bH))
print('m = {}, b= {}'.format(mS, bS))

###################################################################
# Plots
# Plot H vs x
# plt.plot(x, H, 'ro')
# plt.plot(xprime, mH*xprime + bH, 'b')
# plt.xlim([0.0, 1.2])
# plt.ylim([-200, 10])
# plt.xlabel('x in CFx')
# plt.ylabel('Delta H at 298 K (kJ/mol)')
# plt.show()
# plt.close()

# Plot S vs x
# plt.plot(x, S, 'ro')
# plt.plot(xprime, mS*xprime + bS, 'b')
# plt.xlim([0.0, 1.2])
# plt.ylim([0, 25])
# plt.xlabel('x in CFx')
# plt.ylabel('S at 298 K (J/mol.K)')
# plt.show()
# plt.close()
###################################################################

Delta_G_CF = (mH*1.0 + bH) - T*(mS*1.0 + bS)/1000
print('Delta G of reaction: ', Delta_G_LiF + Delta_G_C - Delta_G_CF - Delta_G_Li)
print('Voltage: ', -0.0103636*(Delta_G_LiF + Delta_G_C - Delta_G_CF - Delta_G_Li))