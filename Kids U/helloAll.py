studentCount = int(input("\nHow many students are in this class? "))
print("I'm glad to be here with so many Pythonistas")

studentNames = []

for i in range(studentCount):
  name = input("What is one student's name? ")
  studentNames.append(name)


for name in studentNames:
  print("Hello " + name + "! ")

print("Great to meet you all!")
