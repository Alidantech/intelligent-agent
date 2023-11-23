import re
from . import data

swahili_dict = data.load_swahili_dictionary("kamusi/words.json")


def search_word(user_word, swahili_dict):
    user_word = user_word.lower()

    for word_id, word_info in swahili_dict.items():
        if re.match(rf"\b{re.escape(user_word)}\b", word_info["Word"].lower()):
            return f"'{user_word}' is found in the Swahili dictionary. Meaning: {word_info['Meaning']}"

    for word_id, word_info in swahili_dict.items():
        conjugation = word_info.get("Conjugation")
        if conjugation and re.match(
            rf"\b{re.escape(user_word)}\b", conjugation.lower()
        ):
            return f"'{user_word}' is found in a word with conjugations. Original Word: {word_info['Word']}. Meaning: {word_info['Meaning']}"
        elif conjugation is None and re.match(
            rf"\b{re.escape(user_word)}\b", word_info["Word"].lower()
        ):
            return f"'{user_word}' is found in a word without conjugations. Meaning: {word_info['Meaning']}"

    return f"'{user_word}' not found in the Swahili dictionary or any word with conjugations."


def check_sentence_words(user_input):
    user_input = user_input.lower()
    words = re.findall(r"\b\w+\b", user_input)  # Tokenize the input into words

    words_with_indexes = []
    incorrect_word_indexes = []

    for word in words:
        start_index = user_input.find(word)
        end_index = start_index + len(word)
        words_with_indexes.append(
            {"word": word, "start_index": start_index, "end_index": end_index}
        )

        result = search_word(word, swahili_dict)
        if "not found" in result.lower():
            incorrect_word_indexes.append(start_index)
        
    if incorrect_word_indexes:
        return incorrect_word_indexes
    else:
        return words


# Example usage
user_input = "Your input sentence here"
result = check_sentence_words(user_input)
print(result)

check_sentence_words
