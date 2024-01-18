#!/usr/bin/env python
# coding: utf-8

# In[1]:


def info():
    # 01 Create a program that displays your name complete mailing address formatted in the manner that you would usually use it on the of an envelop. Your program does not need to read any input from the user
    print('Raj Wahule')
    print('Department of Computer Science')
    print('University of BAMU')
    print('Address:Vikhroli East kannmwar Nagar')
    print('India')

def welcome():
    # 02 Create a program to dsay Hello
    user_name=input('Enter your name here: ')
    print('Hello:', user_name)

def Compute_the_room():
    # 03 Write a program that asks the user to enter the width and length of a room. Once the values have been read. Your program should compute and display the area of the room. The length and the width will be entered as floating point numbers.Include units in your promt and output message; either feet or meters,depending on which unit you are more comfortable working with.
    ##Compute the area of room
    #
    #Read the input values from th user
    width=float(input('Enter the width here of room: '))
    length=float(input('Enter the length here of room: '))
    #comput the area of room
    area=width*length
    #display the result
    print('The area of the room is',area,'sqaure feet')

def compute_the_field():
    # 04 Creat a program that reads the length and width of a farmer's field from the users in feet. Display the area of the field in acres.
    #Compute the area of a field,reporting the resul in acres.
    sqft_per_acre=43560
    #Read input from the user
    length=float(input('Enter the length of field in feet: '))
    width=float(input('Enter the length of field in feet:' ))
    #compute the area in acres
    acres=length*width/sqft_per_acre
    #Display the result
    print('The area of the field is', acres,'acres')

def collectionof_bottle():    
    # 5 In Many juridiction a small deposit is added to drink containers to encourage people to recycle them. In one paricular juridiction, drink containers holdinng one leter or less have a $0.10 deposit, and drink containers holding more than one litre have a $o.25 deposit.

    ## Compute the refund the amount for a collection of bottles.
    less_deposit = 0.10
    more_deposit = 0.25

    # Redad input from the user

    less = int(input('How many containers 1 liter or less do you have? '))
    more = int(input('How many containers more than 1 littre do you have? '))

    # Compute the refund amount
    refund = less * less_deposit + more * more_deposit

    # Display the result
    print('Yore total refund will be $%.2f.' % refund)

def tax_tip():   
    # 6 The program that you creat for theis exetcise will begin b rading the cost of a mesl ordered at a restarant from the user. Then youre program woll compute the rax and tip for the meal. Use your local tax rate when computing the amount of tax and tip for the meal. Use youre local tax rate when copmputing the amoun of tax owing. Coputer the tip as 18 percent of the meal amount (without the tax). The output from your program should include the tax amount, the tip amount, and the grand total for the meal including both the tax and the rip. Format the output so that all of the values are displayed using two decimal places

    # Compute the tax and tip for a restuarant meal.
    tax_rate = 0.05
    tip_rate = 0.18

    # Read the cost of meal from the user
    cost = float(input('Enter the cost of the meal: '))

    # Compute the tax and the tip

    tax = cost * tax_rate
    tip = cost * tip_rate
    total = cost + tax + tip

    # Display the result
    print('The tax is% .2f and the tip is% .2f, making the total% .2f'% (tax, tip, total))

def n_postive_integers():
    #7 Sum of the First n Positive Integers
    # sum=(n)(n+1)/2

    n=int(input('Enter a positive integers:'))

    # Compute the sum
    sum = n*(n+1)/2
    print('The sum of the first',n ,'positive integers is',sum)

def widgets_gizoms():    
    #8 Widgets and Gizmos

    # constants for widget and gizmo per piece
    widget_wt = 75
    gizmo_wt = 112
    # ask user to enter the widgets and gizmos and store them
    widgets = int(input('Enter the number of widgets: '))
    gizmos = int(input('Enter the number of gizmos: '))
    # compute the total weight for the order
    total_wt = widgets * widget_wt + gizmos *gizmo_wt

    # print the total weight of the order in grams
    print('The total weight of the order is', total_wt,'grams.')

def compound_intrest():   
    #9 Compound interest Pretend that you have just opened a new savings account that earns 4 percent intrest per year. The interest that you earn is paid at the end of the year, and is added to the balance of the saingds account. Write a program that begins by reading theamount of money deposited into the account from the userr. Then your program should compute an
    initial_amount = int(input("Enter the initial deposit amount: $"))
    interest_rate = 4  # 4 percent interest rate

    # Calculate and display savings balance for each year
    for year in range(1, 4):
        initial_amount = initial_amount* (1 + interest_rate / 100)
        print(f"After {year} year(s), the balance is: ${initial_amount:.2f}")

def mathematical_poperators():  
    #10 Create a program that reads two integers, a and b, from the user. Your program should compute and display:

    from math import log10
    a=int(input('Eenter the value of a: '))
    b=int(input('Enter the value of b: '))

    print(a, "+", b, "is", a+b)
    print(a,"-", b, "is", a-b)
    print(a,"*",b, "is", a*b)
    print(a, "/", b, "is", a/b)
    print(a,"%", b, "is", a%b)

    #Compute the logarithm and the power
    print("The base 10 logarithm of",a, "is", log10(a))
    print(a, "^", b, "is", a**b)


# In[2]:


#import tkinter library
import tkinter as tk
#creating a main window
window=tk.Tk()
#change title
window.title("Raj Wahule")

#size
window.geometry("730x500")
#label
tk.Label(window,text='pyhton project',font=("Helvetica",21,'bold'),bg='black',fg='white').place(x=250,y=30)
tk.Label(window,text='Made by : Raj Wahule',font=("Helvetica",16,'bold')).place(x=230,y=100)

#bUTTON
tk.Button(window,text='Info',command=info).place(x=50,y=150,width=200,height=25)
tk.Button(window,text='User Welcome',command=welcome).place(x=270,y=150,width=200,height=25)
tk.Button(window,text='Compute the area room',command=Compute_the_room).place(x=490,y=150,width=200,height=25)
tk.Button(window,text='Compute the field',command=compute_the_field).place(x=50,y=200,width=200,height=25)
tk.Button(window,text='Collection of bottle',command=collectionof_bottle).place(x=270,y=200,width=200,height=25)
tk.Button(window,text='tax and tip',command=tax_tip).place(x=490,y=200,width=200,height=25)
tk.Button(window,text='N positive integers',command=n_postive_integers).place(x=50,y=250,width=200,height=25)
tk.Button(window,text='Widgets Gizoms',command=widgets_gizoms).place(x=270,y=250,width=200,height=25)
tk.Button(window,text='Compound interst',command=compound_intrest).place(x=490,y=250,width=200,height=25)
tk.Button(window,text='Mathematical Poperators',command=mathematical_poperators).place(x=50,y=300,width=200,height=25)

#This is necessary to write
window.mainloop()


# In[ ]:




