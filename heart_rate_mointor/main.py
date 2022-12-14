import streamlit as st
import serial
import matplotlib.pyplot as plt

st.title('Singal Monitor')

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
        serial_object = serial.Serial('COM7' , 9600)
        serial_object.close()
        serial_object.open()
    except:
        st.header("Connect Your Arduino to The Right Port")   
        
    flag = True
    i = 0

    while flag:
        try:
            serial_object.flushInput()
            serial_object.flushOutput()
            serial_object.flush()
            data = serial_object.readline()
            print(data.decode())
            x_axis.append(counter)
            y_axis.append(float(data.decode()))
            counter += 1

            if(len(x_axis) < 20):
                plot(x_axis,y_axis,graph_placeholder)
            else:
                plot(x_axis[i:],y_axis[i:],graph_placeholder)
                i+=1

        except:
            pass
        plt.pause(0.0001)

load_view()