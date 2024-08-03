import streamlit as st
import pandas as pd
import numpy as np

st.title('Option Pricing App')

st.info('Black Scholes option pricing model with a dynamic PNL Heatmap')
with st.sidebar:
  st.header('Inputs Go Here')
  with st.form('addition'):
    a = st.number_input('a')
    b = st.number_input('b')

