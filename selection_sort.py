import matplotlib.pyplot as plt
import matplotlib.animation as animation


class SelectionSort:
    def __init__(self, arr):
        self.arr = arr
        self.fig, self.ax = plt.subplots()
        self.bar_rects = self.ax.bar(range(len(arr)), arr, align="edge")
        self.animation = animation.FuncAnimation(self.fig, self.update_fig, frames=self.selection_sort(), fargs=(self.bar_rects,), repeat=False, interval=10)

    def selection_sort(self):
        n = len(self.arr)
        for i in range(n - 1):
            min_idx = i
            for j in range(i + 1, n):
                if self.arr[j] < self.arr[min_idx]:
                    min_idx = j
            if min_idx != i:
                self.arr[i], self.arr[min_idx] = self.arr[min_idx], self.arr[i]
                yield self.arr

    def update_fig(self, arr, rects):
        for rect, val in zip(rects, arr):
            rect.set_height(val)
        return rects

    def show_animation(self):
        plt.show()
