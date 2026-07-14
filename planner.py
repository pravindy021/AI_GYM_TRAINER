from __future__ import annotations

from typing import Dict, List


def generate_workout_plan(goal: str, experience: str, days_per_week: int, duration_minutes: int, equipment: str) -> Dict[str, object]:
    goal = goal.lower()
    experience = experience.lower()

    if goal == "lose_weight":
        focus = "fat loss and cardio"
    elif goal == "build_muscle":
        focus = "strength and muscle gain"
    else:
        focus = "general fitness"

    if experience == "beginner":
        split = [
            ("Day 1", ["Bodyweight squats", "Incline push-ups", "Glute bridges", "Dead bug"], "Full body"),
            ("Day 2", ["Brisk walk", "Mobility flow", "Plank"], "Cardio + mobility"),
            ("Day 3", ["Step-ups", "Chair dips", "Bird dog", "Wall sit"], "Lower + core"),
        ]
    elif experience == "intermediate":
        split = [
            ("Day 1", ["Goblet squats", "Push-ups", "Bent-over rows", "Plank"], "Upper/lower"),
            ("Day 2", ["Jogging", "Jump rope", "Core circuit"], "Cardio"),
            ("Day 3", ["Romanian deadlifts", "Overhead press", "Lunges", "Side plank"], "Strength"),
            ("Day 4", ["Burpees", "Mountain climbers", "Shadow boxing"], "Conditioning"),
        ]
    else:
        split = [
            ("Day 1", ["Back squat", "Bench press", "Pull-ups", "Dumbbell row"], "Push/pull"),
            ("Day 2", ["Deadlift", "Romanian deadlift", "Farmer carry", "Hanging knee raises"], "Posterior chain"),
            ("Day 3", ["HIIT intervals", "Battle ropes", "Rowing"], "Cardio"),
            ("Day 4", ["Overhead press", "Bulgarian split squat", "Face pulls", "Plank"], "Upper body"),
            ("Day 5", ["Clean and press", "Kettlebell swings", "Burpee ladder"], "Power"),
        ]

    schedule = []
    for day, exercises, theme in split[:days_per_week]:
        schedule.append({"day": day, "theme": theme, "exercises": exercises, "duration": f"{duration_minutes} min"})

    return {
        "goal": goal.replace("_", " ").title(),
        "focus": focus,
        "equipment": equipment.title(),
        "schedule": schedule,
        "tips": [
            "Warm up for 5-10 minutes before every session.",
            "Use slow form and full range of motion.",
            "Rest 45-60 seconds between sets.",
        ],
    }


def generate_diet_plan(goal: str, weight_kg: float, height_cm: float, age: int, activity_level: str) -> Dict[str, object]:
    goal = goal.lower()
    activity_level = activity_level.lower()

    if goal == "lose_weight":
        calorie_target = round(weight_kg * 12 + 200)
        protein_g = round(weight_kg * 1.8)
        carbs_g = round(weight_kg * 2.5)
        fat_g = round(weight_kg * 0.8)
        style = "High protein, high fiber, moderate carbs"
    elif goal == "build_muscle":
        calorie_target = round(weight_kg * 15 + 250)
        protein_g = round(weight_kg * 2.2)
        carbs_g = round(weight_kg * 3.5)
        fat_g = round(weight_kg * 0.9)
        style = "Balanced meals with extra protein"
    else:
        calorie_target = round(weight_kg * 13 + 220)
        protein_g = round(weight_kg * 1.6)
        carbs_g = round(weight_kg * 3.0)
        fat_g = round(weight_kg * 0.8)
        style = "Simple meals with steady energy"

    if activity_level == "low":
        calorie_target -= 100
    elif activity_level == "high":
        calorie_target += 150

    meals = [
        ("Breakfast", "Greek yogurt bowl with berries, oats, and chia seeds"),
        ("Lunch", "Grilled chicken or tofu salad with quinoa and olive oil"),
        ("Dinner", "Salmon or lentil stir-fry with brown rice and vegetables"),
        ("Snack", "Apple with peanut butter or a protein shake"),
    ]

    return {
        "goal": goal.replace("_", " ").title(),
        "style": style,
        "calorie_target": calorie_target,
        "protein_g": protein_g,
        "carbs_g": carbs_g,
        "fat_g": fat_g,
        "meals": meals,
        "hydration": "Drink at least 2.5 to 3 liters of water every day.",
    }


def generate_coaching_media() -> Dict[str, List[str]]:
    return {
        "video": [
            "Follow a 10-minute mobility warm-up video before each workout.",
            "Use a guided form video for squats, lunges, and push-ups.",
            "Watch a posture check video after the session to cool down.",
        ],
        "audio": [
            "Play a motivational audio cue for the first 5 minutes of training.",
            "Use a calming breathing audio track during cooldown.",
            "Add a focus playlist to keep energy high during cardio.",
        ],
    }
