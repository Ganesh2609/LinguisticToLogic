# Linguistic to Logic - The SQL Converter (LTL-SQL)

An intelligent Natural Language Processing tool that converts natural language queries into SQL commands, making database interactions accessible to non-technical users.

## Demo Video
[demo video](Video/Final%20video.mp4)

## 🎯 Project Overview

**Linguistic to Logic - The SQL Converter (LTL-SQL)** is an innovative tool developed by Code Syndicate that bridges the gap between human language and database querying. This system leverages Google's Gemini AI models to interpret natural language questions and automatically generate corresponding SQL queries, complete with visualizations and comprehensive analysis.

## ✨ Key Features

### 🔍 Natural Language Processing
- Converts plain English questions into optimized SQL queries
- Supports complex query structures and multiple database operations
- Intelligent field value analysis for appropriate response types

### 📊 Multi-Modal Outputs
- **General Queries**: Standard data retrieval with formatted results
- **Image Retrieval**: Extracts and displays images stored in BLOB format
- **Data Visualization**: Generates histograms, bar plots, line charts, pie charts, and scatter plots
- **Comparative Analysis**: Performs side-by-side data comparisons
- **Statistical Summaries**: Provides comprehensive dataset overviews

### 🗄️ Database Support
- **Built-in Databases**: Three pre-configured datasets (Real Estate, Student Records, Medical Records)
- **Custom Database Integration**: Support for user-defined database schemas
- **Multiple Database Types**: Compatible with MySQL and other standard SQL databases

### 🤖 AI-Powered Intelligence
- **Google Gemini Integration**: Utilizes multiple Gemini API keys with rotation system
- **Prompt Engineering**: Sophisticated prompt templates for different query types
- **Error Handling**: Robust validation and error recovery mechanisms

## 🏗️ Architecture

### Backend Components
```
Backend/
├── database_functions.py    # Database connection and query execution
├── gemini_functions.py      # Google Gemini API integration
├── processing_functions.py  # Main processing pipeline
├── prompts.py              # AI prompt templates
├── .env                    # Environment variables and API keys
└── key_rotation.json       # API key rotation configuration
```

### Frontend Components
```
Frontend/
├── 1_👨🏻‍💼_About_Us.py           # Team information and contact details
└── Pages/
    ├── 2_💻_The_Project.py        # Project overview and features
    ├── 3_🤖_Builtin_Databases.py  # Built-in database interface
    ├── 4_🧠_Custom_Databases.py   # Custom database creator
    └── 5_✍🏼_Reviews_and_FAQs.py  # User feedback and FAQ section
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- MySQL Server
- Google Gemini API Keys
- Required Python packages (see requirements.txt)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/LinguisticToLogic.git
cd LinguisticToLogic
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure environment variables**
```bash
# Update Backend/.env with your API keys and database credentials
GOOGLE_API_KEY_0 = 'your_api_key_here'
ROOT_PASSWORD = 'your_mysql_password'
```

4. **Set up MySQL database**
```bash
# Create the required databases and tables
# Import sample data for built-in databases
```

5. **Run the application**
```bash
streamlit run Frontend/1_👨🏻‍💼_About_Us.py
```

## 💡 Usage Examples

### Basic Query
```
Input: "Show me all students with marks above 80 in Science"
Output: Generates SQL query and displays filtered results
```

### Visualization Query
```
Input: "Plot a histogram of house prices by city"
Output: Creates SQL query, generates histogram visualization
```

### Image Retrieval
```
Input: "Display the image of the house with the lowest price per square foot"
Output: Retrieves and displays the corresponding property image
```

### Comparative Analysis
```
Input: "Compare the average marks between male and female students"
Output: Generates comparison table and analytical summary
```

## 🛠️ Technical Implementation

### AI Processing Pipeline
1. **Query Analysis**: Determines output type (general, plot, image, comparison, summary)
2. **SQL Generation**: Creates optimized SQL queries using Gemini AI
3. **Data Processing**: Executes queries and processes results
4. **Output Generation**: Formats results according to query type
5. **Visualization**: Creates appropriate charts and graphs when needed

### Key Rotation System
- Implements automatic API key rotation across 11 Google Gemini keys
- Ensures high availability and rate limit management
- Tracks usage patterns for optimal performance

### Database Integration
- Supports multiple database schemas
- Handles BLOB data for image storage and retrieval
- Implements robust error handling and validation

## 🎯 Supported Query Types

### Data Retrieval
- Simple SELECT statements
- Complex JOIN operations
- Aggregation functions (COUNT, AVG, SUM, etc.)
- Conditional filtering with WHERE clauses

### Visualizations
- **Histograms**: Distribution analysis
- **Bar Charts**: Categorical comparisons
- **Line Plots**: Trend analysis
- **Pie Charts**: Proportion visualization
- **Scatter Plots**: Correlation analysis

### Advanced Features
- Statistical summaries with descriptive analytics
- Multi-table comparisons
- Image retrieval from BLOB fields
- Custom database schema support

## 🏆 Project Highlights

- **Intelligent NLP**: Advanced natural language understanding
- **Multi-Modal Output**: Text, images, and visualizations
- **User-Friendly Interface**: Streamlit-based web application
- **Scalable Architecture**: Modular design for easy extension
- **Robust Error Handling**: Comprehensive validation and recovery
---

For more information, visit our [demo video](Video/Final%20video.mp4)