def is_palidnrome(word):
    Reversed=word[::-1]
    return word==Reversed
word=input("Enter the word:")
if is_palidnrome(word):
    print(f"{word} is a plaindrome")
else:
    print(f"{word} is not a palindrome")
