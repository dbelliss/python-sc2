from setuptools import setup, find_packages

setup(
    name = "sc2",
    packages = find_packages(),
    version = "0.8.0",
    description = "A StarCraft II API Client for Python 3, Forked from https://github.com/Dentosal/python-sc2",
    license="MIT",
    author = "Davey Jay Belliss",
    author_email = "daveybelliss@gmail.com",
    url = "https://github.com/dbelliss/python-sc2",
    keywords = ["StarCraft", "StarCraft 2", "StarCraft II", "AI", "Bot"],
    install_requires=["s2clientprotocol", "websockets", "portpicker", "async_timeout"],
    classifiers = [
        "Development Status :: 3 - Alpha",

        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Games/Entertainment",
        "Topic :: Games/Entertainment :: Real Time Strategy",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",

        "License :: OSI Approved :: MIT License",

        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ]
)
