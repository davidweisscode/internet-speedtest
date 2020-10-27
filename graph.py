import csv
import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

timestamps = []
downloads = []
uploads = []

with open("internet-speed.csv", mode="r") as logfile:
    measurements = csv.reader(logfile, delimiter=",")
    for measurement in measurements:
        timestamps.append(datetime.datetime.strptime(measurement[0], "%d-%m-%Y %H:%M:%S"))
        downloads.append(float(measurement[1]))
        uploads.append(float(measurement[2]))

    fig, ax = plt.subplots()
    ax.plot(timestamps, downloads, label="Download", color="#00a")
    ax.plot(timestamps, uploads, label="Upload", color="#88e")
    ax.set_xlabel("Time")
    ax.set_ylabel("Speed in Mb/s")
    myFmt = DateFormatter("%H:%M")
    ax.xaxis.set_major_formatter(myFmt)
    fig.autofmt_xdate()
    ax.legend()
    ax.grid()
    ax.set_title("Download & Upload Internet Speed")
    fig.savefig("internet-speed.jpg", bbox_inches="tight")
    plt.show()
