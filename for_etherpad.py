# This is not meant to be executed directly, but used as a repository of 
# challenges for the material


## Traceback reading

traceback="""
------------------------------------------------------
KeyError             Traceback (most recent call last)
<ipython-input-6-b6988acf1a74> in <module>()
----> 1 error_prone.print_friday_message()

/Users/dave/Dropbox/talks/20160928_ms_teachingdemo/error_prone.py in print_friday_message()
     26 
     27 def print_friday_message():
---> 28     print_message("Friday")
     29 

/Users/dave/Dropbox/talks/20160928_ms_teachingdemo/error_prone.py in print_message(day)
     22         "sunday": "Aw, the weekend is almost over."
     23     }
---> 24     print(messages[day])
     25 
     26 

KeyError: 'Friday'
"""

question="""
Paste answers below the question...
1. What is the file name where the error occurred?
2. On which line number in this file did the error occur?
3. What is the error message? What do you think it means?
"""


## NameErrors

for number in range(10):
    # use a if the number is a multiple of 3, otherwise use b
    if (Number % 3) == 0:
        message = message + a
    else:
        message = message + "b"
print(message)

question="""
What errors do you see without running the example?
Run the example, noting and fixing the error that shows up.
Repeat 2 until you have a working version and paste it into the etherpad
underneath this line:
"""


## IndexErrors 

seasons = ['spring', 'summer', 'fall', 'winter']
print("My fav season is ", seasons[4])

question="""
Correct the error and paste a copy back below this line:

Generate your own IndexError producing code and paste it under here:

"""
