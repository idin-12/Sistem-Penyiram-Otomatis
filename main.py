import streamlit as st

# =========================
# 🎨 Konfigurasi halaman
st.set_page_config(
    page_title="💧 Sprinkler System Control",
    page_icon="💧",
    layout="centered"
)

# =========================
# 💠 Custom CSS untuk mempercantik tampilan
st.markdown("""
<style>
h1 {
    text-align: center;
    color: #2E86C1;
}
h3 {
    text-align: center;
}
.status-box {
    border-radius: 10px;
    padding: 20px;
    text-align: center;
    font-size: 30px;
    font-weight: bold;
}
.green-box {
    background-color: #D4EFDF;
    color: #27AE60;
}
.red-box {
    background-color: #FADBD8;
    color: #C0392B;
}
</style>
""", unsafe_allow_html=True)

# =========================
# 💧 Judul Aplikasi
st.markdown("# 💧 Sistem Penyiram Otomatis 💧")
st.markdown("### Smart Sprinkler System Controller")
st.markdown("### Muhyiddin As Syarif (312410122")

st.write("---")

# =========================
# ✨ Deskripsi Program
st.markdown("""
Program ini mengatur apakah sprinkler harus **MENYALA (ON)** atau **MATI (OFF)** berdasarkan tiga kondisi utama:

- 🌱 **Tanah kering**
- 🌧️ **Tidak sedang hujan**
- 🖐️ **Manual override aktif**

""")

# =========================
# ✅ Input kondisi user dengan layout yang bersih
st.write("### 🔧 Masukkan Kondisi Saat Ini:")
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
        return "Sprinkler ON", "✅", "green-box"
    elif is_dry and not is_raining:
        return "Sprinkler ON", "✅", "green-box"
    else:
        return "Sprinkler OFF", "❌", "red-box"

# =========================
# 🚿 Hitung status sprinkler
status, icon, box_class = sprinkler_control(is_dry, is_raining, manual_override)

# =========================
# 🎯 Tampilkan hasil dengan desain box warna
st.markdown(f"""
<div class="status-box {box_class}">
{icon} {status}
</div>
""", unsafe_allow_html=True)

# =========================
# 🔍 Penjelasan logika (expander)
with st.expander("📄 Penjelasan Logika Keputusan"):
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
