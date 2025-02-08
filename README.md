# EduTech - AI & ML Learning Platform for Children

EduTech is an interactive web application designed to teach children about Artificial Intelligence, Machine Learning, and related technologies through engaging content, gamified learning experiences, and hands-on projects.

## Features

- **Interactive Learning**: Engaging lessons with videos, text, and interactive elements
- **Progress Tracking**: Track your learning progress and earn experience points
- **Achievement System**: Unlock achievements as you complete courses and level up
- **Structured Learning Paths**: Well-organized courses from beginner to advanced levels
- **Resource Library**: Additional learning materials and external resources
- **User Dashboard**: Personal dashboard showing progress and achievements

## Tech Stack

- **Backend**: Python Flask
- **Database**: SQLAlchemy with SQLite
- **Frontend**: HTML, TailwindCSS, JavaScript
- **Authentication**: Flask-Login
- **Forms**: Flask-WTF
- **Database Migrations**: Flask-Migrate

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd EduTech
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize the database:
```bash
flask db upgrade
```

5. Run the application:
```bash
python run.py
```

The application will be available at `http://localhost:5000`

## Project Structure

```
EduTech/
├── app/
│   ├── models/
│   │   ├── user.py
│   │   └── course.py
│   ├── routes/
│   │   ├── main.py
│   │   ├── auth.py
│   │   └── courses.py
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   ├── templates/
│   │   ├── auth/
│   │   ├── courses/
│   │   └── main/
│   └── __init__.py
├── config.py
├── requirements.txt
└── run.py
```

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to all contributors who have helped shape this educational platform
- Special thanks to the open-source community for the tools and libraries used

## Contact

For any questions or suggestions, please open an issue in the repository. 