import os
from app import create_app
from config import configurations

setting = os.getenv("APP_ENVIRONMENT", "development")

app = create_app(setting)

if __name__ == '__main__':
    app.run(debug=configurations[setting].DEBUG)