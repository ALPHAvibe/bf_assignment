# Coding Assignment
## File Structure
```
.
├── race_average
│   ├── race_average.py                # race_average class
│   └── test.py                        # unit test for race_average
├── text_blocking
│   ├── text_blocking.py               # text_blocking class
│   └── test.py                        # unit test for text_blocking
└── README.md
```
## Text Blocking Sample Usage
```python
    from race_average import RaceAverage

    minutes = RaceAverage.average(["12:00 PM, DAY 1", "12:01 PM, DAY 1"])
```
## Race Average Sample Usage
```python
    from text_blocking import TextBlocking
    
    output = TextBlocking.execute(["AAA", "BBB", "CCC"])
```
## Executing Test
Run text_blocking_ unit test

    python text_blocking/test.py
Run race_average unit test

    python race_average/test.py
