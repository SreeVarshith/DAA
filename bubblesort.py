import tkinter as tk
import random

# Function to swap two bars that will be animated
def swap(pos_0, pos_1):
    bar11, _, bar12, _ = canvas.coords(pos_0)
    bar21, _, bar22, _ = canvas.coords(pos_1)
    canvas.move(pos_0, bar21-bar11, 0)
    canvas.move(pos_1, bar12-bar22, 0)

# Animation Function
def animate():
    global worker
    if worker is not None:
        try:
            next(worker)
            window.after(10, animate)
        except StopIteration:
            worker = None

worker = None 

#Bubble Sort
def _bubble_sort():
    global barList
    global lengthList
    
    for i in range(len(lengthList) - 1):
        for j in range(len(lengthList) - i - 1):
            if(lengthList[j] > lengthList[j + 1]):
                lengthList[j] , lengthList[j + 1] = lengthList[j + 1] , lengthList[j]
                barList[j], barList[j + 1] = barList[j + 1] , barList[j]
                swap(barList[j + 1] , barList[j])
                yield        
           

# Function to update the bars in the canvas
def update_bars(lengths):
    for bar, length in zip(barList, lengths):
        x1, y1, x2, y2 = canvas.coords(bar)
        canvas.coords(bar, x1, y1, x1 + barWidth, y1 + length)


#Triggering Fuction
def bubble_sort():     
    global worker
    worker = _bubble_sort()
    animate()    



#Animation Function
def animate():      
    global worker
    if worker is not None:
        try:
            next(worker)
            window.after(200, animate)    
        except StopIteration:            
            worker = None
        finally:
            window.after_cancel(animate) 


#Generator function for generating data
def generate():
    global barList
    global lengthList
    canvas.delete('all')
    barstart = 50
    barwidth = 20
    barList = []
    lengthList = []

    #Creating a rectangle
    for bar in range(1, 30):
        randomY = random.randint(1, 360)
        bar = canvas.create_rectangle(barstart, randomY,barstart + barwidth, 365, fill='black')
        barList.append(bar)
        barstart +=barwidth + 5
       

    #Getting length of the bar and appending into length list
    for bar in barList:
        bar = canvas.coords(bar)
        length = bar[3] - bar[1]
        lengthList.append(length)

    #Maximum is colored Red
    #Minimum is colored Black
    for i in range(len(lengthList)-1):
        if lengthList[i] == min(lengthList):
            canvas.itemconfig(barList[i], fill='green')
        elif lengthList[i] == max(lengthList):
            canvas.itemconfig(barList[i], fill='blue')



#Making a window using the Tk widget
window = tk.Tk()
window.title('Bubble Sorting Visualization')
window.geometry('1200x650')

#Making a Canvas within the window to display contents
canvas = tk.Canvas(window, width='1200', height='400')
canvas.grid(column=0,row=0, columnspan = 20)

#Buttons
bubble = tk.Button(window, text='Bubble Sort', command=bubble_sort)
shuf = tk.Button(window, text='Shuffle', command=generate)
bubble.grid(column=3,row=1)
shuf.grid(column=0, row=1,padx=(20,0))


# Generating initial visualization
generate()
window.mainloop()
