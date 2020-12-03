from ortools.linear_solver import pywraplp

import diet

IDX_NAME = 0
IDX_UNIT = 1
IDX_PRICE = 2
IDX_CALORIES = 3
IDX_PROTEIN = 4
IDX_CALCIUM = 5
IDX_IRON = 6
IDX_VITAMIN_A = 7
IDX_THIAMINE = 8
IDX_RIBOFLAVIN = 9
IDX_NIACIN = 10
IDX_ASCORBIC_ACID = 11

IDX_NUTRIENTS_MIN = 1

def required_index(i):
    return i+3

def GetOptimalDiet():
    solver = pywraplp.Solver.CreateSolver('stigler_diet', 'GLOP')
    nutrients_list = diet.nutrients
    food_list = diet.data

    nutrVars = []
    foodVars = []

    constraints = []

    # for item in nutrients_list:
    #     nutr = solver.NumVar(item[IDX_NUTRIENTS_MIN], solver.infinity(), item[IDX_NAME])
    #     nutrVars.append(nutr)

    # print(' ')

    print(' ')
    print('VARIABLES')
    print(' ')
    
    for item in food_list:
        food = solver.NumVar(0, solver.infinity(), item[IDX_NAME])
        foodVars.append(food)

    print(' ')
    print('CONSTRAINTS')
    print(' ')
    
    index = 0
    for nutrient in nutrients_list:
        constraint = solver.Constraint(nutrient[IDX_NUTRIENTS_MIN], solver.infinity())
        
        ifood = 0
        for food in foodVars:
            constraint.SetCoefficient(food, food_list[ifood][index + IDX_CALORIES])
            ifood += 1
        
        constraints.append(constraint)
        index += 1
        # print('')
        # print(nutrient[IDX_NAME] + ' > ' + str(nutrient[IDX_NUTRIENTS_MIN]))
        # print(nutrient[IDX_NAME] + ' =')
        
        # for item in food_list:
        #     print(str(item[required_index(index)])+' * qnt('+item[IDX_NAME]+') ')
        

        

    print('')
    print('')
    print('')
    print('MINIMIZE')
    print('price = ')
    
    objective = solver.Objective()
    
    for item in foodVars:
        objective.SetCoefficient(item, 1)

    solver.Solve()

    print('SOLUTION')
    index = 0
    for food in foodVars:
        print(str(index) + ' ' + food_list[index][IDX_NAME] + ' = ' + str(food.solution_value()))
        index += 1

        #print(str(item[IDX_PRICE])+' * qnt('+item[IDX_NAME]+') ')       

GetOptimalDiet()