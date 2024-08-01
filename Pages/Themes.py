# %% FC - SQ Consensus Model - Streamlit app
    # Themes page

# Import packages
import streamlit as st
import streamlit_wordcloud as wordcloud

# %% Tab title
st.set_page_config(
    page_title = 'Key Themes',
    page_icon = '🗝',)

# %% Page title
st.write('# 🗝 SQ Consensus Model - Key Themes')

# %% Page text
st.markdown(
    '''
    Preview key, AI-generated themes across all Spiritual Insights from prophets and intercessors
    ### Themes by Option
    Preview key, AI-generated positive insights across all Spiritual Insights from prophets and intercessors for each options; hover over a word or phrase to see how many times it shows up in the Spiritual Insights
    #### Blind vs. Informed Views
    Throughout this dashboard, you get to decide if it's more helpful to view data analyses as blind (ID's) or informed (names). For the per-option themes below, check the box below if you would like the informed view.
''')

# %% Toggle for displaying data as informed (names) or blind (ID's)

    # Toggle
blindInform = st.checkbox(
    '**Show Names?** (_If disabled, will show ID\'s, to keep results blind_)', 
    value = False)

    # Select the appropriate column to display
blindInformColumn = 'Name' if blindInform else 'Option ID'

    ### NEXT: Ensure insights are blind (no names or gender pronouns)

# %% Option 1 themes

    # Import words
opt1Words = [
    {'text': 'youth', 'value': 9},
    {'text': 'intercession', 'value': 5},
    {'text': 'revival', 'value': 5},
    {'text': 'Youth ministry', 'value': 4},
    {'text': 'Evangelism', 'value': 4},
    {'text': 'prayer', 'value': 4},
    {'text': 'prophetic', 'value': 4},
    {'text': 'worship', 'value': 4},
    {'text': 'Mentorship', 'value': 3},
    {'text': 'Teaching', 'value': 3},
    {'text': 'mentor', 'value': 3},
    {'text': 'Prayer', 'value': 2},
    {'text': 'Spiritual Awakening', 'value': 2},
    {'text': 'Leadership', 'value': 2},
    {'text': 'wisdom', 'value': 2},
    {'text': 'revival', 'value': 2},
    {'text': 'Worship Gatherings', 'value': 2},
    {'text': 'Community Transformation', 'value': 2},
    {'text': 'unity', 'value': 2},
    {'text': 'community', 'value': 2},
    {'text': 'Youth Revivals', 'value': 1},
    {'text': 'Strength', 'value': 1},
    {'text': 'Youth leadership', 'value': 1},
    {'text': 'inspiration', 'value': 1},
    {'text': 'Youth revival anointing', 'value': 1},
    {'text': 'Prophetic gift for youth', 'value': 1},
    {'text': 'Spiritual awakening among youth', 'value': 1},
    {'text': 'Peer connection', 'value': 1},
    {'text': 'early ministry start', 'value': 1},
    {'text': 'organizing retreats', 'value': 1},
    {'text': 'organizing revivals', 'value': 1},
    {'text': 'relevant gospel sermons', 'value': 1},
    {'text': 'inspiration for deeper relationship with God', 'value': 1},
    {'text': 'Worship Leadership', 'value': 1},
    {'text': 'Compassion', 'value': 1},
    {'text': 'prophetic gifting', 'value': 1},
    {'text': 'Prophetic Ministry', 'value': 1},
    {'text': 'Intercessory Prayers', 'value': 1},
    {'text': 'Prophetic Insight', 'value': 1},
    {'text': 'Church Planting', 'value': 1},
    {'text': 'practical applications', 'value': 1},
    {'text': 'biblical insights', 'value': 1},
    {'text': 'Intercessory Prayer', 'value': 1},
    {'text': 'Pastoral Care', 'value': 1},
    {'text': 'Worship', 'value': 1}
]

# %% Option 1 word cloud 

    # Title
if blindInform:
    st.markdown('**John Smith**')
else:
    st.markdown('**Option A1B2C3**')

    # Word cloud
opt1Wordcloud = wordcloud.visualize(
    opt1Words,
    tooltip_data_fields = {
        'text': 'Word',
        'value': 'Frequency', 
        'key': 'opt1Wordcloud'
    },
    per_word_coloring = True
)

