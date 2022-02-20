"""Project Setup"""

import versioneer
from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='aladdin',
    packages=find_packages(include=('aladdin')),
    url='https://github.com/amruthvvkp/aladdin',
    description='Aladdin - Automated Learning and Autonomous Distributed Diversified Investment Network - '
    'is a model designed to trade using the user\'s Demat account just the way the user does it. '
    'This is not a replacement of human effort but an assisted trading to the actual human effort.',
    long_description=long_description,
    python_requires='>=3.8',
    license=license,
    setup_requires=['isort', 'yapf'],
    # Versioning
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
)
