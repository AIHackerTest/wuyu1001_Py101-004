formatter = "%r %r %r %r"

a = formatter % (1, 2, 3, 4)
b = formatter % ("one", "two", "three", "four")
c = formatter % (formatter, formatter, formatter, formatter)
d = formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it did't sing.",
    "So I said goodnigt."

)
print(a)
print(b)
print(c)
print(d)
