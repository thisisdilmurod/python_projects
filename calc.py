#Calculator

#Add
def add(n1, n2):
  return n1 + n2

  
#Substract
def substract(n1, n2):
  return n1 - n2


#Multiply
def multiply(n1, n2):
  return n1 * n2


#Divide
def divide(n1, n2):
  return n1 / n2


operations = {"+": add, "-": substract, "*": multiply, "/": divide,}
def calculation():
  
  num1 = float(input("What's the first number?\n"))

  for symbols in operations:
    print(symbols)
  should_continue = True


  while should_continue:

    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the second number?\n"))
    calc_function = operations[operation_symbol]
    ans = float(calc_function(num1, num2))

    print(f"{num1} {operation_symbol} {num2} = {ans}")

    if input(f"Type 'y' to continue calculating with {ans}, or type 'y' to exit: ") == "y":
      num1 = ans
    else:
      should_continue = False
      calculation()

calculation()