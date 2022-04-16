class Bank:
    userName = ""
    userBalance = 0.00
    transactionFile = ""

    def __init__(self,userName,userBalance = 0.00):
        self.userName = userName
        self.userBalance = userBalance
        self.transactionFile = f"{self.userName}TransactionRecord.txt"

        fileLogWrite = f"UserName:\t{self.userBalance}\nUser Start Balance:\t {self.userBalance}\n\n\n---Transaction Record---\nTransaction\t\tAmount\t\tBalance\n"
        with open(self.transactionFile, "w") as file:
            file.write(fileLogWrite)
    
    def deposit(self,depositAmount):
        self.userBalance = self.userBalance + depositAmount
        with open(self.transactionFile, "a") as file:
            file.write(f"Deposit \t\t{depositAmount}\t\t{self.userBalance}\n")
        return self.userBalance

    def withdraw(self,withdrawAmount):
        self.userBalance = self.userBalance - withdrawAmount
        with open(self.transactionFile, "a") as file:
            file.write(f"Withdraw\t\t{withdrawAmount}\t\t{self.userBalance}\n")
        return self.userBalance

    @property
    def getUserBalance(self):
        return self.userBalance

    @property
    def getUserName(self):
        return self.userName


userName = input("Enter User Name:\n")

# Program will start a loop until it gets a float number for Bank class instantiation
isFloat = False
while not isFloat:
    startingAmount = input("How much would you like to deposit to start the account?\n")
    try:
        startingAmount = float(startingAmount)
        isFloat = True
    except Exception as e:
        print("Please Enter a valid number\t\tError Desc:",type(e))

# Create a Bank Class object
client = Bank(userName,startingAmount)

# Create a isSubSystemRunning to keep the loop running until user chooses to exit
isSubSystemRunning = True

while isSubSystemRunning:
    userCommand = input("\nChoose a task\n+ Press 1 to withdraw \n+ Press 2 to deposit\n+ Press 3 to check Balance\n+ Press 4 to exit\n")
    if userCommand == '1':
        userInput = input("How much would you like to withdraw? \n")
        try:
            userInput = float(userInput)
            client.withdraw(userInput)
        except Exception as e:
            print("Please try again, Please Enter a valid number")
            print("Error Type",type(e))
    elif userCommand=='2':
        userInput = input("How much would you like to deposit? \n")
        try:
            userInput = float(userInput)
            client.deposit(userInput)
        except Exception as e:
            print("Please try again, Please Enter a valid number")
            print("Error Type",type(e))
    elif userCommand=='3':
        print(f"User Current Balance is:\t{client.getUserBalance}")
    elif userCommand=='4':
        print(f"Thank you \t{client.getUserName}")
        isSubSystemRunning = False
    else:
        print("User input not understood, please try again")

    