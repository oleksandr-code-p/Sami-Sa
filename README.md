# Samisa - Slovak to English Learning App

A simple and effective web application for learning English from Slovak, built with Django and TailwindCSS.

## Features

- Custom word lists and pre-made lessons
- Multiple exercise types (matching, translation, fill-in-the-blank, phrases)
- Comprehensive testing system
- Interactive dictionary
- Slovak alphabet reference
- User profiles with progress tracking
- AI-powered translation assistance

## Tech Stack

- **Backend**: Django 5.1.1
- **Frontend**: TailwindCSS
- **Database**: SQLite
- **AI Integration**: OpenAI / Anthropic API

## Setup Instructions

### Prerequisites
- Python 3.8+
- Git

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd Sami_sa
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create .env file:
```bash
cp .env.example .env
# Edit .env with your settings
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create superuser:
```bash
python manage.py createsuperuser
```

7. Run development server:
```bash
python manage.py runserver
```

Visit `http://localhost:8000` to see the application.

## Project Structure

```
Sami_sa/
├── apps/           # Django applications
├── config/         # Project configuration
├── static/         # Static files (CSS, JS, images)
├── templates/      # HTML templates
├── media/          # User uploads
└── utils/          # Shared utilities
```

## Development Stages

- [x] Stage 1: Project Setup & Authentication
- [x] Stage 2: Core Navigation & Settings
- [x] Stage 3: Dictionary & Vocabulary Management
- [x] Stage 4: Alphabet Display
- [x] Stage 5: Pre-made Lessons & Theory
- [x] Stage 6-9: Exercise Types
- [ ] Stage 10: Testing System
- [ ] Stage 11: Progress Tracking & Polish
- [ ] Stage 12: Deployment

## Contributing

This project is for a small group. Please contact the maintainer for contribution guidelines.

## License

Private project - All rights reserved
