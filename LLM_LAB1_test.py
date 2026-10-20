# HOlly Rudisill

import secrets
import string

PASSWORD_LENGTH = 10
SPECIAL_CHARS = "!@#$%^&*()-_=+?"

# 50 easy-to-remember words. Each one has no repeated letters, so the
# finished password never repeats a letter.
WORDS = [
    "star", "blue", "fish", "bird", "lake", "rain", "wolf", "gold", "fire",
    "king", "jump", "sand", "rock", "wind", "home", "farm", "snow", "bear",
    "dust", "gift", "hand", "lion", "nest", "pink", "ship",
    "tiger", "plane", "bread", "night", "light", "storm", "cloud", "flame",
    "stone", "water", "mouse", "horse", "brick", "chair", "music", "magic",
    "house", "ocean", "pearl", "dream", "beach",
    "planet", "garden", "orange", "silver",
]

rng = secrets.SystemRandom()


def is_valid(password: str) -> bool:
    lowered = password.lower()
    return (
        len(password) == PASSWORD_LENGTH
        and len(set(lowered)) == PASSWORD_LENGTH  # no repeats (A and a count as the same)
        and any(c.isupper() for c in password)
        and any(c.islower() for c in password)
        and any(c in SPECIAL_CHARS for c in password)
        and any(c.isdigit() for c in password)
    )


def generate_password() -> tuple[str, str]:
    """Return (password, word_used)."""
    word = rng.choice(WORDS)
    tail_len = PASSWORD_LENGTH - len(word)

    # Mix of digits and specials (at least one of each), no repeats.
    num_digits = rng.randint(1, tail_len - 1)
    tail = rng.sample(string.digits, num_digits)
    tail += rng.sample(SPECIAL_CHARS, tail_len - num_digits)
    rng.shuffle(tail)

    password = word.capitalize() + "".join(tail)
    return password, word


if __name__ == "__main__":
    pw, word = generate_password()
    assert is_valid(pw)
    print("Your new password:", pw)
    print("Remember the word:", word)