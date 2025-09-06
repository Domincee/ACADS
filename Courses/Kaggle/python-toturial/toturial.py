
is_member = False

amount = 100

seasonal_sale = True

total_discount = 0;

if(is_member):
    print("A Member")
    if amount >= 100:
        print("Amount spend more than 100")
        total_discount = 20

    elif amount >= 50:
        print("Amount spend more than 50")

    if(seasonal_sale):
          print("It is seasonal_sale")
          total_discount = total_discount + 5
    else:
         print("Not seasonal Sale")

else:
    print("Not a Member")

    if amount >= 100:
        print("Amount spend more than 100")
        total_discount = 20

    elif amount >= 50:
        print("Amount spend more than 50")

        total_discount = 10

    if(seasonal_sale):
          print("It is seasonal_sale")
          total_discount = total_discount + 5
    else:
         print("Not seasonal Sale")




print("You got a total", total_discount ,"% Discount!")




    
