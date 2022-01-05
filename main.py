class tl():
    def check(self):
        if self.mDay > 200:
            print("Daily meal limit exceeded")
        else:
            print("Under daily meal limit")

        if self.tDay > 200:
            print("Daily travel limit exceeded")
        else:
            print("Under Daily travel limit")

        if self.mMonth > 4000:
            print("Monthly meal limit exceeded")
        else:
            print("Under Monthly meal limit")

        if self.tMonth > 4000:
            print("Monthly travel limit exceeded")
        else:
            print("Under Monthly travel limit")

        if self.mQuat > 10000:
            print("Quarterly meal limit exceeded")
        else:
            print("Under Quarterly meal limit")

        if self.tQuat > 10000:
            print("Quarterly travel limit exceeded")
        else:
            print("Under Quarterly travel limit")

    def details(self):
        self.mDay = int(input("enter daily meal expense = "))
        self.mMonth = int(input("enter monthly meal expense = "))
        self.mQuat = int(input("enter quarterly meal expense = "))
        self.tDay = int(input("enter daily travel expense = "))
        self.tMonth = int(input("enter monthly travel expense = "))
        self.tQuat = int(input("enter quarterly travel expense = "))
        self.check()


class manager():
    def __init__(self):
        self.balMeal = 0
        self.balTravel = 0

    def check(self):
        self.balMeal = 21300 - (self.mDay + self.mMonth + self.mQuat)
        self.balTravel = 21300 - (self.tDay + self.tMonth + self.tQuat)

        if self.balTravel < 0:
            self.balTravel = 0

        if self.balMeal < 0:
            self.balMeal = 0

        if self.mDay > 300:
            print("Daily meal limit exceeded")
        else:
            print("Under daily meal limit")

        if self.tDay > 300:
            print("Daily travel limit exceeded")
        else:
            print("Under Daily travel limit")

        if self.mMonth > 6000:
            print("Monthly meal limit exceeded")
        else:
            print("Under Monthly meal limit")

        if self.tMonth > 6000:
            print("Monthly travel limit exceeded")
        else:
            print("Under Monthly travel limit")

        if self.mQuat > 15000:
            print("Quarterly meal limit exceeded")
        else:
            print("Under Quarterly meal limit")

        if self.tQuat > 15000:
            print("Quarterly travel limit exceeded")
        else:
            print("Under Quarterly travel limit")

    def update(self):
        self.mDay = 300
        self.mMonth = 6000
        self.mQuat = 15000 + self.balMeal
        self.tQuat = 15000 + self.balTravel
        self.tDay = 300
        self.tMonth = 6000

    def details(self):
        self.mDay = int(input("enter daily meal expense = "))
        self.mMonth = int(input("enter monthly meal expense = "))
        self.mQuat = int(input("enter quarterly meal expense = "))
        self.tDay = int(input("enter daily travel expense = "))
        self.tMonth = int(input("enter monthly travel expense = "))
        self.tQuat = int(input("enter quarterly travel expense = "))

        print()

        self.check()

        if self.balMeal == 0 or self.balTravel == 0:
            print("your no balance in your account")
        elif self.balMeal != 0 and self.balTravel == 0:
            print(f"you have {self.balMeal} balance in your account and no balance in travel allowance")
        elif self.balMeal == 0 and self.balTravel != 0:
            print(f"you have {self.balTravel} balance in your account and no balance in Meal allowance")
        else:
            print(f"you have an excessive of {self.balMeal} in your meal allowance and {self.balTravel} in travel "
                  f"allowance")

        self.update()


name = input("enter name of the employee = ")
position = input("enter position of employee = ")

if position == "manager":
    name = manager()
    name.details()
else:
    name = tl()
    name.details()
