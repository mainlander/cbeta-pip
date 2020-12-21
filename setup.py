from setuptools import setup

setup(
    name = 'cbetatest',
    version = '1.0',
    description = 'Make any image file to ascii art format.',
    url = 'https://github.com/DILA-edu/cbeta-api',
    author = "cbeta",
    author_email = "ywbonnie@g.ncu.edu.tw",
    install_requires = ["cbeta"],
    license = 'MIT',
    packages = ['package'],
    package_data = {'':['*.json', '*.pkl']},
    zip_safe = False,
    keywords = ['cbeta'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
    
)