import pandas as pd 
import numpy as np
import statistics

data = "data.csv"

# df = pd.DataFrame(data)
mean = np.mean(data)
median = np.median(data)
# mode = st.mode(data))
variance = statistics.variance(data)
standard_dev = statistics.stdev(data)
print(mean, median, max(data), min(data), variance, standard_dev)
# print(df)