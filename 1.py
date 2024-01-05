def divide():
    try:
        x = int(input("First: "))
        y = int(input("Second: "))
        result = x / y
        return result
    except ValueError as e:
        return f"Error: {e}. Please enter valid numbers."
    except ZeroDivisionError as e:
        return f"Error: {e}. Cannot divide by zero."

for i in range(3):
    print(divide())
