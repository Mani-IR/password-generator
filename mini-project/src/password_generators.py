import random
import string
from abc import ABC, abstractmethod
import nltk
from datetime import datetime
import re

nltk.download('words')


# cacacascascacascascacacacac
try:
    nltk.data.find('corpora/words')
except LookupError:
    nltk.download('words')
#  xzccxcxczccccccZcacaaaascvvavcav





class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass

class PinGenerator(PasswordGenerator):
    def __init__(self, length: int ):
        self.length = length
        
    def generate(self) -> str:
        return ''.join(random.choices(string.digits, k=self.length))


class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, length: int = 8 , include_numbers: bool = False,include_symbols: bool = False):
        self.length = length 
        self.characters = string.ascii_letters
        if include_numbers:
            self.characters += string.digits
        if include_symbols:
            self.characters += string.punctuation
            
        
    def generate(self):
        return ''.join(random.choices(self.characters, k=self.length))



class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(
        self,
        num_of_words: int = 4,
        separator: str = '-',
        capitalize: bool = False,
        vocabulary: list = None
    ):
        if vocabulary is None:
            self.vocabulary = nltk.corpus.words.words()

        self.num_of_words: int = num_of_words
        self.separator: str = separator
        self.capitalize: bool = capitalize


    def generate(self):
        password_words = [random.choice(self.vocabulary) for _ in range(self.num_of_words)]
        if self.capitalize:
            password_words = [word.upper()  for word in password_words]
            
        print(password_words)
        return self.separator.join(password_words)
# ===============================
password_generator = MemorablePasswordGenerator()
password_generator.generate()
# ===============================




# ===============================
# Password Strength Checker
# ===============================
def password_strength(password: str) -> dict:
    """
    Basic strength estimation.
    Returns a dict with numeric score, label ('Weak'|'Medium'|'Strong') and detail booleans.
    """
    length = len(password)
    has_lower = bool(re.search(r'[a-z]', password))
    has_upper = bool(re.search(r'[A-Z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_symbol = bool(re.search(r'[^A-Za-z0-9]', password))

    # scoring: length (2 points), categories (4 points) => max 6
    score = 0
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if has_lower:
        score += 1
    if has_upper:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1

    if score <= 2:
        label = "Weak"
    elif score <= 4:
        label = "Medium"
    else:
        label = "Strong"

    return {
        "score": score,          # 0..6
        "label": label,
        "details": {
            "length": length,
            "has_lower": has_lower,
            "has_upper": has_upper,
            "has_digit": has_digit,
            "has_symbol": has_symbol
        }
    }

# ===============================





def save_password_to_file(password: str, filename: str = "passwords.txt"):
    """Save generated password with timestamp to file"""
    with open(filename, "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {password}\n")
    print(f"✅ Password saved to : {filename}")



# if __name__ == "__main__":
#     # PIN
#     pin_generator = PinGenerator(length=6)
#     pin = pin_generator.generate()
#     print(f"Generated PIN: {pin}")
#     save_password_to_file(pin)

#     # Random Password
#     random_password_generator = RandomPasswordGenerator(length=12, include_numbers=True, include_symbols=True)
#     random_pass = random_password_generator.generate()
#     print(f"Generated Random Password: {random_pass}")
#     save_password_to_file(random_pass)

#     # Memorable Password
#     memorable_password_generator = MemorablePasswordGenerator(num_of_words=3, separator='-', capitalize=True)
#     memorable_pass = memorable_password_generator.generate()
#     print(f"Generated Memorable Password: {memorable_pass}")
#     save_password_to_file(memorable_pass)







# Demo when run as script
if __name__ == "__main__":
    # quick demo
    gen = RandomPasswordGenerator(12, include_numbers=True, include_symbols=True)
    p = gen.generate()
    print("random:", p)
    print("strength:", password_strength(p))












