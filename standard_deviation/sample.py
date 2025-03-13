
from math import sqrt

class Sample:
    def __init__(self, data: list[int], pop_size: int = None) -> None:
        self.data = data
        self.size = len(data)
        self.mean = sum(data) / self.size
        self.pop_size = pop_size

    @property
    def sd(self) -> float:
        sum_of_squared_diffs = sum([(val - self.mean) ** 2 for val in self.data])

        divisor = self.size - 1
        # if (self.pop_size != None):
        #     # Finite Population Correction
        #     divisor *= (self.pop_size - 1) / (self.pop_size - self.size)

        return sqrt(sum_of_squared_diffs / divisor)

    def set_pop_size(self, pop_size: int):
        self.pop_size = pop_size

if __name__ == '__main__':
    print("Running sample.py...")
    sample = Sample([i for i in range(1, 11)])
    print(f"{sample.mean = }, {sample.sd = }")