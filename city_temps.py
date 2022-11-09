import pandas as pd
from pathlib import Path

tempsPath = Path("Labs")/("cmsc140-f22-lab7")/("city_temperature.csv")
citytemps = pd.read_csv(tempsPath, sep = ",")



reg = citytemps.groupby(["Region"])
idx_max = reg["AvgTemperature"].idxmax()
max_temps = citytemps.loc[idx_max]

maxPath = Path("Labs")/("cmsc140-f22-lab7")/("city_maxtemps.csv")
max_temps.to_csv(maxPath)

print(max_temps)