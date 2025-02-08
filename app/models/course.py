from app import db
from datetime import datetime

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    difficulty_level = db.Column(db.String(20))  # beginner, intermediate, advanced
    category = db.Column(db.String(50))  # AI, ML, Deep Learning, etc.
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    image_url = db.Column(db.String(200))
    
    # Relationships
    lessons = db.relationship('Lesson', backref='course', lazy='dynamic')
    progress = db.relationship('CourseProgress', backref='course', lazy='dynamic')

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text)
    video_url = db.Column(db.String(200))
    order = db.Column(db.Integer)
    points = db.Column(db.Integer, default=100)  # Experience points for completing
    
    # Additional resources
    additional_resources = db.relationship('Resource', backref='lesson', lazy='dynamic')

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'), nullable=False)
    title = db.Column(db.String(200))
    resource_type = db.Column(db.String(50))  # video, article, image, etc.
    url = db.Column(db.String(500))
    description = db.Column(db.Text)

class CourseProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    completed_lessons = db.Column(db.Text)  # Store as JSON string of completed lesson IDs
    last_accessed = db.Column(db.DateTime, default=datetime.utcnow)
    completion_percentage = db.Column(db.Float, default=0.0)

class Achievement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    badge_image = db.Column(db.String(200))
    earned_at = db.Column(db.DateTime, default=datetime.utcnow)
    achievement_type = db.Column(db.String(50))  # course_completion, level_up, streak, etc. 