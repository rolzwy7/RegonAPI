import setuptools
import pathlib


BASE_DIR = pathlib.Path(__file__).parent
with open(BASE_DIR / "pypi_long.md", encoding="utf-8") as fh:
    README = fh.read()


setuptools.setup(
    name="RegonAPI",
    version="1.3.1",
    author="Bartosz Nowakowski",
    author_email="rolzwy7@gmail.com",
    description="Python 3 API Client for Polish REGON database (Baza Internetowa Regon - BIR)",
    long_description=README,
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
        "zeep >= 3.3,<3.4",
        "beautifulsoup4 >= 4.7,<4.8",
    ],
)
