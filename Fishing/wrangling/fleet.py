import sys
import os
import pandas


def main():
    # BOUNDING BOX
    # LAT 49 to 45.37
    # LONG -125.4 to -120.9
    lowLat = 45.37
    highLat = 49
    lowLong = -125.4
    highLong = -120.9

    # Set up paths for use in walking through directories
    root_name, _, _ = __name__.partition(".")
    root_module = sys.modules[root_name]
    root_dir = os.path.dirname(root_module.__file__)

    print("enter dir name to read csv's from: ")
    work_dir_name = input()

    print("enter a name for the output file")
    output_name = input() + ".csv"

    # Set up initial data dictionary, appending to a dictionary is faster than appending to a pandas dataframe
    data_dir = os.path.join(root_dir, work_dir_name)
    data_dic = {}

    # Walk through files, do panda analysis, add each csv to the running data dictionary
    for subdir, dirs, files in os.walk(data_dir):
        for file in files:
            filepath = subdir + os.sep + file
            print(f"loading from {filepath}")

            # Use pandas to import the csv file for that day and create a dataframe
            df = pandas.read_csv(subdir + os.sep + file)

            # Check that that vessel is within the 'bounding box', is geared as a fishing vessell, and has fished recently
            trimmed_df = df.query(
                (
                    f"cell_ll_lat < {highLat} & cell_ll_lat > {lowLat} & cell_ll_lon < {highLong} & cell_ll_lon > {lowLong} & fishing_hours > 0.0"
                )
            )

            if not trimmed_df.dropna().empty:
                temp_dict = trimmed_df.to_dict("index")
                data_dic = data_dic | temp_dict

    # Output the complete data dictionary as a csv file
    df = pandas.DataFrame.from_dict(data_dic, orient="index")
    df.to_csv(output_name, index_label="index")
    print("output created")


if __name__ == "__main__":
    main()
