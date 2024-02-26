import numpy as np

class Calculations_Service:
    def get_calories(weight, height, age, activity_factor, genre):
        # Harris Benedict's formula
        if genre == "male":
            GEB = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
        else :
            GEB = 655 + (9.6 * weight) + (1.8 * height) - (1.7 * age)

        if activity_factor == "sedentary":
            GEB *= 1.2
        elif activity_factor == "slightly active":
            GEB *= 1.375
        elif activity_factor == "moderately active":
            GEB *= 1.55
        elif activity_factor == "very active":
            GEB *= 1.725
        else:
            GEB *= 1.9
        GEB = round(GEB, 0)
        return GEB

    def get_calories_by_objective(maintenance_calories, objective):
        if objective == "build muscle":
            objective_calories = maintenance_calories * 1.3
        elif objective == "lose fat":
            objective_calories = maintenance_calories * 0.7
        else:
            objective_calories = maintenance_calories
        objective_calories = round(objective_calories, 0)
        return objective_calories

    def get_body_fat_percent(height, neck, waist, hip, genre):
        # Faulkner's formula
        if genre == "male":
            fat_percent = 495 / (1.0324 - 0.19077 * np.log10(waist - neck) + 0.15456 * np.log10(height)) - 450
        else:
            fat_percent = 495 / (1.29579 - 0.35004 * np.log10(hip + waist - neck) + 0.22100 * np.log10(height)) - 450
        fat_percent = round(fat_percent, 1)
        return fat_percent


    def get_hidratation(height, wheight, age, genre):
        # Mifflin St. Jeor's Basal metabolic rate formula
        BMR = (10 * wheight) + (6.25 * height) - (5 * age) + 161
        if genre == "male":
            BMR += 5
        else:
            BMR -= 161
        hidratation = (BMR * 1.2875)
        resp = (hidratation)

        return resp

    def get_hidratation_by_activity_factor(height, wheight, age, genre, activity_factor):
        # Mifflin St. Jeor's Basal metabolic rate formula
        BMR = (10 * wheight) + (6.25 * height) - (5 * age) + 161
        if genre == "male":
            BMR += 5
        else:
            BMR -= 161
        print(BMR)
        # Harris Benedict's formula
        if activity_factor == "sedentary":
            hidratation = BMR * 1.2
        elif activity_factor == "slightly active":
            hidratation = BMR * 1.375
        elif activity_factor == "moderately active":
            hidratation = BMR * 1.55
        elif activity_factor == "very active":
            hidratation = BMR * 1.725
        else:
            hidratation = BMR * 1.9
        result = round(hidratation, 0)
        return hidratation

    # 1 gr of protein = 4 kcal
    # 1 gr of carbs = 4 kcal
    # 1 gr of fat = 9 kcal

    def get_macros(weight, activity_factor, objective_calories):
        remaining_calories = objective_calories
        if activity_factor == "sedentary":
            protein = weight * 1
        elif activity_factor == "slightly active":
            protein = weight * 1.2
        elif activity_factor == "moderately active":
            protein = weight * 1.5
        elif activity_factor == "very active":
            protein = weight * 1.8
        else:
            protein = weight * 2
        protein = round(protein, 0)
        remaining_calories -= (protein * 4)
        carbs = remaining_calories * 0.584
        remaining_calories -= carbs
        carbs = round(carbs/4, 0)
        fat = round(remaining_calories/9, 0)
        return protein, carbs, fat