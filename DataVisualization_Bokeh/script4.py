from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas


df = pandas.read_excel("verlegenhuken.xlsx")

x = df["Temperature"] / 10
y = df["Pressure"] / 10


output_file("weather_chart.html")

f = figure(plot_width=500, plot_height=400, tools='pan')

f.circle(x, y, size=0.5)
# f.circle(x, y)
# f.triangle(x, y)
# print(df)
f.title.text = "Temperature and Air Pressure"
f.title.text_color="Gray"
f.title.text_font="times"
f.title.text_font_style="bold"
f.xaxis.axis_label="Temperature(C)"
f.yaxis.axis_label="Pressure(hPa)"

show(f)
