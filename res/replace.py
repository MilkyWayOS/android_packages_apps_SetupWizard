import os

def replace_string_in_file(file_path, old_string, new_string):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    new_content = content.replace(old_string, new_string)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

def replace_string_in_res_files(directory, old_string, new_string):
    for subdir, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".xml"):
                file_path = os.path.join(subdir, file)
                replace_string_in_file(file_path, old_string, new_string)

if __name__ == "__main__":
    res_directory = input("Enter the path to the res directory: ")
    old_string = "LineageOS"
    new_string = input("Enter the new string to replace 'LineageOS': ")

    replace_string_in_res_files(res_directory, old_string, new_string)
    print(f"Replaced all occurrences of '{old_string}' with '{new_string}' in XML files under {res_directory}")

