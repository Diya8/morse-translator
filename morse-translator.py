from random import choice
import PySimpleGUI as sg   
import morse_dict              

def encoder(s):
    res = ''
    for i in s:
        if i != ' ':
            res += morse_dict.MORSE_CODE_DICT[i.upper()]+' '
        else:
            res += ' / '
    return res

def decoder(s):
    res = ''
    words = s.split('/')
    for word in words:
        word = word.strip()
        letters = word.split()
        for letter in letters:
            res += morse_dict.MORSE_REVERSED[letter]
        res += ' '
    return res

result = ''

choice_layout = [   [sg.Text('Click choice')], [sg.Button('Encode', key=1), sg.Button('Decode', key=2)] ]
choice_window = sg.Window('Choice', choice_layout)
choice_event, choice_val = choice_window.read()
choice_window.close()

if choice_event == 1:

    encode_layout = [   [sg.Text('Enter Text')], [sg.Input()], [sg.Button('OK') ]   ]
    encode_window = sg.Window('Encoder', encode_layout)
    encode_event, encode_val = encode_window.read()
    result = encoder(encode_val[0])
    encode_window.close()
else:
    decode_layout = [   [sg.Text('Enter Morse Code')], [sg.Input()], [sg.Button('OK') ]   ]
    decode_window = sg.Window('Decoder', decode_layout)
    decode_event, decode_val = decode_window.read()
    result = decoder(decode_val[0])
    decode_window.close()

result_layout = [   [sg.Text('Decoded Text')], [sg.Text(result, size=(40,1))], [sg.Button('Exit')] ]
result_window = sg.Window('Result', result_layout)
event, val = result_window.read()
print(result)
result_window.close()