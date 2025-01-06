with open("books/frankenstein.txt") as f:
    file_contents = f.read()
def print_content(str):
    print(str)
def count_words(str):
    words = file_contents.split()
    counter=0
    for word in words:
        counter+=1
    return counter
def count_characters(str):
    dict = {}
    for char in str:
        if char.lower() in dict:
            dict[char.lower()]+=1
        else:
            dict[char.lower()]=1
    return dict
def sort_on(dict):
    return dict["num"]
def print_report(str):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(str)} words found in the document")
    dict = count_characters(str)
    for key, value in dict.items():
        if key.isalpha():
            print(f"The '{key}' character was found {value} times")
    print("--- End report ---")

print_report(file_contents)