import os

def write_file(working_directory, file_path, content):
    working_directory_path = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory_path, file_path))

    if not abs_file_path.startswith(working_directory_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_file_path):
        file_directory = os.path.dirname(file_path)
        abs_file_directory = os.path.abspath(os.path.join(working_directory_path, file_directory))
        if not os.path.exists(abs_file_directory) and file_directory != "":
            try:
                os.makedirs(abs_file_directory)
            except Exception as e:
                return f'Error: Cannot create "{file_directory}", {e}'
    
    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
    except Exception as e:
        return f'Error: Cannot write to "{file_path}", {e}'

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'