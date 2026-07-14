#PRIVATE (LIKE ) ATTRIBUTES AND METHODS

#Conceptual implementation in python.
                                     #private attributes and methods are means to be used only within the class and are not accessible from outside the class

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

acc1 = Account("1234", "abcd")
print(acc1.acc_no)
print(acc1.__acc_pass)

#To make an information secret just put __ before the information

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("1234", "abcd")
print(acc1.acc_no)
print(acc1.reset_pass())