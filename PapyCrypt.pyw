import PySimpleGUI as sg
from PySimpleGUI import vtop, theme_previewer, theme

# ------tutta la parte grafica della finestra------

#theme_previewer()
theme('GrayGrayGray')

lunghezza_testo_1 = 0
lunghezza_testo_2 = 0
lunghezza_testo_3 = 0
lunghezza_testo_4 = 0

# -----tab encrypt-----

colonna_sinistra = [[sg.Text('Frase da Criptare')],
                    [sg.InputText(key='criptare', background_color='#ffffff', text_color='#000000', enable_events=True)],
                    [sg.Text(lunghezza_testo_1, key='lunghezza')],
                    [sg.Text('Chiave per Criptare')],
                    [sg.InputText(key='chiave', background_color='#ffffff', text_color='#000000', enable_events=True)],
                    [sg.Text(lunghezza_testo_2, key='lunghezza_2')],
                    [sg.Button('Traduci!', key='cripta')]]

colonna_destra = [[sg.Text('Frase Criptata')],
                  [sg.InputText(readonly=True, pad=((0, 0), (0, 30)), text_color='#000000', key='read', do_not_clear=False)]]

# -----tab decrypt-----

colonna_sinistra_decr = [[sg.Text('Frase da Decriptare')],
                    [sg.InputText(key='decriptare', background_color='#ffffff', text_color='#000000', enable_events=True)],
                    [sg.Text(lunghezza_testo_3, key='lunghezza_3')],
                    [sg.Text('Chiave per Decriptare')],
                    [sg.InputText(key='chiave_1', background_color='#ffffff', text_color='#000000', enable_events=True)],
                    [sg.Text(lunghezza_testo_4, key='lunghezza_4')],
                    [sg.Button('Traduci!', key='decripta')]]

colonna_destra_decr = [[sg.Text('Frase Decriptata')],
                  [sg.InputText(readonly=True, pad=((0, 0), (0, 30)), text_color='#000000', key='read_1', do_not_clear=False)]]




layout_totale = [[sg.Column(colonna_sinistra),
                  sg.VSeparator(),
                  sg.Column(colonna_destra)]]

layout_totale_decr = [[sg.Column(colonna_sinistra_decr),
                       sg.VSeparator(),
                       sg.Column(colonna_destra_decr)]]

Tabs = [[sg.TabGroup(
            [[sg.Tab('Criptare', layout_totale),
              sg.Tab('Decriptare', layout_totale_decr)]],
              tab_location='topleft')]]


finestra = sg.Window('PapyCrypter', icon=r'C:\Users\casca\Desktop\papycoima.ico', finalize=True).layout(Tabs)

# ------array vuoti da riempire con le parole------

# frase_arr è un array vuoto che verrà riempito con la list(), ovvero l'elenco di tutti i caratteri separati, della stringa di testo della casella "frase da criptare". viene riempito con frase_array = list(frase)
frase_arr = []

# chiave_array è identica a frase array, solo che interessa la casella "chiave per criptare" attualmente non implementato.
chiave_arr = []

# frase è una stringa vuota che verrà riempita con il contenuto  della casella "frase da criptare". viene riempita con frase = text.get().
frase = ''

# chiave è identica a frase, solo che interessa la casella "chiave per criptare". viene riempita con chiave = text.get()
chiave = ''

# mappa è il protagonista di questo programma. Nasce come hashmap vuota e verrà riempita con quattro for loop, dalle lettere dell'alfabeto 26 maiuscole e minuscole, i numeri da 0 a 9 e alcuni segni di punteggiatura. Sono presenti i simboli della tavola ascii dal 32 al 57, dal 65 al 90 e dal 97  al 122. tutti gli altri mancano
mappa = {}  # chiave: valore

mappa_1 = {}

# carattere per il momento è la variabile più inutile del mondo. Doveva essere un intager ed è una tupla. figurati
carattere = ()

# ascii message è una stringa che verrà riempita con tutti i valori assegnati dalla mappa. il suo valore è (str(mappa[frase_arr[i]])) riga 101
ascii_message = ''

# ascii key è identico ad ascii_message, solo che interessa la casella "chiave per tradurre"
ascii_key = ''

ascii_translated = ''

# x è una stringa vuota da inserire tra due caratteri nella casella di testo criptata
x = ''


# ------Funzioni------

def read_1():
    # text è una variabile locale
    text = finestra['criptare']
    global frase
    frase = text.get()
    return text


def read_2():
    text = finestra['chiave']
    print('godo')
    global chiave
    chiave = text.get()
    return text


def print_1():
    # text_1 è una variabile locale
    text_1 = finestra['read']
    # print(ascii_message)
    text_1.update(text_1.get() + ascii_translated)


#def print_2():
#    text_1 = finestra['read']
#   global ascii_key
#    text_1.update(text_1.get() + ascii_translated)


def read_3():
    text = finestra['decriptare']
    global frase
    frase = text.get()
    return text


