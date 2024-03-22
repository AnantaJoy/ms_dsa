import os

# Define the root directory
root_dir = '/home/ananta/Desktop/ms_dsa'

# Iterate over each folder in the root directory
for folder_name in os.listdir(root_dir):
    folder_path = os.path.join(root_dir, folder_name)
    
    # Check if the item is a directory
    if os.path.isdir(folder_path):
        readme_path = os.path.join(folder_path, 'README.md')
        
        # Create the README.md file if it doesn't exist
        if not os.path.exists(readme_path):
            with open(readme_path, 'w') as readme_file:
                readme_file.write(f'# {folder_name}\n\nThis is the README file for the {folder_name} folder.')
                print(f'Created README.md in {folder_name} folder.')