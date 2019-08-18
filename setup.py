import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="multi-imbalance",
    version="0.0.1",
    author="Damian Horna, Kamil Pluciński, Hanna Klimczak, Jacek Grycza",
    author_email="horna.damian@gmail.com",
    description="Python package for tackling multiclass imbalance problems.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/damian-horna/multi-imbalance",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'bleach==3.1.0',
        'certifi==2019.6.16',
        'chardet==3.0.4',
        'docutils==0.15.2',
        'idna==2.8',
        'pkginfo==1.5.0.1',
        'Pygments==2.4.2',
        'readme-renderer==24.0',
        'requests==2.22.0',
        'requests-toolbelt==0.9.1',
        'six==1.12.0',
        'tqdm==4.33.0',
        'twine==1.13.0',
        'urllib3==1.25.3',
        'webencodings==0.5.1',
        'wincertstore==0.2',
    ]
)
