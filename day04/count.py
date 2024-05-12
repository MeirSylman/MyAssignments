import sys

def file_propreties (file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        characters_num = len(content)
        lines_num = content.count('\n')
        words_num = len(content.split(" "))

        print(f'Properties for the file "{file_name}" :')
        print(f"Number of characters: {characters_num}")
        print(f"Number of lines: {lines_num}")
        print(f"Number of words: {words_num}")


file_name = sys.argv[1]
file_propreties(file_name)