# %% Option 2 themes

    # Import words
opt2Words = [
    {'text': 'revival', 'value': 10},
    {'text': 'prophetic', 'value': 8},
    {'text': 'prayer', 'value': 6},
    {'text': 'Evangelism', 'value': 5},
    {'text': 'Teaching', 'value': 5},
    {'text': 'equip', 'value': 4},
    {'text': 'intercession', 'value': 4},
    {'text': 'intercession', 'value': 3},
    {'text': 'revival', 'value': 3},
    {'text': 'Prophetic Insight', 'value': 3},
    {'text': 'unity', 'value': 3},
    {'text': 'community', 'value': 3},
    {'text': 'Prayer', 'value': 2},
    {'text': 'prophetic gifting', 'value': 2},
    {'text': 'Community Transformation', 'value': 2},
    {'text': 'Intercessory Prayers', 'value': 2},
    {'text': 'Intercessory Prayer', 'value': 2},
    {'text': 'Nurturing', 'value': 2},
    {'text': 'Nurturing young faith', 'value': 2},
    {'text': 'Fasting', 'value': 2},
    {'text': 'Family Revivals', 'value': 2},
    {'text': 'family revival', 'value': 2},
    {'text': 'Spiritual Awakening', 'value': 1},
    {'text': 'City Transformation', 'value': 1},
    {'text': 'Region Transformation', 'value': 1},
    {'text': 'Revival catalyst', 'value': 1},
    {'text': 'Prophetic Ministries', 'value': 1},
    {'text': 'Spiritual Fervor', 'value': 1},
    {'text': 'societal transformation', 'value': 1},
    {'text': 'equipping', 'value': 1},
    {'text': 'prophetic gifts', 'value': 1},
    {'text': "Children's Ministry", 'value': 1},
    {'text': 'Family Ministry', 'value': 1},
    {'text': 'Prophetic Intercession', 'value': 1},
    {'text': 'Foundation Building', 'value': 1},
    {'text': 'discernment', 'value': 1},
    {'text': 'creativity', 'value': 1},
    {'text': 'global revival', 'value': 1},
    {'text': 'spiritual growth', 'value': 1},
    {'text': 'Revival Meetings', 'value': 1},
    {'text': 'Equipping Believers', 'value': 1},
    {'text': 'Equipping Others', 'value': 1},
    {'text': 'global ministry', 'value': 1},
    {'text': 'Harvest of Souls', 'value': 1},
    {'text': 'creative teaching', 'value': 1},
    {'text': 'equipping saints', 'value': 1},
    {'text': 'Community Building', 'value': 1}
]

# %% Option 2 word cloud 

    # Title
if blindInform:
    st.markdown('**Sarah Johnson**')
else:
    st.markdown('**Option B2C3D4**')

    # Word cloud
opt2Wordcloud = wordcloud.visualize(
    opt2Words,
    tooltip_data_fields = {
        'text': 'Word',
        'value': 'Frequency', 
        'key': 'opt2Wordcloud'
    },
    per_word_coloring = True
)

# %% Option 3 themes

    # Import words
