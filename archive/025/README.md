# 25 - Pandas

### Topics Covered

* Reading and Writing to CSV

* Introduction to the Pandas Framework
  
### Notes

* WITHOUT PANDAS

```python
weather_data1 = open('archive/025/weather_data.csv')
temp = []
for i in weather_data1.readlines():
    temp.append(i.split(',')[1])
print(temp)
```

* WITH PANDAS

```python
import pandas as pd

weather_data2 = pd.read_csv('archive/025/weather_data.csv')
print(weather_data2['temp'])
```


### Resources

* [Pandas](https://pandas.pydata.org/)
* dataAnalysis-Python - [Github](https://github.com/Pro-Start/dataAnalysis-Python#lesson-4---analyzing-tabular-data-with-pandas)


###  Materials

* [Python File - file-syntax](./025.py)
* [Python File - snake-3](./snake/main.py)

---

**[Home](../README.md)**


