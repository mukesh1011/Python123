from typing import Any, Union

from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas


df = pandas.read_csv("data.csv")

x = df["x"]
y = df["y"]


output_file("line_from_csv.html")

f = figure(plot_width=500,plot_height=400, tools='pan',logo=None)

f.line(x, y)
# f.circle(x, y)
# f.triangle(x, y)
# print(df)

show(f)



