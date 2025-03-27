# Description:
# Description: This python file contains the UI for the project. Here we are using streamlit. You'll need to download
# the streamlit library and follow the directions in the guide to utilize this.
# WARNING: for the app to function, please use streamlit version 1.43.2
# Or if you'd like use: emtato.streamlit.app in your browser to utilize the app that way.
# Created by Emilia on 2025-03-25

import streamlit as st
import main


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
    st.session_state["results"] = [option_comp]
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

            st.session_state["results"].append(option_OS)
            st.session_state["results"].append(option_RAM)
            st.session_state["results"].append(option_STORAGE)

            st.rerun()

    elif option_STORAGE != "":
        st.warning('the hell ya think yer doin mate that aint no **int**')


def mac_page():
    """"""
    option_OS = st.selectbox("What Mac OS version do you use?", ("Big Sur", "Monterey", "Ventura", "Sonoma", "Sequoia"),

                             # May have to replace this with a POSSIBLE OS list from data
                             index=None, placeholder="-", )
    option_RAM = st.selectbox("How much RAM does your computer have?", ("8GB", "16GB", "18GB", "32GB+"),
                              # May have to replace this with a POSSIBLE RAM list from data
                              index=None, placeholder="-", )
    option_STORAGE = st.text_input("How much storage do you have? (put in GB):")
    if option_STORAGE.isdigit():

        if option_OS and option_RAM and option_STORAGE and st.button('hi'):
            st.session_state[0] = True
            st.session_state['start'] = False

            st.session_state["results"].append(option_OS)
            st.session_state["results"].append(option_RAM)
            st.session_state["results"].append(option_STORAGE)

            st.rerun()
    elif option_STORAGE != "":
        st.warning('the hell ya think yer doin mate that aint no **int**')


def linux_page():
    """"""
    option_OS = st.selectbox("What Linux OS version do you use?", ("isert"),
                             # May have to replace this with a POSSIBLE OS list from data
                             index=None, placeholder="-", )
    option_RAM = st.selectbox("How much RAM does your computer have?", ("8GB", "16GB", "32GB", "32GB+"),
                              # May have to replace this with a POSSIBLE RAM list from data
                              index=None, placeholder="-", )
    option_STORAGE = st.text_input("How much storage do you have? (put in GB):")  # DONT FORGET TO RESTRICT TO  #  #
    if option_STORAGE.isdigit():

        if option_OS and option_RAM and option_STORAGE and st.button('hi'):
            st.session_state[0] = True
            st.session_state['start'] = False

            st.session_state["results"].append(option_OS)
            st.session_state["results"].append(option_RAM)
            st.session_state["results"].append(option_STORAGE)

            st.rerun()
    elif option_STORAGE != "":
        st.warning('the hell ya think yer doin mate that aint no **int**')


def get_data():
    cat, gen, lang = main.extract_freq('data.csv', 9), main.extract_freq('data.csv', 10), main.extract_freq('data.csv',
                                                                                                            4)
    st.session_state['cat'] = cat
    st.session_state['gen'] = gen
    st.session_state['lang'] = lang
    st.session_state[0], st.session_state[1] = False, True
    st.session_state['undo_pressed'] = False
    st.rerun()


def category_pick():
    st.title('hi')
    st.write('pick gaming stuff :DD | currently chosen categories:')

    if 'chosen_cat' not in st.session_state:
        st.session_state['chosen_cat'] = []  # list of sleected categories ^•ω•^

    st.write(' | '.join(st.session_state['chosen_cat']))

    selected = st.selectbox("Choose categories okay", st.session_state['cat'], index=None,
                            placeholder='I AM GOING CUCKOO')
    if st.button("undo select"):
        st.session_state["undo_pressed"] = True
        if len(st.session_state['chosen_cat']) > 0:
            st.session_state['chosen_cat'].pop()
            st.rerun()
    if selected and selected not in st.session_state['chosen_cat'] and not st.session_state['undo_pressed']:
        st.session_state['chosen_cat'].append(selected)
        st.rerun()
    st.session_state['undo_pressed'] = False

    if st.button("submmit"):
        st.session_state[1] = False
        st.session_state[2] = True

        st.session_state["results"].append("CATEGORIES:" + str(st.session_state['chosen_cat']))

        st.rerun()


