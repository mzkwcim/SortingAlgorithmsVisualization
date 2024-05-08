import matplotlib.pyplot as plt
import matplotlib.animation as animation


class InsertionSort:
    def __init__(self, arr):
        self.arr = arr
        self.fig, self.ax = plt.subplots()
        self.bar_rects = self.ax.bar(range(len(arr)), arr, align="edge")
        self.animation = animation.FuncAnimation(self.fig, self.update_fig, frames=self.insertion_sort(), fargs=(self.bar_rects,), repeat=False,  interval=10)

    def insertion_sort(self):
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i - 1
            while j >= 0 and self.arr[j] > key:
                self.arr[j + 1] = self.arr[j]
                j -= 1
                yield self.arr
            self.arr[j + 1] = key
            yield self.arr

    def update_fig(self, arr, rects):
        for rect, val in zip(rects, arr):
            rect.set_height(val)
        return rects

    def show_animation(self):
        plt.show()
