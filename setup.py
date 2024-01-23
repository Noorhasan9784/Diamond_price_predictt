from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines('requirements.txt')
        requirements= [req.replace("\n","") for req in requirements]
    return requirements

setup(
    name='DiamondPricePrediction',
    version = '0.0.1',
    author='NoorPWPrac',
    author_email="noorhasan9784@gmail.com",
    install_requires=['pandas','sklearn'],
    packages= find_packages()
)