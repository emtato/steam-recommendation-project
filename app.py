# Description: This piethon file contains the UI for the project. Here we are using streamlit.
# Run locally: install streamlit and run shell command
# View finished product: https://emtato.streamlit.app (not as up to date if not completed)
# WARNING: for the app to function, please use streamlit version 1.43.2
# Created by Emilia on 2025-03-25

import streamlit as st
import main
from main import random_selection

# states 0: get data occurence frequency, 1: categories, 2: genres, 3: cost, 4: language, 5: first game pick page
# 6: probably full filter and next game picks menu
col1, col2 = st.columns([1, 1])  # or adjust the ratio like [2, 1] if you want left side bigger


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

    Made by Emilia 🐱, Amanda 🦆, Nicole 🐔 & Grace 🐸

    Click the button below 🔘👇 to get started 🚀🎉🎯
    """)

    if st.button("Start"):
        st.balloons()
        st.session_state["prestart"] = True
        st.session_state['start'] = 0.5
        st.rerun()
    if st.button("im feeling lucky (dont sue us)"):
        st.session_state['start'] = 2
        st.session_state['prestart'] = False
        st.session_state['skip'] = False
        st.session_state[0] = False
        st.session_state[1] = False
        st.session_state[2] = False
        st.session_state[3] = False
        st.session_state[4] = False
        st.session_state[5] = False
        st.session_state[6] = False
        st.session_state[69] = True
        st.rerun()


def password():
    """test function to skip setup and reach the end"""
    password = st.text_input("password please")
    if password and 'e>a' in password:
        st.session_state['start'] = 2
        st.session_state['prestart'] = False
        st.session_state['skip'] = False
        st.session_state[0] = False
        st.session_state[1] = False
        st.session_state[2] = False
        st.session_state[3] = False
        st.session_state[4] = False
        st.session_state[5] = False
        st.session_state[6] = True
        st.rerun()


def prestart():
    """informs user about wide mode"""
    with col1:
        if st.button('no'):
            for i in range(0, 30):
                st.write("ḥ̸̨̧̗̮̖̽̂̓̀̍̋͋́̅̃͘͜͝ŏ̸̡̼̺̫̥̻͈̞̍͆̏̓́͜͝ͅẃ̸̝̝̰͋͒ "
                         "d̶̡̲̗̼̮̤̤̳̲͖͓͍͔͓̓̎̽́̽̏̐͂̆͆͘͘͘ǎ̴̯̀͠r̵̡͕͈͚͍͍̼͕̍̀̈́̽̎̍͗̍́̏̚͜͠ë̸͓̮͉͈͇͍̖͎̩̞͈́́́̋̇̾͋̈́̾͆͑͘͘͜͠͝ "
                         "y̶͔͗ŏ̸̡̼̺̫̥̻͈̞̍͆̏̓́͜͝ͅu̷̬̩̰̫͕̘͎̔́̃̄̍͋̓")
                st.write(' ')
                st.write(' ')
            st.write('you will pay.')
            st.stop()
        if st.button('skip'):
            st.session_state['prestart'] = False
            st.session_state['skip'] = True
            st.rerun()
    with col2:
        st.markdown("<div style='text-align: right;'>Psst, click the 3 dots, ---------------------------------------> "
                    "settings and activate <strong>W I D E</strong> "
                    "mode for a better viewing experience!</div>", unsafe_allow_html=True)
        if st.button('oki'):
            st.session_state['start'] = 1
            st.session_state['skip'] = False
            st.session_state['prestart'] = False
            st.rerun()
        st.write("if youre on mobile, we hate you")


def pc_req_page():
    """
    A page that lets the user choose their type of computer.
    1 OPTION TEST
    """
    st.title("Choosing your pc requirements")
    option_comp = st.selectbox("What type of computer do you have?", (
        "Window (ew)", "Mac", "Linux"), index=None, placeholder="-", )

    # st.write("You selected:", option)
    st.session_state["results"] = [option_comp]
    if option_comp == "Window (ew)":
        window_page()
    elif option_comp == "Mac":
        mac_page()
    elif option_comp == "Linux":
        linux_page()  # st.write("You chose: " + results.pop())  # game_genre_page()
    st.write(' ')
    st.write(' ')
    if st.button('back', key="back from page 1"):
        st.session_state['start'] = 0
        st.rerun()


def window_page():
    """"""
    st.write('To whoever who stole my Microsoft Office copy, I will find you..')
    st.write('You have my Word.')
    option_OS = st.selectbox("What Windows (ew) OS version do you use?", (
        "Windows 11", "Windows 10", "Windows 7"), index=None, placeholder="-", )
    option_RAM = st.selectbox("How much RAM does your computer "
                              "have?", ("8GB", "16GB", "32GB", "32GB+"), index=None, placeholder="-", )

    option_STORAGE = st.text_input("How much storage do you have? (put in GB):")  # DONT FORGET TO RESTRICT TO
    if option_STORAGE.isdigit():

        if option_OS and option_RAM and option_STORAGE and st.button('hi'):
            st.session_state[0] = True
            st.session_state['start'] = 2

            st.session_state["results"].append("OS: " + str(option_OS))
            st.session_state["results"].append("RAM: " + str(option_RAM))
            st.session_state["results"].append("STORAGE (GB): " + str(option_STORAGE))

            st.rerun()

    elif option_STORAGE != "":
        st.warning('the hell ya think yer doin mate that aint no **int**')


def mac_page():
    """"""
    st.write('Wwy should you never fart in an Apple store becuause they dnt have any windows BAHJJHHJSBFADJ')
    option_OS = st.selectbox("What Mac OS version do you use?", ("Big Sur", "Monterey", "Ventura", "Sonoma", "Sequoia"),

                             # May have to replace this with a POSSIBLE OS list from data
                             index=None, placeholder="-", )
    option_RAM = st.selectbox("How much RAM does your computer have?", (
        "8GB", "16GB", "18GB", "32GB+"), index=None, placeholder="-", )
    option_STORAGE = st.text_input("How much storage do you have? (put in GB):")
    if option_STORAGE.isdigit():

        if option_OS and option_RAM and option_STORAGE and st.button('hi'):
            st.session_state[0] = True
            st.session_state['start'] = 2

            st.session_state["results"].append("OS: " + str(option_OS))
            st.session_state["results"].append("RAM: " + str(option_RAM))
            st.session_state["results"].append("STORAGE (GB): " + str(option_STORAGE))

            st.rerun()
    elif option_STORAGE != "":
        st.warning('the hell ya think yer doin mate that aint no **int**')


def linux_page():
    """"""
    st.write('computers are like air conditioners—they stop working properly if you open windows')
    option_OS = st.selectbox("What Linux OS version do you use?", (
        "isert"),  # May have to replace this with a POSSIBLE OS list from data
                             index=None, placeholder="-", )
    option_RAM = st.selectbox("How much RAM does your computer have?", (
        "8GB", "16GB", "32GB", "32GB+"), index=None, placeholder="-", )
    option_STORAGE = st.text_input("How much storage do you have? (put in GB):")  # DONT FORGET TO RESTRICT TO  #  #
    if option_STORAGE.isdigit():

        if option_OS and option_RAM and option_STORAGE and st.button('hi'):
            st.session_state[0] = True
            st.session_state['start'] = 2

            st.session_state["results"].append("OS: " + str(option_OS))
            st.session_state["results"].append("RAM: " + str(option_RAM))
            st.session_state["results"].append("STORAGE (GB): " + str(option_STORAGE))

            st.rerun()
    elif option_STORAGE != "":
        st.warning('the hell ya think yer doin mate that aint no **int**')


def get_data():
    cat, gen, lang = main.extract_freq('data.csv', 9), main.extract_freq('data.csv', 10), main.extract_freq(
        'data.csv', 4)
    st.session_state['cat'] = cat
    gen = [one for one in gen if one != 'mac' and one != 'windows' and one != 'linux']
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

    selected = st.selectbox("Choose categories okay",
                            st.session_state['cat'], index=None, placeholder='I AM GOING CUCKOO')
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

    st.write(' ')
    st.write(' ')
    if st.button('back', key='back from page 3'):
        st.session_state['start'] = True
        st.session_state[1] = False
        st.rerun()


def game_genre_page():
    st.title('hi')
    st.write('pick gaming stuff :DD | currently chosen game genres:')

    if 'chosen_genres' not in st.session_state:
        st.session_state['chosen_genres'] = []  # list of sleected genres ^•ω•^

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
    st.write(' ')
    st.write(' ')
    if st.button('back', key='back from page 4'):
        st.session_state[1] = True
        st.session_state[2] = False
        st.rerun()


def brokeness_level():
    st.title('bald')
    selected = st.selectbox("how broke are u be fr", (
        "free plz", "≤10$", "≤25$", "my dad works at roblox"), index=None, placeholder='im hungry')

    if st.button("next"):
        st.session_state[3] = False
        st.session_state[4] = True

        st.session_state["results"].append(selected)
        st.rerun()

    st.write(' ')
    st.write(' ')
    if st.button('back', key='back from page 5'):
        st.session_state[2] = True
        st.session_state[3] = False
        st.rerun()


def lnaugeg():
    if 'chosen_lang' not in st.session_state:
        st.session_state['chosen_lang'] = []  # list of sleected lanusggage ^•ω•^

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
    st.write(' ')
    st.write(' ')
    if st.button('back', key='back from page 6'):
        st.session_state[3] = True
        st.session_state[4] = False
        st.rerun()


def first_pick():
    """
       A page that shows the results the user chose, aka the options.
       """
    st.title('zaza')
    st.write(str(st.session_state["results"]))
    with open('scrolly.html', 'r') as f:
        hrml = f.read()
        # input first game rec cycle games here

        gamers = [f"Game {i}" for i in range(30)]  # placeholder

        # games = [format_game(game) for game in gamers] doesnt work when placeholder doesnt work
        games = gamers
        htmlformatted = '<br>'.join(games)
        final_html = hrml.replace("<!-- placeholder-->", htmlformatted)
        with open('scrolly.css') as fe:
            css = f"<style>{fe.read()}</style>"
            st.markdown(css, unsafe_allow_html=True)
        st.markdown(final_html, unsafe_allow_html=True)

    if st.button("choose game (temp button to get to next page)"):
        st.session_state[5] = False
        st.session_state[6] = True
        st.rerun()
    st.write(' ')
    st.write(' ')

    if st.button('back', key='back from page 7'):
        st.session_state[3] = True
        st.session_state[4] = False
        st.rerun()


def final_page():
    # function i can use later to split by the middle right side is the box left side filters!!
    st.title('additional recommendations :3')
    st.write(" ")
    suggestions = []
    graph = main.load_graph('data.csv')
    coll1, coll2 = st.columns([1, 2])
    with coll1:
        st.markdown("Assign weights to what you think is most important when comparing game similarities. "
                    "Assign a weight of <strong><u>100</u></strong> if you think the condition is critically "
                    "important when "
                    "sorting, and <strong><u>0</u></strong> if its not important at all.", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1, 1])  # can add more columns
        # weights: price, language, dev, platform, category, genre
        with col1:
            price = int(st.text_input('price', key='price'))
            platform =  int(st.text_input('platform', key='platform'))
        with col2:
            languages =  int(st.text_input('language', key='language'))
            category =  int(st.text_input('category', key='category'))

        with col3:
            dev =  int(st.text_input('dev', key='dev'))
            genre =  int(st.text_input('genre', key='genre'))
        if st.button("make  grpah !!"):
            # call make graph function
            graph.clear_edges()
            st.write({type(price)}, price)
            graph.build_edges([price, languages, dev, platform, category, genre])
            suggestions = graph.recommend_games(1291170, 30)
    with coll2:
        st.write('recommended games according to weights. click on image for link')
        if suggestions != []:
            with open('scrolly.html', 'r') as f:
                hrml = f.read()

                games = [format_game(game) for game in suggestions]
                htmlformatted = '<br>'.join(games)
                final_html = hrml.replace("<!-- placeholder-->", htmlformatted)
                with open('scrolly.css') as fe:
                    css = f"<style>{fe.read()}</style>"
                    st.markdown(css, unsafe_allow_html=True)
                st.markdown(final_html, unsafe_allow_html=True)
            st.write(' ')
            st.write(' ')
        else:
            st.markdown(""" <span style = "color:red"> No data</span>""", unsafe_allow_html=True)

    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")

    if st.button('back', key='back from final page'):
        st.session_state[5] = True
        st.session_state[6] = False
        st.rerun()


def contains_cjk(text):
    for char in text:
        code = ord(char)
        if (
                0x4E00 <= code <= 0x9FFF or 0x3400 <= code <= 0x4DBF or 0x3040 <= code <= 0x309F or 0x30A0 <= code <=
                0x30FF or 0xAC00 <= code <= 0xD7AF):
            return True
    return False


def format_game(game):
    spacesname, spacesprice = 70, 20

    name = game[1].strip("'")

    if len(name) > 55:
        name = name[:55] + '...'
    if contains_cjk(name):
        spacesname = int(spacesname / 1.15)
    spacesname -= len(name)
    price = f"${float(game[2]):.2f}" if game[2] != 'unknown' else 'idk :('
    spacesprice -= len(price)
    genre = ', '.join(game[5]) if isinstance(game[5], list) else 'im lost too okay :('
    image = game[4]
    paddingname = '&nbsp;' * max(1, spacesname)  # force html to keep the spacing
    paddingprice = '&nbsp;' * max(1, spacesprice)

    return (f"<a href=\"https://google.com/search?q={name}\"><img src={image}></a><div style='font-family: monospace; "
            f"white-space: nowrap; font-size: 13px;'>{name}</a>"
            f"{paddingname}{price}{paddingprice}{genre}<div>")


def RANDOM_SELECT():
    gamers = random_selection()
    with open('scrolly.html', 'r') as f:
        hrml = f.read()
        st.write('recommended games according to weights. click on image for link')
        games = [format_game(game) for game in gamers]
        htmlformatted = '<br>'.join(games)
        final_html = hrml.replace("<!-- placeholder-->", htmlformatted)
        with open('scrolly.css') as fe:
            css = f"<style>{fe.read()}</style>"
            st.markdown(css, unsafe_allow_html=True)
        st.markdown(final_html, unsafe_allow_html=True)
    st.write(' ')
    st.write(' ')
    if st.button('back', key='back from page 69'):
        st.session_state['start'] = 0
        st.session_state[69] = False
        st.rerun()

    # this section checks the session_state and loads the next page, this is to prevent the app's   #  # cache from
    # maxing  # and  # restarting the app, making the user lose progress.


if 'start' not in st.session_state or st.session_state['start'] == 0:
    start_page()
elif st.session_state['prestart']:
    prestart()
elif st.session_state['skip']:
    password()
elif st.session_state['start'] == 1:
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
    first_pick()
elif st.session_state[6]:
    final_page()

elif st.session_state[69]:
    RANDOM_SELECT()

# The code below creates tabs! We can use this to show the results later  #   # tab1,
# tab2 = st.tabs(["Tab 1", "Tab2"])  # tab1.write("this is tab 1")  # tab2.write("this is tab 2")

# g = Graph()
# g.build_graph("data.csv", 1)

# st.write("Graph built successfully!")

# run streamlit run app.py in terminal
