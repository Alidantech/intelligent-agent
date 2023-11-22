from . import data

swahili_dict = data.load_swahili_dictionary("kamusi/words.json")


def get_suggestions(current_word):
    suggestions = []

    # Look for suggestions in the main dictionary
    for word_info in swahili_dict.values():
        word = word_info["Word"].lower()
        if word.startswith(current_word):
            suggestions.append(word)

    # Look for suggestions in words with conjugations
    for word_info in swahili_dict.values():
        conjugation = word_info.get("Conjugation")
        if conjugation and conjugation.lower().startswith(current_word):
            suggestions.append(conjugation)

    return suggestions
