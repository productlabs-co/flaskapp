# run.py

from app import create_app

# Create the Flask app instance
app = create_app(config_filename='config.py')

if __name__ == '__main__':
    app.run()
