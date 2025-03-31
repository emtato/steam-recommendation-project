"""# Description: This piethon file contains the UI for the project. Here we are using streamlit.
# Run locally: install streamlit and run shell command
# View finished product: https://emtato.streamlit.app (not as up to date if not completed)
# WARNING: for the app to function, please use streamlit version 1.43.2
# Created by Emilia, Amanda, Nicole, Grace on 2025-03-25
"""

import streamlit as st
import main
from main import random_selection

col1, col2 = st.columns([1, 1])  # or adjust the ratio like [2, 1] if you want left side bigger
# necessary code! ignore python ta


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
        st.session_state[7] = False
        st.session_state[69] = True
        st.rerun()


def password():
    """test function to skip setup and reach the end"""
    password = st.text_input("password please")
    st.session_state['chosen'] = password
    if password:
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
        # st.write("if youre on mobile, we hate you")


def pc_req_page():
    """
    A page that lets the user choose their type of computer.
    """
    st.title("Choosing your pc requirements")
    option_comp = st.selectbox("What type of computer do you have?", (
        "Windows", "Mac", "Linux"), index=None, placeholder="-", )

    # st.write("You selected:", option)
    st.session_state["results"] = {"COMPUTER": option_comp}
    if option_comp == "Windows":
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
    """
    This page lets the user specify their windows computer's attributes,
    """
    st.write('To whomever stole my Microsoft Office copy, I will find you..')
    st.write('You have my Word.')
    option_OS = st.selectbox("What Windows OS version do you use?", (
        "Windows 11", "Windows 10", "Windows 8", "Windows 7", "Windows Vista",
        "Windows XP"), index=None, placeholder="-", )

    option_RAM = st.text_input("How much Memory (RAM) do you have? (in GB):")

    option_STORAGE = st.text_input("How much storage do you have available? (in GB): ")
    if option_STORAGE.isdigit():

        if option_OS and option_RAM and option_STORAGE and st.button('next'):
            st.session_state[0] = True
            st.session_state['start'] = 2

            res = st.session_state["results"]
            res["OS"] = str(option_OS)
            # res["RAM"] = [option_RAM, option_RAM_TYPE]
            res["RAM"] = [option_RAM]
            res["STORAGE"] = [option_STORAGE, 'GB']

            st.rerun()

    elif option_STORAGE != "":
        st.warning('HEY! That aint no **int**')


def mac_page():
    """
    This page lets the user specify their mac computer's attributes,
    """
    st.write('Why should you never fart in an Apple store? Because they don\'t have any windows BAHJJHHJSBFADJ')
    option_OS = st.selectbox("What Mac OS version do you use?", (
        "11 and below", "12", "13", "14", "15"), index=None, placeholder="-", )

    option_RAM = st.text_input("How much Memory (RAM) do you have? (in GB):")

    option_STORAGE = st.text_input("How much storage do you have available? (in GB):")
    if option_STORAGE.isdigit():

        if option_OS and option_RAM and option_STORAGE and st.button('next'):
            st.session_state[0] = True
            st.session_state['start'] = 2

            res = st.session_state["results"]
            res["OS"] = str(option_OS)
            res["RAM"] = [option_RAM]
            res["STORAGE"] = [option_STORAGE, 'GB']

            st.rerun()
    elif option_STORAGE != "":
        st.warning('HEY! That aint no **int**')


def linux_page():
    """
    This page lets the user specify their linux computer's attributes,
    """
    st.write('Computers are like air conditioners—they stop working properly if you open windows')
    option_OS = st.selectbox("What Linux OS version do you use?", (
        "Ubuntu 12", "Ubuntu 14", "Ubuntu 16", "Ubuntu 18", "Ubuntu 20", "Ubuntu 22",
        "SteamOS"), index=None, placeholder="-", )
    option_RAM = st.text_input("How much Memory (RAM) do you have? (in GB):")

    option_STORAGE = st.text_input("How much storage do you have available? (in GB):")

    if option_STORAGE.isdigit():

        if option_OS and option_RAM and option_STORAGE and st.button('next'):
            st.session_state[0] = True
            st.session_state['start'] = 2

            res = st.session_state["results"]
            res["OS"] = str(option_OS)
            res["RAM"] = [option_RAM]
            res["STORAGE"] = [option_STORAGE, 'GB']

            st.rerun()
    elif option_STORAGE != "":
        st.warning('HEY! That aint no **int**')


def get_data():
    """
    gets the data from the data.csv file
    """
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
    """
    This page lets the user pick their desired categories
    """
    st.title('Category pick: (remember you don\'t have to chose anything, and can leave this blank)')
    st.write('What categories are you interested in? | currently chosen categories:')

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

        st.session_state["results"]["CATEGORIES"] = st.session_state['chosen_cat']

        st.rerun()

    st.write(' ')
    st.write(' ')
    if st.button('back', key='back from page 3'):
        st.session_state['start'] = True
        st.session_state[1] = False
        st.rerun()


