import pandas as pd
import statistics as s
import plotly.figure_factory as pf

df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()

mean = s.mean(data)
median = s.median(data)
mode = s.mode(data)
std = s.stdev(data)

print("Mean, median, mode is {}, {}, {}".format(mean, median, mode))

fig = pf.create_distplot([data], ["reading score"], show_hist = False)
#fig.show()

first_std_start, first_std_end = mean-std, mean+std
second_std_start, second_std_end = mean-(2*std), mean+(2*std)
third_std_start, third_std_end = mean-(3*std), mean+(3*std)

datawithin_std1 = [result for result in data if result > first_std_start and result < first_std_end]
datawithin_std2 = [result for result in data if result > second_std_start and result < second_std_end]
datawithin_std3 = [result for result in data if result > third_std_start and result < third_std_end]

print("{}The percentage data for the first standard deviation lies in  ".format(len(datawithin_std1)*100.0/len(data)))
print("{}The percentage data for the second standard deviation lies in  ".format(len(datawithin_std2)*100.0/len(data)))
print("{}The percentage data for the third standard deviation lies in  ".format(len(datawithin_std3)*100.0/len(data)))