opt3Words = [
    {'text': 'worship', 'value': 11},
    {'text': 'prophetic', 'value': 10},
    {'text': 'revival', 'value': 7},
    {'text': 'Worship Leadership', 'value': 6},
    {'text': 'Teaching', 'value': 5},
    {'text': 'unity', 'value': 5},
    {'text': 'intercession', 'value': 4},
    {'text': 'revival', 'value': 4},
    {'text': 'Prophetic Ministry', 'value': 4},
    {'text': 'intercession', 'value': 4},
    {'text': 'Evangelism', 'value': 3},
    {'text': 'mentoring', 'value': 3},
    {'text': 'Unity', 'value': 3},
    {'text': 'Diversity', 'value': 3},
    {'text': 'spiritual renewal', 'value': 3},
    {'text': 'mentor', 'value': 3},
    {'text': 'prophetic gifting', 'value': 2},
    {'text': 'Training', 'value': 2},
    {'text': 'Miracles', 'value': 2},
    {'text': 'healing', 'value': 2},
    {'text': 'apostolic calling', 'value': 2},
    {'text': 'Supernatural Encounters', 'value': 2},
    {'text': 'community', 'value': 2},
    {'text': 'Community Transformation', 'value': 1},
    {'text': 'Church Planting', 'value': 1},
    {'text': 'prophetic gifts', 'value': 1},
    {'text': 'global revival', 'value': 1},
    {'text': 'spiritual growth', 'value': 1},
    {'text': 'Community Building', 'value': 1},
    {'text': 'Spiritual Strongholds', 'value': 1},
    {'text': 'Global Worship Gatherings', 'value': 1},
    {'text': 'Intimate worship encounters', 'value': 1},
    {'text': 'Evangelistic zeal', 'value': 1},
    {'text': 'Prophetic teaching', 'value': 1},
    {'text': 'Apostolic Role', 'value': 1},
    {'text': 'prophetic worship', 'value': 1},
    {'text': 'prophetic utterance', 'value': 1},
    {'text': 'Worship Revival', 'value': 1},
    {'text': 'Revival Fires', 'value': 1},
    {'text': 'deliverance', 'value': 1},
    {'text': 'equipping future leaders', 'value': 1},
    {'text': 'deep understanding of Scripture', 'value': 1},
    {'text': 'inspiration through worship music', 'value': 1},
    {'text': 'establishing new works', 'value': 1},
    {'text': 'Kingdom Expansion', 'value': 1},
    {'text': 'equip', 'value': 1}
]

# %% Option 3 word cloud 

    # Title
if blindInform:
    st.markdown('**Michael Williams**')
else:
    st.markdown('**Option C3D4E5**')

    # Word cloud
opt3Wordcloud = wordcloud.visualize(
    opt3Words,
    tooltip_data_fields = {
        'text': 'Word',
        'value': 'Frequency', 
        'key': 'opt3Wordcloud'
    },
    per_word_coloring = True
)

# %% Option 4 themes

    # Import words
opt4Words = [
    {'text': 'Teaching', 'value': 7},
    {'text': 'prophetic', 'value': 7},
    {'text': 'Worship Leadership', 'value': 5},
    {'text': 'unity', 'value': 5},
    {'text': 'revival', 'value': 5},
    {'text': 'intercession', 'value': 5},
    {'text': 'worship', 'value': 5},
    {'text': 'Community Transformation', 'value': 4},
    {'text': 'community', 'value': 4},
    {'text': 'prayer', 'value': 4},
    {'text': 'intercession', 'value': 3},
    {'text': 'Intercessory Prayer', 'value': 3},
    {'text': 'spiritual growth', 'value': 3},
    {'text': 'revival', 'value': 2},
    {'text': 'Prophetic Ministry', 'value': 2},
    {'text': 'Church Planting', 'value': 2},
    {'text': 'Pastoral Care', 'value': 2},
    {'text': 'Prophetic Intercession', 'value': 2},
    {'text': 'Miracles', 'value': 2},
    {'text': 'healing', 'value': 2},
    {'text': 'Revival Movements', 'value': 2},
    {'text': 'Compassion', 'value': 1},
    {'text': 'prophetic gifting', 'value': 1},
    {'text': 'mentoring', 'value': 1},
    {'text': 'Unity', 'value': 1},
    {'text': 'Diversity', 'value': 1},
    {'text': 'spiritual renewal', 'value': 1},
    {'text': 'apostolic calling', 'value': 1},
    {'text': 'Supernatural Encounters', 'value': 1},
    {'text': 'Kingdom Expansion', 'value': 1},
    {'text': 'Prophetic accuracy', 'value': 1},
    {'text': 'Apostolic pioneering', 'value': 1},
    {'text': 'Intercessory Teams', 'value': 1},
    {'text': 'prophetic visions', 'value': 1},
    {'text': 'spiritual breakthroughs', 'value': 1},
    {'text': 'breaking strongholds', 'value': 1},
    {'text': 'Prayer Initiatives', 'value': 1},
    {'text': 'Miraculous Healings', 'value': 1},
    {'text': 'divine interventions', 'value': 1},
    {'text': 'equipping intercessors', 'value': 1},
    {'text': 'practical application', 'value': 1},
    {'text': 'transformation through Scripture', 'value': 1},
    {'text': 'Strategic Guidance', 'value': 1},
    {'text': 'Leadership Development', 'value': 1},
    {'text': 'Pioneering', 'value': 1},
    {'text': 'sustaining revival', 'value': 1},
    {'text': 'restoration', 'value': 1},
    {'text': 'mentor', 'value': 1},
    {'text': 'equip', 'value': 1},
    {'text': 'restoration', 'value': 1}
]

