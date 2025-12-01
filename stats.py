def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_chars(text):
    char_dict = {}
    for c in text:
        lowered = c.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1

    return char_dict


def sort_on(items):
    return items["num"]


def sort_dict(char_dict):
    dict_list = []
    for c in char_dict:
        new_dict = {"char": c, "num": char_dict[c]}
        dict_list.append(new_dict)

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
