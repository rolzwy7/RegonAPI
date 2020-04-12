import setuptools

with open("pypi_long.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="RegonAPI",
    version="1.1.1",
    author="Bartosz Nowakowski",
    author_email="rolzwy7@gmail.com",
    description="Python 3 API Client for Polish REGON database (Baza Internetowa Regon - BIR)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rolzwy7/RegonAPI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Database :: Front-Ends",
        "Environment :: Console",
        ],
    install_requires=[
       "zeep",
       "beautifulsoup4",
       ]
)