def game_genre_page():
    """
    This page lets the user pick the genres they want for their game recommendation
    """
    st.title('Genre pick: (remember you don\'t have to chose anything, and can leave this blank)')
    st.write('What type of genres are you into? | currently chosen game genres:')

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

    if st.button("submit"):
        st.session_state[2] = False
        st.session_state[3] = True

        st.session_state["results"]["GENRES"] = st.session_state['chosen_genres']

        st.rerun()
    st.write(' ')
    st.write(' ')
    if st.button('back', key='back from page 4'):
        st.session_state[1] = True
        st.session_state[2] = False
        st.rerun()


def brokeness_level():
    """
    This sections asks the user for a MAXIMUM (inclusive) price in CAD
    """
    st.title('Price? (please write your MAX (inclusive) price in CAD)')
    selected = st.text_input("How much are you willing to pay? (input 0 for Free)")

    if selected.isdigit() or selected == '':
        if st.button("next"):
            st.session_state[3] = False
            st.session_state[4] = True

            if selected.isdigit():
                st.session_state["results"]["PRICE"] = float(selected)
            else:
                st.session_state["results"]["PRICE"] = 1e9
            st.rerun()

        st.write(' ')
        st.write(' ')
        if st.button('back', key='back from page 5'):
            st.session_state[2] = True
            st.session_state[3] = False
            st.rerun()
    else:
        st.warning("Price must be an INTEGER! :)")


def lnaugeg():
    """
    Allows the user to specify what language(s) they want the game to be in.
    """
    if 'chosen_lang' not in st.session_state:
        st.session_state['chosen_lang'] = []  # list of sleected lanusggage ^•ω•^

    st.title("Language?")
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

    if st.button("submit"):
        st.session_state[4] = False
        st.session_state[5] = True

        st.session_state["results"]["LANGUAGES"] = st.session_state['chosen_lang']
        st.rerun()
    st.write(' ')
    st.write(' ')
    if st.button('back', key='back from page 6'):
        st.session_state[3] = True
        st.session_state[4] = False
        st.rerun()


def selection_box(text: str, gamers: list) -> int:
    selectbox_list = ['-'] + [f'{i + 1}. {gamers[i][1]}' for i in range(len(gamers))]
    chosen_index = st.selectbox(text, selectbox_list, key='unique2')
    if chosen_index and chosen_index != '-':
        chosen_index = chosen_index.split('.')[0]
        if chosen_index.isdigit():
            chosen_index = int(chosen_index) - 1
            if 0 <= chosen_index < len(gamers):
                game_id = gamers[chosen_index][0]
                st.session_state['chosen'] = (game_id, gamers[chosen_index][1])
        return chosen_index


def first_pick():
    """
       A page that shows the results the user chose, aka the options.
       """
    st.title('Here are the possible options for games that exactly match your requirements!')
    # st.write(str(st.session_state["results"]))
    # st.write(main.filtering_games('data.csv', st.session_state["results"]))
    gamers = main.filtering_games('data.csv', st.session_state["results"])
    gamers = [[g.id, g.name, g.price['final'] if g.price and 'final' in g.price else 'unknown', g.description, g.image,
               g.genres] for g in gamers]

    if 'gamers_list' not in st.session_state or st.session_state['gamers_list'] is None:
        st.session_state['gamers_list'] = gamers
    if len(gamers) > 0:
        col1, col2 = st.columns([1, 4])
        with col1:
            chosen_index = selection_box("select game", gamers)
            if chosen_index is not None:
                st.session_state[6] = True
                st.session_state[5] = False
                # st.session_state['start'] = 3
                if 'list' not in st.session_state or not st.session_state['list']:
                    st.session_state['list'] = [gamers[chosen_index]]
                elif gamers[chosen_index] not in st.session_state['list']:
                    st.session_state['list'].append(gamers[chosen_index])
                st.rerun()

        with col2:

            with open('scrolly.html', 'r') as f:
                hrml = f.read()
                games = [format_game(game, 'img') for game in gamers]
                htmlformatted = '<ol>' + ''.join(f"<li>{game}</li>" for game in games) + '</ol>'
                final_html = hrml.replace("<!-- placeholder-->", htmlformatted)
                with open('scrolly.css') as fe:
                    css = f"<style>{fe.read()}</style>"
                    st.markdown(css, unsafe_allow_html=True)
                st.markdown(final_html, unsafe_allow_html=True)
    else:
        st.write("we cuwuldnt find any games :<< sowwy!")

    if st.button('back', key='back from page 7'):
        st.session_state[4] = True
        st.session_state[5] = False
        st.session_state['gamers_list'] = None
        st.rerun()


