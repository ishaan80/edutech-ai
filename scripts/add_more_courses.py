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

# Additional courses with more videos
ADDITIONAL_COURSES = [
    # Deep Learning Basics
    {
        "title": "Deep Learning for Young Minds",
        "description": "Explore neural networks and deep learning concepts in a fun way.",
        "difficulty_level": "intermediate",
        "category": "Deep Learning",
        "image_url": "https://img.youtube.com/vi/6M5VXKLf4D4/maxresdefault.jpg",
        "lessons": [
            {
                "title": "Neural Networks Explained",
                "content": "Understanding how neural networks work",
                "video_url": "https://www.youtube.com/embed/6M5VXKLf4D4",
                "order": 1,
                "points": 100
            },
            {
                "title": "Training Neural Networks",
                "content": "Learn how neural networks learn patterns",
                "video_url": "https://www.youtube.com/embed/aircAruvnKk",
                "order": 2,
                "points": 100
            }
        ]
    },
    
    # AI Ethics and Safety
    {
        "title": "AI Ethics for Kids",
        "description": "Learn about responsible AI use and ethical considerations.",
        "difficulty_level": "beginner",
        "category": "AI Ethics",
        "image_url": "https://img.youtube.com/vi/tcdVC4e6EV4/maxresdefault.jpg",
        "lessons": [
            {
                "title": "Being Responsible with AI",
                "content": "Understanding AI ethics and responsibility",
                "video_url": "https://www.youtube.com/embed/tcdVC4e6EV4",
                "order": 1,
                "points": 100
            },
            {
                "title": "AI Safety and Privacy",
                "content": "Learning about AI safety and privacy concerns",
                "video_url": "https://www.youtube.com/embed/z1KqxHy1XvE",
                "order": 2,
                "points": 100
            }
        ]
    },
    
    # AI in Games
    {
        "title": "AI in Gaming",
        "description": "Discover how AI makes games more fun and challenging.",
        "difficulty_level": "beginner",
        "category": "AI in Games",
        "image_url": "https://img.youtube.com/vi/DXgwOKXkCjY/maxresdefault.jpg",
        "lessons": [
            {
                "title": "Game AI Basics",
                "content": "How AI works in video games",
                "video_url": "https://www.youtube.com/embed/DXgwOKXkCjY",
                "order": 1,
                "points": 100
            },
            {
                "title": "Creating Smart Game Characters",
                "content": "Understanding AI-controlled characters",
                "video_url": "https://www.youtube.com/embed/J3MZ1TSqXP0",
                "order": 2,
                "points": 100
            }
        ]
    },
    
    # AI Art and Creativity
    {
        "title": "Creative AI",
        "description": "Learn how AI can create art, music, and stories.",
        "difficulty_level": "intermediate",
        "category": "AI Creativity",
        "image_url": "https://img.youtube.com/vi/9Wk_xQ6JEik/maxresdefault.jpg",
        "lessons": [
            {
                "title": "AI-Generated Art",
                "content": "How AI creates artwork",
                "video_url": "https://www.youtube.com/embed/9Wk_xQ6JEik",
                "order": 1,
                "points": 100
            },
            {
                "title": "AI Music Composition",
                "content": "Understanding AI music creation",
                "video_url": "https://www.youtube.com/embed/UWxfnNXlVy8",
                "order": 2,
                "points": 100
            }
        ]
    },
    
    # AI in Daily Life
    {
        "title": "AI Around Us",
        "description": "Discover AI applications in everyday life.",
        "difficulty_level": "beginner",
        "category": "AI Applications",
        "image_url": "https://img.youtube.com/vi/BrNs0M77Pd4/maxresdefault.jpg",
        "lessons": [
            {
                "title": "AI in Smart Homes",
                "content": "How AI makes homes smarter",
                "video_url": "https://www.youtube.com/embed/BrNs0M77Pd4",
                "order": 1,
                "points": 100
            },
            {
                "title": "AI in Transportation",
                "content": "Understanding self-driving vehicles",
                "video_url": "https://www.youtube.com/embed/Yjrfm_oRO0w",
                "order": 2,
                "points": 100
            }
        ]
    }
]

def add_more_courses():
    try:
        # Add new courses
        for course_data in ADDITIONAL_COURSES:
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
        print("Additional courses added successfully!")
        
    except Exception as e:
        print(f"Error adding courses: {e}")
        db.session.rollback()

if __name__ == "__main__":
    add_more_courses() 