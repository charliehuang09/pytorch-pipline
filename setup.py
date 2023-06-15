from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1.1'
DESCRIPTION = 'Making pytorch training easier'

# Setting up
setup(
    name="CPytorch Pipline",
    version=VERSION,
    author="Charlie Huang",
    author_email="<charliehuang09@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['torch', 'numpy', 'tqdm', 'torchvision'],
    keywords=['python', 'pytorch'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)