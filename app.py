from flask import Flask, render_template, request, jsonify
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)


def create_mock_model():
    X = np.random.rand(1000, 5)  
    y = np.random.randint(0, 5, 1000)  
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

model = create_mock_model()
scaler = StandardScaler()
scaler.fit(np.random.rand(1000, 5))

def calculate_bmi(weight, height):
    bmi = weight / ((height / 100) ** 2)
    return round(bmi, 2)

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def calculate_calories(weight, height, age, gender, activity_level):
    if gender == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    activity_multipliers = {
        'sedentary': 1.2,
        'lightly_active': 1.375,
        'moderately_active': 1.55,
        'very_active': 1.725,
        'extra_active': 1.9
    }

    return round(bmr * activity_multipliers[activity_level])

def get_ai_recommendations(age, gender, bmi, activity_level, goal):
    gender_num = 1 if gender == 'male' else 0
    activity_num = ['sedentary', 'lightly_active', 'moderately_active', 'very_active', 'extra_active'].index(activity_level)
    goal_num = ['maintain', 'lose', 'gain'].index(goal)

    input_data = np.array([[age, gender_num, bmi, activity_num, goal_num]])
    input_data_scaled = scaler.transform(input_data)

    recommendation_class = model.predict(input_data_scaled)[0]

    recommendations = [
        "Focus on a balanced diet with plenty of fruits and vegetables.",
        "Incorporate strength training exercises into your routine.",
        "Ensure you're staying hydrated throughout the day.",
        "Consider adding more protein to your diet to support muscle growth.",
        "Try to get at least 7-8 hours of sleep each night for optimal health.",
        "Practice mindfulness or meditation to reduce stress.",
        "Include more whole grains in your diet for sustained energy.",
        "Try high-intensity interval training (HIIT) for efficient workouts.",
        "Incorporate regular stretching or yoga for flexibility and relaxation.",
        "Experiment with meal prepping to maintain a consistent diet.",
        "Aim to eat at least 5 servings of colorful vegetables daily.",
        "Incorporate healthy fats like nuts, seeds, and avocados into your diet.",
        "Try to limit your screen time before bed to improve sleep quality.",
        "Incorporate activities that bring you joy and help reduce stress.",
        "Consider working with a registered dietitian to create a personalized meal plan.",
        "Aim to drink at least 8 cups (64 oz) of water each day.",
        "Incorporate strength training exercises that target multiple muscle groups at once.",
        "Try to limit your intake of processed and packaged foods.",
        "Incorporate activities that challenge your mind, such as puzzles or learning a new skill.",
        "Aim to get at least 10,000 steps per day to support overall health.",
        "Incorporate exercises that improve balance and coordination, such as tai chi or balance training.",
        "Try to eat a variety of different colored fruits and vegetables to ensure a range of nutrients.",
        "Consider incorporating omega-3 rich foods, such as salmon or walnuts, into your diet.",
        "Incorporate stress-reducing activities, such as deep breathing or progressive muscle relaxation.",
        "Aim to limit your intake of added sugars and refined carbohydrates.",
        "Incorporate exercises that improve flexibility, such as Pilates or yoga.",
        "Try to get some morning sunlight exposure to help regulate your circadian rhythms.",
        "Incorporate activities that promote social connection, such as joining a club or volunteering.",
        "Consider incorporating probiotic-rich foods, such as yogurt or kefir, into your diet.",
        "Aim to limit your intake of saturated and trans fats.",
        "Incorporate exercises that improve cardiovascular health, such as brisk walking or swimming.",
        "Try to get enough vitamin D through sun exposure, supplements, or fortified foods.",
        "Incorporate activities that promote mental stimulation, such as reading or learning a new language."
    ]

    return recommendations[recommendation_class:recommendation_class+5]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    age = int(request.form['age'])
    gender = request.form['gender']
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    activity_level = request.form['activity_level']
    goal = request.form['goal']

    bmi = calculate_bmi(weight, height)
    bmi_category = interpret_bmi(bmi)
    calories = calculate_calories(weight, height, age, gender, activity_level)
    recommendations = get_ai_recommendations(age, gender, bmi, activity_level, goal)

    return jsonify({
        'bmi': bmi,
        'bmi_category': bmi_category,
        'calories': calories,
        'recommendations': recommendations
    })

if __name__ == '__main__':
    app.run(debug=False,host='0,0,0,0')