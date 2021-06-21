"""Build the Brython-typed package."""
from setuptools import setup, find_packages


setup(
    name='brython-typed',
    version='1.0.0',
    description="Types and IDE support for Brython 3.9.4.",
    url='https://github.com/ENDERZOMBI102/brython-typed',

    author='ENDERZOMBI102',
    author_email='enderzombi102.end@gmail.com',
    license='mit',

    project_urls={
        "Bug Tracker": "https://github.com/ENDERZOMBI102/brython-typed/issues",
    },

    keywords='brython,python,browser',
    classifiers=[
        'License :: Public Domain',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        "Operating System :: OS Independent"
    ],

    package_dir={"": "src"},

    python_requires='>=3.7, <3.10'
)
