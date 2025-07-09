name = "Hassan"
n = int(input("Enter a number: "))

# Rainbow emojis
colors = ["❤️", "🧡", "💛", "💚", "💙", "💜", "🤍", "🤎"]

# 🔼 Top Half
for i in range(1, n + 1):
    spaces = " " * (n - i)
    color = colors[(i - 1) % len(colors)]
    line = (f"{color} {name}" * i).strip()
    print(spaces + line)

# 🔽 Bottom Half
for i in range(n - 1, 0, -1):
    spaces = " " * (n - i)
    color = colors[(i - 1) % len(colors)]
    line = (f"{color} {name}" * i).strip()
    print(spaces + line)
