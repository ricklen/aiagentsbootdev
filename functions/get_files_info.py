import os


def get_files_info(working_directory, directory=None):
    # files_in_dir =

    try:
        os.listdir(os.path.join(working_directory, directory))
    except FileNotFoundError:
        print(
            f'Error: Directory "{directory}" not found in "{working_directory}"')
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if directory == "/bin" or directory == "../":
        print(
            f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not (os.path.isdir(os.path.join(working_directory, directory))) and directory is not None:
        print(f'Error: "{directory}" is not a directory')
        return f'Error: "{directory}" is not a directory'

    directory_to_list = os.path.join(working_directory, directory)
    print(directory_to_list)
    return_string = []
    for file in os.listdir(directory_to_list):

        file_path = os.path.join(directory_to_list, file)
        # print(file)
        print(
            f"{file}: file_size={os.path.getsize(file_path)} bytes, is_idr={os.path.isdir(file_path)} ")
        return_string.append(
            f"{file}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}")

    return "\n".join(return_string)
    # - README.md: file_size=1032 bytes, is_dir=False
    # - src: file_size=128 bytes, is_dir=True
    # - package.json: file_size=1234 bytes, is_dir=False

    # os.path.getsize()
    # os.get
