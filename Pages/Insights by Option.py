# %% FC - SQ Consensus Model - Streamlit app
    # Insights by Option page

# Import packages
import pandas as pd
import requests
import streamlit as st

# %% Tab title
st.set_page_config(
    page_title = "SQCM Insights",
    page_icon = "💡",)

# %% Page title
st.write("# 💡 SQ Consensus Model - Insights by Option")

# %% Page text
st.markdown(
    """
    Preview key, AI-generated positive, neutral, and negative insights across all Spiritual Insights from prophets and intercessors for each option
    #### Blind vs. Informed Views
    Throughout this dashboard, you get to decide if it's more helpful to view data analyses as blind (ID's) or informed (names). For this page, check the box below if you would like the informed view.
""")

# %% Toggle for displaying data as informed (names) or blind (ID's)

    # Toggle
blindInform = st.checkbox(
    '**Show Names?** (_If disabled, will show ID\'s, to keep results blind_)', 
    value = False)

    # Select the appropriate column to display
blindInformColumn = 'Name' if blindInform else 'Option ID'

    ### NEXT: Ensure insights are blind (no names or gender pronouns)

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

# %% Section header
st.markdown(
    """
    ### 💚 Overall Positive Insights
    Preview key, AI-generated positive insights across all Spiritual Insights from prophets and intercessors for each option
""")

# %% Overall positive insights table

    # Define rows to include
overallPosInsightRows = 'Overall - ALL Spiritual Insights'

    # Define columns to include
overallPosInsightColumns = ['Option ID', 'Name', 'Insights - Positive']

    # Create dataframe with limited dataset
overallPosInsightDf = SQCMdf[SQCMdf['Info'] == overallPosInsightRows][overallPosInsightColumns]

    # Updated dataframe to work with blind / informed toggle
overallPosInsightToggleDf = overallPosInsightDf[[
    blindInformColumn, 'Insights - Positive']]

        # Rename toggled column
overallPosInsightToggleDf = overallPosInsightToggleDf.rename(
    columns = {blindInformColumn: 'Option', 
               'Insights - Positive': 'Positive Insight'})

    # Display toggle-able dataframe
st.dataframe(overallPosInsightToggleDf, hide_index = True)

        # Help text
st.write("_Double-click a Summary cell to open its full text; drag the column separator to adjust column widths_")

# %% Section header
st.markdown(
    """
    ### 💛 Overall Neutral Insights
    Preview key, AI-generated neutral insights across all Spiritual Insights from prophets and intercessors for each option
""")

# %% Overall neutral insights table

    # Define rows to include
overallNeutInsightRows = 'Overall - ALL Spiritual Insights'

    # Define columns to include
overallNeutInsightColumns = ['Option ID', 'Name', 'Insights - Neutral']

    # Create dataframe with limited dataset
overallNeutInsightDf = SQCMdf[SQCMdf['Info'] == overallNeutInsightRows][overallNeutInsightColumns]

    # Updated dataframe to work with blind / informed toggle
overallNeutInsightToggleDf = overallNeutInsightDf[[
    blindInformColumn, 'Insights - Neutral']]

        # Rename toggled column
overallNeutInsightToggleDf = overallNeutInsightToggleDf.rename(
    columns = {blindInformColumn: 'Option', 
               'Insights - Neutral': 'Neutral Insight'})

    # Display toggle-able dataframe
st.dataframe(overallNeutInsightToggleDf, hide_index = True)

        # Help text
st.write("_Double-click a Summary cell to open its full text; drag the column separator to adjust column widths_")

# %% Section header
st.markdown(
    """
    ### 🚫 Overall Negative Insights
    Preview key, AI-generated negative insights across all Spiritual Insights from prophets and intercessors for each option
""")

# %% Overall negative insights table

    # Define rows to include
overallNegInsightRows = 'Overall - ALL Spiritual Insights'

    # Define columns to include
overallNegInsightColumns = ['Option ID', 'Name', 'Insights - Negative']

    # Create dataframe with limited dataset
overallNegInsightDf = SQCMdf[SQCMdf['Info'] == overallNegInsightRows][overallNegInsightColumns]

    # Updated dataframe to work with blind / informed toggle
overallNegInsightToggleDf = overallNegInsightDf[[
    blindInformColumn, 'Insights - Negative']]

        # Rename toggled column
