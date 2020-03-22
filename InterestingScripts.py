#        ======== Bank balance inquiry script ==========

''' import csv

def bank_balance(file_name):
    file_name = input("Enter the file name: ")
    extension = input("what is the extension of your file: ")
    BankData = None
    if extension == "csv":
        StringFileName =file_name+".csv"
    else:
        StringFileName =file_name+".xlsx"
    reader_ = open(StringFileName, 'r')
    reader = csv.reader(reader_)
    BankData = {rows[0]:(rows[1],rows[2]) for rows in reader}
    reader_.close()
    writer_ = open('coors_new.csv', 'w')
    writer = csv.writer(writer_)
    writer_.close()

    def inquiry():
        print ("Enter the customer name,and if you want to finish the inquiry \nType \"STOP\"")
        CustomerName = input("Enter The Customer\'s name : ")
        if CustomerName == "STOP":
            return "n"
        else:
            FullDate = BankData[CustomerName]
            if BankData[CustomerName] in BankData:
                Balance = FullDate[0]
                Date = FullDate[1]
                print("Customer: ",CustomerName," has balance of: $", Balance," as of ",Date)
            # i need some help here to avoid keyerror, 
            #and show the print statement
            else:
                print("No record of customer")


    Quit = inquiry()
    while Quit != "n":
        Quit = inquiry()
        #print("Type y to continue \nor type n to quit")
        #Quit = str(input("Choose y/n: "))
    print("Thanks for visiting Ajax bank!")
    return 0

bank_balance("cv.csv") '''

#       ===== for Arabic writing

# install: pip install --upgrade arabic-reshaper
import arabic_reshaper

# install: pip install python-bidi
from bidi.algorithm import get_display

text = "ذهب الطالب الى المدرسة"
reshaped_text = arabic_reshaper.reshape(text)    # correct its shape
bidi_text = get_display(reshaped_text)           # correct its direction
print(bidi_text)
