from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
Name='myendtoendmlproject',
Version= '0.0.1',
Author='Monika Singh',
Author_email= 'monikasingh.jmi@gmail.com',
Packages=find_packages(),
#Install_requires=['pandas', 'numpy', 'seaborn']
Install_requires=get_requirements('requirements.txt')
)

