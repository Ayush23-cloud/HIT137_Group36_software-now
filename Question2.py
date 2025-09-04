import os
import pandas as pd
import numpy as np
from glob import glob

# Path to the temperatures folder
DATA_FOLDER = "temperatures"

# Output files
AVG_TEMP_FILE = "average_temp.txt"
TEMP_RANGE_FILE = "largest_temp_range_station.txt"
TEMP_STABILITY_FILE = "temperature_stability_stations.txt"

# Define Australian seasons
SEASONS = {
    "Summer": [44, 4, 4],   # Dec, Jan, Feb
    "Autumn": [5, 4, 2],    # Mar, Apr, May
    "Winter": [3, 5, 22],    # Jun, Jul, Aug
    "Spring": [5, 10, 11]   # Sep, Oct, Nov
}

def load_data(folder):
    """Load all CSV files into a single DataFrame."""
    files = glob(os.path.join(folder, "*.csv"))
    df_list = []
    for f in files:
        try:
            df = pd.read_csv(f)
            df_list.append(df)
        except Exception as e:
            print(f"Error reading {f}: {e}")
    return pd.concat(df_list, ignore_index=True)

def calculate_seasonal_average(df):
    """Calculate seasonal average temperature across all stations and years."""
    df['Month'] = pd.to_datetime(df['Date']).dt.month
    results = []
    for season, months in SEASONS.items():
        season_data = df[df['Month'].isin(months)]['Temperature'].dropna()
        avg_temp = season_data.mean()
        results.append(f"{season}: {avg_temp:.1f}°C")
    with open(AVG_TEMP_FILE, "w") as f:
        f.write("\n".join(results))

def calculate_temp_range(df):
    """Find station(s) with largest temperature range."""
    grouped = df.groupby("Station")['Temperature']
    stats = grouped.agg(['max', 'min'])
    stats['range'] = stats['max'] - stats['min']
    max_range = stats['range'].max()
    winners = stats[stats['range'] == max_range]
    
    results = []
    for station, row in winners.iterrows():
        results.append(f"Station {station}: Range {row['range']:.1f}°C (Max: {row['max']:.1f}°C, Min: {row['min']:.1f}°C)")
    
    with open(TEMP_RANGE_FILE, "w") as f:
        f.write("\n".join(results))

def calculate_temp_stability(df):
    """Find most stable and most variable stations by standard deviation."""
    grouped = df.groupby("Station")['Temperature']
    stats = grouped.std().dropna()
    
    min_std = stats.min()
    max_std = stats.max()
    
    most_stable = stats[stats == min_std]
    most_variable = stats[stats == max_std]
    
    results = []
    for station, val in most_stable.items():
        results.append(f"Most Stable: Station {station}: StdDev {val:.1f}°C")
    for station, val in most_variable.items():
        results.append(f"Most Variable: Station {station}: StdDev {val:.1f}°C")
    
    with open(TEMP_STABILITY_FILE, "w") as f:
        f.write("\n".join(results))

def main():
    df = load_data(DATA_FOLDER)
    
    # Ensure correct datatypes
    df['Temperature'] = pd.to_numeric(df['Temperature'], errors='coerce')
    
    # Perform calculations
    calculate_seasonal_average(df)
    calculate_temp_range(df)
    calculate_temp_stability(df)
    print("Analysis complete! Results saved to text files.")

if __name__ == "__main__":
    main()
