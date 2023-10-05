from setuptools import setup, find_packages
from typing import List

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


HYPEN_E_DOT='-e .'
__version__ = "0.0.0"

REPO_NAME = "DeepL_Chicken_Disease_Classification"
AUTHOR_USER_NAME = "EljayiYassir"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "yassireljay@gmail.com"



def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirement package that are in the file_path
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        # delete the "-e ." which connect the requirements.txt with setup.py from the installing the requirements package with  setup.py
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements




setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    # long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },

    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=get_requirements('requirements.txt')
)