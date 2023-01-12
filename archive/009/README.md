# 9 - Dictionaries

### Topics Covered

* Python Dictionaries and Lists

* Nested Collections


### Notes

**DICTIONARY**
```py
dictionary = {
    "name": "John",
    "age": 30,
}
print(dictionary["name"])
```

**ADD**
```py
dictionary["city"] = "New York"
print(dictionary["city"])
```

**VS. LIST**
```py
my_list = [1, 2, 3, 4, 5]
print(my_list[2])  # Output: 3
```

**NESTED LIST**
```py
country = [
    {
        'name':  'usa',
        'visited':  ['nyc', 'wa', 'tx'],
        'times_visited': 14
    },
    {
        'name': 'france',
        'visited':  ['paris', 'lille'],
        'times_visited': 10
    },
]

# DICTIONARY > DICTIONARY > LIST

print(country[0]['visited'][1])  # wa
```


### Materials

* [Python File - grading-program](./009a.py)
* [Python File - travel-log](./009b.py)
* [Python File - blind-auction](./009b.py)

---

**[Home](../README.md)**