from setuptools import setup, find_packages

__name__ = "bitches"
__version__ = "0.0.2"

setup(
    name=__name__,
    version=__version__,
    author="Rdimo",
    author_email="<contact.rdimo@gmail.com>",
    description="how about you pip install some bitches",
    long_description_content_type="text/markdown",
    long_description=open("README.md", encoding="utf-8").read(),
    url = "https://github.com/rdimo/pip-install-bitches",
    project_urls={
      "Bug Tracker": "https://github.com/rdimo/pip-install-bitches/issues",
    },
    install_requires=['requests'],
    packages=find_packages(),
    keywords=['bitches', 'python', 'package', 'library', 'lib', 'module', 'checker'],
    classifiers=[
      "Intended Audience :: Developers",
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
    ]
)