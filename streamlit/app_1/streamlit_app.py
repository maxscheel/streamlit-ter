import streamlit as st

import plotly.figure_factory as ff
import numpy as np

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
         hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)


from streamlit_echarts import st_echarts

option = {
    "xAxis": {
        "type": "category",
        "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    },
    "yAxis": { "type": "value" },
    "series": [
        {"data": [820, 932, 901, 934, 1290, 1330, 1320], "type": "line" }
    ],
}
events = {
    "click": "function(params) { console.log(params.name); return params.name }",
    "dblclick":"function(params) { return [params.type, params.name, params.value] }"
}
value = st_echarts(option, events=events)
st.write(value)  # shows name on bar click and type+name+value on bar double click


