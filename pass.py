import random
import string
def generate_password(length, complexity, exclude_similar, ensure_types, custom_chars):
    if complexity == '1':
        characters = string.ascii_lowercase
    elif complexity == '2':
        characters = string.ascii_letters
    elif complexity == '3':
        characters = string.ascii_letters + string.digits
    elif complexity == '4':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid complexity level.")
        return None
    if exclude_similar:
        similar_chars = 'Il1O0'
        characters = ''.join(c for c in characters if c not in similar_chars)
    if ensure_types:
        password = []
        if 'a' in complexity: 
            password.append(random.choice(string.ascii_lowercase))
        if 'A' in complexity:
            password.append(random.choice(string.ascii_uppercase))
        if 'd' in complexity:  
            password.append(random.choice(string.digits))
        if 'p' in complexity:
            password.append(random.choice(string.punctuation))

        length -= len(password) 

        if length > 0:
            password += [random.choice(characters) for _ in range(length)]
        
        random.shuffle(password) 
        return ''.join(password)
    else:
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

def main():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                raise ValueError("Length must be at least 1.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive integer.")

    print("Select complexity level:")
    print("1. Lowercase letters only")
    print("2. Uppercase and lowercase letters")
    print("3. Uppercase, lowercase letters, and digits")
    print("4. Uppercase, lowercase letters, digits, and special characters")
    complexity = input("Enter your choice (1/2/3/4): ")
    exclude_similar = input("Exclude similar characters (e.g., I, l, 1, O, 0)? (yes/no): ").strip().lower() == 'yes'
    ensure_types = input("Ensure the password contains at least one of each selected character type? (yes/no): ").strip().lower() == 'yes'
    custom_chars = input("Enter any custom characters to include (leave blank for none): ").strip()
    password = generate_password(length, complexity, exclude_similar, ensure_types, custom_chars)
    if password:
        print(f"Generated password: {password}")
if __name__ == "__main__":
    main()
