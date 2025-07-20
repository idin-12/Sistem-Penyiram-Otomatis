# Sistem Penyiram Otomatis 
# (Sprinkler System)
# Author: [Muhyiddin As Syarif]
# Description:
# Aplikasi Streamlit dengan desain UI menarik untuk menentukan status sprinkler.

import streamlit as st

# =========================
# 🎨 Konfigurasi halaman
st.set_page_config(page_title="Sprinkler System", page_icon="💧", layout="centered")

# =========================
# 💧 Judul dan deskripsi
st.markdown("""
# 💧 Sistem Penyiram Otomatis (Sprinkler System)

Program ini mengatur apakah sprinkler harus **menyala (ON)** atau **mati (OFF)** berdasarkan tiga kondisi utama:
""")

st.markdown("""
1. 🌱 **Tanah kering**
2. 🌧️ **Tidak sedang hujan**
3. 🖐️ **Manual override aktif**
""")

st.write("---")

# =========================
# ✅ Input kondisi user (dengan kolom layout)
col1, col2, col3 = st.columns(3)

with col1:
    is_dry = st.checkbox("🌱 Tanah kering", value=False)

with col2:
    is_raining = st.checkbox("🌧️ Sedang hujan", value=False)

with col3:
    manual_override = st.checkbox("🖐️ Manual override", value=False)

st.write("---")

# =========================
# 🔧 Fungsi kontrol sprinkler
def sprinkler_control(is_dry, is_raining, manual_override):
    if manual_override:
        return "Sprinkler ON", "✅", "green"
    elif is_dry and not is_raining:
        return "Sprinkler ON", "✅", "green"
    else:
        return "Sprinkler OFF", "❌", "red"

# =========================
# 🚿 Hitung status sprinkler
status, icon, color = sprinkler_control(is_dry, is_raining, manual_override)

# =========================
# 🎯 Tampilkan hasil dengan desain
st.markdown(f"""
## 🚿 Status Sprinkler:

<span style="font-size:30px; color:{color};">{icon} {status}</span>
""", unsafe_allow_html=True)

# =========================
# 🔍 Penjelasan logika (expander)
with st.expander("📄 Lihat Logika Keputusan"):
    st.markdown("""
- Jika **Manual Override aktif**, maka sprinkler akan selalu **ON**.
- Jika **Tanah kering** dan **tidak hujan**, sprinkler **ON**.
- Selain itu, sprinkler **OFF**.
""")

# =========================
# 📦 Import packages tambahan (placeholder agar requirements.txt valid)
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import plotly.graph_objs as go
from scipy.optimize import linprog
from pulp import LpProblem, LpVariable, LpMaximize, value
