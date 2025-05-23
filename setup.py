from setuptools import setup, find_packages

setup(
    name='pyGebra',
    version='0.1.0',
    author='Arnav Choudhary',
    author_email='arnavchoudhary.6969@gmail.com',
    description='A brief description of your Python module',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ArnavChoudhary9/pyGebra',
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
