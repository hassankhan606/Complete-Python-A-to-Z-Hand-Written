def say_again(n):
    if n == 0:
        return  # ❌ stop if n is 0
    print("Hello!")
    say_again(n - 1)  # ✅ call itself with smaller number
say_again(3)