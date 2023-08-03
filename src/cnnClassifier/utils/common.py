
import yaml, os,json,base64
from box.exceptions import BoxValueError
from cnnClassifier import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
# read yaml file and return configbox object
@ensure_annotations
def read_yaml_file(filename):
    try:
        with open(filename, 'r') as f:
            content=yaml.safe_load(f)
            logger.info(f"read_yaml_file{filename}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Could not read")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directory:list,verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directory:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Creating directory at: {path}")

@ensure_annotations
def save_json(path:Path,data:dict):
    with open(path, 'w') as outfile:
        json.dump(data, outfile, indent=4)

    logger.info(f"Json saved to: {path}")

@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    with open(path, 'r') as f:
        content=json.load(f)
        logger.info(f"Json loaded from: {path}")
        return ConfigBox(content)
    
@ensure_annotations
def get_sizes(path:Path) -> str:
    size_in_kb=round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB"

def decodeImage(imgstring,filename):
    imgdata=base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImage(cropped_image):
    with open(cropped_image,"rb") as f:
        return base64.b64encode(f.read())


