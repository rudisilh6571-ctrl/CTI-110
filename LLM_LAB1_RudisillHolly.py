# Holly Rudisill


import secrets
import string

PASSWORD_LENGTH = 10
SPECIAL_CHARS = "!@#$%^&*()-_=+?"

# Small blocklist of common words/patterns that must not appear in a password.
COMMON_WORDS = {
    "password", "pass", "admin", "login", "welcome", "qwerty", "letmein",
    "monkey", "dragon", "master", "hello", "love", "abc", "user", "test",
    "secret", "iloveyou", "sunshine", "football", "baseball",
}

rng = secrets.SystemRandom()


def contains_common_word(password: str) -> bool:
    lowered = password.lower()
    return any(word in lowered for word in COMMON_WORDS)


def is_valid(password: str) -> bool:
    lowered = password.lower()
    return (
        len(password) == PASSWORD_LENGTH
        and len(set(lowered)) == PASSWORD_LENGTH  # no repeats (A and a count as the same letter)
        and any(c.isupper() for c in password)
        and any(c.islower() for c in password)
        and any(c in SPECIAL_CHARS for c in password)
        and not contains_common_word(password)
    )


def generate_password() -> str:
    all_chars = string.ascii_letters + string.digits + SPECIAL_CHARS
    while True:
        # Guarantee one of each required type, then fill the rest randomly.
        chars = [
            rng.choice(string.ascii_uppercase),
            rng.choice(string.ascii_lowercase),
            rng.choice(SPECIAL_CHARS),
        ]
        chars += rng.choices(all_chars, k=PASSWORD_LENGTH - len(chars))
        rng.shuffle(chars)
        password = "".join(chars)
        if is_valid(password):
            return password


if __name__ == "__main__":
    print("Your new password:", generate_password())