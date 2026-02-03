while True:
    try:
        gross = float(input("Enter gross salary: "))
        children = int(input("Enter number of children: "))
        break
    except ValueError:
        print("Invalid input. Please enter numbers (e.g., 1500 and 2).")

# --- base tax rate from gross ---
if gross < 1000:
    tax_rate = 0.10
elif gross < 2000:
    tax_rate = 0.12
elif gross < 4000:
    tax_rate = 0.14
else:
    tax_rate = 0.18

# --- child tax cut ---
if gross < 2000:
    tax_rate -= children * 0.01      # 1% per child
else:
    tax_rate -= children * 0.005     # 0.5% per child

# don't allow negative tax
if tax_rate < 0:
    tax_rate = 0

net = gross * (1 - tax_rate)

print("Net salary:", net)
