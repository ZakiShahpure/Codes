char = input("Enter character to check vowel or consonant")

if char.lower() in ['a','e','i','o','u']:
    print("The character is a vowel")
else:
    print("The character is consonant")