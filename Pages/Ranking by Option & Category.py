#  %% FC - SQ Consensus Model - Streamlit app
    # Ranking by Option & Category page

# Import packages
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# %% Tab title
st.set_page_config(
    page_title = 'Option & Category Ranking',
    page_icon = '📉',)

# %% Page title
st.write('# 📉 SQ Consensus Model - Ranking by Option & Category')

# %% Page text
st.markdown(
    '''
    ### Ranking
    Preview how each option ranks across categories – according to AI algorithms based on Spiritual Insights from prophets and intercessors
    #### Blind vs. Informed Views
    Throughout this dashboard, you get to decide if it's more helpful to view data analyses as blind (ID's) or informed (names). For this page, check the box below if you would like the informed view.
''')

# %% Toggle for displaying data as informed (names) or blind (ID's)

    # Toggle
blindInform = st.checkbox(
    '**Show Names?** (_If disabled, will show ID\'s, to keep results blind_)', 
    value = False)

    # Select the appropriate column to display
blindInformColumn = 'Name' if blindInform else 'Option ID'

# %% Import and cache data
@st.cache_data

def load_data():
    googleDriveURL = 'https://docs.google.com/spreadsheets/d/1pdPZG75JMgBwZGzcfNpDuo0xaOX2je7Z5QVElsx3hyY/edit?usp=sharing'
    csvImport = googleDriveURL.replace('/edit?usp=sharing', '/export?format=csv')
    return pd.read_csv(csvImport)

    # Load data
SQCMdf = load_data()

    # Display data
# st.write(SQCMdf)

# %% Visualize Identity ranking - setup and chart

    # Define rows to include
rankRows = ['Identity', 'Assets', 'Foretelling', 'Actionable Intel', 
    'Scriptural Intelligence', 'Future Intel', 
    'Overall - ALL Spiritual Insights']

    # Define columns to include
rankColumns = ['Option ID', 'Name', 'Ranking', 'Ranking Avg AI', 'Info']

    # Create dataframe with limited dataset
rankDf = SQCMdf[SQCMdf['Info'].isin(rankRows)][rankColumns]

    # Update text value
rankDf.loc[rankDf[
    'Info'] == 'Overall - ALL Spiritual Insights', 'Info'] = 'Average Ranking'

    # Move averages to Ranking column
rankDf.loc[rankDf[
    'Info'] == 'Average Ranking', 'Ranking'] = rankDf[
        'Ranking Avg AI']

        # Drop the 'Ranking Avg AI' column
rankDf = rankDf.drop(columns = ['Ranking Avg AI'])

    # Define the order you want for the 'Info' column
rankRowsOrder = ['Identity', 'Assets', 'Foretelling', 'Actionable Intel', 
    'Scriptural Intelligence', 'Future Intel', 'Average Ranking']

        # Convert Info to categorical to be able to sort
rankDf['Info'] = pd.Categorical(
    rankDf['Info'], categories = rankRowsOrder, ordered = True)

        # Sort dataframe
rankDf = rankDf.sort_values(by = 'Info').reset_index(drop = True)

# %% Option 1

    # Title
if blindInform:
    st.markdown('**John Smith**')
else:
    st.markdown('**Option A1B2C3**')

    # Limit data
opt1Df = rankDf[rankDf['Option ID'] == 'A1B2C3']

    # Bar chart
st.bar_chart(opt1Df, x = 'Info', y = 'Ranking', 
             x_label = 'Category', y_label = 'Ranking', )

# %% Option 2

    # Title
if blindInform:
    st.markdown('**Sarah Johnson**')
else:
    st.markdown('**Option B2C3D4**')

    # Limit data
opt1Df = rankDf[rankDf['Option ID'] == 'B2C3D4']

    # Bar chart
st.bar_chart(opt1Df, x = 'Info', y = 'Ranking', 
             x_label = 'Category', y_label = 'Ranking', )

# %% Option 3

    # Title
if blindInform:
    st.markdown('**Michael Williams**')
else:
    st.markdown('**Option C3D4E5**')

    # Limit data
opt1Df = rankDf[rankDf['Option ID'] == 'C3D4E5']

    # Bar chart
st.bar_chart(opt1Df, x = 'Info', y = 'Ranking', 
             x_label = 'Category', y_label = 'Ranking', )

# %% Option 4

    # Title
if blindInform:
    st.markdown('**Emily Davis**')
else:
    st.markdown('**Option D4E5F6**')

    # Limit data
opt1Df = rankDf[rankDf['Option ID'] == 'D4E5F6']

    # Bar chart
st.bar_chart(opt1Df, x = 'Info', y = 'Ranking', 
             x_label = 'Category', y_label = 'Ranking', )

# %% Option 5

    # Title
if blindInform:
    st.markdown('**David Brown**')
else:
    st.markdown('**Option E5F6G7**')

    # Limit data
opt1Df = rankDf[rankDf['Option ID'] == 'E5F6G7']

    # Bar chart
st.bar_chart(opt1Df, x = 'Info', y = 'Ranking', 
             x_label = 'Category', y_label = 'Ranking', )
# %%
