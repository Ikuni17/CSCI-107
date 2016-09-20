# ---------------------------------------------+
# Bradley White                                | 
# CSCI 107, Assignment 11                      |
# Last Updated: December 5, 2013               |  
# ---------------------------------------------|
# This is a program to mutate and crossover    |
# strands of DNA.                              |
# ---------------------------------------------+
import random

# Main function to adjust the parameters of the experiments, calls the other functions,
# and prints the results.
def main():
    strand_1 = "AAAAAA"
    strand_2 = "GGGGGG"

    print("Crossover Experiments with", strand_1, "and", strand_2)
    print("--------------------------------------------")
    for i in range(10):
        new_strand = crossover(strand_1, strand_2)
        print("Experiment", i+1, "results in", new_strand)

    print()
    print("Mutation Experiments with", strand_1)
    print("--------------------------------")
    for i in range(10):
        new_strand = mutate(strand_1)
        print("Experiment", i+1, "results in", new_strand)

# Function that randomly chooses a position within strand_1, other then the zeroth,
# and slices it. strand_1 is then concatenated with strand_2.
def crossover(first_strand, second_strand):
    position = random.randint(1,len(first_strand)-1)
    crossed_strand = (first_strand[position:] + second_strand[:position])
    return crossed_strand

# Function that randomly chooses a position within the strand and replaces it with a
# random base other then the base within the strand.
def mutate(strand):
    position = random.randint(0,len(strand)-1)
    chosen = random.choice('ACGT')
    while True:
        if chosen == strand[0]:
            chosen = random.choice('ACGT')
        else:
            mutated_strand = (strand[:position] + chosen + strand[position+1:])
            return mutated_strand

main()
