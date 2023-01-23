import numpy as np

data = np.array(range(1, 11, 1))
n_boot = 10000
means = np.zeros(n_boot)

for i in range(n_boot):
    means[i] = np.mean(np.random.choice(data, size=data.size, replace=True))

print(np.quantile(means, [.025, .975]))
print(np.mean(data))


data = np.array(range(1, 11, 1)).astype(float)
n_boot = 10000
sds = np.zeros(n_boot)

for i in range(n_boot):
    boot_data = np.random.choice(data, size=data.size, replace=True)
    sds[i] = np.std(boot_data, ddof=1)

print(np.quantile(sds, [.025, .975]))
print(np.std(data, ddof=1))
