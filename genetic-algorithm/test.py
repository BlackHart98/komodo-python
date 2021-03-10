import population

def fitness(goal,output):
	val=0
	for i in range(len(goal)):
		if goal[i] == output[i]:
			val+=1
	return val

if __name__ == "__main__":
	
	goal=[1,0,1,1,0,0,1,1,0,1,0,0]
	pop_size=10

	species=population.population(pop_size,len(goal),.25,(0,1))
	species.initialize()

	# x=species.getIndividual(0)

	# print("aye")
	# print(x.getChromosome())
	fit_val=[]
	for i in range(pop_size):
		cur_chrom=species.getIndividual(i)
		print("{} : {}".format(goal,cur_chrom.getChromosome()))
		num=fitness(goal,cur_chrom.getChromosome())
		print("fit value: {}".format(num))
		fit_val.append(num)

	# print(fit_val)
	species.setFitness(fit_val)

	best_specie=species.getBestCandidate()
	print("best fitness value: {}".format(best_specie.getFitness()))
	epoch_count=1
	while best_specie.getFitness() < len(goal):
		species.epoch()
		fit_val=[]
		for i in range(pop_size):
			cur_chrom=species.getIndividual(i)
			print("{} : {}".format(goal,cur_chrom.getChromosome()))
			num=fitness(goal,cur_chrom.getChromosome())
			print("fit value: {}".format(num))
			fit_val.append(num)
		species.setFitness(fit_val)
		best_specie=species.getBestCandidate()
	
		epoch_count+=1
	print(best_specie.getChromosome())

	print("number of generations: {}".format(epoch_count))