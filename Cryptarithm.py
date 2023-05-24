from  CSP_solver import *

#The set of variables of the CSP with domains

domain = [num for num in range(10)]
variables = [
	Variable("U", domain= domain.copy()),
	Variable("N", domain= domain.copy()),
	Variable("E", domain= domain.copy()),
    Variable("F", domain= domain.copy()),
    Variable("O", domain= domain.copy()),
    Variable("Z", domain= domain.copy())
    
]

#Here are the constraints:
constraints = [
	Constraint("U*10+ N + U*10+ N + N*1000+E*100+U*10+F == O*1000+ N*100+ Z*10 + E"),
    Constraint("U != 0"),
    Constraint("N != 0"),
    Constraint("O != 0"),
    Constraint("U != N"),
    Constraint("U != E"),
    Constraint("U != F"),
    Constraint("U != O"),
    Constraint("U != Z"),
    Constraint("N != E"),
    Constraint("N != F"),
    Constraint("N != O"),
    Constraint("N != Z"),
    Constraint("E != F"),
    Constraint("E != O"),
    Constraint("E != Z"),
    Constraint("F != O"),
    Constraint("F != Z"),
    Constraint("O != Z")
    
    
]

#construct a csp with the variables and constraints
csp = CSP(variables, constraints, init_node = True, init_arc= True, keep_node= True, keep_arc= True)

#Solve the csp and use verbose = True in order to print the search tree
csp.solve(verbose=False)
