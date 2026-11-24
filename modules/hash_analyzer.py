import hashlib
import re
from pathlib import Path


HASH_FORMATS = {
    32: "MD5",
    40: "SHA-1",
    56: "SHA-224",
    64: "SHA-256 or SHA3-256",
    96: "SHA-384",
    128: "SHA-512 or SHA3-512"
}


def identify_hash(hash_value):
    hash_value = hash_value.strip().lower()

    if not re.fullmatch(r"[0-9a-f]+", hash_value):
        return "Invalid: Non-hexadecimal characters"

    possible_format = HASH_FORMATS.get(len(hash_value))

    if possible_format:
        return f"Possible format: {possible_format}"

    return "Unknown hash length"


def load_hashes(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return [
            line.strip()
            for line in file
            if line.strip()
        ]


def analyze_hashes(file_path):
    hashes = load_hashes(file_path)

    print("\n========== HASH ANALYZER ==========")

    for index, hash_value in enumerate(hashes, start=1):
        result = identify_hash(hash_value)

        print(f"\nHash {index}: {hash_value}")
        print(f"Length: {len(hash_value)}")
        print(f"Analysis: {result}")

    print("\n========== ANALYSIS COMPLETED ==========")


def generate_hash(text, algorithm="sha256"):
    supported_algorithms = {
        "md5",
        "sha1",
        "sha224",
        "sha256",
        "sha384",
        "sha512"
    }

    algorithm = algorithm.lower()

    if algorithm not in supported_algorithms:
        raise ValueError("Unsupported hash algorithm")

    encoded_text = text.encode("utf-8")

    return hashlib.new(
        algorithm,
        encoded_text
    ).hexdigest()


if __name__ == "__main__":
    analyze_hashes("datasets/sample_hashes.txt")

    sample = "hello"

    print("\nSample SHA-256 generation:")
    print(generate_hash(sample, "sha256"))
