import unittest

from planner import generate_coaching_media, generate_diet_plan, generate_workout_plan


class PlannerTests(unittest.TestCase):
    def test_workout_plan_contains_schedule(self):
        plan = generate_workout_plan("lose_weight", "beginner", 3, 40, "home")
        self.assertGreater(len(plan["schedule"]), 0)
        self.assertIn("Day 1", plan["schedule"][0]["day"])

    def test_diet_plan_has_macro_targets(self):
        plan = generate_diet_plan("build_muscle", 75, 180, 30, "high")
        self.assertGreater(plan["calorie_target"], 0)
        self.assertGreater(plan["protein_g"], 0)
        self.assertGreater(plan["carbs_g"], 0)

    def test_media_has_video_and_audio_tips(self):
        media = generate_coaching_media()
        self.assertGreater(len(media["video"]), 0)
        self.assertGreater(len(media["audio"]), 0)


if __name__ == "__main__":
    unittest.main()
