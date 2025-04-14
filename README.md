# 🔐 Password Generator CLI

A Python-based command-line tool to generate strong, secure passwords and evaluate their strength — fully customizable by the user.

---

## 🧠 About the Project

I wanted to build something small but useful — and a password generator seemed like the perfect fit. While the concept isn't complicated, I was curious how to structure the logic to make the tool flexible and interactive via the command line.

Instead of writing every part from scratch, I leaned on examples and tutorials to understand how to combine different character sets and create random strings securely. From there, I added features like password strength checking and user preferences.

The result is a CLI utility that’s both functional and educational. I learned a lot about working with Python’s built-in libraries and handling user input gracefully.

---

## ✨ Features

- 🔑 Generate secure passwords of any length  
- 🔢 Include uppercase, numbers, and special characters  
- 🧪 Built-in password strength checker  
- 📏 Validates user input and uses defaults where needed  
- 🔄 Loop until user quits

---

## 🛠️ How It Works

1. User chooses between generating a password or checking one  
2. If generating, user specifies length and character types  
3. A password is created and its strength is shown  
4. Strength is evaluated by length and character variety  
5. Users can loop through options or quit anytime

---

## 🧰 Technologies Used

- Python 3  
- `random` and `string` modules (standard library)

---

## ▶️ Run It Locally

```bash
# Clone the repository
git clone https://github.com/CanMus04/password-generator-cli.git

# Move into the directory
cd password-generator-cli

# Run the script
python password_generator.py
