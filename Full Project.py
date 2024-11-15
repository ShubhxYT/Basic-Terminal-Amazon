import csv
import pickle

yes_l = ["YES",'yes','Yes','Y','y']
no_l = ['NO','no','No','N','n']

try:
    f=open('cart.txt','rb')
    cart1=pickle.load(f)
    f.close()
except:
    cart1=[]

def c_save(lst): #Cart saver
    f=open('cart.txt','wb')
    pickle.dump(lst,f)
    f.close()
    
def Try(line): #int or str checker
    t=True
    while t!=False:
        try:
            opt=int(input(line))
            return opt
            t=False
        except:
            print("Please Enter a valid option\n")
            
def start(): #starting page
    print("""
Which one of the following you want to perform :
Enter:1 To open your cart
Enter:2 To start adding items in your cart
""")
    o=True
    while o!=False:
        ans = Try("What do you want to perform : ")
        if ans == 1:
            cart(cart1)
            break
        elif ans == 2:
            items()
            break
        else:
            print("Please enter a valid option\n")
            
def items(): #to show all the types of items
    g=True
    print("""
Which one of the following you want to search for:
Enter:1 Mobiles
Enter:2 Tabs(iPads)
Enter:3 Earbuds
Enter:4 Smart Watches
Enter:5 Laptops
Enter:6 EXIT\n""")
    while g!=False:
        choice = Try("Which one you want to search for : ")
        if choice == 1:
            mobile()
            break
        elif choice == 2:
            tab()
            break
        elif choice == 3:
            earbuds()
            break
        elif choice == 4:
            smart_w()
            break
        elif choice == 5:
            laptop()
            break
        elif choice == 6:
            print("Thank You for using the Program")
            break
        else:
            print("Please enter a valid option\n")
        
def menu_c(lst): #menu creator
    sno=1
    if len(lst)>1:
        q=True
        line=1
    else:
        q=False
    print("""
==============================================================================
 SNo.    Brand               Name                               Price(INR)  
==============================================================================""")
    
    for x in lst:
        print(' ',sno,'   ',x[1],'   ',x[2],)
        if int(x[0])==1:
            price = convertor(int(x[3]))
            print('\t\t\t\t\t\t\t\t',price)
            sno+=1
            
        elif int(x[0])>1: #Quantity checker
            price = convertor(int(x[3]))
            print('\t\t\t\t\t\t\t\t',price,' x ',x[0],sep='')
            sno+=1
        
        if q==True:
            if line < len(lst):
                line+=1
                print("------------------------------------------------------------------------------")
    print("==============================================================================")

