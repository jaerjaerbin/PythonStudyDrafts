from datetime import datetime


# Trick 1
n: int = 1_000_000_000

print(f"{n:_}") # will print 1_000_000_000
print(f"{n:,}") # will print 1,000,000,000


# Trick 2
var: str = "var"

print(f"{var:_>20}:")
print(f"{var:#<20}:")
print(f"{var:|^20}:")
print(f"{'':!>20}")

# Trick 3

now: datetime = datetime.now()
print(f"{now:%d.%m.%y}")
print(f"{now:%c}")


# Trick 4

n: float = 1234.5678
print(f"{n:.2f}")
print(f"{n:.0f}")
print(f"{n:,.3f}")


# Trick 5

a: int = 5
b: int = 10
my_var: str = "Bob says hi"

print(f"{my_var = }")
print(f"{a + b = }")
