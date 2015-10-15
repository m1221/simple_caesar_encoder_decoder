# Caesar Cipher Encoder and Decoder README

## Table of Contents
1. Author and Version Information
1. What is a Caesar Cipher?
1. Installation & Operation Instructions
1. File Manifest
1. Licensing Information


### 1. AUTHOR AND VERSION INFORMATION
* PRINCIPAL AUTHOR: Mario Portocarrero Jr
* AUTHOR EMAIL: m.portocarrero.jr@gmail.com
* DATE OF V1.0 RELEASE: 08/11/2015 
* AUTHOR OS: Windows 8.1
* PYTHON VERSION: 2.7.10
* GITHUB ACCOUNT: m1221
* CURRENT VERSION: 1.1
* CURRENT VERSION RELEASE DATE: 08/24/2015

### 2. WHAT IS A CAESAR CIPHER?
A Caesar cipher is a primative method of encryption that relies
on a letter-to-letter listing to transform plaintext characters 
to cipher characters.

The most basic type of Caesar cipher is a simple Caesar cipher.
A simple caesar cipher uses a numerical key (valued 1-25) to indicate
the magnitude of the displacement between pairngs of the plaintext
and cipher alphabets.

To make a caesar cipher table, follow the directions below.

1. Line up two alphabets, one on top of another. one is the plaintext alphabet and the other is the cipher alphabet
1. Displace the bottom alphabet by a numerical value (1-25). This value is referred to as the cipher key.
1. Replace the letters of the message using the alphabet table.

*_EXAMPLE:_*

CIPHER KEY: 2

PLAINTEXT: A B C D E F G H I J K... Z

CIPHER   : C D E F G H I J K L M... X

MSG: BRUTUS IS A BACKSTABBER

ENCODED MSG: DTWVWU KU C DCEMUVCDDGT

### 3. INSTALLATION & OPERATION INSTRUCTIONS
1. download the simple_caesar file onto your computer
1. have Python 2.7.10 installed
1. open your shell program and navigate to the simple_caesar file (If you don't know how to use your shell program, look up 'zed shaw shell crash course' in your favorite search engine.)
1. with the simple_caesar file as your current directory, enter `$ python simple_caesar.py`
1. have fun with simple caesar ciphers!

### 4. FILE MANIFEST
1. read_in.txt
1. read_out.txt
1. README.txt
1. simplecaesar.py

### 5. LICENSING INFORMATION
GNU GPLv3
