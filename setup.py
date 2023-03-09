from setuptools import setup, find_packages
from typing import List
file_path = 'requirements.txt'

def read_installs(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file:
        for rqmt in file.readlines():
            rqmt = rqmt.replace('/n', "")
            requirements.append(rqmt)

        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(name='ml-project', 
      description='end to end ml project',
      author='Rohan Sharma',
      author_email='rohanshar11@gmail.com',
      packages=find_packages(),
      install_requires=read_installs(file_path)
    )