import csv
from datetime import datetime
from speedtest import Speedtest

speedtest = Speedtest()

with open("internet-speed.csv", mode="a") as logfile:
    csvwriter = csv.writer(logfile)

    while True:
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        download = round((round(speedtest.download()) / 1048576), 2)
        upload = round((round(speedtest.upload()) / 1048576), 2)

        print(timestamp, download, upload)
        csvwriter.writerow([timestamp, download, upload])
