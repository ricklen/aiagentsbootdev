from functions.get_files_info import get_files_info

result = get_files_info("calculator", ".")
get_files_info("calculator", "pkg")
get_files_info("calculator", "/bin")
get_files_info("calculator", "../")

print("Files in the current directory:")
print(result)
