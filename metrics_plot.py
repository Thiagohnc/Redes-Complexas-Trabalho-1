import numpy as np
import matplotlib.pyplot as plt


def plot_normalized_histogram(sample):
    bin_max_number = 0
    bin_size = 1
    x, y, bin_sizes = [], [], []

    sample.sort()
    for i in range(len(sample)):
        if sample[i] <= bin_max_number:
            y[-1] += 1
        else:
            bin_max_number += bin_size
            x.append(bin_max_number)
            y.append(1)
            bin_sizes.append(bin_size)
            bin_size *= 2

    x = np.array(x)
    y = np.array(y)
    y = y / len(sample)  # Getting fraction of the counts
    y = y / bin_sizes  # Normalizing

    plt.loglog(x, y, '.')
    plt.show()


def plot_ccdf(sample):
    x, y, bin_sizes = [], [], []

    sample.sort()
    uniques, counts = np.unique(np.array(sample), return_counts=True)
    total_remaining = sum(counts)
    total = sum(counts)
    for i in range(len(uniques)):
        x.append(uniques[i])
        y.append(total_remaining / total)
        total_remaining -= counts[i]
    plt.loglog(x, y, '.')
    plt.show()


# fixme result seems to be wrong
def estimate_by_ccdf(sample):
    x0 = min(sample)
    n = len(sample)
    sample = np.array(sample)

    a = n / np.sum(np.log(sample / x0))

    print(a)
    return a
