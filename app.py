from __future__ import annotations

import argparse
import tkinter as tk
from tkinter import ttk
from planner import generate_coaching_media, generate_diet_plan, generate_workout_plan


def build_plan(goal: str, experience: str, days_per_week: int, duration_minutes: int, equipment: str, weight_kg: float, height_cm: float, age: int, activity_level: str):
    workout = generate_workout_plan(goal, experience, days_per_week, duration_minutes, equipment)
    diet = generate_diet_plan(goal, weight_kg, height_cm, age, activity_level)
    media = generate_coaching_media()
    return workout, diet, media


def format_plan(workout: dict, diet: dict, media: dict) -> str:
    lines = []
    lines.append(f"Goal: {workout['goal']}")
    lines.append(f"Focus: {workout['focus']}")
    lines.append(f"Equipment: {workout['equipment']}")
    lines.append("")
    lines.append("Workout plan:")
    for item in workout["schedule"]:
        lines.append(f"- {item['day']} ({item['theme']}): {', '.join(item['exercises'])} [{item['duration']}]")
    lines.append("")
    lines.append("Diet plan:")
    lines.append(f"- Calorie target: {diet['calorie_target']} kcal")
    lines.append(f"- Protein: {diet['protein_g']} g | Carbs: {diet['carbs_g']} g | Fat: {diet['fat_g']} g")
    for meal_name, meal_desc in diet["meals"]:
        lines.append(f"- {meal_name}: {meal_desc}")
    lines.append(f"- Hydration: {diet['hydration']}")
    lines.append("")
    lines.append("Video coaching:")
    for item in media["video"]:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("Audio coaching:")
    for item in media["audio"]:
        lines.append(f"- {item}")
    return "\n".join(lines)


def run_cli(args: argparse.Namespace) -> None:
    workout, diet, media = build_plan(
        args.goal,
        args.experience,
        args.days,
        args.duration,
        args.equipment,
        args.weight,
        args.height,
        args.age,
        args.activity,
    )
    print(format_plan(workout, diet, media))


def run_gui() -> None:
    root = tk.Tk()
    root.title("AI Gym Trainer")
    root.geometry("760x520")

    tk.Label(root, text="AI Gym Trainer", font=("Segoe UI", 18, "bold")).pack(pady=(12, 8))

    form = ttk.Frame(root, padding=10)
    form.pack(fill="x")

    fields = {}
    row = 0
    for label, key, default in [
        ("Goal", "goal", "lose_weight"),
        ("Experience", "experience", "beginner"),
        ("Days / week", "days", "3"),
        ("Duration (min)", "duration", "45"),
        ("Equipment", "equipment", "home"),
        ("Weight (kg)", "weight", "70"),
        ("Height (cm)", "height", "175"),
        ("Age", "age", "28"),
        ("Activity", "activity", "medium"),
    ]:
        ttk.Label(form, text=label).grid(row=row, column=0, sticky="w", padx=(0, 10), pady=4)
        entry = ttk.Entry(form)
        entry.insert(0, default)
        entry.grid(row=row, column=1, sticky="ew", pady=4)
        fields[key] = entry
        row += 1

    output = tk.Text(root, wrap="word", height=20)
    output.pack(fill="both", expand=True, padx=10, pady=(8, 10))

    def generate_clicked() -> None:
        workout, diet, media = build_plan(
            fields["goal"].get(),
            fields["experience"].get(),
            int(fields["days"].get()),
            int(fields["duration"].get()),
            fields["equipment"].get(),
            float(fields["weight"].get()),
            float(fields["height"].get()),
            int(fields["age"].get()),
            fields["activity"].get(),
        )
        output.delete("1.0", tk.END)
        output.insert(tk.END, format_plan(workout, diet, media))

    ttk.Button(root, text="Generate plan", command=generate_clicked).pack(pady=(0, 10))
    root.mainloop()


def main() -> None:
    parser = argparse.ArgumentParser(description="AI gym trainer")
    parser.add_argument("--goal", default="lose_weight")
    parser.add_argument("--experience", default="beginner")
    parser.add_argument("--days", type=int, default=3)
    parser.add_argument("--duration", type=int, default=45)
    parser.add_argument("--equipment", default="home")
    parser.add_argument("--weight", type=float, default=70)
    parser.add_argument("--height", type=float, default=175)
    parser.add_argument("--age", type=int, default=28)
    parser.add_argument("--activity", default="medium")
    parser.add_argument("--gui", action="store_true")
    args = parser.parse_args()

    if args.gui:
        run_gui()
    else:
        run_cli(args)


if __name__ == "__main__":
    main()