def cart(lst): #all the cart related operations
    cont=''
    if len(lst)==0: # Empty Cart Checker
        print()
        print("Your Cart is Empty")
        print("Add items to your Cart to see them")
        print("Being Forwarded toward the item list.....")
        items()
        cont='no'
    elif cont=='no': #Code finisher
        print()
    else:
        print("Number of items in your list :",len(lst))
        T=[]
        for t in lst: #Total price list maker
            if int(t[0])==1:
                T.append(int(t[3]))
            elif int(t[0])>1: #quantity checker
                pp=int(t[3])*int(t[0])
                T.append(pp)
        total=convertor(sum(T))
        print("Total Value of your items :",total)
        menu_c(lst) #menu creator
        print("""
Which one of the following you want to perform now :
Enter:1 Add more items to your Cart
Enter:2 Choose the number of quantity of an item
Enter:3 Delete any item from your Cart
Enter:4 Proceed to Checkout
Enter:5 Save your Cart items\n""")
        j=True
        while j!=False:
            p = Try("Which one do you want to perform : ")
            if p == 1: #add more items to the cart
                items()
                j=False
            elif p == 2:#choose the number of quantities
                no=1
                for i in lst:
                    if int(i[0])==1:
                        print(no,'. ---> ',i[2],sep="")
                        no+=1
                    elif int(i[0])>1:
                        print(no,'. ---> ',i[2],' x ',i[0],sep="")
                        no+=1
                print()
                q=True
                while q!=False:
                    choice = Try("Which item you want to increase the quantity of : ")
                    if choice > len(lst):
                        print("Please enter a valid option\n")
                    elif choice <= 0 :
                        print("Please enter a valid option\n")
                    else:
                        choice-=1
                        quan = Try("How much quantity you want : ")
                        if quan<=0:
                            lst.pop(choice)
                            c_save(lst)
                            cart(lst)
                            q=False
                            j=False
                        else:
                            pos_int=int(lst[choice][0])
                            lst[choice][0]=str(quan)
                            c_save(lst)
                            cart(lst)
                            q=False
                            j=False
            elif p == 3 : #To delete an item from the cart
                no = 1
                print("Which one of the following you want to remove :\n")
                for i in lst:
                    if int(i[0])==1:
                        print(no,'. ---> ',i[2],sep="")
                        no+=1
                    elif int(i[0])>1:
                        print(no,'. ---> ',i[2],' x ',i[0],sep="")
                        no+=1
                print()
                r=True
                while r!=False:
                    choice = Try("What do you choose ? : ")
                    print()
                    if choice > len(lst):
                        print("Please enter a valid option\n")
                    elif choice <= 0 :
                        print("Please enter a valid option\n")
                    else:
                        choice-=1
                        lst.pop(choice)
                        c_save(lst)
                        r=False
                        j=False
                        print("Your Cart Now")
                        cart(lst)
                    
            elif p == 4: #Proceed to checkout with all the cart items c_save(lst)
                checkout(lst)
                delivery(lst)
                j=False
            elif p == 5: #To just save the items and end the program
                c_save(lst)
                print()
                print("All your items are been saved")
                print("Thank you for using the program")
                j=False
            else:
                print("Please Enter a valid option\n")

            
def checkout(lst): #cart or item checkout
    menu_c(lst)
    t_price = []
    for t in lst:
        if int(t[0])==1: #price checker if only one quantity
            t_price.append(int(t[3]))
        elif int(t[0])>1: #price checker if multiple quantities
            pp=int(t[3])*int(t[0])
            t_price.append(pp)
        
    t_p = sum(t_price)
    gst = int(round((t_p*18/100),2)) 
    gst_c = convertor(gst)
    total = int(t_p+gst)
    total_c = convertor(total)
    
    print(""" GST(18%)\t\t\t\t\t\t\t""",gst_c,"""
==============================================================================
 Total\t\t\t\t\t\t\t\t""",total_c,"""
==============================================================================\n""")
    
def delivery(cart):
    print("Proceeding to the Delivery system")
    print("""
what you want to proceed:
Enter:1 Deliver to a new address
Enter:2 Deliver to an already saved address\n""")
    d=True
    while d!=False:
        Del=Try("What do you want to proceed : ")
        if Del==1:
            dell_new()
            delivery(cart)
            d=False
        elif Del==2:
            try:
                f1=open("address.txt","rb")
                add = pickle.load(f1)
                f1.close()
            except:
                add=[]
            if len(add)<=0:
                print("You Don't have any saved Addresses")
                print("Please add an address to continue")
                print("Being forwarded to adding a new address....")
                dell_new()
                delivery(cart)
                d=False
            elif len(add)>0:
                add_menu_c(add)
                print("SNo :",(len(add)+1),"""
\tTo add a new Address in the system\n""")
                print("SNo :",(len(add)+2),"""
\tTo delete a an Address from the system\n""")
                s=True
                while s != False:
                    inp=Try("Which address you want to choose : ")
                    if inp > (len(add)+2):
                        print("Please choose a valid option\n")
                    elif inp == (len(add))+1:
                        dell_new()
                        print("""
what you want to proceed:
Enter:1 Deliver to a new address
Enter:2 Deliver to an already saved address\n""")
                        s=False
                    elif inp == (len(add))+2:
                        dell_del()
                        print("""
what you want to proceed:
Enter:1 Deliver to a new address
Enter:2 Deliver to an already saved address\n""")
                        s=False
                    elif inp <= 0 :
                        print("Please choose a valid option\n")
                    else:
                        inp=int(inp)-1
                        add_c=add[inp] #address chosed list
                        print("You Chose : ")
                        print(""" Name : """,add_c[0],"""
 Phone : """,add_c[1],"""
 Address : """,add_c[2],"""
 State : """,add_c[3],"""
 City : """,add_c[4],"""
 Pincode : """,add_c[5],"\n")
                        total_deliv_checkout(cart,add_c)
                        s=False
                        d=False
        else:
            print("Please enter a valid option\n")
   
