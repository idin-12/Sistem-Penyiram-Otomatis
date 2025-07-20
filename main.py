# Sistem Penyiram Otomatis (Sprinkler System)
# Author: [Nama Kamu]
# Description:
# Aplikasi Streamlit untuk menentukan status sprinkler berdasarkan tiga kondisi.

import streamlit as st

# Judul aplikasi
st.title("💧 Sistem Penyiram Otomatis (Sprinkler System)")

st.write("""
Program ini mengatur apakah sprinkler harus **menyala (ON)** atau **mati (OFF)**
berdasarkan tiga kondisi:
1. Tanah kering (is_dry)
2. Tidak sedang hujan (not is_raining)
3. Manual override aktif (manual_override)
""")

# Input kondisi dari user
is_dry = st.checkbox("Tanah kering", value=False)
is_raining = st.checkbox("Sedang hujan", value=False)
manual_override = st.checkbox("Manual override aktif", value=False)

# Fungsi kontrol sprinkler
def sprinkler_control(is_dry, is_raining, manual_override):
    if manual_override:
        return "Sprinkler ON"
    elif is_dry and not is_raining:
        return "Sprinkler ON"
    else:
        return "Sprinkler OFF"

# Hitung status sprinkler
status = sprinkler_control(is_dry, is_raining, manual_override)

# Tampilkan hasil
st.subheader(f"🚿 Status Sprinkler: **{status}**")

# Penjelasan logika
with st.expander("Lihat Logika Keputusan"):
    st.write("""
    - Jika **Manual Override aktif**, maka sprinkler akan selalu ON.
    - Jika **Tanah kering** dan **tidak hujan**, sprinkler ON.
    - Selain itu, sprinkler OFF.
    """)

# Catatan penggunaan packages lain
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import plotly.graph_objs as go
from scipy.optimize import linprog
from pulp import LpProblem, LpVariable, LpMaximize, value

# Placeholder penggunaan packages untuk memastikan requirements.txt tidak error saat deploy
st.write("---")
st.write("📦 **Packages Loaded:** numpy, sympy, matplotlib, plotly, scipy, pulp")