overallNegInsightToggleDf = overallNegInsightToggleDf.rename(
    columns = {blindInformColumn: 'Option', 
               'Insights - Negative': 'Negative Insight'})

    # Display toggle-able dataframe
st.dataframe(overallNegInsightToggleDf, hide_index = True)

        # Help text
st.write("_Double-click a Summary cell to open its full text; drag the column separator to adjust column widths_")

# %% Section header
st.markdown(
    """
    ### 💚 Identity Positive Insights
    Preview key, AI-generated positive insights across all Spiritual Insights from prophets and intercessors for each option
""")

# %% Identity positive insights table

    # Define rows to include
identityPosInsightRows = 'Identity'

    # Define columns to include
identityPosInsightColumns = ['Option ID', 'Name', 'Insights - Positive']

    # Create dataframe with limited dataset
identityPosInsightDf = SQCMdf[SQCMdf['Info'] == identityPosInsightRows][identityPosInsightColumns]

    # Updated dataframe to work with blind / informed toggle
identityPosInsightToggleDf = identityPosInsightDf[[
    blindInformColumn, 'Insights - Positive']]

        # Rename toggled column
identityPosInsightToggleDf = identityPosInsightToggleDf.rename(
    columns = {blindInformColumn: 'Option', 
               'Insights - Positive': 'Positive Insight'})

    # Display toggle-able dataframe
st.dataframe(identityPosInsightToggleDf, hide_index = True)

        # Help text
st.write("_Double-click a Summary cell to open its full text; drag the column separator to adjust column widths_")

# %% Section header
st.markdown(
    """
    ### 💛 Identity Neutral Insights
    Preview key, AI-generated neutral insights across all Spiritual Insights from prophets and intercessors for each option
""")

# %% Identity neutral insights table

    # Define rows to include
identityNeutInsightRows = 'Identity'

    # Define columns to include
identityNeutInsightColumns = ['Option ID', 'Name', 'Insights - Neutral']

    # Create dataframe with limited dataset
identityNeutInsightDf = SQCMdf[SQCMdf['Info'] == identityNeutInsightRows][identityNeutInsightColumns]

    # Updated dataframe to work with blind / informed toggle
identityNeutInsightToggleDf = identityNeutInsightDf[[
    blindInformColumn, 'Insights - Neutral']]

        # Rename toggled column
identityNeutInsightToggleDf = identityNeutInsightToggleDf.rename(
    columns = {blindInformColumn: 'Option', 
               'Insights - Neutral': 'Neutral Insight'})

    # Display toggle-able dataframe
st.dataframe(identityNeutInsightToggleDf, hide_index = True)

        # Help text
st.write("_Double-click a Summary cell to open its full text; drag the column separator to adjust column widths_")

# %% Section header
st.markdown(
    """
    ### 🚫 Identity Negative Insights
    Preview key, AI-generated negative insights across all Spiritual Insights from prophets and intercessors for each option
""")

# %% Identity negative insights table

    # Define rows to include
identityNegInsightRows = 'Identity'

    # Define columns to include
identityNegInsightColumns = ['Option ID', 'Name', 'Insights - Negative']

    # Create dataframe with limited dataset
identityNegInsightDf = SQCMdf[SQCMdf['Info'] == identityNegInsightRows][identityNegInsightColumns]

    # Updated dataframe to work with blind / informed toggle
identityNegInsightToggleDf = identityNegInsightDf[[
    blindInformColumn, 'Insights - Negative']]

        # Rename toggled column
identityNegInsightToggleDf = identityNegInsightToggleDf.rename(
    columns = {blindInformColumn: 'Option', 
               'Insights - Negative': 'Negative Insight'})

    # Display toggle-able dataframe
st.dataframe(identityNegInsightToggleDf, hide_index = True)

        # Help text
st.write("_Double-click a Summary cell to open its full text; drag the column separator to adjust column widths_")

# %% Section header
st.markdown(
    """
    ### 💚 Assets Positive Insights
    Preview key, AI-generated positive insights across all Spiritual Insights from prophets and intercessors for each option
""")

# %% Assets positive insights table

    # Define rows to include
assetsPosInsightRows = 'Assets'

    # Define columns to include
assetsPosInsightColumns = ['Option ID', 'Name', 'Insights - Positive']

    # Create dataframe with limited dataset
assetsPosInsightDf = SQCMdf[SQCMdf['Info'] == assetsPosInsightRows][assetsPosInsightColumns]

    # Updated dataframe to work with blind / informed toggle
