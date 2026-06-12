# type_conversion.py
num_str = "123"
num_int = int(num_str)      # string → integer
print(num_int + 10)         # 133

price_str = "45.67"
price_float = float(price_str)
print(price_float * 2)      # 91.34

age = 25
age_str = str(age)
print("I am " + age_str)    # I am 25