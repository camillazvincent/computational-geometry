import runpy

while True:
    selection = input("Please select what you would like to do. \n 1. Intersection \n 2. Closest pair \n 3. Convex hull \n 4. Largest Circle \n")

    if selection.startswith('1') or selection.lower().startswith('i'):
        runpy.run_module('intersection.py')
        break
    elif selection.startswith('2') or selection.lower().startswith('cl'):
        break
    elif selection.startswith('3') or selection.lower().startswith('co'):
        runpy.run_module('convex_hull.py')
        break
    elif selection.startswith('4') or selection.lower().startswith('l'):
        runpy.run_module('largest_circle.py')
        break
    else:
        print("Invalid input. Please enter a number between 1 and 4.")

