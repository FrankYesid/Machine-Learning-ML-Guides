import streamlit as st
import numpy as np
import pandas as pd

st.title('Interactive Data Visualization')

data = np.random.rand(10, 3)
df = pd.DataFrame(data, columns=['A', 'B', 'C'])

st.write(df)
