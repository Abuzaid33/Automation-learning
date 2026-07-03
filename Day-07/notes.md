.
🧠 Warm-up Quiz (Don't Google)

Answer these in notes.md.

What is an error in programming?
An error is fault occur when something goes wrong in the program and it gets stuck.
What is the difference between a syntax error and a runtime error?
Syntax error is when there is something wrong with the syntax like the way which it should be coded if we try out something which is not already exist in language while runtime error is an error occurs when we run the program and its not running
Should professional software crash because one operation fails?
never 
Why is error handling important in automation?
Error handling is important in automation because if an error occurs the program should never stops it should keep running regardless of the error.
What do you think finally means?
finnaly is like a default statment wether the condition is true or false or wether there is an error in program its able to run like program ended successfully .


📚 New Technical Terms

Write these definitions in your own words.

Exception
execption is something when a program gets an error instead of stoping it just give you an error and continue running
Syntax Error
gramatical error in the program
Runtime Error
when the program is running but get the error not because of error in program but during runnig it ran into something which stops its execution
try
Try in python to cehck wether there is an error or not 
except
exeption in python is if you get an error just simply raise that and continue running
else
if there is no error in th eprogramm else statment will be printed
finally
the statment under finally will be printed regardless of the error or no error situation
ValueError
when the requested value is not found
FileNotFoundError
when the requested file is not present
Defensive Programming
in which you handle the error before it occurs

🧠 Think Like an Engineer

Imagine your automation processes 50,000 invoices.

One invoice is corrupted.

Without exception handling:

Invoice 1 ✅

Invoice 2 ✅

Invoice 3 ❌

Program crashes

With exception handling:

Invoice 1 ✅

Invoice 2 ✅

Invoice 3 ❌ Logged

Invoice 4 ✅

Invoice 5 ✅

Which system would a company trust?


second system is good beacause a software should never stop