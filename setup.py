import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Simplate",
    version="1.0.0",
    author="Kyle Kimery",
    author_email="kylekimery@gmail.com",
    description="Simple object-based string templating in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/krkimery/simplate",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)