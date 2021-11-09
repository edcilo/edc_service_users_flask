import os
from dotenv import load_dotenv
from users import app


load_dotenv()


config = {
    'app': {
        'APP_NAME': os.getenv('APP_NAME', 'app'),
        'APP_VERSION': os.getenv('APP_VERSION', '1.0.0'),
    },
}


app.config.update(**config.get('app'))
