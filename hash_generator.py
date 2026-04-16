import hashlib

def generate_hash(text, algorithm="sha256"):
    if algorithm == "md5":
        return hashlib.md5(text.encode()).hexdigest()
    elif algorithm == "sha1":
        return hashlib.sha1(text.encode()).hexdigest()
    elif algorithm == "sha256":
        return hashlib.sha256(text.encode()).hexdigest()
    else:
        return "Invalid algorithm"

print("=== Password Hash Generator ===")

text = input("Enter text: ")

print("\nChoose hash type:")
print("1 - MD5")
print("2 - SHA-1")
print("3 - SHA-256")

choice = input("Your choice: ")

if choice == "1":
    result = generate_hash(text, "md5")
elif choice == "2":
    result = generate_hash(text, "sha1")
elif choice == "3":
    result = generate_hash(text, "sha256")
else:
    result = "Invalid choice"

print("\nHashed Result:", result)