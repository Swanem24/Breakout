from tkinter import*

window = Tk()
window.title("Breakout Instruction")
w = Canvas(window, bg = "BLACK", width="1000", height="600")
Title = Label(window, text="Breakout: Instructions", bg="Black", fg="White", font=("Space Bd BT",40))    
LineInstruction = Label(window, text='''The concept of the game is to break all
the bricks with a ball using the paddle to deflect the ball within the time limit.
"You will have 3 live points at the start.
If you run out of life points, it will be game over.
If you fail to destroy all the bricks in time limit it will be game over.
You can begin the game by pressing the spacebar button.''', bg="Black", fg="Green", font=("Space Bd BT",17))

w.pack()
Title.place(x=250,y=10) 
LineInstruction.place(x=90,y=100) 
