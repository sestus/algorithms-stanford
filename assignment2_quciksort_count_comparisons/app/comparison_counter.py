class ComparisonCounter(object):
    def __init__(self, input_file=None):
        self._array = []
        self._inversions = 0
        self.read_input(input_file)

    @property
    def array(self):
        return self._array

    @array.setter
    def array(self, arr):
        self._array = arr

    def read_input(self, input_file=None):
        if input_file is None:
            self._array = [int(elem) for elem in input().split()]
            return
        with open(input_file) as numbers:
            for number in numbers:
                self._array.append(int(number))

    def sort(self,):
        if len(self._array) <= 1:
            return
        self._qsort(0, len(self._array) - 1)

    def _qsort(self, start, end):
        if start >= end:
            return
        pivot = self._partition(start, end)
        self._qsort(start, pivot - 1)
        self._qsort(pivot + 1, end)

    def _partition(self, start, end):
        pivot = start
        for i in range(start + 1, end + 1):
            if self._array[i] < self._array[start]:
                pivot += 1
                self._array[i], self._array[pivot] = self._array[pivot], self._array[i]
        self._array[start], self._array[pivot] = self._array[pivot], self._array[start]
        return pivot