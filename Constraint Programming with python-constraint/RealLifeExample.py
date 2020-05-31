# Code for article: https://stackabuse.com/constraint-programming-with-python-constraint/

# Text:
    # A friend of mine, someone who only learned of Python's existence a few months before, needed to solve a problem for a physical chemistry research project she was working on.
    # That friend needed the following problem solved:
        # Generate all combinations (that have a length equal to the number of keys) of values stored in a dictionary
        # (the order of output doesn't matter). The dictionary is {String : List_of_Strings}.
        # In such a way that every combination has exactly one value from the List_of_Strings of a key.
        # You don't know the number of keys in the dictionary in advance,
        # nor do you know how long a List_of_String is, every List_of_String can be of different length.
        # I.e. the dictionary is dynamically generated via user input.
        #
        # Example input: dictionary = {"A" : [1,2], "B" -> [4], "C" -> [5,6,7], "D" -> [8,9]}
        # Example output: (1,4,5,8), (1,4,5,8), (1,4,6,8), (1,4,6,9), (1,4,7,8)....

import constraint

# input example
generated_dictionary = {'A' : [1,2], 'B' : [4], 'C' : [5,6,7], 'D' : [8,9]}

problem = constraint.Problem()

for key, value in generated_dictionary.items():
    problem.addVariable(key, value)

solutions = problem.getSolutions()

for solution in solutions:
    print(solution)