def read_4():
    text = finestra['chiave_1']
    global chiave
    chiave = text.get()


def print_2():
    text_1 = finestra['read_1']
    text_1.update(text_1.get() + ascii_translated)


def lunghezza():
    lung = finestra['criptare']
    lungh = finestra['lunghezza']
    global lunghezza_testo_1
    lunghezza_testo_1 = len(lung.get())
    lungh.update(lunghezza_testo_1)


def lunghezza_1():
    lung = finestra['chiave']
    lungh = finestra['lunghezza_2']
    global lunghezza_testo_2
    lunghezza_testo_2 = len(lung.get())
    lungh.update(lunghezza_testo_2)


def lunghezza_2():
    lung = finestra['decriptare']
    lungh = finestra['lunghezza_3']
    global lunghezza_testo_3
    lunghezza_testo_3 = len(lung.get())
    lungh.update(lunghezza_testo_3)


def lunghezza_3():
    lung = finestra['chiave_1']
    lungh = finestra['lunghezza_4']
    global lunghezza_testo_4
    lunghezza_testo_4 = len(lung.get())
    lungh.update(lunghezza_testo_4)


# ------lettere maiuscole da a alla z 26 in ascii------

for i in range(65, 91):
    print(chr(i))
    # carattere = i
    mappa[chr(i)] = len(mappa) + 1
    mappa_1[len(mappa_1) + 1] = chr(i)
# print(len(mappa))

# ------lettere minuscole dalla a alla z 26 in ascii------

for i in range(97, 123):
    print(chr(i))
    # carattere = i
    mappa[chr(i)] = len(mappa) + 1
    mappa_1[len(mappa_1) + 1] = chr(i)
# print(len(mappa))

# ------numeri da 0 a 9 in ascii------


for i in range(48, 58, 1):
    print(chr(i))
    # carattere = i
    mappa[chr(i)] = len(mappa) + 1
    mappa_1[len(mappa_1) + 1] = chr(i)
# print(len(mappa))

for i in range(32, 48, 1):
    print(chr(i))
    # carattere = i
    mappa[chr(i)] = len(mappa) + 1
    mappa_1[len(mappa_1) + 1] = chr(i)
# print(len(mappa))

print(mappa)

# ------Tutto quello che accade nella finestra------

while True:

    # print(len(mappa))

    event, values = finestra.read()

    if event == 'criptare':
        lunghezza()
    if event == 'chiave':
        lunghezza_1()
    if event == 'decriptare':
        lunghezza_2()
    if event == 'chiave_1':
        lunghezza_3()


    if event == 'cripta':
        print('Test_1')
        read_1()
        read_2()
        frase_arr = list(frase)
        chiave_arr = list(chiave)

        for i in range(0, len(frase_arr)):

            a = mappa[frase_arr[i]]
            b = mappa[chiave_arr[i]]
            l = len(mappa)

            ascii_message = f'{ascii_message + (str(a))}'
            # ascii_key = f'{ascii_key + (mappa_1[mappa[chiave_arr[i]] + mappa[frase_arr[i]]])} {x}'
            ascii_key = f'{ascii_key + (str(b))}'

            if a + b <= l:
                ascii_translated = f'{ascii_translated + (mappa_1[a + b])}'

            else:
                ascii_translated = f'{ascii_translated + (mappa_1[a + b - l])}'

        print(frase_arr)
        print(f'Frase ascii: {ascii_message}')
        # print_1()
        ascii_message = ''

        print(chiave_arr)
        print(f'Chiave ascii : {ascii_key}')
        # print_2()
        ascii_key = ''

        print(f' Frase tradotta : {ascii_translated}')
        print_1()
        ascii_translated = ''

# ------decriptare------

    if event == 'decripta':
        print('Test_1')
        read_3()
        read_4()
        frase_arr = list(frase)
        chiave_arr = list(chiave)

        for i in range(0, len(frase_arr)):

            a = mappa[frase_arr[i]]
            b = mappa[chiave_arr[i]]
            l = len(mappa)
            print(a)
            print(b)
            ascii_message = f'{ascii_message + (str(a))}'
            # ascii_key = f'{ascii_key + (mappa_1[mappa[chiave_arr[i]] + mappa[frase_arr[i]]])} {x}'
            ascii_key = f'{ascii_key + (str(b))}'

            if a - b >= 1:
                ascii_translated = f'{ascii_translated + (mappa_1[a - b])}'

            else:
                ascii_translated = f'{ascii_translated + (mappa_1[a - b + l])}'

        print(frase_arr)
        print(f'Frase ascii: {ascii_message}')
        # print_1()
        ascii_message = ''

        print(chiave_arr)
        print(f'Chiave ascii : {ascii_key}')
        # print_2()
        ascii_key = ''

        print(f' Frase tradotta : {ascii_translated}')
        print_2()
        ascii_translated = ''

    if event == sg.WIN_CLOSED:
        break
finestra.close()
