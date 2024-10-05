<p align="center">
    <h1 align="center">PYTHON-VIGENERE</h1>
</p>
<p align="center">
    <em><code>❯ encryption, decryption and kasiski</code></em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/naguiagahnim/Python-Vigenere?style=flat&logo=opensourceinitiative&logoColor=white&color=ff00bc" alt="license">
	<img src="https://img.shields.io/github/last-commit/naguiagahnim/Python-Vigenere?style=flat&logo=git&logoColor=white&color=ff00bc" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/naguiagahnim/Python-Vigenere?style=flat&color=ff00bc" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/naguiagahnim/Python-Vigenere?style=flat&color=ff00bc" alt="repo-language-count">
</p>
<p align="center">
		<em>Built with:</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
</p>

<br>

![Camus](https://media1.tenor.com/m/aNzzrsihnysAAAAC/albertcamus.gif)

#####  Quick Links

- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
    - [ Prerequisites](#-prerequisites)
    - [ Installation](#-installation)
    - [ Usage](#-usage)
    - [ Tests](#-tests)
- [ Acknowledgments](#-acknowledgments)

---

##  Overview

This project implements the Vigenère cipher for encryption and decryption of text. It includes functions for both encrypting and decrypting messages using a given key, and handles both alphabetic and special characters.

---

##  Features

- Encrypts text using the Vigenère cipher.
- Decrypts text using the Vigenère cipher.
- Handles both alphabetic and special characters.
- Implements the Kasiski method for cryptanalysis.

---

##  Repository Structure

```sh
└── Python-Vigenere/
    ├── Sauvegarde
    │   ├── clef.txt
    │   ├── texte.txt
    │   └── texte_chiffre.txt
    ├── main.py
    ├── kasiski.py
    └── tests.py
```
---

##  Modules

<details closed><summary>Summary</summary>

| File | Summary                                                                                   |
| --- |-------------------------------------------------------------------------------------------|
| [main.py](https://github.com/naguiagahnim/Python-Vigenere/blob/main/main.py) | <code>❯ The main file that is executed</code>                                             |
| [kasiski.py](https://github.com/naguiagahnim/Python-Vigenere/blob/main/kasiski.py) | <code>❯ The file containing the Kasiski method implementation</code>                      |
[vigenere.py](https://github.com/naguiagahnim/Python-Vigenere/blob/main/vigenere.py) | <code>❯ The file containing the Vigenere encryption and decryption implementations</code> |
| [tests.py](https://github.com/naguiagahnim/Python-Vigenere/blob/main/tests.py) | <code>❯ The file containing the test cases</code>                                         |

</details>

<details closed><summary>Save files (./Sauvegarde)</summary>

| File                                                                                                                                | Summary                                                                       |
|-------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| [texte_chiffre.txt](https://github.com/naguiagahnim/Python-Vigenere/blob/main/Sauvegarde/texte_chiffre.txt)                         | <code>❯ The file saving the encrypted text</code>                             |
| [texte.txt](https://github.com/naguiagahnim/Python-Vigenere/blob/main/Sauvegarde/texte.txt)                                         | <code>❯ An input file for the functions, containing the decrypted text</code> |
| [clef.txt](https://github.com/naguiagahnim/Python-Vigenere/blob/main/Sauvegarde/clef.txt)                                           | <code>❯ An input file for the functions, containing the key</code>            |
| [texte_chiffre_tests_vian.txt](https://github.com/naguiagahnim/Python-Vigenere/blob/main/Sauvegarde/texte_chiffre_tests_vian.txt)   | <code>❯ A sample non-crypted text used for test cases</code>                  
| [texte_chiffre_tests_camus.txt](https://github.com/naguiagahnim/Python-Vigenere/blob/main/Sauvegarde/texte_chiffre_tests_camus.txt) | <code>❯ A sample non-crypted text used for test cases</code>                  |

</details>

---

##  Getting Started

###  Prerequisites

`Python 3.x`

###  Installation

Build the project from source:

1. Clone the Python-Vigenere repository:
```sh
❯ git clone https://github.com/naguiagahnim/Python-Vigenere
```

2. Navigate to the project directory:
```sh
❯ cd Python-Vigenere
```

3. Install the required dependencies:
```sh
❯ pip install -r requirements.txt
```

###  Usage

To run the project, execute the following command:

```sh
❯ python main.py
```

###  Tests

#### Test Case 1
- **Plaintext**: BONJOUR$@25
- **Key**: CLEF
- **Expected Ciphertext**: E@SPRFW*C>:

#### Test Case 2
- **Plaintext**: The original text used in `./Sauvegarde/texte.txt`
- **Key**: The key used in `./Sauvegarde/clef.txt`
- **Expected Ciphertext**: The expected encrypted text in `./Sauvegarde/texte_chiffre.txt`

#### Test Case 3
- **Plaintext**: The encrypted text used in `./Sauvegarde/texte_chiffre_tests_camus.txt`
- **Key**: ABSURDE
- **Expected Key Length**: 7

#### Test Case 4
- **Plaintext**: The encrypted text used in `./Sauvegarde/texte_chiffre_tests_vian.txt`
- **Key**: BORIS
- **Expected Key Length**: 5

Execute the test suite using the following command:

```sh
❯ pytest
```

---


##  Acknowledgments


- Resources: [Wikipedia - Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher), [Wikipedia - List of Unicode Characters](https://en.wikipedia.org/wiki/List_of_Unicode_characters), [Wikipedia - Kasiski examination](https://en.wikipedia.org/wiki/Kasiski_examination), [Onete.net](onete.net).

---
