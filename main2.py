from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
random_card = {}
to_learn = {}

#---------------------------- User Action & Saving------------------------ #
def flip_card():

	canvas.itemconfig(canvas_image, image=card_back_image)
	canvas.itemconfig(title_text, text="English",fill='white')
	canvas.itemconfig(word_text, text=random_card['English'],fill='white')

def next_card():
	global random_card,flip_timer
	#this will stop multiple click events to reset
	window.after_cancel(flip_timer)
	# output is a dictionary from the list
	random_card = random.choice(to_learn)
	print(f"Items shown {random_card}")
	canvas.itemconfig(canvas_image, image=card_front_image)
	canvas.itemconfig(title_text, text="French",fill='black')
	canvas.itemconfig(word_text, text=random_card['French'],fill='black')
	#this is a new flip_timer than from the main body
	flip_timer = window.after(3000, flip_card)
	
def is_known():
	print(f"Items to be removed : {random_card}")
	to_learn.remove(random_card)
	dataframe_tobe_saved = pd.DataFrame(to_learn)
	dataframe_tobe_saved.to_csv("./data/words_to_learn_2.csv",index=False)
	next_card()
# ---------------------------- UI SETUP ------------------------------- #

try :
	data = pd.read_csv("./data/words_to_learn_2.csv")
except FileNotFoundError:
	original_data = pd.read_csv("./data/french_words_2.csv")
	to_learn = original_data.to_dict(orient='records')
else:
	to_learn = data.to_dict(orient='records')

window = Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
window.title("Flashy")
# we using flip_timer to cancel it for multiple clicks after
flip_timer=window.after(3000, flip_card)


canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_back_image = PhotoImage(file="./images/card_back.png")
card_front_image = PhotoImage(file="./images/card_front.png")
canvas_image = canvas.create_image(400,263,image=card_front_image)
canvas.grid(column=0, row=0, columnspan=2)

title_text = canvas.create_text(400,150,text="",font=("Arial",40,"italic"))
word_text = canvas.create_text(400,263,text="",font=("Arial",60,"bold"))

right_button_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_image,bg=BACKGROUND_COLOR,highlightthickness=0,command=is_known)
right_button.grid(column=0,row=1)

wrong_button_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0,command=next_card)
wrong_button.grid(column=1,row=1)

next_card()

window.mainloop()