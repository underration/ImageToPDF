from setuptools import setup, find_packages

setup(
    name="ImagetoPDF",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "flet",
        "fpdf",
    ],
    entry_points={
        "console_scripts": [
            "imagetoPDF=main:main",
        ],
    },
)