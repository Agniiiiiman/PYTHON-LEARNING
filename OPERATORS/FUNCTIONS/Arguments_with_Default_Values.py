def greet(name="Guest"):
    print("Hello,", name)

greet("Agniv")    # Output: Hello, Agniv
greet()           # Output: Hello, Guest




def power(base, exponent=2):
    print(base, "raised to the power", exponent, "is", base ** exponent)

power(3)         # Uses default exponent = 2
power(2, 5)      # Uses given exponent = 5


def print_info(**info):
    for key, value in info.items():
        print(key + ":", value)

print_info(name="Agniv", age=19, course="BTech", branch="AI & ML")


def profile(name, age=18, **extra_info):
    print("Name:", name)
    print("Age:", age)
    for key, value in extra_info.items():
        print(key + ":", value)

profile("Agniv", location="Kolkata", hobby="Coding")
