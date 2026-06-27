# args_demo.py
def sum_all(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(sum_all(1, 2, 3))        # 6
print(sum_all(10, 20, 30, 40)) # 100

def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Ram", age=25, job="Engineer")