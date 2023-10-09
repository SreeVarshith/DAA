import tkinter as tk
import time
import random

# Function to perform merge sort
def merge_sort(arr, canvas):
    merge_sort_helper(arr, canvas, 0, len(arr) - 1)

# Helper function for merge sort
def merge_sort_helper(arr, canvas, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort_helper(arr, canvas, start, mid)
        merge_sort_helper(arr, canvas, mid + 1, end)
        merge(arr, canvas, start, mid, end)

# Function to merge subarrays
def merge(arr, canvas, start, mid, end):
    left_arr = arr[start:mid + 1]
    right_arr = arr[mid + 1:end + 1]

    i = j = 0
    k = start

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        draw_bars(canvas, arr)
        time.sleep(0.1)
        k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        draw_bars(canvas, arr)
        time.sleep(0.1)
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        draw_bars(canvas, arr)
        time.sleep(0.1)
        j += 1
        k += 1

# Function to draw bars representing array elements
def draw_bars(canvas, arr):
    canvas.delete("all")
    canvas_height = 300
    canvas_width = 500
    num_bars = len(arr)
    bar_width = (canvas_width - 20) / num_bars  # Adjusted bar width to fit within the canvas with a little gap
    max_height = max(arr)
    min_height = min(arr)

    for i in range(num_bars):
        normalized_height = (arr[i] / max_height) * (canvas_height - 20)  # Adjusted height to fit within the canvas with a little gap
        if arr[i] == max_height:
            canvas.create_rectangle(
                i * bar_width + 20,  # Added 10 for gap
                canvas_height - normalized_height,
                (i + 1) * bar_width + 20,  # Added 10 for gap
                canvas_height,
                fill="blue"
            )
        elif arr[i] == min_height:
            canvas.create_rectangle(
                i * bar_width + 20,  # Added 10 for gap
                canvas_height - normalized_height,
                (i + 1) * bar_width + 20,  # Added 10 for gap
                canvas_height,
                fill="green"
            )
        else:
            canvas.create_rectangle(
                i * bar_width + 20,  # Added 10 for gap
                canvas_height - normalized_height,
                (i + 1) * bar_width + 20,  # Added 10 for gap
                canvas_height,
                fill="black"
            )

    root.update_idletasks()
    root.update()

# Function to shuffle the array
def shuffle_array():
    global array
    random.shuffle(array)
    draw_bars(canvas, array)

# Function to initiate merge sort when the button is pressed
def start_merge_sort():
    merge_sort(array, canvas)

# Initialize the Tkinter window
root = tk.Tk()
root.title("Merge Sort Visualization")
root.geometry("800x400")

# Create a canvas to draw bars
canvas = tk.Canvas(root, width=800, height=300)
canvas.pack()

# Generate a random array of integers
array = [random.randint(5, 100) for _ in range(20)]

# Draw the initial bars
draw_bars(canvas, array)

# Button to start merge sort
merge_sort_button = tk.Button(root, text="Merge Sort", command=start_merge_sort)
merge_sort_button.pack(pady=10)

# Button to shuffle the array
shuffle_button = tk.Button(root, text="Shuffle", command=shuffle_array)
shuffle_button.pack(pady=10)

root.mainloop()
