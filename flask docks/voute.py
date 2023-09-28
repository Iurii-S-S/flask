def search4letters(phrase:str, letters:'aeiou') -> set:
    return set(letters).intersection(set(phrase))