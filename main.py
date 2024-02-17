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
        closest_pair()
        break
    elif selection.startswith('3') or selection.lower().startswith('co'):
        convex_hull()
        break
    elif selection.startswith('4') or selection.lower().startswith('l'):
        largest_circle()
        break
    else:
        print("Invalid input. Please enter a number between 1 and 4.")

