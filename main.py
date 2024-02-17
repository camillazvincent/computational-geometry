import runpy

def main():
    '''
    This function lets the user select what they would like to do. Then it executes runs the module that the user selected.
    '''
    while True:
        selection = input("Please select what you would like to do. \n 1. Intersection \n 2. Closest pair \n 3. Convex hull \n 4. Largest Circle \n")

        if selection.startswith('1') or selection.lower().startswith('i'):
            runpy.run_module('intersection')
            break
        elif selection.startswith('2') or selection.lower().startswith('cl'):
            runpy.run_module('closest_pair')
            break
        elif selection.startswith('3') or selection.lower().startswith('co'):
            runpy.run_module('convex_hull')
            break
        elif selection.startswith('4') or selection.lower().startswith('l'):
            runpy.run_module('largest_circle')
            break
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()