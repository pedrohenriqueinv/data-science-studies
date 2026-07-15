# 🐍 Introduction to Python for Developers

Welcome to the **Python for Developers** study guide! This repository contains organized notes, core concepts, and quick-reference syntax guides.

---

## 🚀 Course Overview

### What is Python?
Python is a highly popular, free, and open-source programming language known for its **clean, human-readable syntax**. It powers major platforms worldwide, including *Netflix, Spotify, and Facebook*.

### The Practical Project
Throughout the course, we develop a **Recipe Scaler** (a script that scales recipes into shopping lists). 
> 💡 **Best Practice:** Start small, test constantly, and document your code as you write.

---

## 🛠️ Essential Syntax

### 1. Output & Debugging
The `print()` function is your primary tool to display results and debug code.
python
print("Hello, World!")  # Using double quotes
print('Hello, World!')  # Using single quotes



### 2. Comments

Use the `#` symbol to add explanatory notes. The computer completely ignores these lines.

python
# This is a comment. It won't run!



### 3. Variables & Strings

Variables act as labeled containers for storing data.

* **Naming Convention:** Use `snake_case` (lowercase separated by underscores).
* **Quotes Rule:** Use double quotes if your text contains an apostrophe.

python
# Good practice
ingredient_name = "Chef's secret spice" 



---

## 📊 Variables & Basic Operators

### 1. New Data Types

* **Float:** Numbers with a decimal point (do not use quotes).
* **Boolean:** Only `True` or `False` (must be capitalized, no quotes).

python
price = 1.5           # Float
is_in_stock = True    # Boolean



### 2. Checking Types

Use `type()` inside a `print()` to inspect the data type of any variable:

python
print(type(price))  # Output: <class 'float'>



### 3. Math & String Operators

| Operator | With Numbers (`int`/`float`) | With Strings (`str`) |
| --- | --- | --- |
| **`+`** | Addition (`5 + 5 = 10`) | Joins text (`"Play" + "Station" = "PlayStation"`) |
| **`-`** | Subtraction (`10 - 2 = 8`) | ❌ *Causes Error* |
| **`*`** | Multiplication (`3 * 3 = 9`) | Repeats text (`"Kkk" * 3 = "KkkKkkKkk"`) |
| **`/`** | Division (`10 / 2 = 5.0`) | ❌ *Causes Error* |

---

## ✍️ Advanced String Manipulation

### Multi-line Strings

To store large paragraphs while preserving line breaks, enclose the text in triple double quotes (`"""`):

python
instructions = """1. Chop the tomatoes.
2. Mix with the pasta.
3. Serve hot."""



### Core String Methods

Methods are functions built specifically for a data type, called using the `.method()` syntax.

python
# 1. .replace(old, new) - Substitutes text
message = "Hello, George"
print(message.replace("George", "John"))  # Output: "Hello, John"

# 2. .lower() - Converts to lowercase (great for email normalization)
email = "USER@DOMAIN.COM"
print(email.lower())                      # Output: "user@domain.com"

# 3. .upper() - Converts to uppercase
name = "vitu"
print(name.upper())                       # Output: "VITU"



---

## 📋 Lists & Slicing

Lists store multiple items in a single variable using square brackets `[]`.

python
# Creating lists
ingredients = ["tomato", "garlic", "basil", "olive oil", "salt"]
mixed_list = [3, True, "pasta"]



### Indexing & Slicing Cheat Sheet

Let's use: `games = ["Apex", "Elden Ring", "Minecraft", "Valorant"]`

* **Single Indexing:**
* `games[0]` $\rightarrow$ `"Apex"` (First item)
* `games[-1]` $\rightarrow$ `"Valorant"` (Last item)
* `games[-2]` $\rightarrow$ `"Minecraft"` (Second-to-last item)


* **Slicing (`list[start:end]`):**
> ⚠️ **The Golden Rule:** Slicing goes up to, but **does not include**, the `end` index.


* `games[1:3]` $\rightarrow$ `['Elden Ring', 'Minecraft']` (Indices 1 and 2)
* `games[:3]` $\rightarrow$ `['Apex', 'Elden Ring', 'Minecraft']` (From start to index 2)
* `games[2:]` $\rightarrow$ `['Minecraft', 'Valorant']` (From index 2 to the end)


* **Steps (`list[start:end:step]`):**
* `games[::2]` $\rightarrow$ `['Apex', 'Minecraft']` (Skips every other item)



---

## 🔑 Dictionaries

Dictionaries store data in **Key-Value** pairs inside curly brackets `{}`. They are ideal for connecting related attributes.

python
# Creating a Dictionary
recipe = {
    "fusilli": 500,
    "tomatoes": 400,
    "garlic": 15
}

# Accessing a value by its key
print(recipe["tomatoes"])  # Output: 400



### Dictionary Methods & Operations

