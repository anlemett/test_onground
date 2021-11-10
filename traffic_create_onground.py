import pandas as pd

filename = "traffic_test_2021_10_arrivals.csv"
#filename = "traffic_test_2021_10_departures.csv"
df = pd.read_csv(filename, sep=' ')

ground_df = df[df["onground"]==True]

ground_df = ground_df[["callsign", "day", "latitude", "longitude"]]

ground_df.to_csv("traffic_test_onground_2021_10_arrivals.csv", sep=' ', encoding='utf-8', float_format='%.6f', header=True, index = False)
#ground_df.to_csv("traffic_test_onground_2021_10_departures.csv", sep=' ', encoding='utf-8', float_format='%.6f', header=True, index = False)
