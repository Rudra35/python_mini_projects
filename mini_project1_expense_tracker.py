#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Expense Tracker Project 

expensesList = [] #list of expenses in form of dictionary 
print(" Welcome to Expense Tracker : ")

while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Khrcha")
    print("4. Exit")

    choice= int(input("Please Enter Your Choice : "))

#ADD Expense
    if(choice == 1):
        date= input("Date: ")
        category= input("(Food, Travel, Makeup, Books)?: ")
        description= input("Detail: ")
        amount= float(input("Enter the amount: "))

        expense= {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print(" \n DONE bro. Expense is added succesfully")

# 2. VIEW ALL EXPENSES 
    elif(choice == 2):
        if( len(expensesList)==0 ):
            print("No Expenses Added.")
        else:
            print("===== Ye y apka sara expense ======")
            count= 1
            for eachKharcha in expensesList:
                print(f"Kharcha Number {count} -> {eachKharcha['date']}, {eachKharcha['category']}, {eachKharcha['description']}, {eachKharcha['amount']} ")
                count= count+1

# 3. View TOtal Spending 
    elif(choice == 3):
        total= 0
        for eachKrcha in expensesList:
            total = total + eachKrcha["amount"]

        print("\n TOTAL EXPENSE = ", total)

#4. EXIT 
    elif(choice == 4):
        print("Thank you for using our system")
        break

    else:
        print("INVALID CHOICE. TRY AGAIN")


# In[ ]:





# In[ ]:





# In[ ]:




