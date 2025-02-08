from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify
from flask_login import current_user, login_required
from app.models.course import Course, Lesson, CourseProgress, Achievement
from app import db
import json

bp = Blueprint('courses', __name__)

@bp.route('/course/<int:course_id>')
def course_detail(course_id):
    course = Course.query.get_or_404(course_id)
    lessons = course.lessons.order_by(Lesson.order).all()
    
    if current_user.is_authenticated:
        progress = CourseProgress.query.filter_by(
            user_id=current_user.id,
            course_id=course_id
        ).first()
        
        if not progress:
            progress = CourseProgress(
                user_id=current_user.id,
                course_id=course_id,
                completed_lessons='[]'
            )
            db.session.add(progress)
            db.session.commit()
    else:
        progress = None
    
    return render_template('courses/detail.html',
                         course=course,
                         lessons=lessons,
                         progress=progress)

@bp.route('/lesson/<int:lesson_id>')
@login_required
def lesson_detail(lesson_id):
    lesson = Lesson.query.get_or_404(lesson_id)
    course = lesson.course
    
    progress = CourseProgress.query.filter_by(
        user_id=current_user.id,
        course_id=course.id
    ).first()
    
    completed_lessons = json.loads(progress.completed_lessons)
    
    return render_template('courses/lesson.html',
                         lesson=lesson,
                         course=course,
                         completed_lessons=completed_lessons)

@bp.route('/lesson/<int:lesson_id>/complete', methods=['POST'])
@login_required
def complete_lesson(lesson_id):
    lesson = Lesson.query.get_or_404(lesson_id)
    progress = CourseProgress.query.filter_by(
        user_id=current_user.id,
        course_id=lesson.course_id
    ).first()
    
    completed_lessons = json.loads(progress.completed_lessons)
    if lesson_id not in completed_lessons:
        completed_lessons.append(lesson_id)
        progress.completed_lessons = json.dumps(completed_lessons)
        
        # Calculate completion percentage
        total_lessons = lesson.course.lessons.count()
        progress.completion_percentage = (len(completed_lessons) / total_lessons) * 100
        
        # Add experience points
        level_up = current_user.add_experience(lesson.points)
        
        # Check for achievements
        if progress.completion_percentage == 100:
            achievement = Achievement(
                user_id=current_user.id,
                title=f"Completed {lesson.course.title}",
                description=f"Finished all lessons in {lesson.course.title}",
                achievement_type='course_completion'
            )
            db.session.add(achievement)
        
        if level_up:
            achievement = Achievement(
                user_id=current_user.id,
                title=f"Reached Level {current_user.level}",
                description=f"Leveled up to level {current_user.level}",
                achievement_type='level_up'
            )
            db.session.add(achievement)
        
        db.session.commit()
        
        return jsonify({
            'status': 'success',
            'message': 'Lesson completed!',
            'experience_gained': lesson.points,
            'level_up': level_up
        })
    
    return jsonify({
        'status': 'info',
        'message': 'Lesson already completed'
    }) 