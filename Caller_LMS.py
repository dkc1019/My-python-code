import Loan_Mngmnt_Sys as lms

l_CustomerName=None
l_CreditScore=None
l_LoanAmount=None
print ('\nHello Dear Customer\n')

while True :
    l_CustomerName= input('Enter your name :')
    if l_CustomerName.isalpha()== False:
        print("That is not a valid Name")
    else:
        break
while True :
    l_CreditScore= input('Enter your CreditScore : ')
    if l_CreditScore.isnumeric()==False:
        print("That is not a valid CreditScore")
    else:
        l_CreditScore= int(l_CreditScore)
        break
while True:
    l_LoanAmount= input ('Enter your LoanAmount : ')
    if l_LoanAmount.isnumeric()==False: 
        print("That is not a valid LoanAmount")
    else:
        l_LoanAmount= int(l_LoanAmount)
        break
    
#print ('\nHello Dear Customer',l_CustomerName,'\n')
lms.Calculate_TotalLoanAmount(l_CreditScore,l_LoanAmount)
