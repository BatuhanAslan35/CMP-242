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
class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def withdraw(balance, x):
    if balance < x:
        raise CustomError("Not enough money!")
    elif x == 0 or x < 0:
        raise CustomError("The amount cannot be zero or negative.")
    else:
        balance -= x
        return f"Withdrawal successful, Balance = {balance}"

try:
    x = float(input("How much money you want to withdraw = "))
    print(withdraw(1500,x))
except ValueError:
    print("input cannot be Word!")
except CustomError as error:
     print(f"Error handled = {error}")
except CustomError as error:
    print(f"Error handled = {error}")
except Exception:
    print("Something went wrong!")
    
