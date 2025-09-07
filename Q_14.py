import numpy as np

def read_matrix(p, q, r):
    print(f"\nEnter elements for a {p}x{q}x{r} matrix:")
    arr = []
    for i in range(p):
        layer = []
        print(f"Layer {i+1}:")
        for j in range(q):
            row = list(map(int, input(f" Row {j+1}: ").split()))
            if len(row) != r:
                print(" Please enter exactly", r, "numbers.")
                return None
            layer.append(row)
        arr.append(layer)
    return np.array(arr)

def display_matrix(name, mat):
    print(f"\n{name}:")
    print(mat)

def menu():
    print("\nMenu:")
    print("1. Read Matrices")
    print("2. Display Matrices")
    print("3. Sum of Matrices")
    print("4. Transpose of Matrix 1")
    print("5. Product of Matrices")
    print("6. Exit")

# --- Main Program ---
p = int(input("Enter p (layers): "))
q = int(input("Enter q (rows): "))
r = int(input("Enter r (columns): "))

mat1 = None
mat2 = None

while True:
    menu()
    choice = int(input("Enter choice: "))

    if choice == 1:
        mat1 = read_matrix(p, q, r)
        mat2 = read_matrix(p, q, r)
    elif choice == 2:
        if mat1 is not None and mat2 is not None:
            display_matrix("Matrix 1", mat1)
            display_matrix("Matrix 2", mat2)
        else:
            print("Please read matrices first.")
    elif choice == 3:
        if mat1 is not None and mat2 is not None:
            print("\nSum of Matrices:")
            print(mat1 + mat2)
        else:
            print("Please read matrices first.")
    elif choice == 4:
        if mat1 is not None:
            print("\nTranspose of Matrix 1 (swap rows & cols in each layer):")
            print(np.transpose(mat1, (0, 2, 1)))
        else:
            print("Please read matrices first.")
    elif choice == 5:
        if mat1 is not None and mat2 is not None:
            print("\nProduct of Matrices (element-wise):")
            print(mat1 * mat2)
        else:
            print("Please read matrices first.")
    elif choice == 6:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")