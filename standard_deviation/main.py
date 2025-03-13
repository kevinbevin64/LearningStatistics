
from sample import Sample
from population import Population
from study import Study

def main():
	
	number_of_iterations = 1000
	sample_size = 49
	population_size = 50

	pop = Population([i for i in range (1, 1 + population_size)])

	sd_sum = 0
	for _ in range(number_of_iterations):
		new_sample = pop.create_sample(sample_size, pop_size=population_size)
		sd_sum += new_sample.sd
		print(f"SD = {new_sample.sd}")

	print("==================")
	print(sd_sum / number_of_iterations)
	print(str(round(pop.sd, 3)))

if __name__ == '__main__':
	main()