def dell_new(): #new address maker
    try:
        f=open("address.txt","rb")
        add_s = pickle.load(f)
        f.close()
    except:
        add_s=[]
    print("Please fill the following to proceed\n")
    name=input("Enter your name : ")
    p=True
    while p!=False:
        phone=Try("Enter your Phone No. : ")
        if len(str(phone))==10:
            p=False
        else:
            print("Please enter a valid phone number")
    add=input("Address : ")
    state=input("State : ")
    city=input("City : ")
    pin = input("Pincode : ")
    address=[name,phone,add,state,city,pin]
    add_s.append(address)
    f1=open("address.txt","wb")
    pickle.dump(add_s,f1)
    f1.close()
    print()
    print("Address saved\n")

def dell_del():
    f=open('address.txt','rb')
    add_s=pickle.load(f)
    f.close()
    add_menu_c(add_s)
    c=True
    while c != False:
        choice=Try("Which one do you choose : ")
        if choice > len(add_s):
            print("Please choose a valid option\n")
        elif choice <= 0 :
            print("Please choose a valid option\n")
        else:
            choice-=1
            conf=True
            while conf!=False:
                conform = input("Are you sure you want to delete this card info? (Yes or No pls) : ")
                if conform in yes_l:
                    add_s.pop(choice)
                    f1=open('address.txt','wb')
                    pickle.dump(add_s,f1)
                    f1.close()
                    print("Address info deleted successfully")
                    print("Forwarding you back to the address system.....\n")
                    conf=False
                elif conform in no_l:
                    print("OK Forwarding you back to address choosing system.....\n")
                    conf=False
                else:
                    print("Please type a valid answer\n")
                c=False

def total_deliv_checkout(lst,address):
    print("""Which Payment option you want to choose :
Enter:1 Pay On Dilvery
Enter:2 Debit/Credit Card\n""")
    pay=True
    while pay!=False:
        p_opt=Try("Which payment option you choose : ")
        if p_opt == 1:
            payment=["Pay On Delivery (POD)"]
            pay=False
        elif p_opt == 2:
            payment=card_pay()
            pay=False
        else:
            print("Please choose a valid option\n")
    print()
    print()
    print("Your Items - \n")
    checkout(lst)
    print()
    if len(payment)==1:
        print("Your Payment Method -",payment[0],'\n')
    elif len(payment)==3:
        print("Your Payment Method - Credit/Debit Card")
        print("Card info - ")
        lst_card=[]
        for x in payment[1]:
            lst_card.append(x)
        card_hide_lst=[lst_card[0],lst_card[1],lst_card[2],lst_card[3]," ",lst_card[4],lst_card[5],'XX XXXX X',lst_card[13],lst_card[14],lst_card[15]]
        card_hide="".join(card_hide_lst)
        print("""\tName : """,payment[0],"""
\tCard No. : """,card_hide,"\n")
    print("Thank You For Ordering")
    if len(lst)>1:
        lst2=[]
        c_save(lst2) #cart emptier
    
