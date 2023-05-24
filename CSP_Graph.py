from  CSP_solver import *

#The set of variables of the CSP with domains
variables = [
	Variable("A", domain= [1,2,3,4]),
	Variable("B", domain= [1,2,3,4]),
	Variable("C", domain= [1,2,3,4]),
    Variable("D", domain= [1,2,3,4]),
    Variable("E", domain= [1,2,3,4])
    
]

#Here are the constraints:
constraints = [
	Constraint("B >= A"),
	Constraint("A > D"),
	Constraint("C != A"),
    Constraint("B != C"),
	Constraint("C != D + 1"),
	Constraint("C != D"),
    Constraint("D > E"),
    Constraint("C > E")
]

#construct a csp with the variables and constraints
csp = CSP(variables, constraints, init_node = True, init_arc= True, keep_node= True, keep_arc= True, heuristic="mrv")

#Solve the csp and use verbose = True in order to print the search tree
csp.solve(verbose=True)
