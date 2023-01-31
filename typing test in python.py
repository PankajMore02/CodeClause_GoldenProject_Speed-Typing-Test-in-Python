# importing all libraries
from tkinter import *
from timeit import default_timer as timer
import random
from PIL import Image,ImageTk
# creating window using gui
window = Tk()

# the size of the window is defined
window.geometry("1300x700")
window.configure(bg='pink')
x = 0

# defining the function for the test
def game():
	global x

	# loop for destroying the window
	# after on test
	if x == 0:
		window.destroy()
		x = x+1

	# defining function for results of test
	def check_result():
		if entry.get() == words[word]:

			# here start time is when the window
			# is opened and end time is when
			# window is destroyed
			end = timer()

			# we deduct the start time from end
			# time and calculate results using
			# timeit function
			print(end-start)
			label4=Label(windows,text='The Typing Speed is:'+str(end-start)).place(x=500,y=400)
		else:
			print("Wrong Input")
			label5=Label(windows,text="Wrong Input, Try Again").place(x=500,y=400)
	words = ['Whatever you are late you are good one',
	         'Be The change You Wish to see in real world',
			 'India is my countary.I am proud of it',
			 'Wake up early in the morning,is a good habbit',
			 'Accuracy,Time Management,Hard work is part of success']                            
											

	# Give random words for testing the speed of user
	word = random.randint(0, (len(words)-1))

	# start timer using timeit function
	start = timer()
	windows = Tk()
	windows.geometry("1300x700")
	windows.configure(bg='pink')
	# use label method of tkinter for labeling in window
	x2 = Label(windows, text=words[word], font="times 20")

	# place of labeling in window
	x2.place(x=450, y=100)
	x3 = Label(windows, text="Start Typing", font="times 20")
	x3.place(x=300, y=200)

	entry = Entry(windows,width=50,font='Arial 15')
	entry.place(x=450, y=200)

	# buttons to submit output and check results
	b2 = Button(windows, text="Done",
				command=check_result, width=12, bg='grey')
	b2.place(x=500, y=300)

	b3 = Button(windows, text="Try Again",
				command=game, width=12, bg='grey')
	b3.place(x=625, y=300)
	label6=Label(windows,text="Copyright @Pankaj More 2023").place(x=550,y=600)
	windows.mainloop()
image = Image.open("mickey.jpg")
 
# Resize the image using resize() method
resize_image = image.resize((300, 150))
 
img = ImageTk.PhotoImage(resize_image)

label1 = Label(image=img,bg='purple')
label1.image =img
label1.place(x=0,y=0)
x2=Label(window,text="Mickey Foundation",font="times 15")
x2.place(x=80,y=180)
x1 = Label(window, text="Lets Test Your Typing Speed", font="times 20")
x1.place(x=500, y=250)

b1 = Button(window, text="Go", command=game, width=12, bg='yellow')
b1.place(x=600, y=300)
label6=Label(window,text="Copyright @Pankaj More 2023").place(x=550,y=600)
# calling window
window.mainloop()
