from flask import Flask
from flask_migrate import Migrate
from app import create_app, db
from app.models.user import User
from app.models.course import Course, Lesson, Resource, CourseProgress, Achievement

app = create_app()
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Course': Course,
        'Lesson': Lesson,
        'Resource': Resource,
        'CourseProgress': CourseProgress,
        'Achievement': Achievement
    }

if __name__ == '__main__':
    app.run(debug=True) 