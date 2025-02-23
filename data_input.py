import pandas as pd

# Function to get user input
def get_user_data():
    name = input("👤 Enter your name: ")
    age = input("🎂 Enter your age: ")
    gender = input("⚧️ Enter your gender (Male/Female/Other): ")
    height = input("📏 Enter your height in cm: ")
    weight = input("⚖️ Enter your weight in kg: ")
    
    print("\n💪 How many days do you work out per week? (Choose a number from 0 to 6)")
    workout_days = input("🏋️‍♂️ Enter the number of workout days: ")
    
    print("\n🔥 Choose your workout intensity level:")
    print("1️⃣ Basic\n2️⃣ Moderate\n3️⃣ Intense\n4️⃣ Athlete Level")
    
    intensity_choice = input("⚡ Enter the number corresponding to your workout intensity: ")
    intensity_levels = {"1": "Basic", "2": "Moderate", "3": "Intense", "4": "Athlete Level"}
    intensity = intensity_levels.get(intensity_choice, "Unknown")
    
    return {
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Height (cm)": height,
        "Weight (kg)": weight,
        "Workout Days per Week": workout_days,
        "Workout Intensity": intensity
    }

# Function to display data in table format
def display_data(data):
    df = pd.DataFrame([data])
    print("\n📊 User Workout Details:")
    print(df.to_string(index=False))

# Main function to execute the script
if __name__ == "__main__":
    user_data = get_user_data()
    display_data(user_data)
