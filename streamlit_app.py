import streamlit as st
import pandas as pd
import numpy as np

st.title('Black-Scholes Option Pricing Model')

st.info('Black Scholes option pricing model with a dynamic PNL Heatmap')
with st.sidebar:
  st.header('Inputs Go Here')
  with st.form('addition'):
    cap = st.number_input('Current Asset Price')
    sp = st.number_input('Strike Price')
    t = st.number_input('Time To Maturity (Years)')
    v = st.number_input('Volatility (σ)')
    r = st.number_input('Risk-Free Interest Rate')
    
    submit = st.form_submit_button()

