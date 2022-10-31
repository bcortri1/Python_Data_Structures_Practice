def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    rev_vowels = ''.join([char for char in s[::-1] if char.lower() in "aeiou"])
    r_index = 0
    for index in range(len(s)):
        if s[index].lower() in "aeiou":
            s = s[:index] + rev_vowels[r_index] + s[index+1:]
            r_index += 1
    return s