def list_choser(suggestions):
    selectbox_list = ['-'] + [f'{i + 1}. {suggestions[i][1]}' for i in range(len(suggestions))]
    help = ('Adding a game to your list will help better personalize your future recommendations (maybe), and you’ll '
            'be able to view your list of chosen games whenever you want.')
    if 'select_index' in st.session_state:

        chosen_index = st.selectbox("add game to your list?", selectbox_list, key='aasa', help=help, index=0)
        del st.session_state['select_index']
    else:
        chosen_index = st.selectbox("add game to your list?", selectbox_list, key='asaa', help=help)
    if chosen_index and chosen_index != '-':
        chosen_index = chosen_index[:2]
        if chosen_index[1] == '.':
            chosen_index = chosen_index[:1]
        chosen_index = int(chosen_index) - 1
        if 'list' not in st.session_state or not st.session_state['list']:
            st.session_state['list'] = [suggestions[chosen_index]]
            st.rerun()
        elif suggestions[chosen_index] not in st.session_state['list']:
            st.session_state['list'].append(suggestions[chosen_index])
            st.rerun()


def final_page():
    # function i can use later to split by the middle right side is the box left side filters!!
    st.title('additional recommendations :3')
    st.write(" ")
    suggestions = []

    if 'suggestions' in st.session_state:
        suggestions = st.session_state['suggestions']

    graph = main.load_graph('data.csv')

    chosen = st.session_state['chosen']
    chosen = int(chosen[0]) if type(chosen) == tuple else int(chosen)  # only for testing (with skip button)

    coll1, coll2 = st.columns([1, 2])
    with coll1:
        st.markdown("Assign weights to what you think is most important when comparing game similarities. "
                    "Assign a weight of <strong><u>100</u></strong> if you think the condition is critically "
                    "important when "
                    "sorting, and <strong><u>0</u></strong> if its not important at all.", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1, 1])  # can add more columns
        # weights: price, language, dev, platform, category, genre
        with col1:
            price = st.text_input('price', help="For example, if you chose a free game and set the price weight to "
                                                "100, the system will strongly favor other free games. Higher weights "
                                                "mean more importance is given to how similar that feature is to your "
                                                "chosen game—like language, platform, category, etc. Lower weights "
                                                "reduce that impact.", key='price', placeholder="0")
            price = int(price) if price.isdigit() else 10
            platform = st.text_input('platform', key='platform', placeholder="0")
            platform = int(platform) if platform.isdigit() else 10
        with col2:
            languages = st.text_input('language', key='language', placeholder="0")
            languages = int(languages) if languages.isdigit() else 10
            category = st.text_input('category', key='category', placeholder="0")
            category = int(category) if category.isdigit() else 10
        with col3:
            dev = st.text_input('dev', key='dev', placeholder="0")
            dev = int(dev) if dev.isdigit() else 10
            genre = st.text_input('genre', key='genre', placeholder="0")
            genre = int(genre) if genre.isdigit() else 10

        if st.button("make  grpah !!"):
            st.write('working on it— may take up to 30s if you\'re on x86 (or this code is running on cloud) (no '
                     'unified memory L </3)')
            graph.clear_edges()  # modify this to account for multiple games if want
            graph.build_edges([price, languages, dev, platform, category, genre])
            suggestions = graph.recommend_games([int(game[0]) for game in st.session_state['list']], 50)

            suggestions = [[s.id, s.name, s.price['final'] if s.price is not None and 'final' in s.price else 'unknown',
                            s.description, s.image, s.genres] for s in suggestions]
            st.session_state['suggestions'] = suggestions
            st.write(" ")
            st.write(" ")

        if 'suggestions' in st.session_state:
            list_choser(suggestions)

        st.write(" ")
        st.write(" ")
        if st.button('back', key='back from final page'):
            st.session_state[6] = False
            if 'suggestions' in st.session_state:
                del st.session_state['suggestions']
            if st.session_state['start'] == 3:
                st.session_state[7] = False
                st.session_state[69] = True
            else:
                st.session_state[5] = True
            st.rerun()
    with coll2:
        st.write('recommended games according to weights. click on image for link')
        if suggestions != []:
            with open('scrolly.html', 'r') as f:
                hrml = f.read()

                games = [format_game(game, 'img') for game in suggestions]
                htmlformatted = '<ol>' + ''.join(f"<li>{game}</li>" for game in games) + '</ol>'
                final_html = hrml.replace("<!-- placeholder-->", htmlformatted)
                with open('scrolly.css') as fe:
                    css = f"<style>{fe.read()}</style>"
                    st.markdown(css, unsafe_allow_html=True)
                st.markdown(final_html, unsafe_allow_html=True)
            st.write(' ')
            st.write(' ')
        else:
            st.markdown(""" <span style = "color:red"> No data</span>""", unsafe_allow_html=True)

    if 'list' in st.session_state:
        with open('scrolly2.html', 'r') as f:
            hrml = f.read()
            st.write('your currnt list!!')

            games = [format_game(game, 'img-small') for game in st.session_state['list']]
            htmlformatted = '<ol>' + ''.join(f"<li>{game}</li>" for game in games) + '</ol>'
            final_html = hrml.replace("<!-- placeholder-->", htmlformatted)
            with open('scrolly2.css') as fe:
                css = f"<style>{fe.read()}</style>"
                st.markdown(css, unsafe_allow_html=True)
            st.markdown(final_html, unsafe_allow_html=True)
        col1, col2, c3 = st.columns([1, 1, 2])
        with col1:
            if st.button('remove last item') and len(st.session_state['list']) > 0:
                st.session_state['select_index'] = 0
                st.session_state['list'].pop()
                st.rerun()
        with col2:
            chosen_index = selection_box('more info about game?', st.session_state['list'])
            if chosen_index is not None:
                st.session_state[6] = False
                st.session_state[7] = True
                st.session_state['more'] = st.session_state['list'][chosen_index]
                st.rerun()


