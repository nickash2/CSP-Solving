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
csp = CSP(variables, constraints, init_node = False, init_arc=True, keep_node= False, keep_arc=True)

#Solve the csp and use verbose = True in order to print the search tree
csp.solve(verbose=True)
# deg arc off: Number Solutions: 1; Number States visited 4116; Number constraints evaluated 288406
# mrv arc off: Number Solutions: 1; Number States visited 4116; Number constraints evaluated 288406
# normal arc off: Number Solutions: 1; Number States visited 4692; Number constraints evaluated 315406

# deg node off: Number Solutions: 1; Number States visited 693; Number constraints evaluated 421334

# deg both on: Number Solutions: 1; Number States visited 589; Number constraints evaluated 286753
# mrv both on: same
# normal both on: Number Solutions: 1; Number States visited 661; Number constraints evaluated 293648