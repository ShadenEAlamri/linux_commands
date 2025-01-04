import os
file_path='file.py'
try:
	os.chmod(file_path, 0o775)
	print(f"permissions for'{file_path}' set to rwxrwxr-x")
except permissionsError:
	print(f"Error: you do not have permission to change the permission of '{file_pth}'")
except FileNotFoundError:
	print(f"Error: the file '{file_path}' does not exist.")
except Exception as e:
	print(f"An unexpected error occurred: {e}")