def card_pay(): #card payment system
    z=True
    while z!= False:
        try:
            f=open('card.txt','rb')
            cards=pickle.load(f)
            f.close()
        except:
            cards=[]
        if len(cards)==0:
            print("No Payment Cards are saved")
            print("Please add one to proceed")
            card_create()
        elif len(cards)>0:
            card_menu_c(cards)
            print("SNo :",(len(cards)+1),"""
\tTo add a new Debit/Credit Card\n""")
            print("SNo :",(len(cards)+2),"""
\tTo delete a Debit/Credit Card info from the system\n""")
            c=True
            while c != False:
                choice=Try("Which one do you choose : ")
                if choice > (len(cards)+2):
                    print("Please choose a valid option\n")
                elif choice == (len(cards))+1:
                    card_create()
                    c=False
                elif choice == (len(cards))+2:
                    card_delete()
                    c=False
                elif choice <= 0 :
                    print("Please choose a valid option\n")
                else:
                    choice-=1
                    #print(cards[choice]) #Just to get the hidden CVV for testing
                    cv=True
                    t=3
                    while cv!=False:
                        cvv_check = Try("Enter The CVV to Proceed with the payment : ")
                        if cvv_check == int(cards[choice][2]):
                            print("Confirmation completed\n")
                            cv=False
                            z=False
                            return cards[choice]
                        elif t==0:
                            print("Incorrect CVV\n")
                            print("You have succeeded the number of attempts")
                            print("Forwarding you back to the card choosing system.....\n")
                            cv=False
                        else:
                            print("Incorrect CVV")
                            t-=1
                            print(t+1,'attempts are left\n')
                c=False
                
def card_menu_c(cards): #card menu creator
    sno=1
    for i in cards:
        lst_card=[]
        for x in i[1]:
            for y in x:
                lst_card.append(y)
        card_hide_lst=[lst_card[0],lst_card[1],lst_card[2],lst_card[3]," ",lst_card[4],lst_card[5],'XX XXXX X',lst_card[13],lst_card[14],lst_card[15]]
        card_hide="".join(card_hide_lst)
        print("""SNo :""",sno,"""
\tName : """,i[0],"""
\tCard No. : """,card_hide,"""
\tCVV : """,'XXX',"\n")
        sno+=1
def card_delete(): #Card info deleter
    f=open('card.txt','rb')
    cards=pickle.load(f)
    f.close()
    card_menu_c(cards)
    c=True
    while c != False:
        choice=Try("Which one do you choose : ")
        if choice > len(cards):
            print("Please choose a valid option\n")
        elif choice <= 0 :
            print("Please choose a valid option\n")
        else:
            choice-=1
            conf=True
            while conf!=False:
                conform = input("Are you sure you want to delete this card info? (Yes or No pls) : ")
                if conform in yes_l:
                    cards.pop(choice)
                    f1=open('card.txt','wb')
                    pickle.dump(cards,f1)
                    f1.close()
                    print("Card info deleted successfully")
                    print("Forwarding you back to Card payment system.....")
                    conf=False
                elif conform in no_l:
                    print("OK Forwarding you back to Card payment system.....")
                    conf=False
                else:
                    print("Please type a valid answer\n")
                c=False
    
def card_create(): #Debit/Credit card adder
    try:
        f=open('card.txt','rb')
        cards=pickle.load(f)
        f.close()
    except:
        cards=[]
    print("Please fill the following to add a card : ")
    name=input("Card Holder Name : ")
    c=True
    while c!=False:
        card_no = Try("Card number : ")
        card_no=str(card_no)
        c_no = 0
        for x in card_no:
            c_no+=1
        if c_no == 16:
            c=False
        else:
            print("Card number you entered is not valid\n")
    cv=True
    while cv!=False:
        cvv=Try("CVV no : ")
        cvv=str(cvv)
        cv_n = 0
        for x in cvv:
            cv_n+=1
        if cv_n==3:
            cv=False
        else:
            print("CVV number you enytered is not valid\n")
    print(cards)
    lst=[name,card_no,cvv]
    cards.append(lst)
    f1=open('card.txt','wb')
    pickle.dump(cards,f1)
    f1.close()
    print("Your Card have succesfully been added to our system\n")
    print("Proceeding you back to card choosing system....")

def add_menu_c(lst):#Address Menu Creator
    sno=1
    lst2=[]
    print("All saved Addresses are : \n")
    for i in lst:
        print("""SNo :""",sno,"""
\tName : """,i[0],"""
\tPhone : """,i[1],"""
\tAddress : """,i[2],"""
\tState : """,i[3],"""
\tCity : """,i[4],"""
\tPincode : """,i[5],"\n")
        sno+=1
    
