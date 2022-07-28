from tkinter import *
import pandas
import random

try:
    data = pandas.read_csv('./data/new_data.csv')
except FileNotFoundError:
    data = pandas.read_csv('./data/french_words.csv')

print(data)
list_fw = pandas.DataFrame.to_dict(data, orient='records')
BACKGROUND_COLOR = "#B1DDC6"
data_new = data
x = 101
l=0

def wrong_ones():
    global l
    l+=1
    print(l)
    if l == 1:
        quit()
    else:
        global data_new
        data_new = pandas.DataFrame.to_dict(data_new, orient='records')
        print(i)
        data_new.remove(current_card)
        print(data_new)
        data_new = pandas.DataFrame(data_new)
        data_new.to_csv("./data/new_data.csv", index=False)
        right_wrong()

def right_wrong():
    global x, i, l
    l+=1
    i = random.randint(0, x)
    x -= 1
    global current_card
    current_card=list_fw[i]
    print(current_card)
    french_word = list_fw[i]['French']
    global english_word
    english_word = list_fw[i]['English']
    canvas.itemconfig(title, text='French')
    canvas.itemconfig(image_on_canvas, image=image1)
    canvas.itemconfig(word, text=f'{french_word}')
    window.after(5000, english_card)


def english_card():
    print(english_word)
    canvas.itemconfig(title, text='English')
    canvas.itemconfig(word, text=f'{english_word}')
    canvas.itemconfig(image_on_canvas, image=image2)


window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
image1 = PhotoImage(file='./images/card_front.png', height=526, width=800)
image2 = PhotoImage(file='./images/card_back.png', height=526, width=800)
image_on_canvas = canvas.create_image(400, 263, image=image1)

title = canvas.create_text(400, 150, text='Title', font=('Ariel', 40, 'italic'))
word = canvas.create_text(400, 263, text='Word', font=('Ariel', 60, 'bold'))


button_correct = PhotoImage(file="./images/right.png")
right = Button(image=button_correct, command=right_wrong, bg=BACKGROUND_COLOR, highlightthickness=0)
right.grid(row=1, column=0)
button_wrong = PhotoImage(file="./images/wrong.png")
wrong = Button(image=button_wrong, command=wrong_ones, bg=BACKGROUND_COLOR, highlightthickness=0)
wrong.grid(row=1, column=1)


window.mainloop()