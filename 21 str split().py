# String Operations :-

# String Methods :-

#1. s.split(delimiter) :- When we split a string(line) we get list of sub strings (words) 


cities="nasik pune nagpur mumbai"

print("Origional string  :- ",cities, len(cities))

res=cities.split(" ")

print(res,len(res))

print(res[-1])  # mumbai
