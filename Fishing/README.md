# Fishing effort data

This dataset contains point data from [Global Fishing Watch](https://globalfishingwatch.org/data-download/datasets/public-fishing-effort).\
"Data is based on fishing detections of >114,000 unique AIS devices on fishing vessels, of which ~70,000 are active each year. Fishing vessels are identified via a neural network classifier, vessel registry databases, and manual review by GFW and regional experts. Data are binned into grid cells 0.01 (or 0.1) degrees on a side and measured in units of hours. The time is calculated by assigning an amount of time to each AIS detection (which is the time to the previous position), and then summing all positions in each grid cell."\
\
Data was downloaded in the format: **Fishing effort by flag state and gear type at 100th degree resolution.**\
\
Pandas was then used to trim down the dataset by selecting only vessels that were identified as fishing boats and had spent more than 0 hours fishing. Only boats that fished within the greater Puget Sound area were included. This dataset represents a large amount of vessel activity that took place between 2016 and 2021.
