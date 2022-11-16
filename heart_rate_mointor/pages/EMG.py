import streamlit as st
import pandas    as pd
import altair    as alt
import matplotlib.pyplot as plt
import numpy as np
import statistics
from matplotlib import animation
import time

class variables:
    start      = 0
    graph_size = 10

start_btn  = st.sidebar.button(label='Show Graph Dynamically')

uploaded_file = st.sidebar.file_uploader(label='')

placeholder = st.empty()

fig, axs = plt.subplots(2, figsize=(15, 15))

def plot(means,ranges,placeholder):
    axs[0].plot(means,marker='o', color='black')
    axs[1].plot(ranges,marker='o', color='black')
    placeholder.write(fig)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    signal_x_axis = (df.iloc[:,0]).to_numpy() # dataframe x axis
    signal_y_axis = (df.iloc[:,1]).to_numpy() # dataframe y axis

#---------------------------------------Hoba------------------------------------

    mean_list = []
    ranges_list = []

    samples = signal_y_axis[:16500]
    dataSize = len(samples)
    
   

    groups = (np.split(samples,dataSize//10))

    for group in groups:
        mean_list.append(group.mean())
        ranges_list.append(group.max() - group.min())

    # x_axis = np.arange(0,220,1)

    # Plot x-bar and ranges_list charts
    

    # x-bar chart
    # axs[0].plot(mean_list, linestyle='-', marker='o', color='black')
    A2 = 0.31
    D3 = 0.22
    D4 = 1.78
    axs[0].axhline((statistics.mean(mean_list)+A2*statistics.mean(ranges_list)),
                    color='red', linestyle='dashed')
    axs[0].axhline((statistics.mean(mean_list)-A2*statistics.mean(ranges_list)),
                    color='red', linestyle='dashed')
    axs[0].axhline((statistics.mean(mean_list)), color='blue')
    axs[0].set_title('x-bar Chart')
    axs[0].set(xlabel='Group', ylabel='Mean')

    # ranges_list chart
    # axs[1].plot(ranges_list, linestyle='-', marker='o', color='black')
    axs[1].axhline((D4*statistics.mean(ranges_list)), color='red', linestyle='dashed')
    axs[1].axhline((D3*statistics.mean(ranges_list)), color='red', linestyle='dashed')
    axs[1].axhline((statistics.mean(ranges_list)), color='blue')
    axs[1].set_ylim(bottom=0)
    axs[1].set_title('ranges_list Chart')
    axs[1].set(xlabel='Group', ylabel='Range')

    for i in range(len(signal_x_axis)):
        plot(mean_list[:i],ranges_list[:i],placeholder)
        if mean_list[i] > statistics.mean(mean_list)+A2*statistics.mean(ranges_list) or mean_list[i] < statistics.mean(mean_list)-A2*statistics.mean(ranges_list):
            st.write('Group', i, 'out of mean control limits!')
        if ranges_list[i] > D4*statistics.mean(ranges_list) or ranges_list[i] < D3*statistics.mean(ranges_list):
            st.write('Group', i, 'out of range cotrol limits!')
        time.sleep(0.2)
        

    # st.pyplot(fig)

    # Validate points out of control limits for x-bar chart
    i = 0
    control = True
    for group in mean_list:
        if group > statistics.mean(mean_list)+A2*statistics.mean(ranges_list) or group < statistics.mean(mean_list)-A2*statistics.mean(ranges_list):
            st.write('Group', i, 'out of mean control limits!')
            control = False
        i += 1
    if control == True:
        st.write('All points within control limits.')

    # Validate points out of control limits for ranges_list chart
    i = 0
    control = True
    for group in ranges_list:
        if group > D4*statistics.mean(ranges_list):
            st.write('Group', i, 'out of range cotrol limits!')
            control = False
        i += 1
    if control == True:
        st.write('All points within control limits.')

    # -------------------------------------- Plot Dynamic ----------------------------------------------------
    def plot_animation(df):
        brush  = alt.selection_interval ()
        chart1 = alt.Chart(df).mark_line().encode(x=alt.X('time', axis=alt.Axis(title='Time')),).properties(width=800, height=500).add_selection(brush).interactive()
        figure = chart1.encode(y=alt.Y('amplitude',axis=alt.Axis(title='Amplitude')))
        return figure

    def Dynamic_graph(signal_x_axis, signal_y_axis, start_btn):

        df = pd.DataFrame({'time': signal_x_axis[::15], 'amplitude': signal_y_axis[:: 15]}, columns=['time', 'amplitude'])

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


    def Dynamic_x_bar(signal_x_axis, signal_y_axis, start_btn):

        df = pd.DataFrame({'time': signal_x_axis[::], 'amplitude': signal_y_axis[::]}, columns=['time', 'amplitude'])

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
    # Dynamic_x_bar(x_axis,mean_list,start_btn)