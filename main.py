from  math_op import basic_op
from math_op import advanced_op

def main():
    
    while True:
        choice = input("Enter operation or enter \"op\" to get the hint: ")
        
        if choice == "op":
            print("\nOperations:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Average")
            print("6. Power")
            print("7. Square root")
            print("8. Logarithm")
            print("Enter \"exit\" to exit")
            choice = input("\nEnter operation: ")
            continue
        
        elif choice in ["1", "2", "3", "4"]:
            num1 = int(input("\nEnter first number: "))
            num2 = int(input("Enter second number: "))
            
            if choice == "1":
                print(basic_op.add(num1, num2))
            elif choice == "2":
                print(basic_op.substract(num1, num2))
            elif choice == "3":
                print(basic_op.multiply(num1, num2))
            elif choice == "4":
                try:
                    print(basic_op.divide(num1, num2))
                except ValueError as e:
                    print(e)
                    
        elif choice == "5":
            nums = list(map(float, input("\nEnter number seperated by space: ").split()))
            try:
                print(advanced_op.average(nums))
            except ValueError as e:
                print(e)
        
        elif choice == "6":
            base = int(input("\nEnter base: "))
            exponent = int(input("Enter exponent: "))
            print(advanced_op.power(base, exponent))
        
        elif choice == "7":
            num = int(input("\nEnter number: "))
            try:
                print(advanced_op.sqrt(num))
            except ValueError as e:
                print(e)
        
        elif choice == "8":
            num = int(input("\nEnter number: "))
            base = int(input("Enter base: "))
            try:
                print(advanced_op.log(num, base))
            except ValueError as e:
                print(e)
        
        elif choice == "exit":
            break
        
        else:
            print("\nInvalid operation")
            continue
            
if __name__ == "__main__":
    main()