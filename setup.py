import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="label_shift-flaviovdf", # Replace with your own username
    version="0.0.1",
    author="Flávio Vinícius",
    author_email="",
    description="Label shift",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/flaviovdf/label-shift",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
