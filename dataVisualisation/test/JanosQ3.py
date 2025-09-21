from plotly.graph_objs import Line, Layout
from plotly import offline
from JanosQ2 import *

data = [Line(x= possible_nums, y= frequency_list)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling three D6 1,000 times',
                xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data, 'layout':my_layout}, filename='d6_d6_d6.html')
