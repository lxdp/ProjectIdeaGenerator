# Project Idea Generator

A web application that generates personalized project ideas based on real job market data. Users can search for jobs, get AI-generated project suggestions aligned with market demands, and view evidence showing how their projects match job qualifications.

## Features

- 🔍 **Job Market Search**: Filter jobs by role, location, employment type, and posting date
- 🤖 **AI-Powered Project Generation**: Generate project ideas tailored to job market requirements
- 📊 **Market Evidence**: View how project achievements align with real job qualifications
- 💾 **Save Projects**: Save and manage your generated projects
- 📈 **Recent Searches**: Quick access to your recent job searches

## Technology Stack

### Frontend
- **React.js** 19.2.3 - UI framework
- **React Router** 7.11.0 - Client-side routing
- **React Select** 5.10.2 - Multi-select dropdowns
- **Lucide React** 0.562.0 - Icons
- **CSS Modules** - Scoped styling

### Backend
- **Flask** - Python web framework
- **PostgreSQL** - Database for saving projects
- **Redis** - Caching layer for job listings and project ideas
- **Azure OpenAI** - GPT models for project generation
- **Pydantic** - Data validation and serialization
- **TheFuzz** - Fuzzy string matching for evidence calculation

## Prerequisites

Before running this project, ensure you have:

- **Python** 3.12+ 
- **Node.js** 16+ and npm
- **PostgreSQL** database running
- **Redis** server running
- **Azure OpenAI** API credentials
- Access to **OpenWebNinja** job listings API (or equivalent)

## Installation

### 1. Clone the repository

git clone <repository-url>
cd ProjectIdeaGenerator

### 2. Backend Setup

Create a Python virtual environment:
sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Python dependencies:
pip install -r requirements.txt
pip install flask flask-cors flask-caching pydantic psycopg2-binary redis thefuzz sentence-transformers

### 3. Frontend Setup

Navigate to the frontend directory:

cd frontend
npm install
cd ..

### 4. Database Setup

Create a PostgreSQL database and table:

CREATE DATABASE project_ideas;

CREATE TABLE history (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    parameters JSONB NOT NULL,
    project_list JSONB NOT NULL,
    evidence JSONB
);

### 5. Environment Variables

Create a `.env` file in the root directory:
v
# Flask Configuration
SECRET_KEY=your-secret-key-here
FLASK_DEBUG=false
FLASK_HOST=0.0.0.0
FLASK_PORT=5001

# CORS
ALLOWED_ORIGINS=http://localhost:3000

# Redis Configuration
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
CACHE_DEFAULT_TIMEOUT=3600

# PostgreSQL Configuration
DATABASE_NAME=project_ideas
USERNAME=your-db-username
PASSWORD=your-db-password
DB_HOST=localhost
PORT=5432

# Azure OpenAI Configuration
AZURE_OPENAI_API_KEY=your-azure-openai-api-key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_VERSION=2024-02-15-preview
AZURE_OPENAI_DEPLOYMENT_NAME=your-deployment-name

# OpenWebNinja API
JOB_LISTINGS_API_KEY=your-api-key

## Running the Application

### Start Redis
sh
redis-server

### Start PostgreSQL

Ensure PostgreSQL is running on your system.

### Start Backend Server

python -m api/app.pyThe Flask API will be available at `http://localhost:5001`

### Start Frontend Development Server

In a new terminal:
ash
cd frontend
npm startThe React app will be available at `http://localhost:3000`

## Project Structure

ProjectIdeaGenerator/
├── api/
│   └── app.py                 # Flask API routes and server
├── frontend/
│   ├── public/
│   │   └── ukCities.json     # City data for location selector
│   └── src/
│       ├── components/        # React components
│       ├── styles/            # CSS Modules
│       ├── config.js          # Frontend configuration
│       └── App.jsx            # Main React app with routing
├── src/
│   ├── pipelines/             # Core pipeline classes
│   │   ├── run.py            # MainPipeline orchestrator
│   │   ├── job_listings_api.py
│   │   ├── project_generation_api.py
│   │   ├── project_evidence.py
│   │   └── save_project_data.py
│   ├── schemas/               # Pydantic models
│   ├── prompts/               # GPT prompt templates
│   ├── queries/               # SQL queries
│   └── utils/                 # Utility functions
├── requirements.txt           # Python dependencies
└── .env                       # Environment variables (not in git)


