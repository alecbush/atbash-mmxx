# Atbash MMXX Cipher
Atbash MMXX, or 2020, is an experimental cipher project that explores the advanced capabilities of [Atbash](https://en.wikipedia.org/wiki/Atbash) by adding rotation key values to a reversed alphabet.

This project is intended only for research and personal use.

## Install
```
$ pip install .
```

## Rotbash
Rotbash is a modifed Atbash cipher that takes in a "rotate" variable. 
```
$ python -m atbashmmxx rotbash "Hello, World!" -r 7
Lohhe, Webhp!
```
To decrypt, pass the cipher text back into the Rotbash command.
```
$ python -m atbashmmxx rotbash "Lohhe, Webhp!" -r 7
Hello, World!
```
Providing no rotate value produces the same output as a standard Atbash cipher.
```
$ python -m atbashmmxx rotbash "Hello, World!"
Svool, Dliow!
```

## Keybash
Keybash is a series of Rotbash operations that uses an alphabetic key instead of a rotation value.
```
$ python -m atbashmmxx keybash "Hello, World!" -k "secret"
Armxh, Ktemf!
```
Decrypting, like Rotbash, only requires inputting the cipher text through the same command with the correct key.
```
$ python -m atbashmmxx keybash "Armxh, Ktemf!" -k "secret"
Hello, World!
```
