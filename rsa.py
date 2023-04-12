import random
import math
import argparse

def generate_keys():
    p = generate_prime_number()
    q = generate_prime_number()

    n = p * q

    phi = (p - 1) * (q - 1)

    e = choose_public_key(phi)

    d = compute_private_key(e, phi)

    return (n, e), (n, d)

def generate_prime_number():
    while True:
        num = random.randint(2, 100)
        if is_prime(num):
            return num

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def choose_public_key(phi):
    while True:
        e = random.randint(2, phi)
        if math.gcd(e, phi) == 1:
            return e

def compute_private_key(e, phi):
    d = 0
    while True:
        d += 1
        if (d * e) % phi == 1:
            return d

def encrypt(message, public_key):
    n, e = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

def decrypt(encrypted_message, private_key):
    n, d = private_key
    decrypted_message = [chr(pow(char, d, n)) for char in encrypted_message]
    return "".join(decrypted_message)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="RSA")
    parser.add_argument("operation", choices=["encrypt", "decrypt", "generate_keys"])
    parser.add_argument("-f", "--file", type=str, help="Input file")
    parser.add_argument("-n", "--public_key", type=int, nargs=2, help="two integers")
    parser.add_argument("-d", "--private_key", type=int, nargs=2, help="two integers")

    args = parser.parse_args()

    if args.operation == "encrypt":
        if not args.file or not args.public_key:
            print("Missing the file and public key.")
        else:
            with open(args.file, "r") as file:
                message = file.read()
                public_key = tuple(args.public_key)
                encrypted_message = encrypt(message, public_key)
                print("Encrypted message:", encrypted_message)

    elif args.operation == "decrypt":
        if not args.file or not args.private_key:
            print("Missing the file and private key.")
        else:
            with open(args.file, "r") as file:
                encrypted_message = list(map(int, file.read().split()))
                private_key = tuple(args.private_key)
                decrypted_message = decrypt(encrypted_message, private_key)
                print("Decrypted message:", decrypted_message)

    elif args.operation == "generate_keys":
        public_key, private_key = generate_keys()
        print("Public key:", public_key)
        print("Private key:", private_key)

