def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        total_words = get_num_words(words)
        get_num_chars(words)
    print(total_words)
    

def get_num_words(words):
    count = 0
    for f in words:
        count += 1
    return count

def get_num_chars(words):
    total_lowered_chars = {}
    
    
    for k in words:
        lowered_string = k.lower()
        for char in lowered_string:
            if char in total_lowered_chars:
                total_lowered_chars[char] += 1
            else:
                total_lowered_chars[char] = 1
    
    sorted_total_lowered_chars = dict(sorted(total_lowered_chars.items()))

    
    print("done")
    total_lowered_chars.sort(reverse=True, key=sort_on)
    print(total_lowered_chars)
    print(sorted_total_lowered_chars)
    #return lowered_string

if __name__ == "__main__":
    main()