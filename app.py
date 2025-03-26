from http.client import responses

import streamlit as st
#from main import Graph

results = []

def start_page():
    """
    Hello user! 👋😎 Are you interested in playing games 🎮🕹️ on Steam but don't really know where to start? 🤔📉 Are you overwhelmed 😵‍💫🌊 by the sheer amount of options 📚💥 on Steam?

    Well, boy do I have news 📢👀 for you! 🚨🧠

    This is the :rainbow[Steam Game Recommendation System] 🌈✨🎮🧃🧠!!
    Here we'll recommend games 🎲🔥 that YOU 🫵💯 can play/buy 💸🧾 on Steam based on YOUR OWN necessities 🧍‍♀️💅📋! Cool right? 😎😜

    (insert some for stuff here / desc 📝💭🛠️)

    Click the button below 🔘👇 to get started 🚀🎉🎯
    """

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
    option_comp = st.selectbox(
        "What type of computer do you have?",
        ("PC", "Mac", "Linux"),
        index=None,
        placeholder="-",
    )



    # st.write("You selected:", option)
    results.append(option_comp)
    if option_comp == "PC":
        pc_page()
    elif option_comp == "Mac":
        mac_page()
    elif option_comp == "Linux":
        linux_page()
    # st.write("You chose: " + results.pop())
    # game_genre_page()


def pc_page():
    """"""
    option_OS = st.selectbox(
        "What Windows OS version do you use?",
        ("Windows 11", "Windows 10", "Windows 7"),  # May have to replace this with a POSSIBLE OS list from data
        index=None,
        placeholder="-",
    )
    option_RAM = st.selectbox(
        "How much RAM does your computer have?",
        ("8GB", "16GB", "32GB", "32GB+"),  # May have to replace this with a POSSIBLE RAM list from data
        index=None,
        placeholder="-",
    )
    option_STORAGE = st.text_input("How much storage do you have? (put in GB):")
    # DONT FORGET TO RESTRICT TO INTEGERS ONLY


def mac_page():
    """"""
    option_OS = st.selectbox(
        "What Mac OS version do you use?",
        ("insert"),  # May have to replace this with a POSSIBLE OS list from data
        index=None,
        placeholder="-",
    )
    option_RAM = st.selectbox(
        "How much RAM does your computer have?",
        ("8GB", "16GB", "32GB", "32GB+"),  # May have to replace this with a POSSIBLE RAM list from data
        index=None,
        placeholder="-",
    )
    option_STORAGE = st.text_input("How much storage do you have? (put in GB):")
    # DONT FORGET TO RESTRICT TO INTEGERS ONLY


def linux_page():
    """"""
    option_OS = st.selectbox(
        "What Linux OS version do you use?",
        ("isert"),  # May have to replace this with a POSSIBLE OS list from data
        index=None,
        placeholder="-",
    )
    option_RAM = st.selectbox(
        "How much RAM does your computer have?",
        ("8GB", "16GB", "32GB", "32GB+"),  # May have to replace this with a POSSIBLE RAM list from data
        index=None,
        placeholder="-",
    )
    option_STORAGE = st.text_input("How much storage do you have? (put in GB):")
    # DONT FORGET TO RESTRICT TO INTEGERS ONLY


def game_genre_page():
    """
    A page that lets the user choose the genres they want.
    MULTIPLE CHOICE TEST
    """
    st.title("")


def final_page():
    """
    A page that shows the results the user chose, aka the options.
    """
    st.write(str(results))


# this section checks the session_state and loads the next page, this is to prevent the app's cache from maxing and
# restarting the app, making the user lose progress.
if "start" not in st.session_state:
    start_page()
else:
    pc_req_page()



# The code below creates tabs! We can use this to show the results later
    # tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
    # tab1.write("this is tab 1")
    # tab2.write("this is tab 2")




#g = Graph()
#g.build_graph("data.csv", 1)

#st.write("Graph built successfully!")

#run streamlit run app.py in terminal
