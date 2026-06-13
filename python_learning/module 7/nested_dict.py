# nested dictionaries example
import math


students = {
    "ram": {"math": 85, "science": 90},
    "sita": {"math": 78, "science": 88},
    "gita": {"math": 92, "science": 85}

}

print(students["ram"]["math"])
print(students["sita"]["science"])
print(students["gita"]["math"])


print(f"Ram math: {students['ram']['math']} and science: {students['ram']['science']}")