def game_genre_page():
    st.title('hi')
    st.write('pick gaming stuff :DD | currently chosen game genres:')

    if 'chosen_genres' not in st.session_state:
        st.session_state['chosen_genres'] = []  # list of sleected categories ^•ω•^

    st.write(' | '.join(st.session_state['chosen_genres']))

    selected = st.selectbox("Choose genres okay", st.session_state['gen'], index=None, placeholder='I AM GOING CUCKOO')
    if st.button("undo select"):
        st.session_state["undo_pressed"] = True
        if len(st.session_state['chosen_genres']) > 0:
            st.session_state['chosen_genres'].pop()
            st.rerun()
    if selected and selected not in st.session_state['chosen_genres'] and not st.session_state['undo_pressed']:
        st.session_state['chosen_genres'].append(selected)
        st.rerun()
    st.session_state['undo_pressed'] = False

    if st.button("submmit"):
        st.session_state[2] = False
        st.session_state[3] = True

        st.session_state["results"].append("GENRES: " + str(st.session_state['chosen_genres']))

        st.rerun()

    st.title("")


def brokeness_level():
    st.title('bald')
    selected = st.selectbox("lmk how broke u are", ("free plz", "≤10$", "≤25$", "my dad works at roblox"), index=None,
                            placeholder='im hungry')

    temp = "next"
    if st.button("next"):
        st.session_state[3] = False
        st.session_state[4] = True

        st.session_state["results"].append(selected)

        st.rerun()


def lnaugeg():
    if 'chosen_lang' not in st.session_state:
        st.session_state['chosen_lang'] = []  # list of sleected categories ^•ω•^

    st.write(' | '.join(st.session_state['chosen_lang']))

    selected = st.selectbox("blipblop bloop", st.session_state['lang'], index=None, placeholder='hai')
    if st.button("undo select"):
        st.session_state["undo_pressed"] = True
        if len(st.session_state['chosen_lang']) > 0:
            st.session_state['chosen_lang'].pop()
            st.rerun()
    if selected and selected not in st.session_state['chosen_lang'] and not st.session_state['undo_pressed']:
        st.session_state['chosen_lang'].append(selected)
        st.rerun()
    st.session_state['undo_pressed'] = False

    if st.button("submmit"):
        st.session_state[4] = False
        st.session_state[5] = True

        st.session_state["results"].append("LANGUAGES: " + str(st.session_state['chosen_lang']))

        st.rerun()


def final_page():
    """
    A page that shows the results the user chose, aka the options.
    """
    st.write('zaza')
    st.write(str(st.session_state["results"]))

    with open('scrolly.html','r') as f:
        hrml = f.read()

        games = [f"Game {i}" for i in range(30)] #placeholder
        games = [f'{game}<br>' for game in games] #add image display later
        htmlformatted = ''.join(games)
        final_html = hrml.replace("<!-- placeholder-->", htmlformatted)
        with open('scrolly.css') as fe:
            css =f"<style>{fe.read()}</style>"
            st.markdown(css, unsafe_allow_html=True)
        st.markdown(final_html,unsafe_allow_html=True)




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
    brokeness_level()
elif st.session_state[4]:
    lnaugeg()
elif st.session_state[5]:
    final_page()  # The code below creates tabs! We can use this to show the results later  #   # tab1,
    # tab2 = st.tabs(["Tab 1", "Tab2"])  # tab1.write("this is tab 1")  # tab2.write("this is tab 2")

# g = Graph()
# g.build_graph("data.csv", 1)

# st.write("Graph built successfully!")

# run streamlit run app.py in terminal
