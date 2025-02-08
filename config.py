import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-please-change-in-production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # YouTube API Key (optional, for fetching video content)
    YOUTUBE_API_KEY = os.environ.get('YOUTUBE_API_KEY')
    
    # Maximum content size for uploads
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    
    # Upload folder for learning materials
    UPLOAD_FOLDER = os.path.join(basedir, 'app/static/uploads') 