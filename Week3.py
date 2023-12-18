import random

# Define a list of characters to choose from
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"

def generate_password(length):
  """
  Generates a random password of the specified length.

  Args:
    length: The desired length of the password.

  Returns:
    A randomly generated password.
  """
  password = "".join(random.choice(characters) for _ in range(length))
  return password

def generate_passwords(number, length):
  """
  Generates a list of the specified number of random passwords of the specified length.

  Args:
    number: The desired number of passwords to generate.
    length: The desired length of each password.

  Returns:
    A list of randomly generated passwords.
  """
  passwords = []
  for _ in range(number):
    passwords.append(generate_password(length))
  return passwords

# Example usage
number_of_passwords = 5
password_length = 12

passwords = generate_passwords(number_of_passwords, password_length)

print(f"Generated {number_of_passwords} passwords of length {password_length}:")
for password in passwords:
  print(password)
