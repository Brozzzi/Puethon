from setuptools import setup, find_packages

setup(
    name="püthon",
    version="0.1.0",
    author="Brozzzi",
    author_email="",
    description="Püthon: Python auf Deutsch",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/Brozzzi/Puethon/tree/main",
    packages=find_packages(),
    install_requires=[
        "astor",
    ],
    entry_points={
        'console_scripts': [
            'püthon=püthon.cli:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
