# %% FC - SQ Consensus Model - Streamlit app
    # Alignment page

# Import packages
import matplotlib.pyplot as plt
import streamlit as st
from matplotlib_venn import venn3

# %% Tab title
st.set_page_config(
    page_title = 'Alignment',
    page_icon = '✅',)

# %% Page title
st.write('# ✅ SQ Consensus Model - Alignment')

# %% Page text
st.markdown(
    '''
    Preview alignment across key attributes from all Spiritual Insights from prophets and intercessors for each option
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

# %% Option 1

    # Title
if blindInform:
    st.markdown('**John Smith**')
else:
    st.markdown('**Option A1B2C3**')

    # Define data subsets
opt1Blind = {'Trailblazer', 'Wisdom', 'Pastoral', 'Apostolic', 'Intercessor', 
    'Revival', 'Prophetic', 'Spiritual Leadership', 'Teaching', 
    'Pastoral Heart', 'Love', 'Compassion'}
opt1Informed = {'Youth', 'Revival', 'Evangelist', 'Teaching', 'Inspiration', 
    'Mentor', 'Global Awakening', 'Strength', 'Wisdom', 'Intercessor', 
    'Prophetic', 'Apostolic', 'Global Awakening', 'Love', 'Dignity', 
    'Justice', 'Compassion'}
org = {'Dignity', 'Freedom', 'Combat human trafficking', 'Prevention', 
    'Rescue', 'Restoration', 'Love', 'Justice', 'Christ', 'Compassion', 
    'Justice', 'Integrity', 'Dignity', 'Hope'}

    # Create & customize a Venn diagram
plt.figure(figsize = (8, 8))

        # Use the data to create the Venn diagram
opt1Venn = venn3([opt1Blind, opt1Informed, org], 
             ('Blind Spiritual Insights', 'Informed Spiritual Insights', 
             'Organization Info'))

        # Helper function to safely set text
def set_label_text(opt1Venn, label_id, text):
    label = opt1Venn.get_label_by_id(label_id)
    if label is not None:
        label.set_text('\n'.join(text))

        # Set texts for each subset
set_label_text(opt1Venn, '100', opt1Blind - opt1Informed - org)
set_label_text(opt1Venn, '010', opt1Informed - opt1Blind - org)
set_label_text(opt1Venn, '001', org - opt1Blind - opt1Informed)
set_label_text(opt1Venn, '110', opt1Blind & opt1Informed - org)
set_label_text(opt1Venn, '101', opt1Blind & org - opt1Informed)
set_label_text(opt1Venn, '011', opt1Informed & org - opt1Blind)
set_label_text(opt1Venn, '111', org & opt1Blind & opt1Informed)

    # Display the Venn diagram in Streamlit
st.pyplot(plt)

    ### NEXT: Clean up text to be contained in circles - and update colors?

# %% Option 2

    # Title
if blindInform:
    st.markdown('**Sarah Johnson**')
else:
    st.markdown('**Option B2C3D4**')

    # Define data subsets
opt2Blind = {'Spiritual Mother', 'Intercessor', 'Watchman', 'Teacher', 
    'Evangelist', 'Revival', 'Justice', 'Dignity', 'Integrity'}
opt2Informed = {'Revival', 'Spiritual Mentor', 'Children\'s Ministry', 
    'Global Awakening', 'Prayer Leader', 'Intercessor', 'Dignity', 'Compassion'}

    # Create & customize a Venn diagram
plt.figure(figsize = (8, 8))

        # Use the data to create the Venn diagram
opt2Venn = venn3([opt2Blind, opt2Informed, org], 
             ('Blind Spiritual Insights', 'Informed Spiritual Insights', 
             'Organization Info'))

        # Helper function to safely set text
def set_label_text(opt2Venn, label_id, text):
    label = opt2Venn.get_label_by_id(label_id)
    if label is not None:
        label.set_text('\n'.join(text))

        # Set texts for each subset
set_label_text(opt2Venn, '100', opt2Blind - opt2Informed - org)
set_label_text(opt2Venn, '010', opt2Informed - opt2Blind - org)
set_label_text(opt2Venn, '001', org - opt2Blind - opt2Informed)
set_label_text(opt2Venn, '110', opt2Blind & opt2Informed - org)
set_label_text(opt2Venn, '101', opt2Blind & org - opt2Informed)
set_label_text(opt2Venn, '011', opt2Informed & org - opt2Blind)
set_label_text(opt2Venn, '111', org & opt2Blind & opt2Informed)

    # Display the Venn diagram in Streamlit
st.pyplot(plt)

# %% Option 3

    # Title
if blindInform:
    st.markdown('**Michael Williams**')
else:
    st.markdown('**Option C3D4E5**')

    # Define data subsets
opt3Blind = {'Apostolic', 'Evangelist', 'Worship Leader', 'Prophetic', 
    'Teacher', 'Strategic', 'Intercessor', 'Pioneer', 'Justice', 'Revival'}

opt3Informed = {'Worship Revival', 'Prophet', 'Teacher', 'Strategic', 
    'Intercessor', 'Justice', 'Global Awakening'}

    # Create & customize a Venn diagram
plt.figure(figsize = (8, 8))

        # Use the data to create the Venn diagram
opt3Venn = venn3([opt3Blind, opt3Informed, org], 
             ('Blind Spiritual Insights', 'Informed Spiritual Insights', 
             'Organization Info'))

        # Helper function to safely set text
def set_label_text(opt3Venn, label_id, text):
    label = opt3Venn.get_label_by_id(label_id)
    if label is not None:
        label.set_text('\n'.join(text))

        # Set texts for each subset
set_label_text(opt3Venn, '100', opt3Blind - opt3Informed - org)
set_label_text(opt3Venn, '010', opt3Informed - opt3Blind - org)
set_label_text(opt3Venn, '001', org - opt3Blind - opt3Informed)
set_label_text(opt3Venn, '110', opt3Blind & opt3Informed - org)
set_label_text(opt3Venn, '101', opt3Blind & org - opt3Informed)
set_label_text(opt3Venn, '011', opt3Informed & org - opt3Blind)
set_label_text(opt3Venn, '111', org & opt3Blind & opt3Informed)

    # Display the Venn diagram in Streamlit
st.pyplot(plt)

# %% Option 4

    # Title
if blindInform:
    st.markdown('**Emily Davis**')
else:
    st.markdown('**Option D4E5F6**')

    # Define data subsets
opt4Blind = {'Prophetic', 'Worship', 'Strategic', 'Intercessor', 'Teacher', 
    'Pastoral Leader', 'Revival', 'Hope', 'Love'}
opt4Informed = {'Spiritual Watchman', 'Prophetic Teacher', 'Prayer Leader', 
    'Global Awakening', 'Intercessor', 'Hope', 'Justice'}

    # Create & customize a Venn diagram
plt.figure(figsize = (8, 8))

        # Use the data to create the Venn diagram
opt4Venn = venn3([opt4Blind, opt4Informed, org], 
             ('Blind Spiritual Insights', 'Informed Spiritual Insights', 
             'Organization Info'))

        # Helper function to safely set text
def set_label_text(opt4Venn, label_id, text):
    label = opt4Venn.get_label_by_id(label_id)
    if label is not None:
        label.set_text('\n'.join(text))

        # Set texts for each subset
set_label_text(opt4Venn, '100', opt4Blind - opt4Informed - org)
set_label_text(opt4Venn, '010', opt4Informed - opt4Blind - org)
set_label_text(opt4Venn, '001', org - opt4Blind - opt4Informed)
set_label_text(opt4Venn, '110', opt4Blind & opt4Informed - org)
set_label_text(opt4Venn, '101', opt4Blind & org - opt4Informed)
set_label_text(opt4Venn, '011', opt4Informed & org - opt4Blind)
set_label_text(opt4Venn, '111', org & opt4Blind & opt4Informed)

    # Display the Venn diagram in Streamlit
st.pyplot(plt)

# %% Option 5

    # Title
if blindInform:
    st.markdown('**David Brown**')
else:
    st.markdown('**Option E5F6G7**')

    # Define data subsets
opt5Blind = {'Strategic Guidance', 'Spiritual Insight', 'Evangelist', 
    'Evangelistic Passion', 'Dynamic Preacher', 'Compassionate', 'Healer', 
    'Revival', 'Love', 'Dignity', 'Hope'}
opt5Informed = {'Shepherd Leader', 'Revival', 'Preacher', 'Global Evangelist', 
    'Teaching', 'Prayer Leader', 'Intercessor', 'Love', 'Justice', 'Hope'}

    # Create & customize a Venn diagram
plt.figure(figsize = (8, 8))

        # Use the data to create the Venn diagram
opt5Venn = venn3([opt5Blind, opt5Informed, org], 
             ('Blind Spiritual Insights', 'Informed Spiritual Insights', 
             'Organization Info'))

        # Helper function to safely set text
def set_label_text(opt5Venn, label_id, text):
    label = opt5Venn.get_label_by_id(label_id)
    if label is not None:
        label.set_text('\n'.join(text))

        # Set texts for each subset
set_label_text(opt5Venn, '100', opt5Blind - opt5Informed - org)
set_label_text(opt5Venn, '010', opt5Informed - opt5Blind - org)
set_label_text(opt5Venn, '001', org - opt5Blind - opt5Informed)
set_label_text(opt5Venn, '110', opt5Blind & opt5Informed - org)
set_label_text(opt5Venn, '101', opt5Blind & org - opt5Informed)
set_label_text(opt5Venn, '011', opt5Informed & org - opt5Blind)
set_label_text(opt5Venn, '111', org & opt5Blind & opt5Informed)

    # Display the Venn diagram in Streamlit
st.pyplot(plt)

# %%

