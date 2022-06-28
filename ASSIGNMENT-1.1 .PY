1) What is Python? What are the benefits of using Python

Python is a high-level, interpreted, and general-purpose dynamic programming language that focuses on code readability. It generally has small programs when compared to Java and C. It was founded in 1991 by developer Guido Van Rossum. Python ranks among the most popular and fastest-growing languages in the world.

2) What is PEP 8 and why is it important?

PEP 8, sometimes spelled PEP8 or PEP-8, is a document that provides guidelines and best practices on how to write Python code. It was written in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan. The primary focus of PEP 8 is to improve the readability and consistency of Python code.

3)What is Scope in Python?

Local (or function) scope is the code block or body of any Python function or lambda expression. This Python scope contains the names that you define inside the function. These names will only be visible from the code of the function.

4)What are built-in type does python provides?
Built-in Data Types in Python
Binary Types: memoryview, bytearray, bytes.
Boolean Type: bool.
Set Types: frozenset, set.
Mapping Type: dict.
Sequence Types: range, tuple, list.
Numeric Types: complex, float, int.
Text Type: str.


5)What are Python decorators?
A decorator in Python is a function that takes another function as its argument, and returns yet another function . Decorators can be extremely useful as they allow the extension of an existing function, without any modification to the original function source code


6)What is negative index in Python?
Negative indexing in Python means the indexing starts from the end of the iterable. The last element is at index -1, the second last at -2, and so on.


7)When to use list vs. tuple vs. dictionary vs. set?

A list is a collection of ordered data. A tuple is an ordered collection of data. A set is an unordered collection. A dictionary is an unordered collection of data that stores data in key-value pairs.


8)What are lists and tuples? What is the key difference between the two?

The key difference between the tuples and lists is that while the tuples are immutable objects the lists are mutable. This means that tuples cannot be changed while the lists can be modified. Tuples are more memory efficient than the lists.

9)What are the common built-in data types in Python?

Built-in Data Types in Python
Binary Types: memoryview, bytearray, bytes.
Boolean Type: bool.
Set Types: frozenset, set.
Mapping Type: dict.
Sequence Types: range, tuple, list.
Numeric Types: complex, float, int.
Text Type: str.

10)What are modules and packages in Python?

A module is a file containing Python code in run time for a user-specific code. A package also modifies the user interpreted code in such a way that it gets easily functioned in the run time. A python “module” consists of a unit namespace, with the locally extracted variables.


11)What are global, protected and private attributes in Python?

There are three types of access modifiers in Python: public, private, and protected. Variables with the public access modifiers can be accessed anywhere inside or outside the class, the private variables can only be accessed inside the class, while protected variables can be accessed within the same package.


12)What is the use of self in Python?

The self is used to represent the instance of the class. With this keyword, you can access the attributes and methods of the class in python. It binds the attributes with the given arguments. The reason why we use self is that Python does not use the '@' syntax to refer to instance attributes


13)What is __init__?

The INIT function initializes the data structures required by the rest of the computation of the aggregate


14)What is break, continue and pass in Python?
Break, Pass, and Continue statements are loop controls used in python. The break statement, as the name suggests, breaks the loop and moves the program control to the block of code after the loop (if any). The pass statement is used to do nothing.


15)What is slicing in Python?

The slice() function returns a slice object. A slice object is used to specify how to slice a sequence. You can specify where to start the slicing, and where to end. You can also specify the step, which allows you to e.g. slice only every other item.

16)How is memory managed in Python?
Memory management in Python involves a private heap containing all Python objects and data structures. The management of this private heap is ensured internally by the Python memory manager.


17)What are the key features of Python?

Python Features and Advantages
Easy to Code. Python is a very high-level programming language, yet it is effortless to learn. ...
Easy to Read. Python code looks like simple English words. ...
Free and Open-Source. ...
Robust Standard Library. ...
Interpreted. ...
Portable. ...
Object-Oriented and Procedure-Oriented. ...
Extensible.

18)How to convert a list into a tuple?

list() method
To convert a tuple to list in Python, use the list() method. The list() is a built-in Python method that takes a tuple as an argument and returns the list. The list() takes sequence types and converts them to lists.

19)use python To find the first n numbers in a Fibonacci series.

# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1


20)use python To find the sum of digits of a number.

def getSum(n):
    
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
   
n = 12345
print(getSum(n))

