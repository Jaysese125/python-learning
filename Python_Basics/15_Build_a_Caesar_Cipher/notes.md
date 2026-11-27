# Build a Caesar Cipher

## Overview

This workshop focuses on implementing a Caesar cipher, a basic encryption technique that shifts letters in the alphabet by a fixed number of positions.

The program can encrypt and decrypt messages using a reusable function.

## 1. String Slicing and Alphabet Shifting

A Caesar cipher replaces each letter with another letter based on a specified shift.

For example, with a shift of 5:

- a → f
- b → g
- c → h

Python string slicing allows us to create a shifted alphabet.

```python
alphabet = 'abcdefghijklmnopqrstuvwxyz'
shift = 5

shifted_alphabet = alphabet[shift:] + alphabet[:shift]
```

The first slice extracts the alphabet starting from the shift position, while the second slice adds the missing characters to the end.

## 2. Creating a Translation Table

Python provides `str.maketrans()` to create a character translation table.

```python
translation_table = str.maketrans(
    alphabet,
    shifted_alphabet
)
```

The method maps each character in the first string to its corresponding character in the second string.

To support uppercase characters, both lowercase and uppercase alphabets can be included.

```python
str.maketrans(
    alphabet + alphabet.upper(),
    shifted_alphabet + shifted_alphabet.upper()
)
```

## 3. Translating Strings

The `.translate()` method applies the translation table to a string.

```python
text = 'hello world'
encrypted_text = text.translate(translation_table)
```

It returns a new string with the mapped characters replaced.

## 4. Making the Cipher Reusable with Functions

Instead of hardcoding the message and shift, we can use function parameters.

```python
def caesar(text, shift, encrypt=True):
    pass
```

- `text`: Message to process.
- `shift`: Number of positions to move letters.
- `encrypt`: Determines whether to encrypt or decrypt. Its default value is `True`.

## 5. Returning Values

The `return` statement allows the function to send the encrypted or decrypted message back to the caller.

```python
return text.translate(translation_table)
```

This makes the function reusable because its result can be stored in a variable or passed to another function.

## 6. Input Validation

The program validates the shift before performing encryption or decryption.

**Checking the data type:**

```python
if not isinstance(shift, int) or isinstance(shift, bool):
    return 'Shift must be an integer value.'
```

An important Python behavior is that Boolean values are considered a subclass of integers.

```python
isinstance(True, int)   # True
isinstance(False, int)  # True
```

Because of this, an additional Boolean check is necessary to prevent `True` and `False` from being accepted as shift values.

**Checking the allowed range:**

```python
if shift < 1 or shift > 25:
    return 'Shift must be an integer between 1 and 25.'
```

The shift must be between 1 and 25.

## 7. Encryption and Decryption

Encryption shifts letters forward in the alphabet.

Decryption shifts letters in the opposite direction.

```python
if not encrypt:
    shift = -shift
```

Using a negative shift reverses the direction of the translation.

Two separate functions make the program easier to use:

```python
def encrypt(text, shift):
    return caesar(text, shift)


def decrypt(text, shift):
    return caesar(text, shift, False)
```

Both functions use the same Caesar cipher implementation.

## Key Takeaways

- String slicing can be used to rearrange characters.
- `str.maketrans()` creates a character translation table.
- `.translate()` applies the translation table to strings.
- Functions can have default parameter values.
- `return` allows functions to produce reusable results.
- `isinstance()` checks data types.
- Boolean values are subclasses of integers in Python.
- Logical operators can combine multiple validation conditions.
- Negative shifts can reverse the direction of encryption.

## Workshop Result

The program successfully decrypts:

`Pbhentr vf sbhaq va hayvxryl cynprf.`

Result:

**Courage is found in unlikely places.**

---

## Personal Experiment Ideas

These are ideas I want to explore after completing the workshop.

### 1. Automatic Caesar Cipher Decoder

Build a separate Python script that attempts to decrypt a Caesar cipher without knowing the original shift.

Possible approaches:

- Try all 25 possible shifts (brute force).
- Display every possible decrypted message.
- Identify likely English words.
- Rank possible results based on letter frequency.
- Eventually automate the selection of the most likely plaintext.

### 2. Python Boolean and Integer Behavior

Experiment with how Python treats `True` and `False` as integer values.

```python
print(True + True)   # 2
print(True + False)  # 1
print(False * 10)    # 0
```

Investigate:

- Why Boolean values are subclasses of integers.
- How `isinstance()` behaves with Boolean values.
- Why explicit Boolean validation is sometimes necessary.
- What happens when Boolean values are accepted by numeric calculations.
- How to write safer input validation.

### 3. Cipher Security Experiments

Explore the weaknesses of Caesar ciphers through controlled experiments using messages that I create.

- Test all possible shifts automatically.
- Investigate frequency analysis.
- Compare encryption and decryption results.
- Understand why a Caesar cipher is not suitable for protecting sensitive information.

**Future goal:** Build an automatic Caesar cipher decoder and experiment with Python's Boolean and integer behavior to strengthen my understanding of data types, validation, and basic security concepts.