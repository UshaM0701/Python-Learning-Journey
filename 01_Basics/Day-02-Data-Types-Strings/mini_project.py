print("=== Username Generator ===")

name = input("Enter your name: ").strip()
birth_year = input("Enter your birth year: ").strip()

# Clean name
clean_name = name.lower().replace(" ", "")

# Create username
username = clean_name + birth_year

# Password suggestion
password = clean_name.title() + "@123"

print("\n--- Your Credentials ---")
print("Username:", username)
print("Suggested Password:", password)
print("------------------------")
