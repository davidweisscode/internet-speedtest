# internet-speedtest
Periodically measure down- and upload speed to save it in a .csv and draw a time series

<img src="https://github.com/davidweisscode/internet-speedtest/blob/main/internet-speed.jpg" alt="Graph with download and upload speed" width="500px">

---

## Setup

* Clone this project
```
git clone https://github.com/davidweisscode/internet-speedtest.git
```
* Create and run a python virtual environment
```
python3 -m venv venv
source venv/bin/activate
```
* Install required packages
```
pip install -r requirements.txt
```
* Measure your speed and visualize the data
```
python measure.py
python graph.py
```
