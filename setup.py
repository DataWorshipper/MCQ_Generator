from setuptools import find_packages, setup

setup(
    name="MCQ_GEN",
    version="0.0.1",
    author="Abhiraj Mandal",
    author_email="mandalabhiraj04@gmail.com",
    install_requires=[
        "langchain",
        "langchain_huggingface",
        "langchain_core",
        "PyPDF2",
        "bitsandbytes",
        "streamlit"
    ],
    packages=find_packages()
)


