def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    space_found = True
    new_phrase = ""
    phrase = phrase.lower()
    for char in phrase:
        if space_found:
            new_phrase += char.upper()
        else:
            new_phrase += char

        if char == " ":
            space_found = True
        else:
            space_found = False
    return new_phrase