def proceed(lst): #mid stuff
    menu_c(lst)
    s=True
    while s != False:
        inp=Try("Which one do you want : ")
        if inp > len(lst):
            print("Please choose a valid option\n")
        elif inp <= 0 :
            print("Please choose a valid option\n")
        else:
            inp=int(inp)-1
            print("""
Which one of the following you want to perform :
Enter:1 Add the item in your cart
Enter:2 Proceed to the Checkout (with this item only)\n""")
            x=True
            while x != False:
                opt = Try("Which one of the following you want to perform : ")
                if opt == 1:
                    print("""
Your Item""",lst[inp][2],"""have been added to your cart""")
                    cart1.append(lst[inp])
                    c_save(lst)
                    print("""
Which one of the following you want to perform :
Enter:1 See your Cart
Enter:2 Add more items to your cart\n""")
                    y = True
                    while y != False:
                        a = Try("Which one of the following you want to perform : ")
                        if a == 1:
                            cart(cart1)
                            s=False #to break all the loops
                            x=False
                            y=False
                        elif a == 2:
                            items()
                            s=False
                            x=False
                            y=False
                        else:
                            print("Please choose a valid option\n")
                elif opt == 2 :
                    one_item = [lst[inp]]
                    checkout(one_item)
                    delivery(one_item)
                    s=False
                    break
                else:
                    print("Please choose a valid option\n")
                    
def smart_w(): #smart watches Brands
    lst=[]
    f=open("smart_w.csv","r")
    c=csv.reader(f)
    for i in c:
        lst.append(i)
    print("""
Which one of the following brand you want to search for
Enter:1 Samsung
Enter:2 Apple\n""")
    sw=True
    while sw!=False:
        choice=Try("Which one you want to search for : ")
        if choice==1:
            lst2=[]
            for x in lst:
                if x[1]=='Samsung':
                    lst2.append(x)
            proceed(lst2)
            sw=False
        elif choice==2:
            lst2=[]
            for x in lst:
                if x[1]=='Apple':
                    lst2.append(x)
            proceed(lst2)
            sw=False
        else:
            print("Please enter a valid option\n")

def earbuds(): #for earbuds brands
    lst=[]
    f=open("earbuds.csv","r")
    c=csv.reader(f)
    for i in c:
        lst.append(i)
    print("""
Which one of the following brand you want to search for
Enter:1 Samsung
Enter:2 Apple
Enter:3 Oneplus\n""")
    e=True
    while e!=False:
        choice=Try("Which one you want to search for : ")
        if choice==1:
            lst2=[]
            for x in lst:
                if x[1]=='Samsung':
                    lst2.append(x)
            proceed(lst2)
            e=False
        elif choice==2:
            lst2=[]
            for x in lst:
                if x[1]=='Apple':
                    lst2.append(x)
            proceed(lst2)
            e=False
        elif choice==3:
            lst2=[]
            for x in lst:
                if x[1]=='Oneplus':
                    lst2.append(x)
            proceed(lst2)
        else:
            print("Please enter a valid option\n")
def tab(): #for tabs brand and series list
    lst=[]
    f=open("tabs.csv","r")
    c=csv.reader(f)
    for i in c:
        lst.append(i)
    print("""
Which one of the following brand you want to search for
Enter:1 Samsung
Enter:2 Apple\n""")
    t=True
    while t!=False:
        choice = Try("Which one you want to search for : ")
        if choice == 1:
            lst2=[]
            print("""
Which one of the following series :
Enter:1 S Series
Enter:2 A series\n""")
            sa=True
            while sa!=False:
                sa_c=Try("Which of the Series of Tabs you want to search for ? : ")
                if sa_c == 1:
                    for x in lst:
                        if x[1]=='Samsung':
                            if x[4]=='S':
                                lst2.append(x)
                    proceed(lst2)
                    t=False
                    sa=False
                elif sa_c == 2:
                    for x in lst:
                        if x[1]=='Samsung':
                            if x[4]=='A':
                                lst2.append(x)
                    proceed(lst2)
                    t=False
                    sa=False
                else:
                    print("Please enter a valid option\n")
        elif choice == 2:
            lst2=[]
            print("""
Which one of the following series :
Enter:1 PRO Series
Enter:2 AIR series
Enter:3 Other series\n""")
            o=True
            while o!=False:
                o_c=Try("Which of the Series of Tabs you want to search for ? : ")
                if o_c == 1:
                    for x in lst:
                        if x[1]=='Apple':
                            if x[4]=='PRO':
                                lst2.append(x)
                    proceed(lst2)
                    t=False
                    o=False
                elif o_c == 2:
                    for x in lst:
                        if x[1]=='Apple':
                            if x[4]=='AIR':
                                lst2.append(x)
                    proceed(lst2)
                    t=False
                    o=False
                elif o_c == 3:
                    for x in lst:
                        if x[1]=='Apple':
                            if x[4]=='N':
                                lst2.append(x)
                    proceed(lst2)
                    t=False
                    o=False
                else:
                    print("Please enter a valid option\n")
        else:
            print("Please enter a valid option\n")
