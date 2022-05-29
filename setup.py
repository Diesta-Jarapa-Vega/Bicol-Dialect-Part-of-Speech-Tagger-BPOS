import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BPOS:Bicol-Part-of-Speeh-Tagger-Vega_Jarapa_Diesta",
    version="0.0.1",
    author="Jarapa Vega Diesta",
    author_email="mikaellajarapa@gmail.com",
    description="BPOS: A PART-OF-SPEECH TAGGER USING  CONDITIONAL RANDOM FIELD  FOR BICOL DIALECT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Diesta-Jarapa-Vega/Bicol-Dialect-Part-of-Speech-Tagger-BPOS",
    project_urls={
        "Bug Tracker": "https://github.com/Diesta-Jarapa-Vega/Bicol-Dialect-Part-of-Speech-Tagger-BPOS/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)