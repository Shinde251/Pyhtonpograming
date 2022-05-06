# String Slicing :- Extracting Perticular Portion from string
# String support both Forward and Backward slicing
# Syntax:-   object[lowerindex : upperindex]-- Upper index is excluded
# index is always lower to upper in slicing.


x="Python"

print(x)

print("\nForward / Positive Slicing \n")


print(x[0:6]) # upper index is excluded

print(x[0:4])

print(x[4:0]) # Empty string returned bcaz index is upper to lower


print(x[0: ])

print(x[ :6])

print(x[ : ])

print("\nBackward / Negative Slicing \n")

print(x[-6 : -1]) #Pytho

print(x[-6 : ]) #Python







