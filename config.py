from pydantic import BaseSettings
from setuptools import setup, find_packages


class APISettings(BaseSettings):
    version = '0.0.1'
    title = 'Aladdin API'
    description = 'API model for Aladdin'


class Settings(BaseSettings):
    name = 'aladdin'
    version = '0.0.2'
    url = 'https://github.com/amruthvvkp/aladdin'
    description = 'Aladdin - Automated Learning and Autonomous Distributed Diversified Investment Network - is a model designed to trade using the user\'s Demat account just the way the user does it. This is not a replacement of human effort but an assisted trading to the actual human effort.'
    python_requires = '>=3.8'
    packages = find_packages(include=('aladdin', 'tests'))
    api_settings: APISettings = APISettings()


settings = Settings()