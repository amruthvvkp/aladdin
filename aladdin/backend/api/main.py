from fastapi import FastAPI
import config

app = FastAPI(title=config.settings.api_settings.title,
              version=config.settings.api_settings.version,
              description=config.settings.api_settings.description)


@app.get('/')
def root():
    return {'message': 'Welcome to Aladdin'}
