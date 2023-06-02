import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import stats
import scipy.stats as sps
import random

mu, beta, var = 0, 0.1, 2  # location and scale


# вычисление выборочных средних
def get_sample_mean(data, N):
    np.random.shuffle(data)
    sample = np.random.randint(0, len(data) - N, 1000)
    sample_mean = []
    for id in sample:
        mean = np.mean(data[id:id + N])
        sample_mean.append(mean)
    return sample_mean


# mu var сосчитано на основе теории с вики
sub_sample_size = 5
random_data = [random.gauss(100, 1000) for i in range(0, 10000)]
print(random_data)
sigma = math.sqrt(var)
se = sigma / math.sqrt(sub_sample_size)
print(f'mu = {mu}, var = {var}, sigma = {sigma}, 2*se = {2 * se}')

# строим искомые графики
bins = plt.hist(get_sample_mean(random_data, N=sub_sample_size), 50, density=True, label='Gumbel actual')
x = np.arange(-1, 1, .0001)
points = np.linspace(sps.norm.ppf(0.01,loc=mu,scale=sigma), sps.norm.ppf(0.9999, loc=mu,scale=sigma), 3)
pdf = sps.norm.pdf(points, loc=mu, scale=sigma)
plt.plot(bins, pdf, label='Gumbel theor')

norm_rv = stats.norm(mu, se)
plt.plot(x, norm_rv.pdf(x), label='Norm theor')
plt.legend()
plt.ylabel('$f(x)$')
plt.xlabel('$x$')
plt.show()

# Строим биплот для сравнения распределений
plt.subplot(3, 1, 3)
plt.title("Сравнение теоретического и фактического PDF для выборки %d", fontsize=16)

x = (pdf - np.min(pdf)) / (np.max(pdf) - np.min(pdf))
y_ = (bins - np.min(bins)) / (np.max(bins) - np.min(bins))

plt.scatter(x, y_)
plt.plot([0, 1], [0, 1], color='y')
plt.xlabel("pdf-theoretical", fontsize=16)
plt.ylabel("pdf-sample point", fontsize=16)

plt.tight_layout()
plt.grid()
print(sigma, np.point(get_sample_mean(random_data, N=sub_sample_size)))
