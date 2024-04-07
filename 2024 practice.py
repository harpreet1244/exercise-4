
name = input("what's your name ? ")
print("hello")
print(name)

print("hello,", name)


name = input("what's your name ? ").strip().title()
# name = name.strip().title()
first, last = name.split()

# say hello to user
print("hello,", name, sep=' ')  # this is a separator
print(f"hello, {last}")
