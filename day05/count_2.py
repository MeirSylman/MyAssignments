import sys

def characters_count(file_content):
    characters_num = len(file_content)
    return characters_num

def lines_count(file_content):
    lines_num = file_content.count('\n')
    return lines_num

def words_count(file_content):
    words_num = len(file_content.split())
    return words_num

def file_properties(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        characters_number = characters_count(content)
        lines_number = lines_count(content)
        words_number = words_count(content)
        print(f'Properties for the file "{file_name}" :')
        print(f"Number of characters: {characters_number}")
        print(f"Number of lines: {lines_number}")
        print(f"Number of words: {words_number}")
        return file_name, characters_number, lines_number, words_number


if __name__ == "__main__":
    file_name = sys.argv[1]
    file_properties(file_name)