assetsPosInsightToggleDf = assetsPosInsightDf[[
    blindInformColumn, 'Insights - Positive']]

        # Rename toggled column
assetsPosInsightToggleDf = assetsPosInsightToggleDf.rename(
    columns = {blindInformColumn: 'Option', 
               'Insights - Positive': 'Positive Insight'})

    # Display toggle-able dataframe
st.dataframe(assetsPosInsightToggleDf, hide_index = True)

        # Help text
st.write("_Double-click a Summary cell to open its full text; drag the column separator to adjust column widths_")

# %% Section header
st.markdown(
    """
    ### 💛 Assets Neutral Insights
    Preview key, AI-generated neutral insights across all Spiritual Insights from prophets and intercessors for each option
""")

# %% Assets neutral insights table

    # Define rows to include
assetsNeutInsightRows = 'Assets'

    # Define columns to include
assetsNeutInsightColumns = ['Option ID', 'Name', 'Insights - Neutral']

    # Create dataframe with limited dataset
assetsNeutInsightDf = SQCMdf[SQCMdf['Info'] == assetsNeutInsightRows][assetsNeutInsightColumns]

    # Updated dataframe to work with blind / informed toggle
assetsNeutInsightToggleDf = assetsNeutInsightDf[[
    blindInformColumn, 'Insights - Neutral']]

        # Rename toggled column
assetsNeutInsightToggleDf = assetsNeutInsightToggleDf.rename(
    columns = {blindInformColumn: 'Option', 
               'Insights - Neutral': 'Neutral Insight'})

    # Display toggle-able dataframe
st.dataframe(assetsNeutInsightToggleDf, hide_index = True)

        # Help text
st.write("_Double-click a Summary cell to open its full text; drag the column separator to adjust column widths_")

# %% Section header
st.markdown(
    """
    ### 🚫 Assets Negative Insights
    Preview key, AI-generated negative insights across all Spiritual Insights from prophets and intercessors for each option
""")

# %% Assets negative insights table

    # Define rows to include
assetsNegInsightRows = 'Assets'

    # Define columns to include
assetsNegInsightColumns = ['Option ID', 'Name', 'Insights - Negative']

    # Create dataframe with limited dataset
assetsNegInsightDf = SQCMdf[SQCMdf['Info'] == assetsNegInsightRows][assetsNegInsightColumns]

    # Updated dataframe to work with blind / informed toggle
assetsNegInsightToggleDf = assetsNegInsightDf[[
    blindInformColumn, 'Insights - Negative']]

        # Rename toggled column
assetsNegInsightToggleDf = assetsNegInsightToggleDf.rename(
    columns = {blindInformColumn: 'Option', 
               'Insights - Negative': 'Negative Insight'})

    # Display toggle-able dataframe
st.dataframe(assetsNegInsightToggleDf, hide_index = True)

        # Help text
st.write("_Double-click a Summary cell to open its full text; drag the column separator to adjust column widths_")

# %% Section header
st.markdown(
    """
    ### 💚 Foretelling Positive Insights
    Preview key, AI-generated positive insights across all Spiritual Insights from prophets and intercessors for each option
""")

# %% Foretelling positive insights table

    # Define rows to include
forePosInsightRows = 'Foretelling'

    # Define columns to include
forePosInsightColumns = ['Option ID', 'Name', 'Insights - Positive']

    # Create dataframe with limited dataset
forePosInsightDf = SQCMdf[SQCMdf['Info'] == forePosInsightRows][forePosInsightColumns]

    # Updated dataframe to work with blind / informed toggle
forePosInsightToggleDf = forePosInsightDf[[
    blindInformColumn, 'Insights - Positive']]

        # Rename toggled column
forePosInsightToggleDf = forePosInsightToggleDf.rename(
    columns = {blindInformColumn: 'Option', 
               'Insights - Positive': 'Positive Insight'})

    # Display toggle-able dataframe
st.dataframe(forePosInsightToggleDf, hide_index = True)

        # Help text
st.write("_Double-click a Summary cell to open its full text; drag the column separator to adjust column widths_")

# %% Section header
st.markdown(
    """
    ### 💛 Foretelling Neutral Insights
    Preview key, AI-generated neutral insights across all Spiritual Insights from prophets and intercessors for each option
""")

# %% Foretelling neutral insights table

    # Define rows to include
foreNeutInsightRows = 'Foretelling'

    # Define columns to include
