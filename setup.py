from setuptools import find_packages,setup
from typing import List
hypen_e='-e.'
def get_requirements(file_path:str)->List[str]:
    ''''
    this function will return the list of the requirements
    '''
   
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()  #it will readlines all the lines
        requirements=[line.replace('\n',"") for line in requirements]
        if hypen_e in requirements:
            requirements.remove(hypen_e)

    return requirements
    


setup(
name='datascience project',
version='1.1.1',
author='aviral rai',
author_email='aviralrai22@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')


)

#after making this above setup make a src folder and in src make a file 
#name __init__.py and run the set up file with the command in the terminal
#python setup.py install