from setuptools import find_packages, setup

setup(
    name="dragonnet",
    packages=find_packages(
        include=["dragonnet"]
    ),
    version="0.1",
    description="pytorch implementation of dragonnet",
    author="Faraz",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pandas>=1.4",
        "numpy>=1.22",
        "torch>=1.12"
    ],
)