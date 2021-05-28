The ['Fishing' folder](https://github.com/OscarLewis/salmon-fishing/tree/main/Fishing) in this repo contains a [GeoPackage](https://github.com/OscarLewis/salmon-fishing/wiki/GeoPackage) file named **'fleet_range.GPKG'**. This is a file of vector point data from [Global Fishing Watch](https://globalfishingwatch.org/data-download/datasets/public-fishing-effort).

From their site: "Data is based on fishing detections of >114,000 unique AIS devices on fishing vessels, of which ~70,000 are active each year. Fishing vessels are identified via a neural network classifier, vessel registry databases, and manual review by GFW and regional experts. Data are binned into grid cells 0.01 (or 0.1) degrees on a side and measured in units of hours. The time is calculated by assigning an amount of time to each AIS detection (which is the time to the previous position), and then summing all positions in each grid cell."

Data for this project was downloaded in the format: **Fishing effort by flag state and gear type at 100th degree resolution.**

Pandas was then used to trim down the dataset by selecting only vessels that were identified as fishing boats and had spent more than 0 hours fishing. Only boats that fished within the greater Puget Sound area were included. This dataset represents a large amount of vessel activity that took place between 2016 and 2021.

Each layer in fleet_range.GPKG represents a year's worth of detections.

The attribute table of each 'fleet' layer contains the following information:

- index: leftover from pandas and can be discarded
- date: a string in format YYYY-MM-DD
- cell_ll_la: the southern edge of the grid cell the vessel was detected in, in 100ths of a degree - 101 is the grid cell with a southern edge at 1.01 degrees north
- cell_ll_lo: the western edge of the grid cell the vessel was detected in, in 100ths of a degree - 101 is the grid cell with a western edge at 1.01 degrees east
- flag: the flag state of the fishing effort, in iso3 value
- geartype: currently only 'fishing' but this is an issue and will be fixed
- vessel_hours: hours that vessels of this geartype and flag were present in this gridcell on this day
- fishing_hours: hours that vessels of this geartype and flag were fishing in this gridcell on this day
- mmsi_present: number of mmsi of this flag state and geartype that visited this grid cell on this day
