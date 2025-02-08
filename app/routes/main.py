from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, login_required
from app.models.course import Course, CourseProgress
from app import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    """Home page with featured courses and learning paths"""
    featured_courses = Course.query.limit(6).all()
    
    if current_user.is_authenticated:
        in_progress_courses = CourseProgress.query.filter_by(
            user_id=current_user.id
        ).order_by(CourseProgress.last_accessed.desc()).limit(3).all()
    else:
        in_progress_courses = []
    
    return render_template('main/index.html',
                         featured_courses=featured_courses,
                         in_progress_courses=in_progress_courses)

@bp.route('/dashboard')
@login_required
def dashboard():
    """User dashboard showing progress and achievements"""
    user_progress = CourseProgress.query.filter_by(
        user_id=current_user.id
    ).order_by(CourseProgress.last_accessed.desc()).all()
    
    achievements = current_user.achievements.all()
    
    return render_template('main/dashboard.html',
                         user_progress=user_progress,
                         achievements=achievements)

@bp.route('/explore')
def explore():
    """Explore all courses and learning paths"""
    categories = [
        'Artificial Intelligence',
        'Machine Learning',
        'Deep Learning',
        'Computer Vision',
        'Natural Language Processing',
        'Robotics'
    ]
    
    courses = Course.query.all()
    return render_template('main/explore.html',
                         categories=categories,
                         courses=courses) 