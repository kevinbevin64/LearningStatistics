
from sample import Sample

from math import sqrt
# from random import randint
import secrets 

class Population(Sample):
	def __init__(self, pop: list[int]) -> None:
		super().__init__(pop)

	@property
	def sd(self):
		return sqrt(sum([(val - self.mean) ** 2 for val in self.data]) / self.size)
	

	def create_sample(self, size: int, pop_size: int = None) -> list[int]:
		"""
		Create sample of specified size.
		"""

		# Draw from the population size number of times 
		# and return a Sample object initialized using those values
		sample = []
		for i in range(size):
			rand_index = secrets.randbelow(self.size)
			sample.append(self.data[rand_index])
		return Sample(sample, pop_size)

if __name__ == '__main__':
	print("Running population.py...")
	pop = Population([i for i in range(1, 11)])
	print(f"{pop.mean = }, {pop.sd = }")
