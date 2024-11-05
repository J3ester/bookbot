def wordcount():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
        
    return word_count

def charcount():
    characters = {}
    cha ="abcdefghijklmnopqrstuvwxyz"
    for c in cha:
        characters[c] = 0
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        wordcontent = file_contents.lower()
        for c in wordcontent:
            for a in characters:
                if c == a:
                    characters[a] += 1
                    break
    return characters

def main():
    print("--- report of books/frankstein.txt ---")
    wc = wordcount()
    abc = charcount()
    print(f"{wc} words found in the document")
    print()
    for a in abc:
        print(f"The {a} character was found {abc[a]} times")
    print("--- End report ---")



main()
