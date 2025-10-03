#!/usr/bin/env bash

# Samisa Project Setup Script
# This script initializes the complete project structure for the Slovak-English learning app

echo "=========================================="
echo "   SAMISA PROJECT SETUP"
echo "=========================================="
echo ""

# Always navigate to C:\ where Sami_sa is located
SCRIPT_DIR="/c"
cd "$SCRIPT_DIR" || exit 1
echo "✓ Working directory set to: $SCRIPT_DIR"
echo ""

# Navigate to Sami_sa directory (which must exist in C:\)
if [ ! -d "Sami_sa" ]; then
    echo "✗ Error: Sami_sa directory not found in C:\\"
    echo "Please ensure C:\Sami_sa exists before running this script."
    exit 1
fi

cd Sami_sa || exit 1
echo "✓ Changed to Sami_sa directory"
echo ""

echo "Creating a virtual environment"
python -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
if [ -d "venv" ]; then
    source venv/Scripts/activate
    echo "✓ Virtual environment activated"
else
    echo "✗ Error: venv directory not found!"
    echo "Create  a virtual environment"
    exit 1
fi
echo ""

# Create .gitignore
echo "Creating .gitignore..."
cat > .gitignore << 'EOF'
# Python
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST
__pycache__/
*.pyc

# Virtual Environment
venv/
env/
ENV/
.venv

# Django
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal
/media
/staticfiles

# Environment variables
.env
.env.local

# IDE
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# Tailwind
node_modules/
package-lock.json
static/css/output.css

# Testing
.coverage
htmlcov/
.pytest_cache/

# OS
Thumbs.db
EOF
echo "✓ .gitignore created"
echo ""

# Create project structure
echo "Creating project structure..."

# Root files
touch manage.py
touch requirements.txt
touch .env.example
touch README.md

# Config directory
mkdir -p config
touch config/__init__.py
touch config/settings.py
touch config/urls.py
touch config/wsgi.py
touch config/asgi.py

# Static directories
mkdir -p static/css
mkdir -p static/js
mkdir -p static/images
mkdir -p static/audio/alphabet

# Create static files
touch static/css/input.css
touch static/css/output.css
touch static/js/main.js
touch static/js/exercises.js
touch static/js/dictionary.js

# Media directory
mkdir -p media/profile_pictures

# Global templates
mkdir -p templates/components
mkdir -p templates/errors
touch templates/base.html
touch templates/components/navbar.html
touch templates/components/buttons.html
touch templates/errors/404.html
touch templates/errors/500.html

# Apps directory
mkdir -p apps

# Accounts app
mkdir -p apps/accounts/templates/accounts
touch apps/accounts/__init__.py
touch apps/accounts/admin.py
touch apps/accounts/apps.py
touch apps/accounts/models.py
touch apps/accounts/forms.py
touch apps/accounts/views.py
touch apps/accounts/urls.py
touch apps/accounts/tests.py
touch apps/accounts/templates/accounts/login.html
touch apps/accounts/templates/accounts/register.html
touch apps/accounts/templates/accounts/profile.html
touch apps/accounts/templates/accounts/profile_edit.html

# Core app
mkdir -p apps/core/templates/core
touch apps/core/__init__.py
touch apps/core/admin.py
touch apps/core/apps.py
touch apps/core/views.py
touch apps/core/urls.py
touch apps/core/tests.py
touch apps/core/templates/core/home.html
touch apps/core/templates/core/menu.html
touch apps/core/templates/core/settings.html

# Dictionary app
mkdir -p apps/dictionary/templates/dictionary
touch apps/dictionary/__init__.py
touch apps/dictionary/admin.py
touch apps/dictionary/apps.py
touch apps/dictionary/models.py
touch apps/dictionary/forms.py
touch apps/dictionary/views.py
touch apps/dictionary/urls.py
touch apps/dictionary/tests.py
touch apps/dictionary/templates/dictionary/dictionary_list.html
touch apps/dictionary/templates/dictionary/word_detail.html
touch apps/dictionary/templates/dictionary/word_create.html
touch apps/dictionary/templates/dictionary/category_list.html

