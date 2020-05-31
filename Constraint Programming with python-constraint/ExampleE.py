# Code for article: https://stackabuse.com/constraint-programming-with-python-constraint/

# Text for Example E:
    # You wish to pack chocolates for your mother. Luckily you work in a chocolate factory that has a lot of leftover chocolate.
    # You have a few chocolate types at your disposal.
    # Your goal is to bring her the sweetest chocolate possible, that you can pack in your bag and sneak through security,
    # and that wouldn't pass a certain net value for which you'd go to prison if you got caught.
    # Security most likely won't get suspicious if you bring less than 3kg. You can fit 1 dm^3 of chocolate in your bag.
    # You won't go to jail if you steal less than $300 worth of chocolate.
# Value table:
    # Chocolate Name	Weight (g)	Dimensions (cm)	Sweetness	Value ($)
    # Chocolate A	    100	        8 × 2.5 × 0.5	20	        8
    # Chocolate B	    45	        7 × 2 × 0.5	    16	        6.8
    # Chocolate C	    10	        3 × 2 × 0.5	    9	        4
    # Chocolate D	    25	        3 × 3 × 0.5	    7	        3

import constraint

problem = constraint.Problem()

problem.addVariable('A', range(31))
problem.addVariable('B', range(45))
problem.addVariable('C', range(76))
problem.addVariable('D', range(101))

# We have 3kg = 3,000g available
def weight_constraint(a, b, c, d):
    if (a*100 + b*45 + c*10 + d*25) <= 3000:
        return True

# We have 1dm^3 = 1,000cm^3 available
def volume_constraint(a, b, c, d):
    if (a*8*2.5*0.5 + b*6*2*0.5 * c*2*2*0.5 + d*3*3*0.5) <= 1000:
        return True

# We can't exceed $200
def value_constraint(a, b, c, d):
    if (a*8 + b*6.8 + c*4 + d*3) < 300:
        return True

problem.addConstraint(weight_constraint, "ABCD")
problem.addConstraint(volume_constraint, "ABCD")
problem.addConstraint(value_constraint, "ABCD")

maximum_sweetness = 0
solution_found = {}
solutions = problem.getSolutions()

for s in solutions:
    current_sweetness = s['A']*10 + s['B']*8 + s['C']*4.5 + s['D']*3.5
    if current_sweetness > maximum_sweetness:
        maximum_sweetness = current_sweetness
        solution_found = s

print("""
The maximum sweetness we can bring is: {}
We'll bring:
{} A Chocolates,
{} B Chocolates,
{} C Chocolates,
{} D Chocolates
""".format(maximum_sweetness, solution_found['A'], solution_found['B'], solution_found['C'], solution_found['D']))