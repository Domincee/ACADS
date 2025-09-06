## 1. Scenario: Shopping Discount System

Imagine an online store that gives customers discounts based on how much they spend:

- Spend **$100 or more** → 20% discount  
- Spend **$50 or more** → 10% discount  
- Otherwise → no discount  

### ✅ Example:
```python


costumer_spend = 50

discount = 0;

if costumer_spend >= 100:
    discount = 0.8
    costumer_spend = costumer_spend * discount
    print("You get 20% Discount!")
    
elif costumer_spend >=50:
    discount = 0.9
    costumer_spend = costumer_spend * discount
    print("You get 10% Discount!")




```

---


##  2. Scenario: Weather Activity Suggestion

Imagine you want a program that suggests what activity to do based on the **temperature**:

- Temperature ≥ 30°C → Go swimming  
- Temperature ≥ 20°C → Go for a walk  
- Temperature ≥ 10°C → Wear a jacket and go outside  
- Otherwise → Stay indoors  


```python

temperature = 20

if temperature >= 30:
    print("We can go swimming")
elif temperature >= 20:
    print("We can go walk")
elif temperature >= 10:
    print("It's called outside wear a jacket")
else:
    print("let's just stay inside") 


```


---

## 3. Scenario: Advanced Shopping Discount System (Nested ifs)

We want a program to calculate a **final price** based on:  
1. Purchase amount  
2. Membership status (member or non-member)  
3. Seasonal sale (e.g., Black Friday)  

**Rules:**  
- If the customer is a **member**:  
  - Purchase ≥ $100 → 25% discount  
  - Purchase ≥ $50 → 15% discount  
  - Otherwise → 5% discount  
- If the customer is **not a member**:  
  - Purchase ≥ $100 → 20% discount  
  - Purchase ≥ $50 → 10% discount  
  - Otherwise → no discount  
- If it’s a **seasonal sale** (like Black Friday), give **extra 5% off** on top of any discount.  


```python
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


```