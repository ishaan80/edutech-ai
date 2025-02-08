import os
import sys
from datetime import datetime

# Add the parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app, db
from app.models.course import Course, Lesson, Resource

# Initialize Flask app context
app = create_app()
app.app_context().push()

# Expanded course content with more categories and videos
EXPANDED_COURSES = [
    # AI Fundamentals Category
    {
        "title": "Understanding AI Basics",
        "description": "Learn the fundamental concepts of Artificial Intelligence through fun and interactive lessons.",
        "difficulty_level": "beginner",
        "category": "AI Fundamentals",
        "image_url": "https://img.youtube.com/vi/mFZazxxCKbw/maxresdefault.jpg",
        "lessons": [
            {
                "title": "What is AI?",
                "content": "Introduction to Artificial Intelligence for beginners",
                "video_url": "https://www.youtube.com/embed/mFZazxxCKbw",
                "order": 1,
                "points": 100
            },
            {
                "title": "How AI Works",
                "content": "Understanding the basics of how AI systems function",
                "video_url": "https://www.youtube.com/embed/nYh-n7EOtMA",
                "order": 2,
                "points": 100
            }
        ]
    },
    
    # Machine Learning for Kids
    {
        "title": "Machine Learning Adventures",
        "description": "Discover how machines learn through fun experiments and examples.",
        "difficulty_level": "beginner",
        "category": "Machine Learning",
        "image_url": "https://img.youtube.com/vi/QghjaS0WQQU/maxresdefault.jpg",
        "lessons": [
            {
                "title": "Introduction to Machine Learning",
                "content": "Basic concepts of machine learning explained for kids",
                "video_url": "https://www.youtube.com/embed/QghjaS0WQQU",
                "order": 1,
                "points": 100
            },
            {
                "title": "Training AI Models",
                "content": "Learn how AI models are trained with data",
                "video_url": "https://www.youtube.com/embed/OeU5m6vRyCk",
                "order": 2,
                "points": 100
            }
        ]
    },
    
    # Robotics
    {
        "title": "Fun with Robotics",
        "description": "Explore the exciting world of robots and how they work.",
        "difficulty_level": "beginner",
        "category": "Robotics",
        "image_url": "https://img.youtube.com/vi/6iJu9-8pjcQ/maxresdefault.jpg",
        "lessons": [
            {
                "title": "Introduction to Robotics",
                "content": "Learn about different types of robots and their applications",
                "video_url": "https://www.youtube.com/embed/6iJu9-8pjcQ",
                "order": 1,
                "points": 100
            },
            {
                "title": "How Robots Think",
                "content": "Understanding robot programming and control",
                "video_url": "https://www.youtube.com/embed/7Gb9nK8-hF4",
                "order": 2,
                "points": 100
            }
        ]
    },
    
    # Computer Vision
    {
        "title": "Seeing Through AI Eyes",
        "description": "Discover how computers understand and process images.",
        "difficulty_level": "intermediate",
        "category": "Computer Vision",
        "image_url": "https://img.youtube.com/vi/2hXG8v8p0KM/maxresdefault.jpg",
        "lessons": [
            {
                "title": "How Computers See",
                "content": "Understanding computer vision basics",
                "video_url": "https://www.youtube.com/embed/2hXG8v8p0KM",
                "order": 1,
                "points": 100
            },
            {
                "title": "Face Detection Fun",
                "content": "Learn about face detection and recognition",
                "video_url": "https://www.youtube.com/embed/uEJ71VlUmMQ",
                "order": 2,
                "points": 100
            }
        ]
    },
    
    # Natural Language Processing
    {
        "title": "Talking with Computers",
        "description": "Learn how computers understand and process human language.",
        "difficulty_level": "intermediate",
        "category": "Natural Language Processing",
        "image_url": "https://img.youtube.com/vi/CMrHM8a3hqw/maxresdefault.jpg",
        "lessons": [
            {
                "title": "Understanding Human Language",
                "content": "How computers process and understand text",
                "video_url": "https://www.youtube.com/embed/CMrHM8a3hqw",
                "order": 1,
                "points": 100
            },
            {
                "title": "Chatbots and Virtual Assistants",
                "content": "Learn about AI-powered conversation systems",
                "video_url": "https://www.youtube.com/embed/5r1ry0DmCRE",
                "order": 2,
                "points": 100
            }
        ]
    }
]

def populate_expanded_database():
    try:
        # Clear existing data
        Resource.query.delete()
        Lesson.query.delete()
        Course.query.delete()
        db.session.commit()
        
        # Add new courses
        for course_data in EXPANDED_COURSES:
            course = Course(
                title=course_data["title"],
                description=course_data["description"],
                difficulty_level=course_data["difficulty_level"],
                category=course_data["category"],
                image_url=course_data["image_url"],
                created_at=datetime.utcnow()
            )
            db.session.add(course)
            db.session.flush()
            
            # Add lessons
            for lesson_data in course_data["lessons"]:
                lesson = Lesson(
                    course_id=course.id,
                    title=lesson_data["title"],
                    content=lesson_data["content"],
                    video_url=lesson_data["video_url"],
                    order=lesson_data["order"],
                    points=lesson_data["points"]
                )
                db.session.add(lesson)
        
        db.session.commit()
        print("Database populated with expanded content successfully!")
        
    except Exception as e:
        print(f"Error populating database: {e}")
        db.session.rollback()

if __name__ == "__main__":
    populate_expanded_database() 