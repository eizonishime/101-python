x = "My"
y = "name"
z = "is simple"
all = x + " " + y + " " + z
print(all)

print(all.upper())
print(all.lower())

print("Reversed lowered: %s " % all.lower()[::-1])
print("Parts: %s " % all.split(" "))

print("%s %s %s, is Jonh Doe" % (x, y, z))

print("x len: %d" % len(x))
print("y len: %d" % len(y))
print("z len: %d" % len(z))

print("i appearences in '%s': %d" %  (z, z.count("i")) ) 

simpleList = [1,2,3]
print("A list: %s" % simpleList)

data = ("John", "Doe", 53.44)
format_string = "Hello, %s %s. Your current balance is %.2f"

print(format_string % data)

hilarious = True
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation % hilarious)

print ("fleece was white as %s." % "snow")


months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the months: ", months)
