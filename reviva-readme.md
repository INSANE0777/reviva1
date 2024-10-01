# Reviva: 🩺 AI-Powered Health Recommendation System

## 🌟 Project Overview

### Deployed Application: [https://reviva1-5.onrender.com/](https://reviva1-5.onrender.com/)

Developed by Afjal Hussein

## Table of Contents
- [Background](#background)
- [Features](#features)
- [AI Algorithm](#ai-algorithm)
- [Instructions to Run](#instructions-to-run)
- [Requirements](#requirements)
- [Description of Project](#description-of-project)
- [Contributions and Acknowledgments](#contributions-and-acknowledgments)

## Background
In an era where personalized health recommendations are becoming increasingly important, Reviva aims to provide users with an AI-powered tool for generating tailored health insights. Our application utilizes advanced machine learning techniques to offer personalized health recommendations based on individual user data.

## Description of Project
The Reviva web application provides users with an intuitive interface to input their health-related data and receive personalized recommendations. Users can input details such as age, gender, weight, height, activity level, and health goals. The application then utilizes cutting-edge AI algorithms to generate insightful health recommendations, including BMI calculations, calorie needs, and personalized advice.

## Features
- Real-time health analysis based on user-provided data.
- Calculation of BMI and interpretation of BMI category.
- Estimation of daily calorie needs based on personal factors.
- AI-generated personalized health recommendations.
- User-friendly interface for easy data input and result visualization.
 ![image](https://github.com/user-attachments/assets/6bc7b0ce-3875-4b83-aa56-834b420aa828)


### Input
User-provided health data including age, gender, weight, height, activity level, and health goals.

### Data Processing
- Utilizes a combination of traditional calculations and machine learning models.
- Employs a Random Forest Classifier for generating personalized recommendations.

### Health Analysis Techniques
- BMI Calculation and Interpretation
- Calorie Needs Estimation
- AI-powered Recommendation System

### Output
BMI score, BMI category, estimated daily calorie needs, and a set of personalized health recommendations.

## Instructions to Run
To run this project locally, follow these steps:

1. Clone the repository
```
git clone https://github.com/yourusername/reviva.git
cd reviva
```

2. Install Requirements
```
pip install -r requirements.txt
```

3. Run the application
```
python app.py
```

4. Open a web browser and navigate to `http://localhost:5000`

## Requirements
```
Flask==2.0.1
numpy==1.21.0
scikit-learn==0.24.2
```

## Contributions and Acknowledgments
This project is open for contributions, and we welcome any feedback or suggestions for improvement. If you find this project useful, feel free to use it for your needs. When attributing this project, please mention:
```
Reviva by [Your Name] & [Your Team Members' Names]
Repository: https://github.com/yourusername/reviva
```
