import tkinter as tk
import time
import random


# Function to perform quick sort
def quick_sort(arr, canvas, low, high):
    if low < high:
        pi = partition(arr, canvas, low, high)
        quick_sort(arr, canvas, low, pi - 1)
        quick_sort(arr, canvas, pi + 1, high)

# Function to partition the array
def partition(arr, canvas, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            draw_bars(canvas, arr, swap1=i, swap2=j)
            time.sleep(0.1)

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    draw_bars(canvas, arr, swap1=i + 1, swap2=high)
    time.sleep(0.1)

    return i + 1

# Function to draw bars representing array elements
def draw_bars(canvas, arr, swap1=None, swap2=None):
    canvas.delete("all")
    canvas_height = 300
    canvas_width = 500
    bar_width = (canvas_width - 20) / len(arr)  # Adjusted to leave a gap between bars
    max_height = max(arr)

    for i in range(len(arr)):
        normalized_height = (arr[i] / max_height) * canvas_height
        color = "black"

        if i == arr.index(min(arr)):
            color = "green"  # Color for min element

        if i == arr.index(max(arr)):
            color = "blue"  # Color for max element

        canvas.create_rectangle(
            i * bar_width + 10,  # Adding a margin to create a gap
            canvas_height - normalized_height,
            (i + 1) * bar_width + 10,  # Adding a margin to create a gap
            canvas_height,
            fill=color
        )

    root.update_idletasks()
    root.update()

# Function to shuffle the array
def shuffle_array():
    global array
    random.shuffle(array)
    draw_bars(canvas, array)

# Initialize the Tkinter window
root = tk.Tk()
root.title("Sort Visualization")
root.geometry("800x400")

# Create a canvas to draw bars
canvas = tk.Canvas(root, width=800, height=300)
canvas.pack()

# Generate a random array of integers
array = [random.randint(5, 100) for _ in range(20)]

# Draw the initial bars
draw_bars(canvas, array)

# Buttons for shuffling, generating data, merge sort, and quick sort
shuffle_button = tk.Button(root, text="Shuffle", command=shuffle_array)
shuffle_button.pack(pady=10)

quick_sort_button = tk.Button(root, text="Quick Sort", command=lambda: quick_sort(array, canvas, 0, len(array) - 1))
quick_sort_button.pack(pady=10)

root.mainloop()
