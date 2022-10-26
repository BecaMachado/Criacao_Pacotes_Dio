from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="package_desafios intermediarios",
    version="0.0.1",
    author="Angelica",
    author_email="becamachado@outlook.pt",
    description="Calculo de reajuste salarial",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BecaMachado/Criacao_Pacotes_Dio.git"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)