# 🏋️‍♂️ Of Course Protein

## 📌 Problem Statement
India faces a significant challenge with protein deficiency in daily diets, leading to malnutrition, weak muscle growth, and health issues. Many individuals, especially those engaged in fitness, struggle to meet their protein intake due to lack of awareness and proper nutritional guidance.

## 💡 Solution
This project aims to provide a personalized approach to calculating protein requirements based on user input, including age, weight, height, gender, and workout intensity. Using logical formulas and data analytics, the system suggests an appropriate protein intake and recommends region-specific protein-rich foods.

---

## 📊 Protein Level Calculation Formula
The calculation of daily protein requirements is based on the user's activity level:

1. **Basic Requirement** (Sedentary Lifestyle):
   \[ \text{Protein Intake} = \text{Weight} \times 0.8 \text{g} \]

2. **Moderate Activity** (Light Workouts, 1-3 days a week):
   \[ \text{Protein Intake} = \text{Weight} \times 1.2 \text{g} \]

3. **Intense Workouts** (4-6 days a week):
   \[ \text{Protein Intake} = \text{Weight} \times 1.5 \text{g} \]

4. **Athlete Level Training** (6+ days of rigorous training):
   \[ \text{Protein Intake} = \text{Weight} \times 2.0 \text{g} \]

### **BMI Calculation**
Body Mass Index (BMI) is calculated using the formula:

\[ \text{BMI} = \frac{\text{Weight (kg)}}{\left(\text{Height (m)}\right)^2} \]

BMI classification:
- **Underweight:** BMI < 18.5
- **Normal weight:** 18.5 - 24.9
- **Overweight:** 25 - 29.9
- **Obese:** BMI ≥ 30

### **Calorie Estimation (BMR Calculation)**
The Basal Metabolic Rate (BMR) is estimated using the **Harris-Benedict equation**:

\[ BMR = (10 \times \text{Weight}) + (6.25 \times \text{Height}) - (5 \times \text{Age}) + S \]

Where:
- \( S = +5 \) for males, \( -161 \) for females.

To determine **total daily energy expenditure (TDEE)**, the BMR is multiplied by an activity factor:

- **Sedentary (little to no exercise):** BMR × 1.2
- **Light activity (1-3 days/week):** BMR × 1.375
- **Moderate activity (4-5 days/week):** BMR × 1.55
- **Very active (6-7 days/week):** BMR × 1.725
- **Super active (twice daily training):** BMR × 1.9

This provides an estimate of daily calorie requirements to maintain weight, and further adjustments can be made for weight gain or loss goals.

---

## 🛠 Features
- 🏋️‍♂️ Personalized protein intake recommendation.
- 🔥 BMI classification and calorie estimation.
- 🍛 AI-based regional diet suggestions.
- 📊 Data visualization for BMI and TDEE insights.

---

## 🚀 How It Works
1. The user provides basic details such as weight, height, age, and activity level.
2. The system calculates their daily protein requirement.
3. The BMR and TDEE are computed to estimate calorie needs.
4. Based on BMI, an AI-powered diet recommendation is generated.
5. A graphical representation of BMI and TDEE levels is displayed for better understanding.
