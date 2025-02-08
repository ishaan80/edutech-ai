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

# Course content structure
COURSES = [
    {
        "title": "Introduction to Artificial Intelligence for Kids",
        "description": "A fun and engaging introduction to AI concepts through interactive lessons and real-world examples.",
        "difficulty_level": "beginner",
        "category": "Artificial Intelligence",
        "image_url": "https://img.youtube.com/vi/mFZazxxCKbw/maxresdefault.jpg",
        "lessons": [
            {
                "title": "What is Artificial Intelligence?",
                "content": """
                Welcome to your first lesson about Artificial Intelligence! 
                
                In this lesson, we'll learn:
                - What AI means and how it works
                - How AI helps us in our daily lives
                - Fun examples of AI that you might already be using
                """,
                "video_url": "https://www.youtube.com/embed/mFZazxxCKbw",
                "order": 1,
                "points": 100,
                "resources": [
                    {
                        "title": "AI for Kids - Simple Explanation",
                        "resource_type": "video",
                        "url": "https://www.youtube.com/embed/nJYho56INKU",
                        "description": "A kid-friendly explanation of AI concepts"
                    },
                    {
                        "title": "AI Examples in Real Life",
                        "resource_type": "article",
                        "url": "https://www.tynker.com/blog/articles/ideas-and-tips/artificial-intelligence-and-kids/",
                        "description": "Examples of AI that kids can relate to"
                    }
                ]
            },
            {
                "title": "Teaching Computers to See",
                "content": """
                Let's explore Computer Vision!
                
                In this lesson, you'll learn:
                - How computers can understand images
                - Fun applications like face filters and object detection
                - Simple activities to understand image recognition
                """,
                "video_url": "https://www.youtube.com/embed/2hXG8v8p0KM",
                "order": 2,
                "points": 100,
                "resources": [
                    {
                        "title": "Computer Vision for Kids",
                        "resource_type": "video",
                        "url": "https://www.youtube.com/embed/v68zYyaEmEA",
                        "description": "Simple explanation of computer vision with fun examples"
                    }
                ]
            }
        ]
    },
    {
        "title": "Machine Learning Basics for Young Minds",
        "description": "Discover how computers learn from examples, just like you do! Through fun activities and simple explanations.",
        "difficulty_level": "beginner",
        "category": "Machine Learning",
        "image_url": "https://img.youtube.com/vi/QghjaS0WQQU/maxresdefault.jpg",
        "lessons": [
            {
                "title": "Teaching Computers to Learn",
                "content": """
                Welcome to Machine Learning!
                
                In this lesson, we'll explore:
                - How computers learn from examples
                - Why Machine Learning is like teaching a pet new tricks
                - Fun activities to understand learning patterns
                """,
                "video_url": "https://www.youtube.com/embed/QghjaS0WQQU",
                "order": 1,
                "points": 100,
                "resources": [
                    {
                        "title": "Machine Learning for Kids",
                        "resource_type": "interactive",
                        "url": "https://machinelearningforkids.co.uk/",
                        "description": "Interactive platform to try machine learning"
                    }
                ]
            },
            {
                "title": "Pattern Recognition Fun",
                "content": """
                Let's find patterns like a computer!
                
                In this lesson, you'll learn:
                - How computers find patterns in data
                - Simple games to understand pattern recognition
                - Real-world applications of pattern finding
                """,
                "video_url": "https://www.youtube.com/embed/Zm9B-DvwOgw",
                "order": 2,
                "points": 100,
                "resources": [
                    {
                        "title": "Pattern Recognition Games",
                        "resource_type": "game",
                        "url": "https://www.brainpop.com/games/patternrecognition/",
                        "description": "Fun games to practice finding patterns"
                    }
                ]
            }
        ]
    }
]

def populate_database():
    try:
        # Clear existing data
        Resource.query.delete()
        Lesson.query.delete()
        Course.query.delete()
        db.session.commit()
        
        # Add new courses
        for course_data in COURSES:
            course = Course(
                title=course_data["title"],
                description=course_data["description"],
                difficulty_level=course_data["difficulty_level"],
                category=course_data["category"],
                image_url=course_data["image_url"],
                created_at=datetime.utcnow()
            )
            db.session.add(course)
            db.session.flush()  # Get course ID
            
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
                db.session.flush()  # Get lesson ID
                
                # Add resources
                for resource_data in lesson_data["resources"]:
                    resource = Resource(
                        lesson_id=lesson.id,
                        title=resource_data["title"],
                        resource_type=resource_data["resource_type"],
                        url=resource_data["url"],
                        description=resource_data["description"]
                    )
                    db.session.add(resource)
        
        db.session.commit()
        print("Database populated successfully!")
        
    except Exception as e:
        print(f"Error populating database: {e}")
        db.session.rollback()

if __name__ == "__main__":
    populate_database() 