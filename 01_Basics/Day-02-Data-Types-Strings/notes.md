# 📘 Day 2: Data Types & Strings

## 🧠 What are Data Types?

Data types define what kind of data a variable can store.

### 🔹 Types in Python:
- int → 10
- float → 3.14
- str → "Hello"
- bool → True / False

Example:
x = 10        # int
y = 3.5       # float
name = "Usha" # string

---

## 🔤 Strings in Python

A string is a sequence of characters.

Example:
name = "Usha"

---

## ✂️ String Operations

### 1. Concatenation
first = "Usha"
last = "M"
print(first + " " + last)

### 2. Repetition
print("Hi " * 3)

---

## 🔍 String Functions

name = "usha learning python"

print(name.upper())      # USHA LEARNING PYTHON
print(name.lower())      # usha learning python
print(name.title())      # Usha Learning Python
print(name.strip())      # removes spaces

---

## 📏 Length

print(len(name))

---

## 🎯 Indexing

text = "Python"

print(text[0])  # P
print(text[-1]) # n

---

## 🧠 Slicing

print(text[0:3])  # Pyt
print(text[2:])   # thon

---

## 💥 Mistakes I Made

❌ Tried to change string directly  
💥 Error: Strings are immutable  
✅ Fix: Created new string  

🧠 Lesson: Strings cannot be modified directly
