def main():
    try:
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()
            print(file_contents)
    except FileNotFoundError:
        print("Error: Could not find frankenstein.txt in books directory!")
    except Exception as e:
        print(f"An error occurred: {e}")

def words_count():
    try:
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()
            words = file_contents.split()
            print(f"Frankenstein book contains {len(words)} words.")
    except FileNotFoundError:
        print("Error: Could not find frankenstein.txt in books directory!")
    except Exception as e:
        print(f"An error occurred: {e}")

def count_characters(text):
    text = text.lower()
    characters = {}
    for c in text:
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    return characters

def character_count():
    try:
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()
        
        result = count_characters(file_contents)
        
        print(result)

    except FileNotFoundError:
        print("Error: Could not find frankenstein.txt in books directory!")
    except Exception as e:
        print(f"An error occurred: {e}")

def character_count_return():
    try:
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()
        
        result = count_characters(file_contents)

        return result
    except FileNotFoundError:
        print("Error: Could not find frankenstein.txt in books directory!")
    except Exception as e:
        print(f"An error occurred: {e}")

def print_report(): # Proposed by Boots
    result = character_count_return()  # Use the "returning" version
    if result:  # Ensure result is valid
        sorted_result = sorted(result.items(), key=lambda item: item[1], reverse=True)
        for char, count in sorted_result:
            if char.isalpha():  # Include only alphabetic characters
                print(f"The '{char}' character was found {count} times")

print("--- Begin report of books/frankenstein.txt ---")
print()
words_count()
print()
print_report()
print()
print("--- End report ---")     
