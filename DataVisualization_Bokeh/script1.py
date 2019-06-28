from bokeh.plotting import figure, show
from bokeh.io import output_file, show

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]

output_file("like.html")

f = figure(plot_width=500, plot_height=400, tools='pan')

f.title.text="Cool Data"
f.title.text_color="Gray"
f.title.text_font="times"
f.title.text_font_style="bold"
f.xaxis.minor_tick_line_color=None
f.yaxis.minor_tick_line_color=None
f.xaxis.axis_label="Date"
f.yaxis.axis_label="Intensity"

f.line(x, y)
# f.circle(x, y)
# f.triangle(x, y)

show(f)



