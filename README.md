# 30 Days of Python
Start learning python and hopefully will use it for Machine Learning and Deep Learning in the future.

- [x] Day 1: Basics [time=Mon, Apr 17, 2017]
- [ ] Days 2&3: Lists, Dictionaries, Tuples and Loops
- [ ] Day 4: Conditionals
- [ ] Day 5: Functions
- [ ] Day 6: Advanced Strings
- [ ] Days 7-9: Classes
- [ ] Days 10 - 20: Python CSV, and Email | Do something Real
- [ ] Days 21 - 24: Web Scraping with Python 3 Python Requests & BeautifulSoup
- [ ] Day 25: Web Scraping on Javascript Driven HTML
- [ ] Day 26: Get Data with an API
- [ ] Days 27 - 28: Text Messaging (SMS/MMS) with Python & Twilio
- [ ] Day 29: Twitter API & Python
- [ ] Day 30: Read Email Inbox using Python & Gmail;

# HackMD Note
https://hackmd.io/AwTgHAJlHAtMAWAjAI1ghBmEsCGIA2AdlhVwCYRNh8BjJBXIA===?view

# Python Day 1: Basics
```Ruby
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Install Python3
```Ruby
brew install python3
```

### Variables
Declare directly with variable name
```Python
abc = 'some string'
```

# Python Day 2: Lists, Dictionaries, Tuples
### Lists
It is also called array in some languages.
String and numbers (Any Type) are allowed to store within the list.
```Python
list_var = ['some thing', 123, 'another thing']
list_var.append('new item') //append new item
list_var.pop() //pop the last item
list_var.pop(0) //index of the item
len(list_var) //get length of array
```

### Dictionaries
It is similar to Objective-C Dictionary, with key-value opinion.
However its key can be integer value while it is not allowed in some other languages.
*It can store a pointer within the value too*
```Python
Car = {'seats': ['driver', 'passanger'], 'mirror': 'front', 1234: 'others'}
Car[1234] //others
Car['mirror'] //front
Car['door'] = 4 //add new or edit key
```

### Tuples
It is a data structure (such as choices), not really everyone will like this.
```Python
Tup = (123, 234)
Tup = (('another', 'another'), ('some', 'some'))
```
Special thing to note
```Python
tup = (('tic', 'tic'), ('tac', 'tac'))
tup += ('toe', 'toe')
```
> (('tic', 'tic'), ('tac', 'tac'), 'toe', 'toe')

To append ```('toe', 'toe')``` in tail
```Python
tup = (('tic', 'tic'), ('tac', 'tac'))
tup += (('toe', 'toe'),)
```
> (('tic', 'tic'), ('tac', 'tac'), **('toe', 'toe')**)

# References
Course [(30 days of python) Udemy](https://www.udemy.com/30-days-of-python)
Python3 [Python Installation](https://gist.github.com/uranusjr/6fa2770a8c8651192e93)

###### tags: `python` `30DaysPython`
