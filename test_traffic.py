#from traffic.core import Traffic

from traffic.data import opensky

flights = opensky.history(

        start="2021-10-01 00:00",

        stop="2021-11-01 00:00",

        #arrival_airport="ESSA",
        departure_airport="ESSA",

        serials=(-1408232560, -1408232534),

    )


print(flights)

#print(flights.data.head())

df = flights.data
ground_df = df[df["onground"]==True]

df.to_csv("traffic_test_2021_10.csv", sep=' ', encoding='utf-8', float_format='%.6f', header=True, index = False)

ground_df = ground_df[["callsign", "latitude", "longitude"]]

ground_df.to_csv("traffic_test_omground_2021_10.csv", sep=' ', encoding='utf-8', float_format='%.6f', header=True, index = False)

df = df.set_index("callsign")
print(len(df.groupby(level="callsign")))

ground_df = ground_df.set_index("callsign")
print(len(ground_df.groupby(level="callsign")))