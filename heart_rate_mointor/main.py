import streamlit as st
import serial
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import altair as alt
import numpy as np
import statistics

#---------------------------------------MARINA------------------------------------
x_m = []

# Set random seed
np.random.seed(42)
x_m = x_m[-5: ]

# Create dummy data
x = np.array([list(np.random.normal(loc=10, scale=2, size=5)),
              list(np.random.normal(loc=10, scale=2, size=5)),
              list(np.random.normal(loc=10, scale=2, size=5)),
              list(np.random.normal(loc=10, scale=2, size=5)),
              list(np.random.normal(loc=10, scale=2, size=5)),
              list(np.random.normal(loc=17, scale=2, size=5)),
              list(np.random.normal(loc=10, scale=2, size=5)),
              list(np.random.normal(loc=10, scale=2, size=5)),
              list(np.random.normal(loc=10, scale=2, size=5)),
              list(np.random.normal(loc=10, scale=2, size=5))])

# Define list variable for groups means
mean_list = []

# Define list variable for groups ranges
ranges_list = []

# Get and append groups means and ranges
for group in x:
    mean_list.append(group.mean())
    ranges_list.append(group.max() - group.min())

# Plot x-bar and ranges_list charts
fig, axs = plt.subplots(2, figsize=(15, 15))

# x-bar chart
axs[0].plot(mean_list, linestyle='-', marker='o', color='black')
axs[0].axhline((statistics.mean(mean_list)+0.577*statistics.mean(ranges_list)),
                color='red', linestyle='dashed')
axs[0].axhline((statistics.mean(mean_list)-0.577*statistics.mean(ranges_list)),
                color='red', linestyle='dashed')
axs[0].axhline((statistics.mean(mean_list)), color='blue')
axs[0].set_title('x-bar Chart')
axs[0].set(xlabel='Group', ylabel='Mean')

# ranges_list chart
axs[1].plot(ranges_list, linestyle='-', marker='o', color='black')
axs[1].axhline((2.574*statistics.mean(ranges_list)), color='red', linestyle='dashed')
axs[1].axhline((0*statistics.mean(ranges_list)), color='red', linestyle='dashed')
axs[1].axhline((statistics.mean(ranges_list)), color='blue')
axs[1].set_ylim(bottom=0)
axs[1].set_title('ranges_list Chart')
axs[1].set(xlabel='Group', ylabel='Range')

st.pyplot(fig)

# Validate points out of control limits for x-bar chart
i = 0
control = True
for group in mean_list:
    if group > statistics.mean(mean_list)+0.577*statistics.mean(ranges_list) or group < statistics.mean(mean_list)-0.577*statistics.mean(ranges_list):
        print('Group', i, 'out of mean control limits!')
        control = False
    i += 1
if control == True:
    print('All points within control limits.')

# Validate points out of control limits for ranges_list chart
i = 0
control = True
for group in ranges_list:
    if group > 2.574*statistics.mean(ranges_list):
        print('Group', i, 'out of range cotrol limits!')
        control = False
    i += 1
if control == True:
    print('All points within control limits.')


#-------------------------------------EMAD-----------------------------------------
plt.ion()
figureGlobal = plt.figure()

def load_view():

    graph_placeholder = st.empty()
    
    def plot(x, y, placeholder):
        fig, axs = plt.subplots()
        fig.set_size_inches(6,3)
        axs.plot(x,y)
        placeholder.write(fig)
        
    ## Initializing the variables
    counter = 0
    x_axis = list()
    y_axis = list()

    try:
        serial_object = serial.Serial('COM21' , 9600)
        serial_object.close()
        serial_object.open()
    except:
        st.write("NO Problem")   
        
    flag = True
    i = 0

    while flag:
        try:
            serial_object.flushInput()
            serial_object.flushOutput()
            serial_object.flush()
            data = serial_object.readline()
            print(data.decode())
            ## concatenating the value of x and y to the list
            x_axis.append(counter)
            y_axis.append(float(data.decode()))
            counter += 1
            # if (counter%5==0):
            #     getx()
            if(len(x_axis) < 20):
                plot(x_axis,y_axis,graph_placeholder)
            else:
                plot(x_axis[i:],y_axis[i:],graph_placeholder)
                i+=1
        except:
            pass
        plt.pause(0.0001)

# load_view()