def mobile(): #for mobile brand list
    f=open("Mobiles.csv","r")
    c=csv.reader(f)
    lst=[]
    for i in c:
        lst.append(i)
    print("""
Which one of the following you want to search
Enter:1 Oneplus
Enter:2 Samsung
Enter:3 Apple\n""")
    m=True
    while m!=False:
        choice = Try("Which one you want to search for : ")
        if choice == 1:
            lst2 = []
            for x in lst :
                if x[1]=='Oneplus':
                    lst2.append(x)
            proceed(lst2)
            m=False
        elif choice == 2:
            lst2 = []
            for x in lst :
                if x[1]=='Samsung':
                    lst2.append(x)
            proceed(lst2)
            m=False
        elif choice == 3:
            lst2 = []
            for x in lst :
                if x[1]=='Apple':
                    lst2.append(x)
            proceed(lst2)
            m=False
        else:
            print("Please enter a valid option\n")

def laptop(): #for Laptops brand list
    f=open("laptop.csv","r")
    c=csv.reader(f)
    lst=[]
    for i in c:
        lst.append(i)
    print("""
Which one of the following Brand you want to search for
Enter:1 Lenovo
Enter:2 HP
Enter:3 Dell\n""")
    l=True
    while l!=False:
        choice = Try("Which one you want to search for : ")
        if choice == 1:
            lst2 = []
            for x in lst :
                if x[1]=='Lenovo':
                    lst2.append(x)
            proceed(lst2)
            l=False
        elif choice == 2:
            lst2 = []
            for x in lst :
                if x[1]=='HP':
                    lst2.append(x)
            proceed(lst2)
            l=False
        elif choice == 3:
            lst2 = []
            for x in lst :
                if x[1]=='Dell':
                    lst2.append(x)
            proceed(lst2)
            l=False
        else:
            print("Please enter a valid option\n")

def convertor(n): #indian style number formator (till 999 Cr)
    n=str(n)
    dig=[]
    for x in str(n):
        dig.append(x)
    if len(dig)<=5:
        conv = ('{:,}'.format(int(n)))
    elif len(dig)==6:
        no=[dig[0],',',dig[1],dig[2],',',dig[3],dig[4],dig[5]]
        conv=(''.join(no))
    elif len(dig)==7:
        no=[dig[0],dig[1],',',dig[2],dig[3],',',dig[4],dig[5],dig[6]]
        conv=(''.join(no))
    elif len(dig)==8:
        no=[dig[0],',',dig[1],dig[2],',',dig[3],dig[4],',',dig[5],dig[6],dig[7]]
        conv=(''.join(no))
    elif len(dig)==9:
        no=[dig[0],dig[1],',',dig[2],dig[3],',',dig[4],dig[5],',',dig[6],dig[7],dig[8]]
        conv=(''.join(no))
    elif len(dig)==10:
        no=[dig[0],dig[1],dig[2],',',dig[3],dig[4],',',dig[5],dig[6],',',dig[7],dig[8],dig[9]]
        conv=(''.join(no))
    else: #if more than a 999 Cr just print as it is 
        conv=n
    return conv

print("\t\t\t\t\tElectronic mart management system")
print("\t\t\t\t\t  Made by - Shubh and Suhani")
print("\t\t\t\t\t\t  Class - 12 A")

start()