foreNeutInsightColumns = ['Option ID', 'Name', 'Insights - Neutral']

    # Create dataframe with limited dataset
foreNeutInsightDf = SQCMdf[SQCMdf['Info'] == foreNeutInsightRows][foreNeutInsightColumns]

    # Updated dataframe to work with blind / informed toggle
foreNeutInsightToggleDf = foreNeutInsightDf[[
    blindInformColumn, 'Insights - Neutral']]

        # Rename toggled column
foreNeutInsightToggleDf = foreNeutInsightToggleDf.rename(
    columns = {blindInformColumn: 'Option', 
               'Insights - Neutral': 'Neutral Insight'})

    # Display toggle-able dataframe
st.dataframe(foreNeutInsightToggleDf, hide_index = True)

        # Help text
st.write("_Double-click a Summary cell to open its full text; drag the column separator to adjust column widths_")

# %% Section header
st.markdown(
    """
    ### 🚫 Foretelling Negative Insights
    Preview key, AI-generated negative insights across all Spiritual Insights from prophets and intercessors for each option
""")

# %% Foretelling negative insights table

    # Define rows to include
foreNegInsightRows = 'Foretelling'

    # Define columns to include
foreNegInsightColumns = ['Option ID', 'Name', 'Insights - Negative']

    # Create dataframe with limited dataset
foreNegInsightDf = SQCMdf[SQCMdf['Info'] == foreNegInsightRows][foreNegInsightColumns]

    # Updated dataframe to work with blind / informed toggle
foreNegInsightToggleDf = foreNegInsightDf[[
    blindInformColumn, 'Insights - Negative']]

        # Rename toggled column
foreNegInsightToggleDf = foreNegInsightToggleDf.rename(
    columns = {blindInformColumn: 'Option', 
               'Insights - Negative': 'Negative Insight'})

    # Display toggle-able dataframe
st.dataframe(foreNegInsightToggleDf, hide_index = True)

        # Help text
st.write("_Double-click a Summary cell to open its full text; drag the column separator to adjust column widths_")

# %% Section header
st.markdown(
    """
    ### 💚 Actionable Intel Positive Insights
    Preview key, AI-generated positive insights across all Spiritual Insights from prophets and intercessors for each option
""")

# %% Actionable Intel positive insights table

    # Define rows to include
actIntelPosInsightRows = 'Actionable Intel'

    # Define columns to include
actIntelPosInsightColumns = ['Option ID', 'Name', 'Insights - Positive']

    # Create dataframe with limited dataset
actIntelPosInsightDf = SQCMdf[SQCMdf['Info'] == actIntelPosInsightRows][actIntelPosInsightColumns]

    # Updated dataframe to work with blind / informed toggle
actIntelPosInsightToggleDf = actIntelPosInsightDf[[
    blindInformColumn, 'Insights - Positive']]

        # Rename toggled column
actIntelPosInsightToggleDf = actIntelPosInsightToggleDf.rename(
    columns = {blindInformColumn: 'Option', 
               'Insights - Positive': 'Positive Insight'})

    # Display toggle-able dataframe
st.dataframe(actIntelPosInsightToggleDf, hide_index = True)

        # Help text
st.write("_Double-click a Summary cell to open its full text; drag the column separator to adjust column widths_")

# %% Section header
st.markdown(
    """
    ### 💛 Actionable Intel Neutral Insights
    Preview key, AI-generated neutral insights across all Spiritual Insights from prophets and intercessors for each option
""")

# %% Actionable Intel neutral insights table

    # Define rows to include
actIntelNeutInsightRows = 'Actionable Intel'

    # Define columns to include
actIntelNeutInsightColumns = ['Option ID', 'Name', 'Insights - Neutral']

    # Create dataframe with limited dataset
actIntelNeutInsightDf = SQCMdf[SQCMdf['Info'] == actIntelNeutInsightRows][actIntelNeutInsightColumns]

    # Updated dataframe to work with blind / informed toggle
actIntelNeutInsightToggleDf = actIntelNeutInsightDf[[
    blindInformColumn, 'Insights - Neutral']]

        # Rename toggled column
actIntelNeutInsightToggleDf = actIntelNeutInsightToggleDf.rename(
    columns = {blindInformColumn: 'Option', 
               'Insights - Neutral': 'Neutral Insight'})

    # Display toggle-able dataframe
st.dataframe(actIntelNeutInsightToggleDf, hide_index = True)

        # Help text
