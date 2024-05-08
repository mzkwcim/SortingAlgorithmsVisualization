import matplotlib.pyplot as plt
import matplotlib.animation as animation


class BubbleSort:
    def __init__(self, arr):
        self.arr = arr
        self.fig, self.ax = plt.subplots()
        self.bar_rects = self.ax.bar(range(len(arr)), arr, align="edge")
        self.animation = animation.FuncAnimation(self.fig, self.update_fig, frames=self.bubble_sort(), fargs=(self.bar_rects,), repeat=False, interval=25)

    def bubble_sort(self):
        n = len(self.arr)
        swapped = True
        while swapped:
            swapped = False
            for i in range(1, n):
                if self.arr[i - 1] > self.arr[i]:
                    self.arr[i - 1], self.arr[i] = self.arr[i], self.arr[i - 1]
                    swapped = True
                    yield self.arr

    def update_fig(self, arr, rects):
        for rect, val in zip(rects, arr):
            rect.set_height(val)
        return rects

    def show_animation(self):
        plt.show()
