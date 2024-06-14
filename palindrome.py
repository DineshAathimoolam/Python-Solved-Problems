def is_palindrome(word):
    return word==word[::-1]
word=input('Enter the Word while check whether the word is palindrome or not: ')
ans=is_palindrome(word)
if ans:
    print(f'You given Word {word} is a Palindrome.')
else:
    print(f'You given Word {word} is not a Palindrome.')

    
