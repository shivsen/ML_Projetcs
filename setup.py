from setuptools import find_packages, setup
#from typing import List


hyphen = '-e .'

def get_requirements(file_path : str) -> list[str]:
    ''' This function will return the list of requirements'''
    requirements=[]
    with open (file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[require.replace("\n", "") for require in requirements]
        
        if hyphen in requirements:
            requirements.remove(hyphen)
    return requirements


setup(
name="ML_Project",
version="0.1", 
author="shivam_uppal",
author_email="shivsen1997@gmail.com",
packages=find_packages(),
install_requires = get_requirements("requirements.txt")
) 