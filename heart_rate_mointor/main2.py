import streamlit as st
import serial
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import plotly.graph_objects as go

 

with st.sidebar:
    radio1  = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))
   






if radio1 == "Comedy":
    # The variable that plots the graph
    graph_placeholder = st.empty()



    def plotting(x,y,placeholder):
        """
        Draws/updates the graph

        Arguments:
            x: x axis value
            y: y axis value
        """
        fig = go.Figure()
    
        fig.add_trace(go.Scatter(x=x,y=y))

        placeholder.write(fig)
    
    ## Initializing the variables
    counter = 0
    x_axis = list()
    y_axis = list()

    try:
        serial_object = serial.Serial('com3' , 9600)
        serial_object.close()
        serial_object.open()
    except:
        pass    
    flag = True
    while radio1 == "Comedy":
        

            try:
                serial_object.flushInput()
                serial_object.flushOutput()
                serial_object.flush()
                data = serial_object.readline()
                print(data.decode())
                ## concatenating the value of x and y to the list
                x_axis.append(counter)
                y_axis.append(data.decode())

                counter += 1
                plotting(x_axis,y_axis,graph_placeholder)
                # if counter == 5:
                #     graph_placeholder.empty()
                #     break
                checbox = st.sidebar.checkbox("test")
                if checbox:
                    radio1 = "Drama"
                st.write(radio1)
                st.write(counter)
                
            except:
                pass

            
            plt.pause(0.0001)
        


elif radio1 == "Drama":
    st.write("HELOOOOOOOO")