# %% Option 4 word cloud 

    # Title
if blindInform:
    st.markdown('**Emily Davis**')
else:
    st.markdown('**Option D4E5F6**')

    # Word cloud
opt4Wordcloud = wordcloud.visualize(
    opt4Words,
    tooltip_data_fields = {
        'text': 'Word',
        'value': 'Frequency', 
        'key': 'opt4Wordcloud'
    },
    per_word_coloring = True
)

# %% Option 5 themes

    # Import words
opt5Words = [
    {'text': 'unity', 'value': 9},
    {'text': 'Evangelism', 'value': 6},
    {'text': 'Teaching', 'value': 6},
    {'text': 'revival', 'value': 6},
    {'text': 'Pastoral Care', 'value': 5},
    {'text': 'prophetic', 'value': 5},
    {'text': 'mentor', 'value': 4},
    {'text': 'community', 'value': 4},
    {'text': 'revival', 'value': 3},
    {'text': 'mentoring', 'value': 3},
    {'text': 'Unity', 'value': 3},
    {'text': 'Discipleship', 'value': 3},
    {'text': 'restoration', 'value': 3},
    {'text': 'Community Transformation', 'value': 2},
    {'text': 'Church Planting', 'value': 2},
    {'text': 'healing', 'value': 2},
    {'text': 'apostolic calling', 'value': 2},
    {'text': 'Preaching', 'value': 2},
    {'text': 'Guidance', 'value': 2},
    {'text': 'Spiritual maturity', 'value': 2},
    {'text': 'Community Restoration', 'value': 2},
    {'text': 'Mentorship', 'value': 1},
    {'text': 'Spiritual Awakening', 'value': 1},
    {'text': 'wisdom', 'value': 1},
    {'text': 'intercession', 'value': 1},
    {'text': 'Mentorship', 'value': 1},
    {'text': 'Compassion', 'value': 1},
    {'text': 'Prophetic Ministry', 'value': 1},
    {'text': 'Prophetic Insight', 'value': 1},
    {'text': 'deliverance', 'value': 1},
    {'text': 'Kingdom Expansion', 'value': 1},
    {'text': 'spiritual breakthroughs', 'value': 1},
    {'text': 'restoration', 'value': 1},
    {'text': 'Sustained Revival', 'value': 1},
    {'text': 'Deep Revivals', 'value': 1},
    {'text': 'Enduring Revivals', 'value': 1},
    {'text': "Love for God's Word", 'value': 1},
    {'text': 'Prophetic strategy', 'value': 1},
    {'text': 'Humility', 'value': 1},
    {'text': 'prophetic edge', 'value': 1},
    {'text': 'Spiritual Depth', 'value': 1},
    {'text': 'prophetic preaching', 'value': 1},
    {'text': 'Conversions', 'value': 1},
    {'text': 'Unity in Worship and Service', 'value': 1},
    {'text': 'Unity in Service', 'value': 1},
    {'text': 'pioneering spirit', 'value': 1},
    {'text': 'reaching the marginalized', 'value': 1},
    {'text': 'honor', 'value': 1},
    {'text': 'Healing Ministry', 'value': 1},
    {'text': 'Outreach', 'value': 1},
    {'text': 'Strategic Discernment', 'value': 1},
    {'text': 'intercession', 'value': 1},
    {'text': 'worship', 'value': 1},
    {'text': 'wisdom', 'value': 1}
]

# %% Option 5 word cloud 

    # Title
if blindInform:
    st.markdown('**David Brown**')
else:
    st.markdown('**Option E5F6G7**')

    # Word cloud
