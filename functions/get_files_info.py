import os

def get_files_info(working_directory, directory=None):
    working_directory_path = os.path.abspath(working_directory)
    
    target_directory = directory if directory is not None else ""
    directory_path = os.path.abspath(os.path.join(working_directory_path, target_directory))

    if not directory_path.startswith(working_directory_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(directory_path):
        display_directory = directory if directory is not None else "."
        return f'Error: "{display_directory}" is not a directory'

    contents = []

    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        try:
            file_size = os.path.getsize(file_path)
            is_dir = os.path.isdir(file_path)
            contents.append("- {}: file_size={} bytes, is_dir={}".format(file_name, file_size, is_dir))
        except OSError:
           continue
        
    return "\n".join(contents)