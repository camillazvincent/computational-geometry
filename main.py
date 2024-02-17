def intersection():
    print(".")

def closest_pair():
    print(".")

def convex_hull():
    print(".")

def largest_circle():
    print(".")



while True:
    selection = input("Please select what you would like to do. \n 1. Intersection \n 2. Closest pair \n 3. Convex hull \n 4. Largest Circle \n")

    if selection.startswith('1') or selection.lower().startswith('i'):
        intersection()
        break
    elif selection.startswith('2') or selection.lower().startswith('cl'):
        print("The color is yellow.")
        break
    elif selection.startswith('3') or selection.lower().startswith('co'):
        print("The color is blue.")
        break
    elif selection.startswith('4') or selection.lower().startswith('l'):
        print("The color is green.")
        break
    else:
        print("Invalid input. Please enter a number between 1 and 4 or the initial letter.")