opt5Wordcloud = wordcloud.visualize(
    opt5Words,
    tooltip_data_fields = {
        'text': 'Word',
        'value': 'Frequency', 
        'key': 'opt5Wordcloud'
    },
    per_word_coloring = True
)

# %% Section header
st.markdown(
    '''
    ### Themes Across All Options
    Preview key, AI-generated positive insights across all Spiritual Insights from prophets and intercessors for all options; hover over a word or phrase to see how many times it shows up in the Spiritual Insights
''')

# %% Overall themes wordcloud

    # Import word counts
overallWords = [
    {'text': 'Mentorship', 'value': 8},
    {'text': 'Prayer', 'value': 18},
    {'text': 'Spiritual Awakening', 'value': 4},
    {'text': 'Youth Revivals', 'value': 1},
    {'text': 'Leadership', 'value': 2},
    {'text': 'Youth ministry', 'value': 4},
    {'text': 'Strength', 'value': 1},
    {'text': 'wisdom', 'value': 6},
    {'text': 'Youth leadership', 'value': 1},
    {'text': 'inspiration', 'value': 1},
    {'text': 'Youth revival anointing', 'value': 1},
    {'text': 'intercession', 'value': 35},
    {'text': 'Prophetic gift for youth', 'value': 1},
    {'text': 'Spiritual awakening among youth', 'value': 1},
    {'text': 'Peer connection', 'value': 1},
    {'text': 'Evangelism', 'value': 18},
    {'text': 'revival', 'value': 47},
    {'text': 'early ministry start', 'value': 1},
    {'text': 'organizing retreats', 'value': 1},
    {'text': 'organizing revivals', 'value': 1},
    {'text': 'relevant gospel sermons', 'value': 1},
    {'text': 'inspiration for deeper relationship with God', 'value': 1},
    {'text': 'Worship Leadership', 'value': 12},
    {'text': 'Worship Gatherings', 'value': 2},
    {'text': 'Compassion', 'value': 3},
    {'text': 'prophetic gifting', 'value': 6},
    {'text': 'Prophetic Ministry', 'value': 8},
    {'text': 'Community Transformation', 'value': 11},
    {'text': 'Intercessory Prayers', 'value': 3},
    {'text': 'Prophetic Insight', 'value': 5},
    {'text': 'Church Planting', 'value': 6},
    {'text': 'Teaching', 'value': 26},
    {'text': 'practical applications', 'value': 1},
    {'text': 'biblical insights', 'value': 1},
    {'text': 'Intercessory Prayer', 'value': 6},
    {'text': 'Pastoral Care', 'value': 8},
    {'text': 'Worship', 'value': 22},
    {'text': 'City Transformation', 'value': 1},
    {'text': 'Region Transformation', 'value': 1},
    {'text': 'Nurturing', 'value': 2},
    {'text': 'Revival catalyst', 'value': 1},
    {'text': 'Nurturing young faith', 'value': 2},
    {'text': 'Prophetic Ministries', 'value': 1},
    {'text': 'Fasting', 'value': 2},
    {'text': 'Spiritual Fervor', 'value': 1},
    {'text': 'Family Revivals', 'value': 2},
    {'text': 'societal transformation', 'value': 1},
    {'text': 'family revival', 'value': 2},
    {'text': 'equipping', 'value': 1},
    {'text': 'prophetic gifts', 'value': 2},
    {'text': 'Children\'s Ministry', 'value': 1},
    {'text': 'Family Ministry', 'value': 1},
    {'text': 'Prophetic Intercession', 'value': 3},
    {'text': 'Foundation Building', 'value': 1},
    {'text': 'discernment', 'value': 1},
    {'text': 'creativity', 'value': 1},
    {'text': 'global revival', 'value': 2},
    {'text': 'spiritual growth', 'value': 5},
    {'text': 'Revival Meetings', 'value': 1},
    {'text': 'Equipping Believers', 'value': 1},
    {'text': 'Equipping Others', 'value': 1},
    {'text': 'global ministry', 'value': 1},
    {'text': 'Harvest of Souls', 'value': 1},
    {'text': 'creative teaching', 'value': 1},
    {'text': 'equipping saints', 'value': 1},
    {'text': 'Community Building', 'value': 2},
    {'text': 'Spiritual Strongholds', 'value': 1},
    {'text': 'Global Worship Gatherings', 'value': 1},
    {'text': 'Intimate worship encounters', 'value': 1},
    {'text': 'Training', 'value': 2},
    {'text': 'mentoring', 'value': 7},
    {'text': 'Evangelistic zeal', 'value': 1},
    {'text': 'Prophetic teaching', 'value': 1},
    {'text': 'Miracles', 'value': 4},
    {'text': 'Unity', 'value': 31},
    {'text': 'Diversity', 'value': 4},
    {'text': 'Apostolic Role', 'value': 1},
    {'text': 'healing', 'value': 6},
    {'text': 'prophetic worship', 'value': 1},
    {'text': 'spiritual renewal', 'value': 4},
    {'text': 'apostolic calling', 'value': 5},
    {'text': 'prophetic utterance', 'value': 1},
    {'text': 'Worship Revival', 'value': 1},
    {'text': 'Revival Fires', 'value': 1},
    {'text': 'deliverance', 'value': 2},
    {'text': 'equipping future leaders', 'value': 1},
    {'text': 'deep understanding of Scripture', 'value': 1},
    {'text': 'Supernatural Encounters', 'value': 3},
    {'text': 'inspiration through worship music', 'value': 1},
    {'text': 'establishing new works', 'value': 1},
    {'text': 'Kingdom Expansion', 'value': 3},
    {'text': 'Revival Movements', 'value': 2},
    {'text': 'Prophetic accuracy', 'value': 1},
    {'text': 'Apostolic pioneering', 'value': 1},
    {'text': 'Intercessory Teams', 'value': 1},
    {'text': 'prophetic visions', 'value': 1},
    {'text': 'spiritual breakthroughs', 'value': 2},
    {'text': 'breaking strongholds', 'value': 1},
    {'text': 'Prayer Initiatives', 'value': 1},
    {'text': 'Miraculous Healings', 'value': 1},
    {'text': 'divine interventions', 'value': 1},
    {'text': 'equipping intercessors', 'value': 1},
    {'text': 'practical application', 'value': 1},
    {'text': 'transformation through Scripture', 'value': 1},
    {'text': 'Strategic Guidance', 'value': 1},
    {'text': 'Leadership Development', 'value': 1},
    {'text': 'Pioneering', 'value': 1},
    {'text': 'sustaining revival', 'value': 1},
    {'text': 'restoration', 'value': 6},
    {'text': 'Discipleship', 'value': 3},
    {'text': 'Preaching', 'value': 2},
    {'text': 'Sustained Revival', 'value': 1},
    {'text': 'Deep Revivals', 'value': 1},
    {'text': 'Enduring Revivals', 'value': 1},
    {'text': 'Guidance', 'value': 2},
    {'text': 'Spiritual maturity', 'value': 2},
    {'text': 'Love for God\'s Word', 'value': 1},
    {'text': 'Prophetic strategy', 'value': 1},
    {'text': 'Humility', 'value': 1},
    {'text': 'Community Restoration', 'value': 2},
    {'text': 'prophetic edge', 'value': 1},
    {'text': 'Spiritual Depth', 'value': 1},
    {'text': 'prophetic preaching', 'value': 1},
    {'text': 'Conversions', 'value': 1},
    {'text': 'Unity in Worship and Service', 'value': 1},
    {'text': 'Unity in Service', 'value': 1},
    {'text': 'pioneering spirit', 'value': 1},
    {'text': 'reaching the marginalized', 'value': 1},
    {'text': 'honor', 'value': 1},
    {'text': 'Healing Ministry', 'value': 1},
    {'text': 'Outreach', 'value': 1},
    {'text': 'Strategic Discernment', 'value': 1},
    {'text': 'mentor', 'value': 11},
    {'text': 'equip', 'value': 6},
    {'text': 'community', 'value': 15},
    {'text': 'youth', 'value': 9},
    {'text': 'prophetic', 'value': 34}
]

# %% Overall word cloud
overallWordcloud = wordcloud.visualize(
    overallWords,
    tooltip_data_fields = {
        'text': 'Word',
        'value': 'Frequency', 
        'key': 'overallWordcloud'
    },
    per_word_coloring = True
    )

# %%
