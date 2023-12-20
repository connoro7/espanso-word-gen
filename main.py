import sys
import itertools
import re

INPUT_FILE = "wordlist.txt"
MINIMUM_WORD_LENGTH = 4


def read_from_file(file_name, loglevel=False):
    try:
        with open(file_name, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        sys.exit(1)


def trim_whitespace(text: str, loglevel=False) -> str:
    result = text.strip()
    if loglevel:
        print("trimmed whitespace:", result)
        print("word count: ", len(result.split()))
    return result


def remove_punctuation(text: str, loglevel=False) -> str:
    text = (
        text.replace(".", "")
        .replace(",", "")
        .replace(";", "")
        .replace(":", "")
        .replace("!", "")
        .replace("?", "")
        .replace("(", "")
        .replace(")", "")
        .replace("[", "")
        .replace("]", "")
        .replace("{", "")
        .replace("}", "")
        .replace("'", "")
        .replace('"', "")
        .replace("-", "")
        .replace("_", "")
        .replace("/", "")
        .replace("\\", "")
        .replace("|", "")
        .replace("<", "")
        .replace(">", "")
        .replace("=", "")
        .replace("+", "")
        .replace("*", "")
        .replace("&", "")
        .replace("^", "")
        .replace("%", "")
        .replace("$", "")
        .replace("#", "")
        .replace("@", "")
    )
    if loglevel:
        print("removed punctuation:", text)
        print("word count: ", len(text.split()))
    return text


def remove_numbers(text: str, loglevel=False) -> str:
    text = (
        text.replace("0", "")
        .replace("1", "")
        .replace("2", "")
        .replace("3", "")
        .replace("4", "")
        .replace("5", "")
        .replace("6", "")
        .replace("7", "")
        .replace("8", "")
        .replace("9", "")
    )
    if loglevel:
        print("removed numbers:", text)
        print("word count: ", len(text.split()))
    return text


def remove_escape_chars(text: str, loglevel=False) -> str:
    text = (
        text.replace("\n", "")
        .replace("\t", "")
        .replace("\r", "")
        .replace("\b", "")
        .replace("\f", "")
        .replace("\v", "")
    )
    if loglevel:
        print("removed escape chars:", text)
        print("word count: ", len(text.split()))
    return text


def remove_short_words(
    text: str, loglevel=False, threshold=MINIMUM_WORD_LENGTH
) -> [str]:
    words = text.split()
    filtered_words = [word for word in words if len(word) > threshold]
    result = " ".join(filtered_words)
    # loglevel = True
    if loglevel:
        print("removed short words:", result)
        print("word count: ", len(result.split()))
    loglevel = False
    return result


def remove_short_words_re(
    text: str, loglevel=False, threshold=MINIMUM_WORD_LENGTH
) -> str:
    # Define a regular expression pattern to match words with at least 'threshold' characters
    pattern = r"\b\w{" + str(threshold) + r",}\b"

    # Use re.sub to remove words that don't meet the length criterion
    result = re.sub(pattern, "", text)

    return result


def remove_non_words(text: str, loglevel=False) -> str:
    text = text.split()
    alpha_words = [word for word in text if word.isalpha()]
    result = " ".join(alpha_words)
    if loglevel:
        print("removed non-words:", result)
        print("word count: ", len(result.split()))
    return result


def to_lowercase(text: str, loglevel=False) -> str:
    result = text.lower()
    if loglevel:
        print("lowercased:", result)
        print("word count: ", len(result.split()))
    return result


def only_unique_words(text: str, loglevel=False) -> str:
    words = text.split()
    if loglevel:
        print("before unique:", words, len(words), "\n")
    set_ = {s for s in words}
    if loglevel:
        print("set:", set_, len(set_), "\n")
    result = " ".join(set_)
    return result


def sort_by_alphabetically(text: str, loglevel=False) -> str:
    words = text.split()
    sorted_ = sorted(words)
    result = " ".join(sorted_)
    print("\nsorted alphabetically:", result)
    return result


def sort_by_length(text: str, loglevel=False) -> str:
    words = text.split()
    sorted_ = sorted(words, key=len)
    result = " ".join(sorted_)
    print("\nsorted by length:", result)
    return result


def process_word_list(loglevel=False):
    # get word list:
    # read words from file
    word_file: str = read_from_file(INPUT_FILE)
    if loglevel:
        print("original file:", word_file)
        print("word count: ", len(word_file.split()))

    word_file = trim_whitespace(word_file, loglevel)

    word_file = remove_punctuation(word_file, loglevel)

    word_file = remove_numbers(word_file, loglevel)

    word_file = remove_escape_chars(word_file, loglevel)

    print("PRE-SHORT: ", word_file)
    word_file = remove_short_words(word_file, loglevel, threshold=MINIMUM_WORD_LENGTH)
    # word_file = remove_short_words_re(
    #     word_file, loglevel, threshold=MINIMUM_WORD_LENGTH
    # )

    word_file = remove_non_words(word_file, loglevel)

    word_file = to_lowercase(word_file, loglevel)

    word_file = only_unique_words(word_file, loglevel)

    # word_file = sort_by_alphabetically(word_file, loglevel)

    word_file = sort_by_length(word_file, loglevel)

    processed_word_list = word_file.split()

    if loglevel:
        print(processed_word_list)
    return processed_word_list


def get_misspellings(word, loglevel=False):
    misspellings = list()
    for index, char in enumerate(word):
        if char == "s" and index == len(word) - 1:  # skip plurals
            continue
        missing_single_char = word[:index] + word[index + 1 :]
        misspellings.append(missing_single_char)
    if loglevel:
        print(f"misspellings: {misspellings}")
    return misspellings
    # for each letter
    # swap adjacent letters in either direction (to the left, to the right), and append to results


def main(loglevel=False):
    processed_words = process_word_list(loglevel)

    # create misspellings
    misspellings = list()
    for word in processed_words:
        misspellings.append(get_misspellings(word))

    flattened = list(itertools.chain.from_iterable(misspellings))

    print(flattened)


if __name__ == "__main__":
    main()