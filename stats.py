def count_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    split_words = file_contents.split()
    num_words = len(split_words)
    return f"Found {num_words} total words"

def count_characters(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    count_dict = {
    }
    for char in file_contents.lower():
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict

def sorted_dict(count_dict):
    chars_list = []

    for char, count in count_dict.items():
        chars_list.append({"char": char, "num": count})

    chars_list.sort(reverse=True, key=lambda dict:dict["num"])

    return chars_list