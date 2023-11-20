import tkinter as tk
from tkinter import ttk
import time

def bubble_sort():
    array = numeric_array.copy()
    n = len(array)

    for i in range(n):
        is_sorted = True  # Flag to check if the array is sorted

        for j in range(0, n-i-1):
            # Highlight elements being compared
            box_labels[j].config(bg='#3498db')  # Blue color
            box_labels[j+1].config(bg='#3498db')
            result_frame.update()
            time.sleep(0.3)

            if array[j] > array[j+1]:
                # Highlight elements being swapped
                box_labels[j].config(bg='#e74c3c')  # Red color
                box_labels[j+1].config(bg='#e74c3c')
                result_frame.update()
                time.sleep(0.3)

                # Swap elements
                array[j], array[j+1] = array[j+1], array[j]
                update_boxes(array)

                # Reset box colors
                box_labels[j].config(bg='#2ecc71')  # Green color
                box_labels[j+1].config(bg='#2ecc71')
                result_frame.update()
                time.sleep(0.3)

                is_sorted = False

        # If no swaps occurred in a pass, the array is sorted
        if is_sorted:
            break

    # Highlight the sorted array in green
    for i in range(n):
        box_labels[i].config(bg='#2ecc71')  # Green color
        result_frame.update()
        time.sleep(0.5)

def insertion_sort():
    array = numeric_array.copy()

    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        box_labels[i].config(bg='#3498db')  # Blue color
        result_frame.update()
        time.sleep(0.3)

        while j >= 0 and key < array[j]:
            # Highlight elements being shifted
            box_labels[j+1].config(bg='#e74c3c')  # Red color
            result_frame.update()
            time.sleep(0.3)

            array[j+1] = array[j]
            update_boxes(array)
            box_labels[j+1].config(bg='#2ecc71')  # Green color
            result_frame.update()
            time.sleep(0.3)
            j -= 1

        array[j+1] = key
        update_boxes(array)

    # Highlight the sorted array in green
    for i in range(len(array)):
        box_labels[i].config(bg='#2ecc71')  # Green color
        result_frame.update()
        time.sleep(0.5)

def selection_sort():
    array = numeric_array.copy()

    for i in range(len(array)):
        min_index = i
        box_labels[i].config(bg='#3498db')  # Blue color
        result_frame.update()
        time.sleep(0.3)

        for j in range(i+1, len(array)):
            # Highlight elements being compared
            box_labels[j].config(bg='#e74c3c')  # Red color
            result_frame.update()
            time.sleep(0.3)

            if array[j] < array[min_index]:
                min_index = j

            # Reset box colors
            box_labels[j].config(bg='#2ecc71')  # Green color
            result_frame.update()
            time.sleep(0.3)

        # Swap elements
        array[i], array[min_index] = array[min_index], array[i]
        update_boxes(array)

        # Highlight elements being swapped
        box_labels[i].config(bg='#e74c3c')  # Red color
        box_labels[min_index].config(bg='#e74c3c')
        result_frame.update()
        time.sleep(0.3)

        # Reset box colors
        box_labels[i].config(bg='#2ecc71')  # Green color
        box_labels[min_index].config(bg='#2ecc71')
        result_frame.update()
        time.sleep(0.3)

    # Highlight the sorted array in green
    for i in range(len(array)):
        box_labels[i].config(bg='#2ecc71')  # Green color
        result_frame.update()
        time.sleep(0.5)

def merge_sort():
    def merge_sort_recursive(array, start, end):
        if start < end:
            mid = (start + end) // 2
            merge_sort_recursive(array, start, mid)
            merge_sort_recursive(array, mid + 1, end)
            merge(array, start, mid, end)

    def merge(array, start, mid, end):
        left = array[start:mid+1]
        right = array[mid+1:end+1]

        i = j = 0
        k = start

        while i < len(left) and j < len(right):
            # Highlight elements being compared
            box_labels[start + i].config(bg='#3498db')  # Blue color
            box_labels[mid + 1 + j].config(bg='#3498db')
            result_frame.update()
            time.sleep(0.3)

            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1

            update_boxes(array)

            # Reset box colors
            box_labels[start + i - 1].config(bg='#2ecc71')  # Green color
            box_labels[mid + 1 + j - 1].config(bg='#2ecc71')
            result_frame.update()
            time.sleep(0.3)

            k += 1

        while i < len(left):
            array[k] = left[i]
            update_boxes(array)
            k += 1
            i += 1

        while j < len(right):
            array[k] = right[j]
            update_boxes(array)
            k += 1
            j += 1

    array = numeric_array.copy()
    merge_sort_recursive(array, 0, len(array) - 1)

    # Highlight the sorted array in green
    for i in range(len(array)):
        box_labels[i].config(bg='#2ecc71')  # Green color
        result_frame.update()
        time.sleep(0.5)

def update_boxes(array):
    for i in range(len(array)):
        box_labels[i].config(text=str(array[i]), bg='#2ecc71')  # Green color
        result_frame.update()
        time.sleep(0.3)

def convert_and_sort():
    global numeric_array
    user_input = entry.get()

    try:
        numeric_array = list(map(int, user_input.split(',')))
    except ValueError:
        result_label.config(text="Invalid input. Please enter a comma-separated numeric array.")
        return

    result_label.config(text="")
    create_boxes(numeric_array)
    selected_algorithm = algorithm_var.get()

    if selected_algorithm == "Bubble Sort":
        bubble_sort()
    elif selected_algorithm == "Insertion Sort":
        insertion_sort()
    elif selected_algorithm == "Selection Sort":
        selection_sort()
    elif selected_algorithm == "Merge Sort":
        merge_sort()

def create_boxes(array):
    global box_labels
    # Clear existing boxes
    for widget in result_frame.winfo_children():
        widget.destroy()

    # Create new boxes
    box_labels = []
    for num in array:
        box = tk.Label(result_frame, text=str(num), relief="solid", width=5, height=2, padx=5, pady=5, bg='#2ecc71')  # Green color
        box.pack(side="left", padx=5)
        box_labels.append(box)

# Create the main window
root = tk.Tk()
root.title("Array to Boxes Converter with Sorting")

# Styling
style = ttk.Style()
style.configure("TButton", padding=10, font=('Helvetica', 12))
style.configure("TLabel", padding=10, font=('Helvetica', 12))
style.configure("TEntry", padding=10, font=('Helvetica', 12))

# Input Frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

input_label = ttk.Label(input_frame, text="Enter a numeric array (comma-separated):")
input_label.pack(side="left")

entry = ttk.Entry(input_frame, width=30)
entry.pack(side="left")

# Sorting Algorithm Dropdown
algorithm_var = tk.StringVar(root)
algorithm_var.set("Bubble Sort")  # default value
algorithm_dropdown = ttk.Combobox(root, textvariable=algorithm_var, values=["Bubble Sort", "Insertion Sort", "Selection Sort", "Merge Sort"])
algorithm_dropdown.pack(pady=10)

# Convert Button
convert_button = ttk.Button(root, text="Convert and Sort", command=convert_and_sort)
convert_button.pack(pady=10)

# Result Frame
result_frame = tk.Frame(root)
result_frame.pack()

result_label = ttk.Label(root, text="")
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