# Lessons app
mkdir -p apps/lessons/templates/lessons
touch apps/lessons/__init__.py
touch apps/lessons/admin.py
touch apps/lessons/apps.py
touch apps/lessons/models.py
touch apps/lessons/views.py
touch apps/lessons/urls.py
touch apps/lessons/tests.py
touch apps/lessons/templates/lessons/lesson_list.html
touch apps/lessons/templates/lessons/lesson_detail.html
touch apps/lessons/templates/lessons/theory.html

# Exercises app
mkdir -p apps/exercises/templates/exercises
touch apps/exercises/__init__.py
touch apps/exercises/admin.py
touch apps/exercises/apps.py
touch apps/exercises/models.py
touch apps/exercises/views.py
touch apps/exercises/urls.py
touch apps/exercises/utils.py
touch apps/exercises/tests.py
touch apps/exercises/templates/exercises/exercise_menu.html
touch apps/exercises/templates/exercises/matching.html
touch apps/exercises/templates/exercises/translation.html
touch apps/exercises/templates/exercises/fill_blank.html
touch apps/exercises/templates/exercises/phrases.html
touch apps/exercises/templates/exercises/exercise_result.html

# Tests app
mkdir -p apps/tests/templates/tests
touch apps/tests/__init__.py
touch apps/tests/admin.py
touch apps/tests/apps.py
touch apps/tests/models.py
touch apps/tests/views.py
touch apps/tests/urls.py
touch apps/tests/tests.py
touch apps/tests/templates/tests/test_list.html
touch apps/tests/templates/tests/test_start.html
touch apps/tests/templates/tests/test_question.html
touch apps/tests/templates/tests/test_result.html

# Alphabet app
mkdir -p apps/alphabet/templates/alphabet
touch apps/alphabet/__init__.py
touch apps/alphabet/admin.py
touch apps/alphabet/apps.py
touch apps/alphabet/models.py
touch apps/alphabet/views.py
touch apps/alphabet/urls.py
touch apps/alphabet/tests.py
touch apps/alphabet/templates/alphabet/alphabet_list.html

# Utils directory
mkdir -p utils
touch utils/__init__.py
touch utils/mixins.py
touch utils/helpers.py

echo "✓ Project structure created"
echo ""

# Create requirements.txt
echo "Creating requirements.txt..."
cat > requirements.txt << 'EOF'
Django==5.1.1
python-decouple==3.8
Pillow==10.4.0
openai==1.51.0
anthropic==0.34.2
requests==2.32.3
EOF
echo "✓ requirements.txt created"
echo ""

# Create .env.example
echo "Creating .env.example..."
cat > .env.example << 'EOF'
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# AI API Keys (choose one or both)
OPENAI_API_KEY=your-openai-api-key
ANTHROPIC_API_KEY=your-anthropic-api-key

# Database
DATABASE_NAME=db.sqlite3
EOF
echo "✓ .env.example created"
echo ""

# Create README.md
echo "Creating README.md..."
cat > README.md << 'EOF'
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
- [ ] Stage 2: Core Navigation & Settings
- [ ] Stage 3: Dictionary & Vocabulary Management
- [ ] Stage 4: Alphabet Display
- [ ] Stage 5: Pre-made Lessons & Theory
- [ ] Stage 6-9: Exercise Types
- [ ] Stage 10: Testing System
- [ ] Stage 11: Progress Tracking & Polish
- [ ] Stage 12: Deployment

## Contributing

This project is for a small group. Please contact the maintainer for contribution guidelines.

## License

Private project - All rights reserved
EOF
echo "✓ README.md created"
echo ""

# Git operations
echo "Preparing Git commit..."
git add .
echo "✓ Files staged for commit"
echo ""

echo "Committing changes..."
git commit -m "Initial project setup"
echo "✓ Changes committed"
echo ""

echo "Pushing to GitHub..."
git push origin main || git push origin master
echo "✓ Pushed to GitHub"
echo ""

echo "=========================================="
echo "   SETUP COMPLETE!"
echo "=========================================="
echo ""
echo "Project structure created successfully!"
echo "Next steps:"
echo "  1. Edit .env file with your API keys"
echo "  2. Install requirements: pip install -r requirements.txt"
echo "  3. Start development with Stage 1"
echo ""
echo "Happy coding!"