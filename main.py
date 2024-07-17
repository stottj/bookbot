def main():
    print("--- Begin report of books/frankenstein.txt ---")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        total_words = get_num_words(words)
        print(f'{total_words} words found in the document')
        print("")
        get_num_chars(words)
    print("--- End report ---")
    

def get_num_words(words):
    count = 0
    for f in words:
        count += 1
    return count

def sort_on(d):
    return d["count"]

def get_num_chars(words):
    total_lowered_chars = {} 
    
    for k in words:
        lowered_string = k.lower()
        for char in lowered_string:
            if char.isalpha():
                if char in total_lowered_chars:
                    total_lowered_chars[char] += 1
                else:
                    total_lowered_chars[char] = 1
    
    list_for_report = []

    for k, v in total_lowered_chars.items():
        new_dictionary = {'char': k, 'count': v}
        list_for_report.append(new_dictionary)
    
    list_for_report.sort(key=sort_on, reverse=True)

    for item in list_for_report:
        print(f'The "{item["char"]}" was found "{item["count"]}" times')

if __name__ == "__main__":
    main()