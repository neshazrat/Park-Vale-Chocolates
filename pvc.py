#SUBROUTINES

def login():
  # to keep the accounts details safe, only having secure and limited access.
  print("-------------------------------------------- LOGIN: -----------------------------------------------")
  print("                     * Please enter your username and password to login! ")
  print("")
  username= input("username: ")
  password= input("password: ")
  while valid_login_check() == False:
    print("Unsuccessful login!")
    username= input("username: ")
    password= input("password: ")


def add_user():
  # enters and stores details of the customer to provide an invoice for customer
 
  print()
  print("------------------------------------ ADD CUSTOMER DETAILS: ----------------------------------------")
  print("                         * Please fill out the following information: ")
  print()
  first_name= input(" * First Name: ")
  while valid_name_check(first_name) == False:
    print("           * An error has occured, please try again.     ")
    first_name= input("* First name: ")
  
  
  second_name= input(" * Second Name: ")
  while valid_name_check(second_name) == False:
    print("           * An error has occured, please try again.")
    second_name= input("Second name: ")
  
  house_number= input(" * House Number: ")
  
  street= input(" * Street: ")
  
  city= input(" * City: ")

  email= input(" * Email:")
  while valid_email_check(email)== False:
    print("           * An error has occured,please try again.")
    email= input(" * Email: ")
  
  postcode= input(" * Postcode:")
  while valid_postcode_check(postcode)== False:
    print("          * An error has occured, please try again later.")
    postcode= input(" * Postcode: ")

  #saves customers information to a text file so data can be used
  file = open("customer_data.txt", "a")
  file.write(f"First Name:{first_name}\n")
  file.write(f"Second Name:{second_name}\n")
  file.write(f"House Number:{house_number}\n")
  file.write(f"Street:{street}\n")     
  file.write(f"City:{city}\n")
  file.write(f"Email:{email}\n")
  file.write(f"Postcode:{postcode}\n")
  file.close()
  print(" ")
  print("                       * Your details have successfully been added!") 


def view_user_details():
  # code to view customer details
 
  print()
  print("Customer Details: ")
  with open("customer_data.txt", "r")as f:
          print(f.read())


def edit_order():
  # allows customer to ammend their order if anything changes.
  
  print("Would yopu like to edit your order?")
  user_choice = 0
  if user_choice == "yes":
    print(*customer_order) 
    file = open(customer-order.txt)
    edit = input("Enter your addition: ") 
    customer_order.append() 
    print("You have successfully edited your order! Press 6 to return to the menu!") 
  elif user_choice == "no": 
    print("That’s okay! Please press 6 to return to the menu!") 
  elif number == 6: 
    starting_menu()
  else: 
    end_program()


def tin_message():
  # optional for customer
 
  cost = 0 
  print("Would you like to engrave a message on your tin can?") 
  if choice == "yes": 
    message= input("Message: ")
  for letter in message: 
    cost = cost + 10 
  else:  
    print("That’s okay! Please press 6 to return to the menu!") 


def create_order():
  # enter and store the customers order
  
   print("                 ======================================================== ")
   print("                |                      CREATE ORDER!                     |")
   print("                |                                                        |")
   print("                |  * Please choose your chocolates to create an order!   |")
   print("                |                                                        |")
   print("                |                 *1 - Caramel Twist                     |")
   print("                |                 *2 - Orange Crush                      |")
   print("                |                 *3 - Chocolate Bar                     |")
   print("                |                 *4 - Brazil Nut in Chocolate           |")
   print("                |                 *5 - Cornish Fudge                     |")
   print("                |                 *6 - Strawberry Treat                  |") 
   print("                |                 *7 - Orange Smoothie                   |")
   print("                |                 *8 - Toffee Bar                        |")
   print("                |                 *9 - Hazelnut Triangle                 |")
   print("                |                 *8 - Cocunut Dream                     |")
   print("                 ======================================================== ")
  
   order = 0 
   order == input("::>")
   if order > 6:
     return
   elif order < 3:
     return
   file = open("customer_order.txt", "a")
   file.write(f"Customer Order:{customer_order} \n")
   file.close()
   print("Your order has been successfully created!")
  
 




def checkout_order():
  # calculate total cost of order including message
 
  user_order == ["Chocolate Tin: 9.99", "chocolate_order:", "Message:" , "Delivery:4.99"]
  print(*user_order_before)
  total== total + chocolatetin + user_order + message + delivery
  print(*total) 
  user= input("To checkout your order, please enter your details:") 


def order_ID():
  # order number given to track and search the customers details
   
  order_number= input("order number: ") 
  while valid_ID_check(ID)== False: 
     print("An error has occured, please try again.") 
  order_number= input("order number:") 
  print("Thank you for shopping at Park Vale Chocolates! Your order should arrive soon.") 
  print("Press 6 to return to the menu!") 
  if number == 6: 
     starting_menu()
  else: 
     end_program()


def weigh_chocolates():
# check that the weight of the order adds up to 1kg
  
  print("Please choose the masses of your chocolate choices!") 
  print("You can only only choose up to 500g of any flavour. Your chocolate masses should add up to 1kg as well!") 
  weight = 0 
  while weight < 1000: 
    while True:
       try: 
         Mass= int(input("Enter a mass: "))
         if Mass == 1000: 
           print ("Your order has reached 1kg! Please press 6 to return to the menu!") 
         else: 
           print("Please try again!") 
         weigh_chocolates() 
       except: 
            break


#VALIDATION

def valid_name_check(name):
  # validate customers name
  
  if len(name) < 2:
    return False
  elif name.isalpha()== False:
    return False
  else:
    return True 


def valid_postcode_check(postcode):
  # validate cutomers postcode
  
  if len(postcode) < 5:
    return False
  elif len(postcode) > 7: 
    return False
  elif postcode[0].isalpha()== False:
    return True
  else:
    return True


def valid_email_check(email):
  # validate customers email
  
  if "@" not in email:
    print("Invalid Email")
    return False
  if "." not in email:
    print("Invalid Email")
    return False
  if email[0] == "@" or email[0]== ".":
    print("An error has occured, please try again.")


def valid_ID_check(ID):
  # validate customers order number
  
  if len(ID) < 4:
    return False
  elif len(ID) > 4: 
    return False
  elif ID[0].isalpha()== True:
    return True
  else:
    return True


def valid_login_check():
  # validate the customers login
  username= "admin"
  password= "123" 
  while username != "admin":
    return False
    print("Unsuccessful Login!")
  while password != "123":
    return False
    print("Unsuccessful Login!")


#STARTING MENU

login()

while True:
  choice = 0
  if choice == 0:
  
   print(" ")
   print("                  ======================================================= ")
   print("                 |            WELCOME TO PARK VALE CHOCOLATES!           |")
   print("                 |*******************************************************|")
   print("                 |              *1 - Add customer                        |")
   print("                 |              *2 - View customer details               |")
   print("                 |              *3 - Create order                        |")
   print("                 |              *4 - Weigh out chocolates                |")
   print("                 |              *5 - Edit order                          |")
   print("                 |              *6 - Tin message                         |") 
   print("                 |              *7 - Checkout order                      |")
   print("                 |              *8 - Order ID                            |")
   print("                  ======================================================= ")
   
  choice = input("::>")
  
  if choice == "1":
    add_user()
  
  elif choice == "2":
    view_user_details()
  
  elif choice == "3":
    create_order()
  
  elif choice == "4": 
    weigh_chocolates()
  
  elif choice == "5":
    edit_order()
  
  elif choice == "6":
    tin_message()
  
  elif choice == "7":
    checkout_order()
  
  elif choice == "8": 
    order_ID()
