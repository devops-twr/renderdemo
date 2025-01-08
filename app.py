# Collect user input for name and skill set
name = input("Enter your name: ")
skills = input("Enter your skills (comma-separated): ")

# Format and display the output
print("\n--- User Profile ---")
print(f"Name: {name}")
print("Skills:")
for skill in skills.split(','):
    print(f"- {skill.strip()}")
