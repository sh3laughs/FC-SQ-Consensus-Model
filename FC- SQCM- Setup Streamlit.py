# %% FC - SQ Consensus Model - Set up Streamlit app

    # Install packages setup
import sys
import subprocess

subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])

# %% Install Streamlit
subprocess.check_call([sys.executable, "-m", "pip", "install", "streamlit"])

# %% Import package to test
import streamlit as st

print("Streamlit is installed and imported successfully!")

# %% Install Streamlit wordcloud
subprocess.check_call([
    sys.executable, "-m", "pip", "install", "streamlit_wordcloud"])

# %% Import package to test
import streamlit_wordcloud as wordcloud

print("Streamlit Wordcloud is installed and imported successfully!")

# %% Install Streamlit wordcloud
subprocess.check_call([
    sys.executable, "-m", "pip", "install", "plotly"])

# %% Import package to test
import plotly.graph_objects as go

print("Streamlit Plotly is installed and imported successfully!")

# %% Install Matplotlib venn diagram
subprocess.check_call([
    sys.executable, "-m", "pip", "install", "matplotlib_venn"])

# %% Import package to test
import matplotlib_venn as wordcloud

print("Matplotlib Venn is installed and imported successfully!")

# %%