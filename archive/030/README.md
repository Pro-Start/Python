# 30 - Error, Exceptions, JSON

### Topics Covered

* Error Handling and Exceptions

### Notes

* Types of errors

  * FileNotFound

```python
file = open('file.txt')
```

  * KeyError

```python
a_dictionary = {"key": "value"}
value = a_dictionary["non_existent_key"]
```

  * IndexError

```python
fruits_list = ["Apple", "Banana", "Pear"]
fruit = fruits_list[3]
```

  * TypeError

```python
text = "abc"
print(text + 5)
```

  * SyntaxError

```python
def add(a, b):
    print(a + b)
    return
```


### Materials

* [Python File - try-catch-syntax](./030syntax.py)
* [Python File - password-generator-2](./030.py)

### Resources

* Problem 1 - [codingrooms](https://app.codingrooms.com/management/assignments/365278/overview)
* Problem 2 - [codingrooms](https://app.codingrooms.com/management/assignments/365280/overview)


---

**[Home](../README.md)**