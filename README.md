# RSA

## Usage

```
$ python3 rsa.py [-h] [-f FILE] [-n PUBLIC_KEY PUBLIC_KEY] [-d PRIVATE_KEY PRIVATE_KEY] {encrypt,decrypt,generate_keys}

positional arguments:
  {encrypt,decrypt,generate_keys}

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Input file
  -n PUBLIC_KEY PUBLIC_KEY, --public_key PUBLIC_KEY PUBLIC_KEY
                        two integers
  -d PRIVATE_KEY PRIVATE_KEY, --private_key PRIVATE_KEY PRIVATE_KEY
                        two integers
```

## Example

```
$ python3 rsa.py generate_keys
Public key: (3233, 2939)
Private key: (3233, 1379)

$ python3 rsa.py -f decrypted.txt -n 3233 2939 encrypt
Encrypted message: [3161, 3079, 1111, 1111, 3122, 21, 1179, 3122, 2112, 1111, 524, 1928, 116]

$ python3 rsa.py -f encrypted.txt -d 3233 1379 decrypt
Decrypted message: Hello world!
```