import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")
data = df["math score"].tolist()

mean = sum(data)/len(data)
median = statistics.median(data)
mode = statistics.mode(data)
std_deviation = statistics.stdev(data)

print("The mean is ", mean)
print("The median is ", median)
print("The mode is ", mode)
print("The Standard Deviation is ", std_deviation)

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

fig = ff.create_distplot([data], ["Result"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.18], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0,0.18], mode="lines", name="STD1START"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0,0.18], mode="lines", name="STD1END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0,0.18], mode="lines", name="STD2START"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0,0.18], mode="lines", name="STD2END"))
fig.show()

std1 = [result for result in data if result > first_std_deviation_start and result < first_std_deviation_end]
std2 = [result for result in data if result > second_std_deviation_start and result < second_std_deviation_end]
std3 = [result for result in data if result > third_std_deviation_start and result < third_std_deviation_end]

print("{}% of data lies within First Standard Deviation".format(len(std1)*100.0/len(data)))
print("{}% of data lies within Second Standard Deviation".format(len(std2)*100.0/len(data)))
print("{}% of data lies within Third Standard Deviation".format(len(std3)*100.0/len(data)))