python
# 1. Get keys, values, or pairs
print(recipe.keys())    # Output: dict_keys(['fusilli', 'tomatoes', 'garlic'])
print(recipe.values())  # Output: dict_values([500, 400, 15])
print(recipe.items())   # Output: dict_items([('fusilli', 500), ...])

# 2. Adding/Updating elements
recipe["salt"] = 10     # Adds a new key-value pair
recipe["garlic"] = 20   # Updates "garlic" from 15 to 20



> ⚠️ **Warning on Duplicate Keys:**
> Dictionaries **cannot** have duplicate keys. If you define a key twice, the last value will silently overwrite the previous one.
> ```python
> duplicate_dict = {"garlic": 15, "garlic": 30}
> print(duplicate_dict["garlic"])  # Output: 30


---

## 🔒 Sets & Tuples

### Sets `{}`

An unordered collection of **unique** elements.

* Used to quickly deduplicate data and perform fast membership tests.
* You cannot access elements by index (e.g., `my_set[0]` raises an error).

python
# Deduplicating a list using set()
dirty_list = [1, 2, 2, 3]
clean_set = set(dirty_list)
print(clean_set)  # Output: {1, 2, 3}

# Sorting a set returns a sorted LIST
print(sorted(clean_set))  # Output: [1, 2, 3]



### Tuples `()`

An **ordered**, **immutable** collection of elements.

* Once created, elements *cannot* be added, removed, or changed.
* Perfect for constants, coordinates, and protecting configuration settings.

python
coordinates = (10, 20, 30)
print(coordinates[1])  # Output: 20



---

## 🔄 Quick Comparison Summary

| Structure | Syntax | Allows Duplicates? | Mutable? (Can edit) | Ordered? (Has Index) |
| --- | --- | --- | --- | --- |
| **List** | `[]` | Yes | Yes | Yes |
| **Dict** | `{k: v}` | No (for keys) | Yes | Yes (by keys) |
| **Set** | `{}` | **No** | Add/Remove only | **No** |
| **Tuple** | `()` | Yes | **No** | Yes |


# Python Cheat Sheet: Conditionals, Loops, and Workflows
*Introduction to Python for Developers*

---

## 🔀 Conditionals & Operators (How Code Makes Decisions)

In Python, we use **comparison operators** to ask questions and **conditional structures** to decide what the code should do based on the answers (which always return `True` or `False`).

### ⚖️ 1. Comparison Operators (For Asking Questions)

*   `==` (**Equal to**): Checks if two values are equal.
    *   *Example:* `2 == 3` returns `False`. 
    *   *Note:* We use a double equals sign `==` for comparison, as a single equals sign `=` is reserved for assigning variables.
*   `!=` (**Not equal to**): Checks if two values are different.
    *   *Example:* `2 != 3` returns `True`.
*   `>` and `<`: **Greater than** / **Less than**.
    *   *Example:* `5 > 3` returns `True`.
*   `>=` and `<=`: **Greater than or equal to** / **Less than or equal to**.

> 🔤 **Golden Tip:** You can also compare strings (text)! Python compares them lexicographically (by alphabetical order).
> *Example:* `"James" > "Brian"` returns `True` because the letter "J" comes after the letter "B" in the alphabet.

---

### ⚙️ 2. Conditional Structures (`if`, `elif`, `else`)

These structures control the execution path of your program.

*   `if` (**If**): The starting point. If the condition is true, Python executes the indented block of code inside it.
*   `elif` (**Else if**): Used to test a new condition, but only if the previous `if` (or `elif`) evaluated to false. You can use as many `elif` statements as you need.
*   `else` (**Else**): The fallback case. If none of the preceding conditions are true, the code block under `else` will run.

#### 🍝 Practical Example:

pasta = 200

if pasta >= 300:
    print("Perfect! We have enough pasta for the recipe.")
elif pasta >= 150:
    print("Not enough for the full recipe, but we can make a smaller portion.")
else:
    print("Error: Insufficient ingredients! Go to the grocery store.")



#### ⚠️ The Two Sacred Rules of Conditionals:

1. **The Colon (`:`):** Every `if`, `elif`, or `else` line must end with a `:` at the end. This signals to Python that an action block is starting.
2. **Indentation (Code Alignment):** The code that runs inside a conditional block must be indented to the right (using one `Tab` or 4 spaces). If you align everything to the left, Python will throw an `IndentationError` and won't run!

---

## 🔁 For Loops (Automating Repetitive Tasks)

`for` loops are used to iterate over a collection (like a list, a dictionary, or even characters in a string) and automatically perform an action for each item.

### 🧩 1. Basic Structure

A `for` loop requires two things: an **iterable** (the collection of data to loop through) and an **iterator** (a temporary variable representing the current item in the loop).


ingredients = ["tomato", "pasta", "basil"]

# "ingredient" is the iterator (current item)
# "ingredients" is the iterable (entire list)
for ingredient in ingredients:
    print(ingredient)



> **Rule of Thumb:** Just like conditionals, the `for` statement must end with a colon (`:`), and the nested action must be indented.

---

### 🔀 2. Loops with Conditionals (`if` inside a `for`)

You can nest decision-making structures inside a loop to analyze items individually.


quantities = [600, 300, 50]

for qty in quantities:
    if qty > 500:
        print("Too many ingredients!")
    elif qty >= 100:
        print("Normal amount.")
    else:
        print("Too few ingredients!")



---

### 📖 3. Iterating Through Dictionaries (`.items()`, `.keys()`, and `.values()`)

To loop through dictionaries (which store key-value pairs), use these specific methods:

* `.items()`: Returns both the key and the value. Requires two temporary variables.

recipe = {"tomato": 500, "pasta": 300}

# "item" becomes the key, "qty" becomes the value
for item, qty in recipe.items():
    print(f"{item}: {qty} grams")




* `.keys()`: Iterates only through keys (e.g., `"tomato"`, `"pasta"`).
* `.values()`: Iterates only through values (e.g., `500`, `300`).

---

### 🔢 4. The `range()` Function (Repeating a Set Number of Times)

When you want to run a block of code a specific number of times, or generate a sequence of numbers, use `range(start, exclusive_end)`.

> **Important:** The stop value in `range()` is never included in the sequence.


# This will print numbers from 1 to 5 (6 is excluded)
for i in range(1, 6):
    print(i)


---

## 🔄 While Loops (Repeating Until a Condition Changes)

Unlike `for` loops (which iterate over a collection from start to finish), a `while` loop checks a condition first. If the condition is `True`, it runs the block and returns to the top to check the condition again, repeating this cycle until the condition evaluates to `False`.

### 🧩 1. Basic Structure


ingredients_left = 3

# While the value is greater than zero, the loop keeps running
while ingredients_left > 0:
    print(f"{ingredients_left} ingredients remaining...")
    # Decrement by 1 each round so the loop doesn't run forever!
    ingredients_left -= 1

print("Shopping list complete!")



---

### ⚠️ 2. Danger: The Infinite Loop!

If you forget to update the variable being tested in the condition (like neglecting `ingredients_left -= 1`), the condition remains `True` forever. The program will run endlessly and freeze your system.

* **How to stop an infinite loop in your terminal?**
* Press **`Ctrl + C`** (Windows) or **`Cmd + C`** (Mac).



---

### 🛑 3. The `break` Statement (Forced Termination)

You can force a loop (`while` or `for`) to stop immediately using the `break` keyword, even if the loop's main condition is still `True`.

counter = 0

while True: # This would normally be an infinite loop...
    print(counter)
    counter += 1
    if counter == 5:
        break # ...but break forces the exit when counter reaches 5!



---

### 🔀 4. Conditionals Within `while` Loops

You can include `if`, `elif`, and `else` blocks inside your `while` loops to provide status updates to users as progress changes.


items_left = 5

while items_left > 0:
    if items_left > 3:
        print("Still several ingredients remaining.")
    elif items_left >= 1:
        print("Almost there! Only a few left.")
    
    items_left -= 1



---

## 🛠️ Tools for Complex Workflows

To design smarter code logic, you can combine loops with keywords that test for element existence or validate multiple conditions simultaneously.

### 🔍 1. Membership Operators (`in` and `not in`)

These operators check whether an item exists (or does not exist) within a collection (like a list or dictionary keys) without needing to loop through every item manually.

* `in`: Returns `True` if the item is present.

# Checking if "pasta" is a key in the recipe dictionary
if "pasta" in recipe:
    print("We have pasta in the recipe!")




* `not in`: Returns `True` if the item is **not** present (ideal for identifying missing items).

if "salt" not in pantry_stock:
    print("No salt in the pantry! Add it to the shopping list.")





---

### 🚦 2. Logical Operators (`and` and `or`)

These allow you to evaluate multiple conditions in a single line.

* `and`: Returns `True` only if **all** conditions are true at the same time.

# Needs to have enough pasta AND enough olive oil
if pantry_stock["pasta"] >= 500 and pantry_stock["olive oil"] >= 30:
    print("Ready to start cooking!")




* `or`: Returns `True` if **at least one** of the conditions is true.

# Having at least one of these helps
if pantry_stock["pasta"] >= 500 or pantry_stock["olive oil"] >= 30:
    print("We have at least one key ingredient ready.")





---

### 📥 3. Building Dynamic Lists (`.append()`)

A common development pattern is to initialize an empty list and populate it with items as they satisfy conditions inside a loop.

* `.append()`: Adds an item to the end of a list.


shopping_list = [] # Starts empty

for ingredient, qty in recipe.items():
    # If the recipe requires more than what we have in our pantry...
    if qty > pantry_stock[ingredient]:
        # ...append the missing ingredient to the shopping list
        shopping_list.append(ingredient)

print(shopping_list)
# Output: [Only the ingredients that are actually missing]



```

```