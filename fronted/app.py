import streamlit as st
import numpy as np
from backend.calculations import *
from backend.fluids import fluids

st.title("Fluid Mechanics Pipe Flow Simulator")

fluid_choice = st.selectbox("Fluid", list(fluids.keys()))

length = st.slider("Pipe Length (m)", 1, 100, 10)
diameter = st.slider("Pipe Diameter (m)", 0.01, 1.0, 0.1)
flow_rate = st.slider("Flow Rate (m³/s)", 0.001, 1.0, 0.05)

rho = fluids[fluid_choice]["density"]
mu = fluids[fluid_choice]["viscosity"]

V = velocity(flow_rate, diameter)
Re = reynolds_number(rho, V, diameter, mu)
f = friction_factor(Re)
dp = pressure_drop(f, length, diameter, rho, V)

st.write("Velocity:", V)
st.write("Reynolds Number:", Re)
st.write("Friction Factor:", f)
st.write("Pressure Drop:", dp)
