# %% FC - SQ Consensus Model - Streamlit app
    # Ranking by Category page

# Import packages
import pandas as pd
import plotly.graph_objects as go
import requests
import streamlit as st

# %% Tab title
st.set_page_config(
    page_title = "Category Ranking",
    page_icon = "📉",)

# %% Page title
st.write("# 📉 SQ Consensus Model - Ranking by Category")

# %% Page text
st.markdown(
    """
    #### Blind vs. Informed Views
    Throughout this dashboard, you get to decide if it's more helpful to view data analyses as blind (ID's) or informed (names). For this page, check the box below if you would like the informed view.
""")

# %% Toggle for displaying data as informed (names) or blind (ID's)

    # Toggle
blindInform = st.checkbox(
    '**Show Names?** (_If disabled, will show ID\'s, to keep results blind_)', 
    value = False)

    # Select the appropriate column for x-axis
overallX = 'Name' if blindInform else 'Option ID'

# %% Section header
st.markdown(
    """
    ### Identity Ranking
    Preview how all considered options rank with each other for the Identity category – according to AI algorithms based on Spiritual Insights from prophets and intercessors
""")

# %% Import and cache data

    # Google sheet API access setup
apiKey = 'AIzaSyD5Sem3ZTjAVClEu8KtFWWjkDdU5oowGtE'
googleSheetId = '1pdPZG75JMgBwZGzcfNpDuo0xaOX2je7Z5QVElsx3hyY'
googleSheetRange = 'People example - merged tables'
url = f'https://sheets.googleapis.com/v4/spreadsheets/{googleSheetId}/values/{googleSheetRange}?key={apiKey}'

    # Function to fetch data
def fetch_data():
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        st.error(f"Error fetching data: {response.status_code}")
        return {}

    # Cache data
@st.cache_data

    # Function to load data
# def load_data():
#     googleDriveURL = "https://docs.google.com/spreadsheets/d/1pdPZG75JMgBwZGzcfNpDuo0xaOX2je7Z5QVElsx3hyY/edit?usp=sharing"
#     csvImport = googleDriveURL.replace('/edit?usp=sharing', '/export?format=csv')
#     return pd.read_csv(csvImport)

def load_data():
    data = fetch_data()
    if 'values' in data and len(data['values']) > 1:
        # Convert JSON data to DataFrame
        df = pd.DataFrame(data['values'][1:], columns = data['values'][0])
        
        # Convert relevant columns to numeric
        numeric_columns = [
            'Score / Rating', 'Score Avg', 'Ranking Avg ALL', 
            'Ranking Sum ALL', 'Ranking Sum AI', 'Ranking Count ALL',
            'Ranking Count AI', 'Ranking Avg ALL', 'Ranking Avg AI'
        ]
        for col in numeric_columns:
            df[col] = pd.to_numeric(df[col], errors = 'coerce')
        
        return df
    else:
        # Handle empty or missing data
        return pd.DataFrame(columns = ['No data available'])

    # Load data
SQCMdf = load_data()

    # Display data
# st.write(SQCMdf)

# %% Visualize Identity ranking - setup and chart

    # Define rows to include
identityRankRows = 'Identity'

    # Define columns to include
identityRankColumns = ['Option ID', 'Name', 'Ranking']

    # Create dataframe with limited dataset
identityRankDf = SQCMdf[SQCMdf['Info'] == identityRankRows][identityRankColumns]

    # Bar chart
st.bar_chart(identityRankDf, x = overallX, y = 'Ranking', 
             x_label = 'Candidate', y_label = 'Identity Ranking', )

# %% Section header
st.markdown(
    """
    ### Assets Ranking
    Preview how all considered options rank with each other for the Assets category – according to AI algorithms based on Spiritual Insights from prophets and intercessors
""")

# %% Visualize Assets ranking - setup and chart

    # Define rows to include
assetsRankRows = 'Assets'

    # Define columns to include
assetsRankColumns = ['Option ID', 'Name', 'Ranking']

    # Create dataframe with limited dataset
assetsRankDf = SQCMdf[SQCMdf['Info'] == assetsRankRows][assetsRankColumns]

    # Bar chart
st.bar_chart(assetsRankDf, x = overallX, y = 'Ranking', 
             x_label = 'Candidate', y_label = 'Assets Ranking', )

# %% Section header
st.markdown(
    """
    ### Foretelling Ranking
    Preview how all considered options rank with each other for the Foretelling category – according to AI algorithms based on Spiritual Insights from prophets and intercessors
""")

# %% Visualize Foretelling ranking - setup and chart

    # Define rows to include
foretellRankRows = 'Foretelling'

    # Define columns to include
foretellRankColumns = ['Option ID', 'Name', 'Ranking']

    # Create dataframe with limited dataset
foretellRankDf = SQCMdf[SQCMdf['Info'] == foretellRankRows][foretellRankColumns]

    # Bar chart
st.bar_chart(foretellRankDf, x = overallX, y = 'Ranking', 
             x_label = 'Candidate', y_label = 'Foretelling Ranking', )

# %% Section header
st.markdown(
    """
    ### Actionable Intel Ranking
    Preview how all considered options rank with each other for the Actionable Intel category – according to AI algorithms based on Spiritual Insights from prophets and intercessors
""")

# %% Visualize Actionable Intel ranking - setup and chart

    # Define rows to include
actIntelRankRows = 'Actionable Intel'

    # Define columns to include
actIntelRankColumns = ['Option ID', 'Name', 'Ranking']

    # Create dataframe with limited dataset
actIntelRankDf = SQCMdf[SQCMdf['Info'] == actIntelRankRows][actIntelRankColumns]

    # Bar chart
st.bar_chart(actIntelRankDf, x = overallX, y = 'Ranking', 
             x_label = 'Candidate', y_label = 'Actionable Intel Ranking', )

# %% Section header
st.markdown(
    """
    ### Scriptural Intelligence Ranking
    Preview how all considered options rank with each other for the Scriptural Intelligence category – according to AI algorithms based on Spiritual Insights from prophets and intercessors
""")

# %% Visualize Scriptural Intelligence ranking - setup and chart

    # Define rows to include
scripIntelRankRows = 'Scriptural Intelligence'

    # Define columns to include
scripIntelRankColumns = ['Option ID', 'Name', 'Ranking']

    # Create dataframe with limited dataset
scripIntelRankDf = SQCMdf[
    SQCMdf['Info'] == scripIntelRankRows][scripIntelRankColumns]

    # Bar chart
st.bar_chart(scripIntelRankDf, x = overallX, y = 'Ranking', 
             x_label = 'Candidate', y_label = 'Scriptural Intelligence Ranking', )

# %% Section header
st.markdown(
    """
    ### Future Intel Ranking
    Preview how all considered options rank with each other for the Future Intel category – according to AI algorithms based on Spiritual Insights from prophets and intercessors
""")

# %% Visualize Future Intel ranking - setup and chart

    # Define rows to include
futIntelRankRows = 'Future Intel'

    # Define columns to include
futIntelRankColumns = ['Option ID', 'Name', 'Ranking']

    # Create dataframe with limited dataset
futIntelRankDf = SQCMdf[SQCMdf['Info'] == futIntelRankRows][futIntelRankColumns]

    # Bar chart
st.bar_chart(futIntelRankDf, x = overallX, y = 'Ranking', 
             x_label = 'Candidate', y_label = 'Future Intel Ranking', )

# %%
