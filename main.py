from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

#---------------------------- User Action & Saving------------------------ #

def right():
	# get the language & word from the window shown to user
	captured_word=canvas.itemcget(word_text,'text')
	captured_title=canvas.itemcget(title_text,'text')
	# print(captured_word,captured_title)
	# print(data_file[data_file[captured_title]==captured_word].index[0])
	# get the row index# of the language & word from the dataframe
	frame_index =data_file[data_file[captured_title] == captured_word].index[0]
	# mark the entry as familiar word.
	data_file.iloc[frame_index,2]='yes'
	# print(data_file[data_file[captured_title]==captured_word])

def wrong():
	captured_word=canvas.itemcget(word_text,'text')
	captured_title=canvas.itemcget(title_text,'text')
	# print(captured_word,captured_title)
	# print(data_file[data_file[captured_title]==captured_word].index[0])
	frame_index =data_file[data_file[captured_title] == captured_word].index[0]
	data_file.iloc[frame_index,2]='no'
	# print(data_file[data_file[captured_title]==captured_word])
#---------------------------- Flash Cards Mechanics ------------------------ #
def run_flash(*args):
	language,count = args
	if count < 4:
		if language == "French":
			canvas.itemconfig(canvas_image,image=card_front_image)
			canvas.itemconfig(title_text, text="French")
			canvas.itemconfig(word_text, text=data_file.French[count])
			window.after(3000, run_flash,"English",count)
		else:
			canvas.itemconfig(canvas_image, image=card_back_image)
			canvas.itemconfig(title_text, text="English")
			canvas.itemconfig(word_text, text=data_file.English[count])
			window.after(1000, run_flash,"French",count+1)
	else:
		data_file.to_csv('./data/french_words.csv', index=False)
		return

# ---------------------------- UI SETUP ------------------------------- #

data_file = pd.read_csv('./data/french_words.csv')
data_file["Repeat"] = 0

window = Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
window.title("Flashy")

canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_back_image = PhotoImage(file="./images/card_back.png")
card_front_image = PhotoImage(file="./images/card_front.png")
canvas_image = canvas.create_image(400,263,image=card_front_image)
canvas.grid(column=0, row=0, columnspan=2)

title_text = canvas.create_text(400,150,text="French",font=("Arial",40,"italic"))
word_text = canvas.create_text(400,263,text="French Word",font=("Arial",60,"bold"))

right_button_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_image,bg=BACKGROUND_COLOR,highlightthickness=0,command=right)
right_button.grid(column=0,row=1)

wrong_button_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0,command=wrong)
wrong_button.grid(column=1,row=1)

run_flash ("French",0)

window.mainloop()