import numpy as np
class DataAnalytics:
    def __init__(self):
        self.array=None

    def create_array(self):
        print("Select the type of array to create:")
        print("1. 1D Array\n2. 2D Array\n3. 3D Array")
        choice=int(input("Enter your choice: "))
        if choice==1:
            n=int(input("Enter number of elements: "))
            elements=list(map(int,input(f"Enter {n} elements: ").split()))
            self.array=np.array(elements)
        elif choice==2:
            rows=int(input("Enter number of rows: "))
            cols=int(input("Enter number of columns: ")) 
            elements=list(map(int,input(f"Enter {rows*cols} elements: ").split()))
            self.array=np.array(elements).reshape(rows,cols)
        elif choice==3:
            x=int(input("Enter dimension X: "))
            y=int(input("Enter dimension Y: "))
            z=int(input("Enter dimension Z: "))
            elements=list(map(int,input(f"Enter {x*y*z} elements: ").split()))
            self.array=np.array(elements).reshape(x,y,z)
        else:
            print("Invalid choice")
        print("Array created successfully:\n",self.array)

    def indexing_slicing(self):
        if self.array is None:
            print("No array created yet!")
            return
        print("\nChoose an operation:\n1. Indexing\n2. Slicing\n3. Go Back")
        choice= int(input("Enter your choice: "))
        if choice==1:
            i=int(input("Enter index: "))
            print("Element:",self.array.flat[i])
        elif choice==2:
            if self.array.ndim<2:
                print("Slicing works for 2D/3D arrays only")
                return
            r=input("Enter row range(start:end): ")
            c=input("Enter column range(start:end): ")
            r1, r2 =map(int, r.split(":"))
            c1, c2 =map(int, c.split(":"))
            print("Sliced Array:\n",self.array[r1:r2,c1:c2])

    def mathematical_operations(self):
        if self.array is None:
            print("No array created yet!")
            return
        print("Choose a mathematical operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
        choice=int(input("Enter your choice: "))
        elements=list(map(int, input(f"Enter {self.array.size} elements for another array: ").split()))
        other=np.array(elements).reshape(self.array.shape)
        print("original Array:\n",self.array)
        print("Second Array:\n",other)
        if choice==1:
            print("Result:\n",self.array+other)
        elif choice==2:
            print("Result:\n",self.array-other)
        elif choice==3:
            print("Result:\n",self.array*other)
        elif choice==4:
            if np.any(other==0):
                print("Division by zero not allowed")
            else:
                print(self.array/other)

    def combine_split(self):
        if self.array is None:
            print("No array created yet!")
            return
        print("\nChoose an option:\n1. Combine Arrays\n2. Split Array")
        choice=int(input("Enter your choice: "))
        if choice==1:
            elements=list(map(int,input(f"Enter {self.array.size} elements for another array: ").split()))
            other=np.array(elements).reshape(self.array.shape)
            combined=np.concatenate((self.array,other),axis=0)
            print("Combined Array:\n",combined)
        elif choice==2:
            print("Splitting array into halves...")
            split=np.array_split(self.array,2)
            for part in split:
                print(part) 

    def search_sort_filter(self):
        if self.array is None:
            print("No array created yet!")
            return
        print("\nChoose an option:\n1. Search a value\n2. Sort the array\n3. Filter values")
        choice = int(input("Enter your choice: "))
        if choice==1:
            val=int(input("Enter value to search: "))
            print("Found at positions:",np.where(self.array==val))
        elif choice==2:
            print("Sorted Array:\n",np.sort(self.array))
        elif choice==3:
            threshold=int(input("Enter threshold: "))
            print("Filtered values:\n",self.array[self.array>threshold])
    
    def aggregates_statistics(self):
        if self.array is None:
            print("No array created yet!")
            return
        print("\nChoose an aggregate/statistical operation:")
        print("1. Sum\n2. Mean\n3. Median\n4. Standard Deviation\n5. Variance")
        choice = int(input("Enter your choice: "))
        if choice==1:
            print("Sum:",np.sum(self.array))
        elif choice==2:
            print("Mean:",np.mean(self.array))
        elif choice==3:
            print("Median:",np.median(self.array))
        elif choice==4:
            print("Standard Devaition:",np.std(self.array))
        elif choice==5:
            print("Variance:",np.var(self.array))

def main():
    analyzer=DataAnalytics()
    print("Welcome to the Numpy Analyzer!")
    while True:
        print("\n====================================")
        print("Choose an option:")
        print("1. Create a Numpy Array")
        print("2. Indexing & Slicing")
        print("3. Perform Mathematical Operations")
        print("4. Combine or Split Arrays")
        print("5. Search, Sort, or Filter Arrays")
        print("6. Compute Aggregates and Statistics")
        print("7. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            analyzer.create_array()
        elif choice == 2:
            analyzer.indexing_slicing()
        elif choice == 3:
            analyzer.mathematical_operations()
        elif choice == 4:
            analyzer.combine_split()
        elif choice == 5:
            analyzer.search_sort_filter()
        elif choice == 6:
            analyzer.aggregates_statistics()
        elif choice == 7:
            print("Thank you for using the NumPy Analyzer! Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()









