import streamlit as st
import serial
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import threading

graph_placeholder = st.empty()
class setInterval():
    def _init_(self, func, sec):
        def func_wrapper():
            self.t = threading.Timer(sec, func_wrapper)
            self.t.start()
            func()
        self.t = threading.Timer(sec, func_wrapper)
        self.t.start()

    def cancel(self):
        self.t.cancel()
   
def test ():
        def plotting(x,y,placeholder):
       
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


with st.sidebar:
    radio1  = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))
   

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])




with tab1:

    okokok = threading.Timer(0.5, test())
    okokok.start()
        


with tab2:
    okokok.cancel()
    st.write("Helloooooooo")

