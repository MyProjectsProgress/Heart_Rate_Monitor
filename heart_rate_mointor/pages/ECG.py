import streamlit as st
import pandas    as pd
import altair    as alt
import matplotlib.pyplot as plt

class variables:
    start      = 0
    graph_size = 10

start_btn  = st.sidebar.button(label='Show Graph Dynamically')

uploaded_file = st.sidebar.file_uploader(label='')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    signal_x_axis = (df.iloc[:,0]).to_numpy() # dataframe x axis
    signal_y_axis = (df.iloc[:,1]).to_numpy() # dataframe y axis

    #-------------------------------------- Plot Dynamic ----------------------------------------------------
    def plot_animation(df):
        brush  = alt.selection_interval ()
        chart1 = alt.Chart(df).mark_line().encode(x=alt.X('time', axis=alt.Axis(title='Time')),).properties(width=800, height=500).add_selection(brush).interactive()
        figure = chart1.encode(y=alt.Y('amplitude',axis=alt.Axis(title='Amplitude')))
        return figure

    def Dynamic_graph(signal_x_axis, signal_y_axis, start_btn):

        df = pd.DataFrame({'time': signal_x_axis[::1], 'amplitude': signal_y_axis[:: 1]}, columns=['time', 'amplitude'])

        lines     = plot_animation    (df)
        line_plot = st.altair_chart(lines)

        N     = df.shape[0]  # number of elements in the dataframe
        burst = 10           # number of elements  to add to the plot
        size  = burst        # size of the current dataset

        if start_btn:
            for i in range(1, N):
                variables.start      = i
                step_df              = df.iloc[0:size]
                lines                = plot_animation      (step_df)
                line_plot            = line_plot.altair_chart(lines)
                variables.graph_size = size
                size                 = i * burst 

    Dynamic_graph(signal_x_axis, signal_y_axis, start_btn)