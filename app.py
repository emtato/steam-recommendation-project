# Description:
# Description: This python file contains the UI for the project. Here we are using streamlit. You'll need to download
# the streamlit library and follow the directions in the guide to utilize this.
# WARNING: for the app to function, please use streamlit version 1.43.2
# Created by Emilia on 2025-03-25

import streamlit as st

import main
from main import Graph

results = []


# states 0: get data occurence frequency, 1: categories, 2: genres, 3: cost

def start_page():
    """
         This serves as the starting page for the application, it contains basic information of what the app does
         how the user can use it, and a button that begins the process.
         """
    st.title("Steam game recommendation system!")

    st.markdown("""
    Hello user! 👋😎 Are you interested in playing games 🎮🕹️ on Steam but don't really know where to start? 🤔📉 
    Are you overwhelmed 😵‍💫🌊 by the sheer amount of options 📚💥 on Steam?

    Well, boy do I have news 📢👀 for you! 🚨🧠

    This is the :rainbow[Steam Game Recommendation System] 🌈✨🎮🧃🧠!!
    Here we'll recommend games 🎲🔥 that YOU 🫵💯 can play/buy 💸🧾 on Steam based on YOUR OWN necessities 🧍‍♀️💅📋! 
    Cool right? 😎😜

    (insert some for stuff here / desc 📝💭🛠️)

    Click the button below 🔘👇 to get started 🚀🎉🎯
    """)
    if st.button("Start"):
        st.balloons()
        st.session_state["start"] = True
        st.rerun()


def pc_req_page():
    """
    A page that lets the user choose their type of PC.
    1 OPTION TEST
    """
    st.title("Choosing your pc requirements")
    option_comp = st.selectbox("What type of computer do you have?", ("PC (ew)", "Mac", "Linux"), index=None,
                               placeholder="-", )

    # st.write("You selected:", option)
    results.append(option_comp)
    if option_comp == "PC (ew)":
        pc_page()
    elif option_comp == "Mac":
        mac_page()
    elif option_comp == "Linux":
        linux_page()  # st.write("You chose: " + results.pop())  # game_genre_page()


def pc_page():
    """"""
    option_OS = st.selectbox("What Windows (ew) OS version do you use?", ("Windows 11", "Windows 10", "Windows 7"),
                             # May have to replace this with a POSSIBLE OS list from data
                             index=None, placeholder="-", )
    option_RAM = st.selectbox("How much RAM does your computer "
                              "have?", ("8GB", "16GB", "32GB", "32GB+"),
                              # May have to replace this with a POSSIBLE RAM list from data
                              index=None, placeholder="-", )

    option_STORAGE = st.text_input("How much storage do you have? (put in GB):")  # DONT FORGET TO RESTRICT TO
    if option_STORAGE.isdigit():

        if option_OS and option_RAM and option_STORAGE and st.button('hi'):
            st.session_state[0] = True
            st.session_state['start'] = False
            st.rerun()

    elif option_STORAGE != "":
        st.warning('the hell ya think yer doin mate that aint no **int**')


def mac_page():
    """"""
    option_OS = st.selectbox("What Mac OS version do you use?", ("insert"),
                             # May have to replace this with a POSSIBLE OS list from data
                             index=None, placeholder="-", )
    option_RAM = st.selectbox("How much RAM does your computer have?", ("8GB", "16GB", "32GB", "32GB+"),
                              # May have to replace this with a POSSIBLE RAM list from data
                              index=None, placeholder="-", )
    option_STORAGE = st.text_input(
        "How much storage do you have? (put in GB):")  # DONT FORGET TO RESTRICT TO  #  # INTEGERS ONLY


def linux_page():
    """"""
    option_OS = st.selectbox("What Linux OS version do you use?", ("isert"),
                             # May have to replace this with a POSSIBLE OS list from data
                             index=None, placeholder="-", )
    option_RAM = st.selectbox("How much RAM does your computer have?", ("8GB", "16GB", "32GB", "32GB+"),
                              # May have to replace this with a POSSIBLE RAM list from data
                              index=None, placeholder="-", )
    option_STORAGE = st.text_input(
        "How much storage do you have? (put in GB):")  # DONT FORGET TO RESTRICT TO  #  # INTEGERS ONLY


def get_data():
    cat, gen = main.extract_freq('data.csv')
    st.session_state['cat'] = cat
    st.session_state['gen'] = gen
    st.session_state[0], st.session_state[1] = False, True
    st.rerun()


def category_pick():
    st.title('hi')
    st.write('pick gaming stuff')
    if 'cat' not in st.session_state:
        st.session_state['cat'] = []  # list of sleected categories ^•ω•^
    selected = st.selectbox("Choose category okay", st.session_state['cat'])


def game_genre_page():
    """
    A page that lets the user choose the genres they want.
    MULTIPLE CHOICE TEST
    """
    st.title("")


def brokeness_level():
    st.title('bald')


def final_page():
    """
    A page that shows the results the user chose, aka the options.
    """
    st.write(str(results))

    # this section checks the session_state and loads the next page, this is to prevent the app's cache from maxing
    # and  # restarting the app, making the user lose progress.


if "start" not in st.session_state:
    start_page()
elif st.session_state['start']:
    pc_req_page()
elif st.session_state[0]:
    get_data()
elif st.session_state[1]:
    category_pick()
elif st.session_state[2]:
    game_genre_page()
elif st.session_state[3]:
    brokeness_level()  # The code below creates tabs! We can use this to show the results later  #   # tab1,
    # tab2 = st.tabs(["Tab 1", "Tab2"])  # tab1.write("this is tab 1")  # tab2.write("this is tab 2")

# g = Graph()
# g.build_graph("data.csv", 1)

# st.write("Graph built successfully!")

# run streamlit run app.py in terminal
