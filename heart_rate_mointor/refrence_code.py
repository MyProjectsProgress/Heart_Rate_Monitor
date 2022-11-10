import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import psutil
import collections

dataframe = pd.read_csv('./sample.csv') # reading csv file from the same directory
signal_x_axis = (dataframe.iloc[:,0]).to_numpy() # dataframe x axis
signal_y_axis = (dataframe.iloc[:,1]).to_numpy() # dataframe y axis

# Let’s start with collecting and storing the data. We’ll define two deques filled with zeros.
cpu = collections.deque(np.zeros(10))
ram = collections.deque(np.zeros(10))

# Then we’ll create a function to update the deques with new data. It’ll remove the last value of each deque and append a new one.
def my_function():
    cpu.popleft()
    cpu.append(psutil.cpu_percent(interval=1))
    ram.popleft()
    ram.append(psutil.virtual_memory().percent)
cpu = collections.deque(np.zeros(10))
ram = collections.deque(np.zeros(10))
# test
my_function()
my_function()
my_function()

# Now we can define the figure and subplots. Besides updating the deques, our function will also need to add this data to our chart.

# function to update the data
def my_function():
    cpu.popleft()
    cpu.append(psutil.cpu_percent(interval=1))
    ax.plot(cpu)
    ram.popleft()
    ram.append(psutil.virtual_memory().percent)
    ax1.plot(ram)
# start collections with zeros
cpu = collections.deque(np.zeros(10))
ram = collections.deque(np.zeros(10))
# define and adjust figure
fig = plt.figure(figsize=(12,6), facecolor='#DEDEDE')
ax = plt.subplot(121)
ax1 = plt.subplot(122)
ax.set_facecolor('#DEDEDE')
ax1.set_facecolor('#DEDEDE')
# test
my_function()
# plt.show()

# When we add FuncAnimation, it’ll repeatedly call our function to refresh the chart.
# But when we use .plot() multiple times on the same axis, it won’t update the line but rather plot new ones.When we add FuncAnimation, it’ll repeatedly call our function to refresh the chart.
# But when we use .plot() multiple times on the same axis, it won’t update the line but rather plot new ones.

# function to update the data
def my_function():
    # get data
    cpu.popleft()
    cpu.append(psutil.cpu_percent(interval=1))
    ram.popleft()
    ram.append(psutil.virtual_memory().percent)
    # clear axis
    ax.cla()
    ax1.cla()
    # plot cpu
    ax.plot(cpu)
    ax.scatter(len(cpu)-1, cpu[-1])
    ax.text(len(cpu)-1, cpu[-1]+2, "{}%".format(cpu[-1]))
    ax.set_ylim(0,100)
    # plot memory
    ax1.plot(ram)
    ax1.scatter(len(ram)-1, ram[-1])
    ax1.text(len(ram)-1, ram[-1]+2, "{}%".format(ram[-1]))
    ax1.set_ylim(0,100)
# start collections with zeros
cpu = collections.deque(np.zeros(10))
ram = collections.deque(np.zeros(10))
# define and adjust figure
fig = plt.figure(figsize=(12,6), facecolor='#DEDEDE')
ax = plt.subplot(121)
ax1 = plt.subplot(122)
ax.set_facecolor('#DEDEDE')
ax1.set_facecolor('#DEDEDE')
# test
my_function()
my_function()
my_function()
# plt.show()

ani = FuncAnimation(fig, my_function, interval=1000)

# function to update the data
def my_function(i):
    # get data
    cpu.popleft()
    cpu.append(psutil.cpu_percent())
    ram.popleft()
    ram.append(psutil.virtual_memory().percent)
    # clear axis
    ax.cla()
    ax1.cla()
    # plot cpu
    ax.plot(cpu)
    ax.scatter(len(cpu)-1, cpu[-1])
    ax.text(len(cpu)-1, cpu[-1]+2, "{}%".format(cpu[-1]))
    ax.set_ylim(0,100)
    # plot memory
    ax1.plot(ram)
    ax1.scatter(len(ram)-1, ram[-1])
    ax1.text(len(ram)-1, ram[-1]+2, "{}%".format(ram[-1]))
    ax1.set_ylim(0,100)
# start collections with zeros
cpu = collections.deque(np.zeros(10))
ram = collections.deque(np.zeros(10))
# define and adjust figure
fig = plt.figure(figsize=(12,6), facecolor='#DEDEDE')
ax = plt.subplot(121)
ax1 = plt.subplot(122)
ax.set_facecolor('#DEDEDE')
ax1.set_facecolor('#DEDEDE')
# animate
ani = FuncAnimation(fig, my_function, interval=1000)
plt.show()


# def plotting_graphs(signal_x_axis, signal_y_axis):

#         fig, axs = plt.subplots()
#         fig.set_size_inches(15,8)
#         plt.plot(signal_x_axis,signal_y_axis)
#         plt.title("ECG MONITOR")
#         # plt.xlim(45, 55)
#         plt.xlabel("Time in s")
#         plt.ylabel("ECG in mV")
#         st.pyplot(fig)