st.write("_Double-click a Summary cell to open its full text; drag the column separator to adjust column widths_")

# %% Section header
st.markdown(
    """
    ### 🚫 Actionable Intel Negative Insights
    Preview key, AI-generated negative insights across all Spiritual Insights from prophets and intercessors for each option
""")

# %% Actionable Intel negative insights table

    # Define rows to include
actIntelNegInsightRows = 'Actionable Intel'

    # Define columns to include
actIntelNegInsightColumns = ['Option ID', 'Name', 'Insights - Negative']

    # Create dataframe with limited dataset
actIntelNegInsightDf = SQCMdf[SQCMdf['Info'] == actIntelNegInsightRows][actIntelNegInsightColumns]

    # Updated dataframe to work with blind / informed toggle
actIntelNegInsightToggleDf = actIntelNegInsightDf[[
    blindInformColumn, 'Insights - Negative']]

        # Rename toggled column
actIntelNegInsightToggleDf = actIntelNegInsightToggleDf.rename(
    columns = {blindInformColumn: 'Option', 
               'Insights - Negative': 'Negative Insight'})

    # Display toggle-able dataframe
st.dataframe(actIntelNegInsightToggleDf, hide_index = True)

        # Help text
st.write("_Double-click a Summary cell to open its full text; drag the column separator to adjust column widths_")

# %% Section header
st.markdown(
    """
    ### 💚 Scriptural Intelligence Positive Insights
    Preview key, AI-generated positive insights across all Spiritual Insights from prophets and intercessors for each option
""")

# %% Scriptural Intelligence positive insights table

    # Define rows to include
scripIntelPosInsightRows = 'Scriptural Intelligence'

    # Define columns to include
scripIntelPosInsightColumns = ['Option ID', 'Name', 'Insights - Positive']

    # Create dataframe with limited dataset
scripIntelPosInsightDf = SQCMdf[SQCMdf['Info'] == scripIntelPosInsightRows][scripIntelPosInsightColumns]

    # Updated dataframe to work with blind / informed toggle
scripIntelPosInsightToggleDf = scripIntelPosInsightDf[[
    blindInformColumn, 'Insights - Positive']]

        # Rename toggled column
scripIntelPosInsightToggleDf = scripIntelPosInsightToggleDf.rename(
    columns = {blindInformColumn: 'Option', 
               'Insights - Positive': 'Positive Insight'})

    # Display toggle-able dataframe
st.dataframe(scripIntelPosInsightToggleDf, hide_index = True)

        # Help text
st.write("_Double-click a Summary cell to open its full text; drag the column separator to adjust column widths_")

# %% Section header
st.markdown(
    """
    ### 💛 Scriptural Intelligence Neutral Insights
    Preview key, AI-generated neutral insights across all Spiritual Insights from prophets and intercessors for each option
""")

# %% Scriptural Intelligence neutral insights table

    # Define rows to include
scripIntelNeutInsightRows = 'Scriptural Intelligence'

    # Define columns to include
scripIntelNeutInsightColumns = ['Option ID', 'Name', 'Insights - Neutral']

    # Create dataframe with limited dataset
scripIntelNeutInsightDf = SQCMdf[SQCMdf['Info'] == scripIntelNeutInsightRows][scripIntelNeutInsightColumns]

    # Updated dataframe to work with blind / informed toggle
scripIntelNeutInsightToggleDf = scripIntelNeutInsightDf[[
    blindInformColumn, 'Insights - Neutral']]

        # Rename toggled column
scripIntelNeutInsightToggleDf = scripIntelNeutInsightToggleDf.rename(
    columns = {blindInformColumn: 'Option', 
               'Insights - Neutral': 'Neutral Insight'})

    # Display toggle-able dataframe
st.dataframe(scripIntelNeutInsightToggleDf, hide_index = True)

        # Help text
st.write("_Double-click a Summary cell to open its full text; drag the column separator to adjust column widths_")

# %% Section header
st.markdown(
    """
    ### 🚫 Scriptural Intelligence Negative Insights
    Preview key, AI-generated negative insights across all Spiritual Insights from prophets and intercessors for each option
""")

# %% Scriptural Intelligence negative insights table

    # Define rows to include
scripIntelNegInsightRows = 'Scriptural Intelligence'

    # Define columns to include
scripIntelNegInsightColumns = ['Option ID', 'Name', 'Insights - Negative']

    # Create dataframe with limited dataset
