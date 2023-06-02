from scipy.optimize import minimize, differential_evolution
import numpy as np
import matplotlib.pyplot as plt


def main(x):
    func = np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)
    return func


def main2(x):
    return int(main(x))


print('1 exercise')
initial_guess = [2]
result = minimize(main, initial_guess, method='BFGS')
print(result.fun)
initial_guess = [30]
result = minimize(main, initial_guess, method='BFGS')
print(result.fun)

print('2 exercise')
initial_second = [1, 30]
result2 = differential_evolution(main, [initial_second])
print(result2.fun)

print('3 exercise')
initial_third = [30]
result3 = minimize(main2, initial_third, method='BFGS')
print(result3.fun)
initial_fourth = [1, 30]
result4 = differential_evolution(main2, [initial_fourth])
print(result4.fun)


# x = np.arange(-100,100,1)
# y = main(x)
# plt.plot(x,y)
# plt.show()

