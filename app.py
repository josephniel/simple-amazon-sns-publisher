from dotenv import load_dotenv

from app import create_app

if __name__ == '__main__':
    load_dotenv()

    app = create_app()
    app.run(
        host=app.config.get('HOST', '0.0.0.0'),
        port=app.config.get('PORT', 5000),
        debug=app.config.get('DEBUG', False)
    )
