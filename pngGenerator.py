import numpy as np
import matplotlib.pyplot as plt
import os
import argparse

parser = argparse.ArgumentParser(description="plot")

parser.add_argument(
    "--name",
    type=str,
    default="bgk"
)


name = parser.parse_args().name

npy_path = "./mydown_" + name + "/loss_list_of_" + name.upper() + ".npy"
loss = np.load(npy_path)


plt.plot(loss)
plt.title(name + " train loss")
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.yscale("log")
plt.show()
