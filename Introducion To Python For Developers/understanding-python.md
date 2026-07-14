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