def more_info():
    st.title('More Info:')
    st.write(st.session_state['more'])
    if st.button('back', key='back from info page'):
        st.session_state[7] = False
        st.session_state[6] = True
        st.rerun()


def contains_cjk(text):
    for char in text:
        code = ord(char)
        if (
                0x4E00 <= code <= 0x9FFF or 0x3400 <= code <= 0x4DBF or 0x3040 <= code <= 0x309F or 0x30A0 <= code <=
                0x30FF or 0xAC00 <= code <= 0xD7AF):
            return True
    return False


def format_game(game: list, img: str):
    spacesname, spacesprice = 70, 20
    name = game[1].strip("'")
    nocrop = name
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

    return (f"<a href=\"https://google.com/search?q={nocrop}+steam+{game[0]}\">"
            f"<img src=\"{image}\" alt=\"{name}\" class=\"{img}\"/>"
            f"</a>"
            f"<div style='font-family: monospace; white-space: nowrap; font-size: 13px;'>"
            f"{name}{paddingname}{price}{paddingprice}{genre}"
            f"</div>")


def RANDOM_SELECT():
    if 'gamers_list' not in st.session_state or st.session_state['gamers_list'] is None:
        st.session_state['gamers_list'] = random_selection()
    gamers = st.session_state['gamers_list']
    col1, col2 = st.columns([1, 4])

    with col1:
        chosen_index = selection_box("select game", gamers)
        if chosen_index is not None:
            st.session_state[6] = True
            st.session_state[69] = False
            st.session_state['start'] = 3
            if 'list' not in st.session_state or not st.session_state['list']:
                st.session_state['list'] = [gamers[chosen_index]]
            elif gamers[chosen_index] not in st.session_state['list']:
                st.session_state['list'].append(gamers[chosen_index])
            st.rerun()

    with col2:
        with open('scrolly.html', 'r') as f:
            hrml = f.read()
            st.write('randomly recommended games. click on image for link')
            games = [format_game(game, 'img') for game in gamers]
            htmlformatted = '<ol>' + ''.join(f"<li>{game}</li>" for game in games) + '</ol>'
            final_html = hrml.replace("<!-- placeholder-->", htmlformatted)
            with open('scrolly.css') as fe:
                css = f"<style>{fe.read()}</style>"
                st.markdown(css, unsafe_allow_html=True)
            st.markdown(final_html, unsafe_allow_html=True)
        st.write(' ')
        st.write(' ')
        if st.button('back', key='back from page 69'):
            st.session_state['start'] = False
            st.session_state[69] = False
            st.session_state['gamers_list'] = None
            st.rerun()


# this section checks the session_state and loads the next page, this is to prevent the app's   #  # cache from
# maxing  # and  # restarting the app, making the user lose progress.
# AND PYTHONTA IS A LIAR, THIS IS NOT A PROBLEM BUT HOW STREAMLIT WORKS THANK YOU

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
elif st.session_state[7]:
    more_info()
elif st.session_state[69]:
    RANDOM_SELECT()
#
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
#
#     import python_ta
#     python_ta.check_all(config={
#         'extra-imports': ['streamlit', 'main'],  # the names (strs) of imported modules
#         'allowed-io': [],  # the names (strs) of functions that call print/open/input
#         'max-line-length': 120
#     })
