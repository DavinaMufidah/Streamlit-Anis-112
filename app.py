
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
def binomial_distribution(n, p):
    x = np.arange(0, n+1)
    y = binom.pmf(x, n, p)

    fig, ax = plt.subplots()
    ax.bar(x, y)
    ax.set_xlabel('X')
    ax.set_ylabel('P(X)')
    ax.set_title('Binomial Distribution')
    st.pyplot(fig)
def main():
    st.title('Kalkulator Distribusi Binomial')

    n = st.slider('Jumlah percobaan (n)', 1, 100, 10)
    p = st.slider('Probabilitas sukses (p)', 0.0, 1.0, 0.5)

    binomial_distribution(n, p)

if __name__ == '__main__':
    main()