scripIntelNegInsightDf = SQCMdf[SQCMdf['Info'] == scripIntelNegInsightRows][scripIntelNegInsightColumns]

    # Updated dataframe to work with blind / informed toggle
scripIntelNegInsightToggleDf = scripIntelNegInsightDf[[
    blindInformColumn, 'Insights - Negative']]

        # Rename toggled column
scripIntelNegInsightToggleDf = scripIntelNegInsightToggleDf.rename(
    columns = {blindInformColumn: 'Option', 
               'Insights - Negative': 'Negative Insight'})

    # Display toggle-able dataframe
st.dataframe(scripIntelNegInsightToggleDf, hide_index = True)

        # Help text
st.write("_Double-click a Summary cell to open its full text; drag the column separator to adjust column widths_")

# %% Section header
st.markdown(
    """
    ### 💚 Future Intel Positive Insights
    Preview key, AI-generated positive insights across all Spiritual Insights from prophets and intercessors for each option
""")

# %% Future Intel positive insights table

    # Define rows to include
futIntelPosInsightRows = 'Future Intel'

    # Define columns to include
futIntelPosInsightColumns = ['Option ID', 'Name', 'Insights - Positive']

    # Create dataframe with limited dataset
futIntelPosInsightDf = SQCMdf[SQCMdf['Info'] == futIntelPosInsightRows][futIntelPosInsightColumns]

    # Updated dataframe to work with blind / informed toggle
futIntelPosInsightToggleDf = futIntelPosInsightDf[[
    blindInformColumn, 'Insights - Positive']]

        # Rename toggled column
futIntelPosInsightToggleDf = futIntelPosInsightToggleDf.rename(
    columns = {blindInformColumn: 'Option', 
               'Insights - Positive': 'Positive Insight'})

    # Display toggle-able dataframe
st.dataframe(futIntelPosInsightToggleDf, hide_index = True)

        # Help text
st.write("_Double-click a Summary cell to open its full text; drag the column separator to adjust column widths_")

# %% Section header
st.markdown(
    """
    ### 💛 Future Intel Neutral Insights
    Preview key, AI-generated neutral insights across all Spiritual Insights from prophets and intercessors for each option
""")

# %% Future Intel neutral insights table

    # Define rows to include
futIntelNeutInsightRows = 'Future Intel'

    # Define columns to include
futIntelNeutInsightColumns = ['Option ID', 'Name', 'Insights - Neutral']

    # Create dataframe with limited dataset
futIntelNeutInsightDf = SQCMdf[SQCMdf['Info'] == futIntelNeutInsightRows][futIntelNeutInsightColumns]

    # Updated dataframe to work with blind / informed toggle
futIntelNeutInsightToggleDf = futIntelNeutInsightDf[[
    blindInformColumn, 'Insights - Neutral']]

        # Rename toggled column
futIntelNeutInsightToggleDf = futIntelNeutInsightToggleDf.rename(
    columns = {blindInformColumn: 'Option', 
               'Insights - Neutral': 'Neutral Insight'})

    # Display toggle-able dataframe
st.dataframe(futIntelNeutInsightToggleDf, hide_index = True)

        # Help text
st.write("_Double-click a Summary cell to open its full text; drag the column separator to adjust column widths_")

# %% Section header
st.markdown(
    """
    ### 🚫 Future Intel Negative Insights
    Preview key, AI-generated negative insights across all Spiritual Insights from prophets and intercessors for each option
""")

# %% Future Intel negative insights table

    # Define rows to include
futIntelNegInsightRows = 'Future Intel'

    # Define columns to include
futIntelNegInsightColumns = ['Option ID', 'Name', 'Insights - Negative']

    # Create dataframe with limited dataset
futIntelNegInsightDf = SQCMdf[SQCMdf['Info'] == futIntelNegInsightRows][futIntelNegInsightColumns]

    # Updated dataframe to work with blind / informed toggle
futIntelNegInsightToggleDf = futIntelNegInsightDf[[
    blindInformColumn, 'Insights - Negative']]

        # Rename toggled column
futIntelNegInsightToggleDf = futIntelNegInsightToggleDf.rename(
    columns = {blindInformColumn: 'Option', 
               'Insights - Negative': 'Negative Insight'})

    # Display toggle-able dataframe
st.dataframe(futIntelNegInsightToggleDf, hide_index = True)

        # Help text
st.write("_Double-click a Summary cell to open its full text; drag the column separator to adjust column widths_")

# %%