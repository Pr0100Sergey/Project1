import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("Test app")

df = pd.DataFrame({'x': [10, 20, 30, 40],
                   'y': [100, 200, 300, 400],
                   'name': ['alpha', 'beta', 'gamma', 'delta']
                   })

x_max = st.slider('Max value of x', float(df['x'].max()))

df[df['x'] <= x_max]

a = st.slider('Amplitude', 0., 10.)
b = st.slider('Frequency', 0., 10.)
x = np.linspace(0, 10, 500)
fig = plt.figure()
plt.plot(x, a * np.sin(x * b))
plt.ylim(-5, 5)
st.pyplot(fig)

st.markdown("""
THE END
""")