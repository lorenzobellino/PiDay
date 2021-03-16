import math
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
plt.rcParams['axes.titlesize'] = 25

def gridplot(nums):
    nums = np.array([int(num) for num in nums])
    lenn = len(nums)
    dims = int(math.ceil(math.sqrt(lenn)))
    nums = np.pad(nums, (0, (dims**2) - nums.shape[0]) ,mode='constant')
    nums = nums.reshape((dims,dims))
    fig, axe = plt.subplots(figsize=(10,10))
    mat = axe.matshow(nums, cmap=cm.nipy_spectral)
    plt.title("HAPPY PI DAY !")
    axe.axis('off')
    plt.savefig("PI.png")


if __name__ == "__main__":
    with open("./pi.txt") as fp:
        PI = fp.read()
        PI=PI.replace("\n","")
    gridplot(PI)
