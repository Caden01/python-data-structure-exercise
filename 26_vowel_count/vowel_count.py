def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    
    return {ltr.lower(): phrase.lower().count(ltr.lower()) for ltr in phrase if ltr.lower() in "aeiou"}
    
print(vowel_count('HOW ARE YOU? i am great!'))