import matplotlib.pyplot as plt
import matplotlib.animation as animation

class HeapSort:
    def __init__(self, arr):
        self.arr = arr
        self.fig, self.ax = plt.subplots()
        self.bar_rects = self.ax.bar(range(len(arr)), arr, align="edge")
        self.animation = animation.FuncAnimation(self.fig, self.update_fig, frames=self.heap_sort(), fargs=(self.bar_rects,), repeat=False, interval=25)

    def heap_sort(self):
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and arr[left] > arr[largest]:
                largest = left

            if right < n and arr[right] > arr[largest]:
                largest = right

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                yield arr
                yield from heapify(arr, n, largest)

        n = len(self.arr)

        for i in range(n // 2 - 1, -1, -1):
            yield from heapify(self.arr, n, i)

        for i in range(n - 1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            yield self.arr
            yield from heapify(self.arr, i, 0)

    def update_fig(self, arr, rects):
        for rect, val in zip(rects, arr):
            rect.set_height(val)
        return rects

    def show_animation(self):
        plt.show()
