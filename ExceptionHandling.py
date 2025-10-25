'''
try:
    a = int(input("a = "))
    b = int(input("b = "))
    print(a/b)
except ZeroDivisionError:
    print("input cannot be 0")
except ValueError:
    print("input cannot be Word")
except Exception:
    print("error")
finally:
    print("check your input")
'''
# We're creating our own custom error class
class CustomError(Exception):
    def __init__(self, message):
        self.message = message  # we're saving the error message
        super().__init__(self.message)  # and passing it to the base Exception class


# This function handles the withdrawal process
def withdraw(balance, x):
    # We're checking if there's not enough balance
    if balance < x:
        raise CustomError("Not enough money!")  # we raise a custom error
    # We're checking if the amount is zero or negative
    elif x == 0 or x < 0:
        raise CustomError("The amount cannot be zero or negative.")  # another custom error
    else:
        # We're subtracting the withdrawal amount from the balance
        balance -= x
        # We're returning a success message
        return f"Withdrawal successful, Balance = {balance}"


# We're wrapping the main code in a try-except block
try:
    # We're asking the user how much they want to withdraw
    x = float(input("How much money you want to withdraw = "))
    # We're trying to make the withdrawal and print the result
    print(withdraw(1500, x))
# We're catching input errors when the user types something that's not a number
except ValueError:
    print("input cannot be Word!")
# We're catching any custom errors (like not enough money or invalid amount)
except CustomError as error:
    print(f"Error handled = {error}")
# We're catching any other unexpected errors
except Exception:
    print("Something went wrong!")
