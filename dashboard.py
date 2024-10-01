import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# baca file
day_df = pd.read_csv('https://raw.githubusercontent.com/ajisakarsyi/bangkit-analisis-data/refs/heads/main/data/day.csv')
hour_df = pd.read_csv('https://raw.githubusercontent.com/ajisakarsyi/bangkit-analisis-data/refs/heads/main/data/hour.csv')

st.title("Dashboard Analisis 'Bike Sharing Dataset'")
st.write("*oleh Muhammad Ajisaka Arsyi Taj*")

tab1, tab2, tab3 = st.tabs(["Daily Dataframe", "Hourly Dataframe", "General"])

with tab1:
    st.header("Daily Dataframe")
    st.header("Distribusi Rata-rata Penjualan Harian Bike Sharing")

    total_sales_per_day = day_df.groupby('weekday')['cnt'].mean().reset_index()
    total_sales_per_day.rename(columns={'cnt': 'average_sales'}, inplace=True)

    # visualisasi
    fig, ax = plt.subplots()
    sns.barplot(x='weekday', y='average_sales', data=total_sales_per_day, ax=ax, color='#72BCD4')
    ax.set_title('Bar plot: Day vs Penjualan')
    ax.set_xlabel('Hari dalam Seminggu (0 = Minggu, 6 = Sabtu)')
    ax.set_ylabel('Rata-rata Penjualan')
    ax.set_ylim(4000,5000)
    
    st.pyplot(fig)

    st.header("Kesimpulan")
    st.write('''
    - Hasil penyewaan sepeda per hari bervariasi, namun semakin mendekat ke weekend semakin menunjukkan tren penyewaan yang naik.
    ''')

with tab2:
    st.header("Hourly Dataframe")
    st.header("Distribusi Rata-rata Penjualan Per Jam Bike Sharing")

    total_sales_per_hour = hour_df.groupby('hr')['cnt'].mean().reset_index()
    total_sales_per_hour.rename(columns={'cnt': 'average_sales'}, inplace=True)

    # visualisasi
    fig, ax = plt.subplots()
    sns.barplot(x='hr', y='average_sales', data=total_sales_per_hour, ax=ax, color='#72BCD4')
    ax.set_title('Bar plot: Hour vs Penjualan')
    ax.set_xlabel('Hour')
    ax.set_ylabel('Rata-rata Penjualan')
    
    st.pyplot(fig)

    st.header("Kesimpulan")
    st.write('''
    - Hasil penyewaan sepeda per jam bervariasi, namun memperlihatkan pola jam sibuk pada umumnya.
    ''')
    
with tab3:
    st.header("Pengaruh Kecepatan Angin terhadap Penjualan")

    # visualisasi
    fig, ax = plt.subplots()
    sns.scatterplot(x='windspeed', y='cnt', data=hour_df, ax=ax, color='#FF6347')
    ax.set_title('Scatter Plot: Windspeed vs Penjualan')
    ax.set_xlabel('Kecepatan Angin')
    ax.set_ylabel('Jumlah Penjualan')
    
    st.pyplot(fig)

    st.header("Kesimpulan")
    st.write('''
    - Meskipun rendah, kecepatan angin dengan penjualan memiliki pengaruh negatif, dimana apabila kecepatan angin terjadi dengan kuat maka hasil penyewaan sepeda cenderung rendah.
    ''')
