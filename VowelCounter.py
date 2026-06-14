def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
 
 
sentence = input("Enter a sentence: ")
print(f"Number of vowels: {count_vowels(sentence)}")