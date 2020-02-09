# datetime-quarter
Simple quarter support for python `datetime.date`

## Setup

1. Install via pip (`pip install datetime-quarter`)
2. or via git (`git clone "https://github.com/BetaS/datetime-quarter"`)
3. Check availability in your project like below
```python
from datequarter import DateQuarter

sample = DateQuarter(2019, 4)
print(sample)  # 2019 4Q
```

## Operations

### 1. Creation
- `item = DateQuarter(2019, 4)  # 2019 4Q`
- `item = DateQuarter(2018, 8)  # 2019 4Q` *for convinience*
- `item = DateQuarter.from_date(datetime.date(2019, 12, 31))  # 2019 4Q`

### 2. Adding or sub quarter
- `DateQuarter(2019, 4)+1  # 2020 1Q`
- `DateQuarter(2019, 4)-4  # 2018 4Q`

### 3. Getting distance
- `DateQuarter(2019, 4) - DateQuarter(2019, 1)  # 3Q`
- `DateQuarter(2019, 1) - DateQuarter(2019, 4)  # -3Q`

### 4. Comparison of `DateQuarter`
- `DateQuarter(2019, 1) > DateQuarter(2019, 4)  # False`
- `DateQuarter(2019, 1) < DateQuarter(2019, 4)  # True`
- `DateQuarter(2019, 1) == DateQuarter(2019, 4)  # False`
- `DateQuarter(2019, 1) != DateQuarter(2019, 4)  # True`
- also support `>=` and `<=`

### 5. Comparison of `datetime.date`
- `datetime.date(2019, 12, 31) in DateQuarter(2019, 1)  # False`
- `datetime.date(2019, 12, 31) in DateQuarter(2019, 4)  # True`
- also support `>`, `>=` and vice versa

### 6. Getting start and end date
- `DateQuarter(2019, 1).start_date()  # datetime.date(2019, 1, 1)`
- `DateQuarter(2019, 1).end_date()  # datetime.date(2019, 3, 31)`

### 7. Iterate over containing date
```python
quarter = DateQuarter(2019, 1)
for day in quarter.days():
    print(day)  # [datetime.date(2019, 1, 1), ..., datetime.date(2019, 3, 31)]
```

### 8. Iterate between `DateQuarter`
```python
start = DateQuarter(2019, 1)
end = DateQuarter(2019, 4)
for quarter in DateQuarter.between(start, end):
    print(quarter)  # [DateQuarter(2019, 1), DateQuarter(2019, 2) , DateQuarter(2019,3)]
```
- also it support reversed case