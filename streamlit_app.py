import streamlit as st
import math
from scipy.stats import norm

def black_scholes(S, K, T, r, sigma, option_type="call"):
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    
    if option_type == "call":
        option_price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        option_price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("option_type must be either 'call' or 'put'")
    
    return option_price

def main():
    st.title("Black-Scholes Pricing Model")

    with st.sidebar:
        st.header("Input Parameters")
        S = st.number_input("Current Stock Price (S)", value=100.0, step=1.0)
        K = st.number_input("Strike Price (K)", value=105.0, step=1.0)
        T = st.number_input("Time to Expiration (T in years)", value=1.0, step=0.1)
        r = st.number_input("Risk-Free Interest Rate (r)", value=0.02, step=0.01)
        sigma = st.number_input("Volatility (σ)", value=0.20, step=0.01)
    st.table({
        "Current Option Price": ["Current Stock Price (S)", "Strike Price (K)", "Time to Expiration (T in years)", "Risk-Free Interest Rate (r)", "Volatility (σ)"],
        "Value": [S, K, T, r, sigma]
    })
    
    call_price = black_scholes(S, K, T, r, sigma, "call")
    put_price = black_scholes(S, K, T, r, sigma, "put")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("CALL Value")
        st.metric(label="Call Price", value=f"${call_price:.2f}")
    with col2:
        st.subheader("PUT Value")
        st.metric(label="Put Price", value=f"${put_price:.2f}")
    
    with st.sidebar:
        st.header("PNL Calculation")
        purchase_price = st.number_input("Option Purchase Price", value=3.0, step=0.1)
        S_T = st.number_input("Stock Price at Expiration (S_T)", value=110.0, step=1.0)
    
    call_pnl = max(0, S_T - K) - purchase_price
    put_pnl = max(0, K - S_T) - purchase_price
    
    st.write("### PNL Calculation")
    st.write(f"Call Option PNL: ${call_pnl:.2f}")
    st.write(f"Put Option PNL: ${put_pnl:.2f}")

if __name__ == "__main__":
    main()
