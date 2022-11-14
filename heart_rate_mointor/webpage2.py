import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.misc import electrocardiogram




st.set_page_config(page_title="Signal Visualizer", page_icon=":🗠:", layout='wide')


hide_st_style = """
            <style>
            # MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """



#Reading the csv file and getting 11 samples each with 20 values
df   = pd.read_csv("ECG.csv")
sample1= df['amplitude'][:21]
sample2= df['amplitude'][21:41]
sample3= df['amplitude'][41:61]
sample4= df['amplitude'][61:81]
sample5= df['amplitude'][81:101]
sample6= df['amplitude'][101:121]
sample7= df['amplitude'][121:141]
sample8= df['amplitude'][141:161]
sample9= df['amplitude'][161:181]
sample10= df['amplitude'][182:202]
sample11= df['amplitude'][203:223]


#Mean for each sample
mean1= np.mean(sample1)
mean2= np.mean(sample2)
mean3= np.mean(sample3)
mean4= np.mean(sample4)
mean5= np.mean(sample5)
mean6= np.mean(sample6)
mean7= np.mean(sample7)
mean8= np.mean(sample8)
mean9= np.mean(sample9)
mean10= np.mean(sample10)
mean11= np.mean(sample11)
Mean= [mean1,mean2,mean3,mean4,mean5,mean6,mean7,mean8,mean9,mean10,mean11] 


#R for each sample
R1= np.max(sample1)-np.min(sample1)
R2= np.max(sample2)-np.min(sample2)
R3= np.max(sample3)-np.min(sample3)
R4= np.max(sample4)-np.min(sample4)
R5= np.max(sample5)-np.min(sample5)
R6= np.max(sample6)-np.min(sample6)
R7= np.max(sample7)-np.min(sample7)
R8= np.max(sample8)-np.min(sample8)
R9= np.max(sample9)-np.min(sample9)
R10= np.max(sample10)-np.min(sample10)
R11= np.max(sample11)-np.min(sample11)
R= [R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11]


Rbar= np.sum(R)
Xbar= np.sum(Mean)


#XBAR CHART
def x_bar():  
    CL= Xbar
    UCL= Xbar+(0.29*Rbar)
    LCL= Xbar-(0.29*Rbar)

    Fig = plt.figure(figsize=(15,5))
    plt.plot(np.arange(1,12), Mean,'go-')
    plt.plot(np.arange(1,12),[UCL,UCL,UCL,UCL,UCL,UCL,UCL,UCL,UCL,UCL,UCL], color='r', linestyle='--')
    plt.plot(np.arange(1,12),[CL,CL,CL,CL,CL,CL,CL,CL,CL,CL,CL], color='g')
    plt.plot(np.arange(1,12),[LCL,LCL,LCL,LCL,LCL,LCL,LCL,LCL,LCL,LCL,LCL], color='r', linestyle='--')
    st.plotly_chart(Fig)


#R CHART
def R_bar():
    CL= Rbar
    UCL= (1.74*Rbar)
    LCL= (0.26*Rbar)

    Fig = plt.figure(figsize=(15,5))
    plt.plot(np.arange(1,12),[UCL,UCL,UCL,UCL,UCL,UCL,UCL,UCL,UCL,UCL,UCL], color='r', linestyle='--')
    plt.plot(np.arange(1,12),[CL,CL,CL,CL,CL,CL,CL,CL,CL,CL,CL], color='g')
    plt.plot(np.arange(1,12),[LCL,LCL,LCL,LCL,LCL,LCL,LCL,LCL,LCL,LCL,LCL], color='r', linestyle='--')
    plt.plot(np.arange(1,12), R,'go-')
    st.plotly_chart(Fig)





st.sidebar.header("Tools")
bt1=st.sidebar.button("Vital signals")
col1,col2= st.sidebar.columns(2)


with col1:
    bt2=st.button("Xbar Chart")
with col2:
    bt3=st.button("Rbar Chart")

if bt2:
        x_bar()  
        print()
if bt3:
        R_bar()