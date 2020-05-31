# Code for article: https://stackabuse.com/constraint-programming-with-python-constraint/

# Text for Example C:
    # You recently got a job as a cashier.
    # You're trying to convince your friend that it's hard work, there are just SO many ways to give someone their change back!
    # Your "friend" shakes his head, obviously not believing you.
    # He says "It can't be that bad. How many ways can there POSSIBLY be to give someone their change back, for like 60 cents?".
    # Your response is, of course, to sit and quickly write a program that would prove your point.
    # You have a decent amount of pennies (1 cent), nickels (5 cents), dimes (10 cents) and quarters (25 cents), and a lot of kinda suspicious coins worth 3 cents each.
    # Calculate in how many ways you can return change for 60 cents.

import constraint

problem = constraint.Problem()

# The maximum amount of each coin type can't be more than 60
# (coin_value*num_of_coints) <= 60

problem.addVariable("1 cent", range(61))
problem.addVariable("3 cent", range(21))
problem.addVariable("5 cent", range(13))
problem.addVariable("10 cent", range(7))
problem.addVariable("20 cent", range(4))

problem.addConstraint(
    constraint.ExactSumConstraint(60,[1,3,5,10,20]),
    ["1 cent", "3 cent", "5 cent","10 cent", "20 cent"]
)
# Where we explicitly give the order in which the weights should be allocated

# We could've used a custom constraint instead, BUT in this case the program will
# run slightly slower - this is because built-in functions are optimized and
# they find the solution more quickly
# def custom_constraint(a, b, c, d, e):
#     if a + 3*b + 5*c + 10*d + 20*e == 60:
#         return True
#     problem.addConstraint(o, ["1 cent", "3 cent", "5 cent","10 cent", "20 cent"])


# A function that prints out the amount of each coin
# in every acceptable combination
def print_solutions(solutions):
    for s in sols:
        print("---")
        print("""
        1 cent: {0:d}
        3 cent: {1:d}
        5 cent: {2:d}
        10 cent: {3:d}
        20 cent: {4:d}""".format(s["1 cent"], s["3 cent"], s["5 cent"], s["10 cent"], s["20 cent"]))
        # If we wanted to we could check whether the sum was really 60
        # print("Total:", s["1 cent"] + s["3 cent"]*3 + s["5 cent"]*5 + s["10 cent"]*10 + s["20 cent"]*20)
        # print("---")

solutions = problem.getSolutions()
#print_solutions(solutions)
print("Total number of ways: {}".format(len(solutions)))