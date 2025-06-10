import os
import argparse

parser = argparse.ArgumentParser(description="timeConsumption")

parser.add_argument(
    "--name",
    type=str,
    default="bgk"
)


name = parser.parse_args().name

path = "./data_" + name + "/zhrlog.txt"

epoch_times = []
with open(path, "r") as f:
    for line in f:
        if "epoch time:" in line:
            time_str = line.split("epoch time:")[1].split("ms")[0].strip()
            epoch_times = epoch_times if 'epoch_times' in locals() else []
            epoch_times.append(float(time_str))

epoch_times = epoch_times[1:]
print("Time", sum(epoch_times)/len(epoch_times))