import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import openai

def get_user_data():
    name = input("Enter your name: ").strip()
    age = input("Enter your age: ").strip()
    weight = float(input("Enter your weight in kg: "))
    gender = input("Enter your gender (Male/Female/Other): ").strip().capitalize()
    height = float(input("Enter your height in cm: "))
    workout_days = input("Enter the number of workout days (0 to 6): ").strip()
    state = input("Enter your state: ").strip().capitalize()

    if workout_days == "0":
        intensity = "No Workout"
    else:
        print("Choose your workout intensity level:")
        print("1. Basic\n2. Moderate\n3. Intense\n4. Athlete Level")
        intensity_choice = input("Enter the number corresponding to your workout intensity: ").strip()
        intensity_levels = {"1": "Basic", "2": "Moderate", "3": "Intense", "4": "Athlete Level"}
        intensity = intensity_levels.get(intensity_choice, "Unknown")

    bmi = calculate_bmi(height, weight)
    maintenance_calories = calculate_calories(weight, height, age, gender, workout_days)

    return {
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Height (cm)": height,
        "Weight (kg)": weight,
        "Workout Days per Week": workout_days,
        "Workout Intensity": intensity,
        "BMI": round(bmi, 2),
        "BMI Category": classify_bmi(bmi),
        "Maintenance Calories": maintenance_calories,
        "State": state
    }

def calculate_bmi(height, weight):
    height_m = height / 100
    return weight / (height_m ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def calculate_calories(weight, height, age, gender, workout_days):
    if gender.lower() == "male":
        bmr = 10 * weight + 6.25 * height - 5 * int(age) + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * int(age) - 161
    activity_multipliers = {"0": 1.2, "1": 1.375, "2": 1.55, "3": 1.725, "4": 1.9, "5": 2.0, "6": 2.2}
    return round(bmr * activity_multipliers.get(workout_days, 1.2))

def display_data(data):
    print("\n========== User Workout Summary ==========")
    print(f"👤 Name: {data['Name']}  |  🎂 Age: {data['Age']}  |  ⚥ Gender: {data['Gender']}")
    print(f"📏 Height: {data['Height (cm)']} cm  |  ⚖ Weight: {data['Weight (kg)']} kg")
    print(f"🔥 Workout: {data['Workout Days per Week']} days/week ({data['Workout Intensity']})")
    print(f"🩺 BMI: {data['BMI']} ({data['BMI Category']})")
    print(f"🍽 Maintenance Calories: {data['Maintenance Calories']} kcal/day")
    print(f"📍 State: {data['State']}")
    print("==========================================\n")

    plot_bmi(data["BMI"])
    suggest_diet(data["Maintenance Calories"], data["State"])

def plot_bmi(bmi):
    categories = ["Underweight", "Normal Weight", "Overweight", "Obese"]
    values = [18.5, 24.9, 29.9, 35]
    positions = np.arange(len(categories))
    
    plt.figure(figsize=(8, 4))
    plt.bar(categories, values, color=["blue", "green", "orange", "red"], alpha=0.6)
    plt.axhline(y=bmi, color='black', linestyle='--', label=f'Your BMI: {bmi}')
    bmi_category = classify_bmi(bmi)
    plt.text(1, bmi + 0.5, f'You are in {bmi_category} range', fontsize=12, color='black')
    plt.xlabel("BMI Categories")
    plt.ylabel("BMI Value")
    plt.title("BMI Level Comparison")
    plt.legend()
    plt.show()

def suggest_diet(maintenance_calories, state):
    goal = input("What is your target? (Maintain/Bulk/Cut): ").strip().lower()
    if goal == "bulk":
        target_calories = maintenance_calories + 500
    elif goal == "cut":
        target_calories = maintenance_calories - 500
    else:
        target_calories = maintenance_calories

    client = openai.OpenAI(api_key="Your API key")  # Replace with your API key
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": f"Suggest 4-5 protein-rich foods commonly eaten in {state} with their protein, carbs, fats, and total calories for a {goal} goal requiring {target_calories} kcal per day."}
        ]
    )
    
    print("\n🍛 Recommended Diet:")
    print(completion.choices[0].message.content)

if __name__ == "__main__":
    user_data = get_user_data()
    display_data(user_data)
