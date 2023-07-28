import os
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    handlers=[
        logging.StreamHandler(),  # Log to console
        logging.FileHandler("script_log.txt")  # Log to a file
    ]
)

project_name = "cnnClassifier"
# List of file names only
file_names = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "trials.ipynb",
    "index.html"
]

# Create directories and files in the main directory
for file_name in file_names:
    try:
        # Get the directory path without the filename
        directory = os.path.dirname(file_name)

        # Create the directory if it doesn't exist
        if directory:
            os.makedirs(directory, exist_ok=True)

        if os.path.exists(file_name):
            logging.info(f"File already exists: {file_name}")
        else:
            with open(file_name, "w") as file:
                # file.write("This is the content of {}".format(file_name))
                logging.info(f"File created: {file_name}")
    except Exception as e:
        logging.error(f"Error creating {file_name}: {str(e)}")
