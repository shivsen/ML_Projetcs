from setuptools import setup, find_packages

hyphon = "-e ."
def get_requirements(file_path):
    requirenments = []
    with open(file_path, "r") as file_obj:
        require = file_obj.readlines()
        requirenments = [req.replace("\n", "") for req in require]
        
        if hyphon in requirenments:
            requirenments.remove(hyphon)
        
        return requirenments
    

setup(
name="ML_Projects",
version= "0.0.1",
author="shivsen1997@gmail.com",
packages=find_packages(),
requires= get_requirements("requirements.txt")
)