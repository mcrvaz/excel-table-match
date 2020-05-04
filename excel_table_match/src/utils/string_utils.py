import unicodedata


def unicode_contains(str1, str2) -> bool:
    normalized1 = remove_diacritics(str1).casefold()
    normalized2 = remove_diacritics(str2).casefold()
    return normalized2 in normalized1


def remove_diacritics(text):
    normalized = unicodedata.normalize("NFKD", text)
    return "".join(c for c in normalized if unicodedata.category(c) != "Mn")
