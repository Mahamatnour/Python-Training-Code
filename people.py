#people.py

amount = int(input("how many people"))

people ={}

average = 0

for x in range(0, amount):

   name = input("what is the person names?")
   people[name]=int(input("age"))

for ages in people.values():
                average += ages
print("the average age of all the people is", average/amount)
print("the oldest person is", max(people.values()))
print("the youngest person is", min(people.values()))
print()
print("all people here")
print(people)
                
