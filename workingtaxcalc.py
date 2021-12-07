def get_income():
    while True:
        try:
            income = int(input("Please enter your taxable income: "))
        except ValueError:
            print("Sorry, I didn't understand that please enter taxable income as a number")
            continue
        else:
            break
    return income

def getpensioncontributions():
    while True:
        try:
            deductionpercent = int(input("(Relief at source) What percent pension contributions do you make? "))
            return deductionpercent
        except ValueError:
            print("Sorry, please enter your percentage as a number only")
            continue
        else:
            break

def reliefatsource(deductionpercent, income):
    basicrate = 0.2
    totalcontribution = (deductionpercent / 100) * income
    hmrccontribution = totalcontribution * basicrate
    employeecontribution = totalcontribution - hmrccontribution


    print("Your total pension contribution is ", totalcontribution)
    print("Out of that contribution,", employeecontribution, "is deducted from your salary and HMRC pay an additional", hmrccontribution, "into your pension.")

    income = income - hmrccontribution

    return income



def calculate_tax(income):
    basic = 0.2
    higher = 0.4
    additional = 0.45
    basicthreshold = 12570
    higherthreshold = 50270
    additionalthreshold = 150000
    taperthreshold = 100000

    if income <= basicthreshold:
        return 0

    elif income > basicthreshold and income < higherthreshold:
        basic_tax = (income - basicthreshold) * basic
        print("tax at 20%", basic_tax)
        tax = basic_tax
        return tax

    elif income > higherthreshold and income < additionalthreshold:
        reducedthreshold = 0
        if income > taperthreshold:
            taper = (income - taperthreshold) / 2
            remainingthreshold = basicthreshold - taper
            reducedthreshold = 12570
            reducedthreshold = reducedthreshold - remainingthreshold
            if reducedthreshold >= basicthreshold:
                reducedthreshold = basicthreshold
                print("basic threshold for higher earner reduced by: ", reducedthreshold)

        higher_tax = (income - (higherthreshold - reducedthreshold)) * higher
        basic_tax = (higherthreshold - reducedthreshold) * basic
        tax = higher_tax + basic_tax
        print ("tax at 40%", higher_tax)
        print ("tax at 20%", basic_tax)
        return tax

    elif income >= additionalthreshold:
        taper = (income - taperthreshold) / 2
        remainingthreshold = basicthreshold - taper
        reducedthreshold = 12570
        reducedthreshold = reducedthreshold - remainingthreshold
        if reducedthreshold >= basicthreshold:
            reducedthreshold = basicthreshold
            print("basic threshold for higher earner reduced by: ", reducedthreshold)

        additional_tax = (income - additionalthreshold) * additional
        print ("tax at 45%: ", additional_tax)
        (higherthreshold - reducedthreshold) * higher
        higher_tax = (additionalthreshold - higherthreshold + reducedthreshold) * higher
        basic_tax = (higherthreshold - reducedthreshold) * basic
        tax = additional_tax + higher_tax + basic_tax
        print ("tax at 40%", higher_tax)
        print ("tax at 20%", basic_tax)
        return tax


def calculate_ni(income):
    lowerlimit = 9568
    upperlimit = 50270
    rate1 = 0.12
    rate2 = 0.02
    if income < lowerlimit:
        ni = 0
        return ni
    elif income >= lowerlimit and income <= upperlimit:
        ni = (income - lowerlimit) * rate1
        return ni
    else:
        band2 = (income - upperlimit) * rate2
        band1 = (upperlimit - lowerlimit) * rate1
        ni = band1 + band2
        return ni







#Main Script
income = get_income()
deductionpercent = getpensioncontributions()
reliefatsource(deductionpercent, income)
tax = calculate_tax(income)
nicontributions = calculate_ni(income)

netincome = income - nicontributions - tax

print ("your income tax for the year is:", tax)
print ("your national insurance contributions for the year are: ", nicontributions)
print ("\n","your total net annual income is: ", netincome)
print ("your net monthly income is: ", netincome / 12)



