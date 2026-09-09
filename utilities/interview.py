import pytest
import requests
# Write Python code to find the first non-repeating character.

# Approach 1
word = "automation"
for char in word:
    if word.count(char) == 1:
        print(char)
        break

# Approach 2
word_count = {}
for char in word:
    word_count[char] = word_count.get(char, 0) + 1

for char in word:
    if word_count[char] == 1:
        print(char)
        break

# Find the second-largest unique number without using:
# sort()
# sorted()
# max()
# any built-in function that directly finds the largest value.

numbers = [10, 5, 8, 10, 3, 8, 15, 15]

if len(numbers) < 2:
    print("No second max number present in the list")
else:
    first_max = 0
    second_max = 0
    for number in numbers:
        if number > first_max:
            second_max = first_max
            first_max = number
        elif first_max > number > second_max:
            second_max = number
        else:
            continue
    print(second_max)

# Remove duplicates while preserving the original order, without using set()
numbers = [1, 2, 3, 2, 4, 1, 5, 3]
seen = set()
unique_number_list = []
for number in numbers:
    if number not in seen:
        seen.add(number)
        unique_number_list.append(number)
print(unique_number_list)

# Find the frequency of each word and print the result.
words = ["selenium", "pytest", "selenium", "python", "pytest", "api"]

words_count = {}
for word in words:
    words_count[word] = words_count.get(word, 0) + 1
print(words_count)

response = {
    "status": "SUCCESS",
    "transactionId": "TX12345",
    "amount": 1000,
    "currency": "EUR",
    "beneficiary": {
        "name": "John",
        "account": "123456"
    }
}

base_url = "https://api.eventhub.rahulshettyacademy.com/api"




