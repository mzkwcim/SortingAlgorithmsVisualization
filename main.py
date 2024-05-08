import tkinter as tk
from tkinter import messagebox
from bubble_sort import BubbleSort
from insertion_sort import InsertionSort
from selection_sort import SelectionSort
from heap_sort import HeapSort
import random


class SortingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sorting Algorithm Visualizer")

        self.length_label = tk.Label(master, text="Długość tablicy:")
        self.length_label.grid(row=0, column=0, padx=10, pady=5)
        self.length_entry = tk.Entry(master)
        self.length_entry.grid(row=0, column=1, padx=10, pady=5)

        self.algorithm_label = tk.Label(master, text="Wybierz algorytm sortujący:")
        self.algorithm_label.grid(row=1, column=0, padx=10, pady=5)
        self.algorithm_var = tk.StringVar()
        self.algorithm_var.set("Bubble Sort")
        self.algorithm_dropdown = tk.OptionMenu(master, self.algorithm_var, "Bubble Sort", "Insertion Sort", "Selection Sort", "Heap Sort")
        self.algorithm_dropdown.grid(row=1, column=1, padx=10, pady=5)

        self.sort_button = tk.Button(master, text="Sortuj", command=self.sort)
        self.sort_button.grid(row=2, columnspan=2, padx=10, pady=5)

    def sort(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Błąd", "Podaj poprawną długość tablicy (liczba całkowita dodatnia).")
            return

        arr = [random.randint(1, 100) for _ in range(length)]

        algorithm = self.algorithm_var.get()

        if algorithm == "Bubble Sort":
            bubble_sort_anim = BubbleSort(arr)
            bubble_sort_anim.show_animation()
        elif algorithm == "Insertion Sort":
            insertion_sort_anim = InsertionSort(arr)
            insertion_sort_anim.show_animation()
        elif algorithm == "Selection Sort":
            selection_sort_anim = SelectionSort(arr)
            selection_sort_anim.show_animation()
        elif algorithm == "Heap Sort":
            heap_sort_anim = HeapSort(arr)
            heap_sort_anim.show_animation()


root = tk.Tk()
app = SortingApp(root)
root.mainloop()
