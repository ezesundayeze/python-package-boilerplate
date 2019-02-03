from setuptools import setup

with open("readme.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ezesundayeze",
    version="0.01",
    description="Say Hello",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["helloworld"],
    package_dir={
        "": "src"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Academic Free License (AFL) ",
        "Operating System :: OS Independent",
    ],

)
