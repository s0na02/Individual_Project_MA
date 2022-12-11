import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cohort",
    version="0.1.2",
    author="Sona Stepanyan",
    author_email="sona_stepanyan@edu.aua.am",
    description="Marketing Cohort Analysis package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/s0na02/Individual-Project-.git",
    packages=setuptools.find_packages(),
    package_data={'package': ['data/*.csv']},
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
)
