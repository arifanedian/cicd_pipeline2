from setuptools import setup, find_packages

def get_requirement(filepath):
    requirements = []
    with open(filepath,"r") as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    return requirements

setup(
    name = "ML Pipeline",
    version = "1.0",
    description= " Project deployment using CI/CD pipeline",
    author= "Arifa Mustafa",
    author_email= "arifa.mustafa@dsu.edu.pk",
    packages= find_packages(),
    install_requires = get_requirement("requirements.txt")

)