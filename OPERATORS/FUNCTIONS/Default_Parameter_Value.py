#Default Parameter Value


# Greeting with Default Name

def greet(name="Guest"):
    print("Hello,", name)

greet("Agniv")
greet()  

#Language Preference
def language(lang="English"):
    print("Preferred language is:", lang)

language("Bengali")
language()  # uses default


#Student Grade

def student(name,grade="A"):
    print(name," got grade ",grade)

student ("Agniv","A+")
student("Soumyajit")  # here it usese the default grade a that is already defined in the function