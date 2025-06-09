def get_num_of_words(content):
    return len(content.split())

def get_count_of_chars(text):
    count_chars_dict = {}
    split_text = list(text.lower())
    for char in split_text:
        if char in count_chars_dict:
            count_chars_dict[char] += 1
        else:
            count_chars_dict[char] = 1
    return count_chars_dict

def get_sorted_dict(text_dict):
    sorted_char_dict = dict(sorted(text_dict.items(), key=lambda item: item[1], reverse=True))
    new_dict = {}
    for item in sorted_char_dict:
        if item.isalpha():
            new_dict[item] = sorted_char_dict[item]
            
    return new_dict
