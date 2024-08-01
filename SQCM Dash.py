# %% FC - SQ Consensus Model - Streamlit app
    # Main page

# Import packages
import pandas as pd
import streamlit as st

# %% Tab title
st.set_page_config(
    page_title = "SQCM Overall Ranking",
    page_icon = "📊",)

# %% Page title
st.write("# 📊 SQ Consensus Model Dashboard")

# %% Text
st.markdown(
    """
    #### _Welcome to Firm Collective's SQ Consensus Model Dashboard!_
    #### Select a page on the left to drill down into additional information and details
    - **Alignment**: Demonstrates alignment across key attributes from all Spiritual Insights
    - **Insights by Option**: Provides key, AI-generated insights across all Spiritual Insights from prophets and intercessors for each option
    - **Ranking by Category**: Shows how options are ranked by category (_Identity, Assets, Foretelling, Actionable Intel, Scriptural Intelligence, Future Intel_) – comparing options within each category
    - **Ranking by Option & Category**: Visualizes how each option ranks across categories - comparing categories for each option
    - **Themes**: Displays key, AI-generated themes across all Spiritual Insights from prophets and intercessors for each option
    #### Blind vs. Informed Views
    Throughout this dashboard, you get to decide if it's more helpful to view data analyses as blind (ID's) or informed (names). For the bar charts below, check the box below if you would like the informed view.
""")

# %% Toggle for displaying chart data as informed (names) or blind (ID's)

    # Toggle
blindInformCharts = st.checkbox(
    '**Show Names?** (_If disabled, will show ID\'s, to keep results blind_)', 
    value = False, key = 'blindInformChartsCheckbox')

    # Select the appropriate column for x-axis
overallX = 'Name' if blindInformCharts else 'Option ID'

# %% Section header
st.markdown(
    """
    ### Overall Ranking
    Preview how all considered options rank with each other – according to AI algorithms and ratings for all Spiritual Insights from prophets and intercessors for each option
""")

# %% Import and cache data
@st.cache_data

def load_data():
    googleDriveURL = "https://docs.google.com/spreadsheets/d/1pdPZG75JMgBwZGzcfNpDuo0xaOX2je7Z5QVElsx3hyY/edit?usp=sharing"
    csvImport = googleDriveURL.replace('/edit?usp=sharing', '/export?format=csv')
    return pd.read_csv(csvImport)

    # Load data
SQCMdf = load_data()

    # Display data
# st.write(SQCMdf)

# %% Visualize overall ranking - create dataframe

    # Define rows to include
overallRankRows = 'Overall - ALL Spiritual Insights'

    # Define columns to include
overallRankColumns = ['Option ID', 'Name', 'Ranking Avg ALL']

    # Create dataframe with limited dataset
overallRankDf = SQCMdf[SQCMdf['Info'] == overallRankRows][overallRankColumns]

# %% Bar chart
st.bar_chart(overallRankDf, x = overallX, y ='Ranking Avg ALL', 
    x_label = 'Option', y_label = 'Score / Rating')

    ### NEXT: Sort descending

# %% Section header
st.markdown(
    """
    ### Overall Rating
    Preview how all considered options rank with each other – according to ratings from prophets and intercessors
""")

# %% Visualize overall rating - create dataframe

    # Define columns to include
overallRatingColumns = ['Option ID', 'Name', 'Score Avg']

    # Create dataframe with limited dataset
overallRatingDf = SQCMdf[
    SQCMdf['Score / Rating'] >= 1][overallRatingColumns]

# %% Bar chart
st.bar_chart(overallRatingDf, x = overallX, y = 'Score Avg',
             x_label = 'Option', y_label = 'Score / Rating')

    ### NEXT: Average AND sort descending

# %% Section header
st.markdown(
    """
    ### Overall Summary
    Preview summaries of each option – according to AI algorithms based on all Spiritual Insights from prophets and intercessors
""")

# %% Toggle for displaying summary data as informed (names) or blind (ID's)

    # Toggle
blindInformTables = st.checkbox(
    '**Show Names?** (_If disabled, will show ID\'s, to keep results blind_)', 
    value = False, key = 'blindInformTablesCheckbox')

    # Select the appropriate column to display
blindInformColumn = 'Name' if blindInformTables else 'Option ID'

    ### NEXT: Ensure summaries are blind (no names or gender pronouns)

# %% Summary table

    # Define rows to include
summaryRows = 'Overall - ALL Spiritual Insights'

    # Define columns to include
summaryColumns = ['Option ID', 'Name', 'Summary']

    # Create dataframe with limited dataset
summaryDf = SQCMdf[SQCMdf['Info'] == summaryRows][summaryColumns]

    # Updated dataframe to work with blind / informed toggle
summaryToggleDf = summaryDf[[
    blindInformColumn, 'Summary']]

        # Rename toggled column
display_df = summaryToggleDf.rename(columns = {blindInformColumn: 'Option'})

    # Display toggle-able dataframe
st.dataframe(display_df, hide_index = True)

        # Help text
st.write("_Double-click a Summary cell to open its full text; drag the column separator to adjust column widths_")

# %%
