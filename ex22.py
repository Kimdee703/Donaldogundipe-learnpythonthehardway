# Strings, Bytes, and Character Encodings
# Excercise 22
import sys
script, input_encoding, errors = sys.argv
# Unpacks the command line arguments provided when running the script.
# script: The name of the Python file (e.g., 'your_script_name.py')
# input_encoding: The target encoding to use for demonstration (e.g., 'utf-8', 'gbk')
# errors: The error handling scheme (e.g., 'strict', 'ignore', 'replace')

# Main function that handles recursive reading of the file lines.
def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main (language_file, encoding, errors)

def print_line(line, encoding, errors):    
    next_lang = line.strip()
    raw_bytes = next_lang.encode (encoding, errors=errors)   
    cooked_string = raw_bytes.decode(encoding, errors=errors)
      
    print(raw_bytes, "<===>", cooked_string)
languages = open("languages.txt", encoding="utf-8")
# using the standard UTF-8 encoding. This is crucial for handling international characters correctly.

main(languages, input_encoding, errors)

