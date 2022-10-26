def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    for index in range(len(phrase)):
        if phrase[index] == to_swap.upper():
            phrase = phrase[:index] + phrase[index].lower() + phrase[index+1:]
        elif phrase[index] == to_swap.lower():
            phrase = phrase[:index] + phrase[index].upper() + phrase[index+1:]
    return phrase