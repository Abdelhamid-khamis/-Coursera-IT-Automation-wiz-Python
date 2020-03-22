''' import csv

def bank_balance(file_name):
    file_name = str(input("Enter the file name: "))
    extension = str(input("what is the extension of your file: "))
    if extension == "csv":
        StringFileName =file_name+".csv"
    else:
        StringFileName =file_name+".xlsx"
    with open(str(StringFileName), 'r') as infile:
        reader = csv.reader(infile)
        with open('coors_new.csv', 'w') as outfile:
            writer = csv.writer(outfile)
            BankData = {rows[0]:(rows[1],rows[2]) for rows in reader}
            #print(BankData)
    def inquiry():
        print ("Enter the customer name,and if you want to finish the inquiry \nType \"STOP\"")
        CustomerName = str(input("Enter The Customer\'s name : "))
        if CustomerName == "STOP":
            return "n"
        else:
            FullDate = BankData[CustomerName]
            if BankData[CustomerName] in BankData:
                Balance = FullDate[0]
                Date = FullDate[1]
                print("Customer: ",CustomerName," has balance of: $", Balance," as of ",Date)
            else:
                print("No record of customer")


    Quit = ""        
    while Quit != "n":
        Quit = inquiry()
        #print("Type y to continue \nor type n to quit")
        #Quit = str(input("Choose y/n: "))
    print("Thanks for visiting Ajax bank!")

bank_balance("cv.csv")
 '''
''' class Learning:
    def CurrencyChanger(self,DollarAmount,nothing):
        stringConverter= str(DollarAmount) + str(nothing)
        DollarAmount = int(stringConverter)
        AnnualEgyptianPounds = DollarAmount * 17
        MonthlyDollars = int(DollarAmount / 12)
        MonthlyEgyptianPounds = int(AnnualEgyptianPounds / 12)
        print("You\'ll get about",MonthlyDollars,"$/Month")
        print("You\'ll get about",MonthlyEgyptianPounds,"LE/Month")
    CurrencyChanger(112,874)
 '''


'''

>>> bank = {'Laaibah': [208.1, '10/22/2019'], 'Arnold':
[380.999, '9/12/2019'], 'Sioned': [327.01, '1/1/2019'],
'Shayaan': [429.5, '2/28/2019'], 'Renee': [535.29, '4/09/2019'],
'Conal': [726.77, '9/21/2019'], 'Katarina': [730.11,
'10/1/2019'], 'Theodor': [637.12, '10/15/2019'], 'Nadia':
[433.33, '8/29/2019'], 'Jia': ['error, try again later',
'7/23/2019'], 'Sana': [829.99, '10/26/2019']}
>>> answer_queries(bank)
Enter customer name: Laaibah
Customer: Laaibah has balance of: 208.10 as of 10/22/2019
Enter customer name: fred
No record of customer: fred
Enter customer name: Jia
Customer: Jia error: error, try again later
Enter customer name: STOP
Thanks for visiting Ajax bank!
>>>

'''
''' import ezgmail
ezgmail.EMAIL_ADDRESS('abdelhameedkhamis50@gmail.com')
ezgmail.send('abdelhameedkhamis@yahoo.com', 'Automated', 'Hello World') '''

''' a_list = [1, 1, 2, 3, 3]

def find_repetition(s):
    result = []
    for i in s:
        if s.count(i) > 1:
            result.append(i)
    return result

    result = []
    for number in a_list:
        result.append(number)
        for i in range (len(a_list)):
            if 

print(find_repetition(a_list)) '''
print(chr(64))
