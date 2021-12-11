import datetime

currentyear = datetime.date.today().year

def get_income():
    while True:
        try:
            income = int(input("Please enter your taxable income: "))
            return income
        except ValueError:
            print("Sorry, I didn't understand that please enter taxable income as a number")
            continue




def getpensioncontributions():
    while True:
        try:
            deductionpercent = int(input("(Relief at source) What percent pension contributions do you make? "))
            oneoffcontribution = int(input("(one off contribution) How much do you intend to contribute to "
                                           "your pension as a lump sum this tax year? "))
            print("\n")
            return deductionpercent, oneoffcontribution
        except ValueError:
            print("Sorry, please enter your percentage as a number only")
            continue

def getpreviouscontributions():
    while True:
        try:
            madeprevcontributions = (input("Have you made pension contributions in the previous 3 tax years? (please type yes or no) "))
            if madeprevcontributions == 'yes':
                year3 = datetime.date.today().year - 3
                year2 = datetime.date.today().year - 2
                year1 = datetime.date.today().year - 1

                print("Please enter your pension contributions for ", year3)
                year3contribution = int(input())

                print("Please enter your pension contributions for ", year2)
                year2contribution = int(input())

                print("Please enter your pension contributions for ", year1)
                year1contribution = int(input())

                return year3contribution, year2contribution, year1contribution
            elif madeprevcontributions.lower() == 'no':
                print("no worked")
                return
        except ValueError:
            print("Sorry, please enter yes or no only")
            return
            continue


def calculate_adjustedincome(deductionpercent, income, oneoffcontribution):
    basicrate = 0.2
    workplacecontribution = (deductionpercent / 100) * income
    hmrcworkplacecontribution = workplacecontribution * basicrate
    hmrclumpsumcontribution = oneoffcontribution * basicrate
    employeecontribution = workplacecontribution - hmrcworkplacecontribution
    adjustedincome = income - employeecontribution - oneoffcontribution
    return adjustedincome, workplacecontribution, employeecontribution, hmrcworkplacecontribution, hmrclumpsumcontribution

def calculate_tax(adjustedincome):
    basic = 0.2
    higher = 0.4
    additional = 0.45
    basicthreshold = 12570
    higherthreshold = 50270
    additionalthreshold = 150000
    taperthreshold = 100000

    if adjustedincome <= basicthreshold:
        basic_tax = 0
        higher_tax = 0
        additional_tax = 0
        tax = 0
        return tax, basic_tax, higher_tax, additional_tax

    elif adjustedincome > basicthreshold and adjustedincome < higherthreshold:
        basic_tax = (adjustedincome - basicthreshold) * basic
        higher_tax = 0
        additional_tax = 0
        tax = basic_tax
        return tax, basic_tax, higher_tax, additional_tax

    elif adjustedincome > higherthreshold and adjustedincome < additionalthreshold:
        reducedthreshold = 0
        if adjustedincome > taperthreshold:
            taper = (adjustedincome - taperthreshold) / 2
            remainingthreshold = basicthreshold - taper
            reducedthreshold = 12570
            reducedthreshold = reducedthreshold - remainingthreshold
            if reducedthreshold >= basicthreshold:
                reducedthreshold = basicthreshold
        additional_tax = 0
        higher_tax = (adjustedincome - (higherthreshold - reducedthreshold)) * higher
        basic_tax = (higherthreshold - basicthreshold) * basic

        tax = higher_tax + basic_tax
        return tax, basic_tax, higher_tax, additional_tax

    elif adjustedincome >= additionalthreshold:
        taper = (income - taperthreshold) / 2
        remainingthreshold = basicthreshold - taper
        reducedthreshold = 12570
        reducedthreshold = reducedthreshold - remainingthreshold
        if reducedthreshold >= basicthreshold:
            reducedthreshold = basicthreshold
        additional_tax = (adjustedincome - additionalthreshold) * additional
        higher_tax = (additionalthreshold - higherthreshold + reducedthreshold) * higher
        basic_tax = (higherthreshold - reducedthreshold) * basic

        tax = additional_tax + higher_tax + basic_tax
        return tax, basic_tax, higher_tax, additional_tax

def calculate_ni(income):
    lowerlimit = 9568
    upperlimit = 50270
    rate1 = 0.12
    rate2 = 0.02
    if income < lowerlimit:
        ni = 0
        niband1, niband2 = 0, 0
        return ni, niband1, niband2
    elif income >= lowerlimit and income <= upperlimit:
        niband1 = (income - lowerlimit) * rate1
        ni = niband1
        niband2 = 0
        return ni, niband1, niband2
    else:
        niband2 = (income - upperlimit) * rate2
        niband1 = (upperlimit - lowerlimit) * rate1
        ni = niband1 + niband2
        return ni, niband1, niband2

#Main Script## Gets user to input icome, pension contribution % and one off lump sum.  Displays tax breakdown

#User Inputs
income = get_income()
deductionpercent, oneoffcontribution = getpensioncontributions()
year3, year2, year1 = getpreviouscontributions()

#Calculate Functions
adjustedincome, workplacecontribution, employeecontribution, hmrcworkplacecontribution, hmrclumpsumcontribution = calculate_adjustedincome(deductionpercent, income, oneoffcontribution)
tax, basic_tax, higher_tax, additional_tax = calculate_tax(adjustedincome)
nicontributions, band1, band2 = calculate_ni(income)
netincome = income - nicontributions - tax

#Report tax position
print("Your tax position for the year is as follows: \n",
       "\n Income taxed at 20%: ", basic_tax,
       "\n Income taxed at 40%: ", higher_tax,
       "\n Income taxed at 45%: ", additional_tax,
       "\n Total income tax: ", tax,
       "\n NI charged at 12%: ", band1,
       "\n NI charged at 2%: ", band2,
       "\n Total NI contributions: ", nicontributions,
       "\n Total Taxs: ", tax + nicontributions, "Looks like HMRC have had your pants down!",
       "\n \n Your total net annual income is: ", netincome,
       "\n Your net monthly income is: ", netincome / 12)

#Report pension contributions and allowances
print("Your total pension contribution this year is ", (workplacecontribution + oneoffcontribution),
      "\n", employeecontribution, "is deducted directly from your payslip",
      "\n", (oneoffcontribution * 0.8), "was paid in directly by you",
      "\n", (hmrcworkplacecontribution + hmrclumpsumcontribution), "was paid in by HMRC.")

#Report potential savings



# Calculate pension contributions required to avoid tax traps (child benefit, annual allowance)

# Calculate net income as a % of gross income for FIB / IP

# Add Class 2 NI & Dividends to tax calc

# Debt repayment calculator + calculate most efficient route.