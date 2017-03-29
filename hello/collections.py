mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# prints out 1,2,3
for x in mylist:
    print(x)

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = names[1]
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append('hello')
strings.append('world')


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)


phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)


phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of {0} is {1}".format(name, number))

for name in phonebook.keys():
    print("Name: {0}".format(name))

phonebook.pop("John")
print(phonebook)

for name in phonebook.keys():
    print("Name: {0}".format(name))


sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
      if word != "the":
          word_lengths.append(len(word))
print(words)
print(word_lengths)   

word_lengths = [word.upper() for word in words]
print(words) 
print(word_lengths)


numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [number for number in numbers if number > 0]
print(numbers)

print("Only positive: {0}".format(newlist))
