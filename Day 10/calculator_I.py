def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {
    "+" : add,
    "-" : sub,
    "*" : multiply,
    "/" : divide
}

num1 = int(input("Input the Number 1:\n"))

for symbols in operations:
    print(symbols);
operation_symbol = ""
answer = num1
another = "Y"
while another=="Y":
    operation_symbol = input("Pick an operation from the symbols above\n")
    num2 = int(input("Input the next number:\n"))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(answer,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    num1=answer
    another = input("Do you want to continue to next operation?(Y/N)\n")
    
print("Calculator Shut down!")