# 🐍 Python Basics for Data Science

In this notebook, I’ll be learning the **core Python skills** that are essential for data science.  


---


## Variables and Assignment
- Just like other programming languages " = " is use to assign value
- Python does not require you to declare the data type of a variable.
```python
spam_amaont = 0
print(spam_amount) #0

#✖️

#int spam_amount = 0

```
---

## Reasignment and Arithmetic
- Variables can be reassigned using arithmethic
```python
spam_amount = spam_amount + 4
print(spawn_amount) #4

```

- Common Operator
 | + | - | / | * | // | % | ** |

 ** = Exponential, for ex.. 2 ** 3 = 8
 // = Floor Devision for ex.. 5//2 = 2

---
 # Functions

- Functions are called with ()

```python



print("Hello")
help(print) #get the details of print
type(10) # get what data type is 10 = int
type(1.1) # a float

```
---
- min() and max() is to get the lowest and largest value among the given element

```python

min(1,5,2) #1
max(5,2,7) #7

```
---
- abs(x) returns absolute value

```python

abs(-10) #10
abs(50) #50

```
---
- float() to int() , int() to float(), string to int()

```python

float(19) #19.0
int(20.122) #20 

total = "50"

int(total) #int 50

int("50") #int 50

```
---
# So how to convert a int to string?
- using str() u can convert int to string

```python

num = 100

stringNumber = str(num)

print(stringNumber) #"100"

```

- joining a string and int with ' + ' will cause error

```python

num = 100
stringNum = "20"

add = num  + stringNum

```

- this will cause error because int and string cannot be add
- convert the string to int before adding

```python 

num = 100
strinNum = "20"

convertedString = int(stringNum)

add = num + convertedString

print(add)#(int type) 20
```
---

# Conditional Statement (if statement)

- The if statement is used to **CONTROL THE FLOW OF EXECUTION** in a program.
- The identation is 4 white spaces to mark which code belong to 'if' block.
- So basically if it's **TRUE** it will run .

### Example Code

```python

this_is_five = 5

if(this_is_five == 5):
    print("It is really five")
#indentation 4 white spaces will be inside of the if block

#here will not be scope of the if(block)

print("The number is: ", this_is_five)


```
---

-There's also a ****if else, elif**,

- Using if else

```python

my_pet = "Dog"


if(my_pet =="Dog"):
    print("Your pet is :" , my_pet)

else:
    print("Your pet is not: ", my_pet)

my_pet = "Cat"

if(my_pet =="Dog"):
    print("Your pet is :" , my_pet)

else:
    print("Your pet is: ", my_pet)
```

---

-  **using elif**

```python

dice = 4

if dice == 1:
    print("Your dice is: ",dice)
elif dice == 2:
    print("Your dice is: ",dice)
if dice == 3:
    print("Your dice is: ",dice)
elif dice == 4:
    print("Your dice is: ",dice)
if dice == 5:
    print("Your dice is: ",dice)
elif dice == 6:
    print("Your dice is: ",dice)


```
--- 
# How it works 
- if → checked first.

- elif → short for else if, used for extra conditions. You can have multiple elif blocks.

- else → runs only if none of the above conditions are True.


# if statement can be also nested (nested if)

- For example

```python

age = 18

gender = "Male"


if(age >= 18): #first check the age > 18
    print("Not Under Age")

    if(gender == "Female"): # second check is gender
        print("Gender is: ",gender )
    else:
        print("Gender is Female")

else:
    print("Under Age")

```

