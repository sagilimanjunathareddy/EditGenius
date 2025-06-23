def calculate_reward(score: int) -> float:
    """Convert feedback score (1–5) to a reward (0.0–1.0)."""
    return round(score / 5, 2)

def log_feedback(original, rewritten, score, reward):
    """Log feedback and reward for RL simulation."""
    with open("feedback_log.txt", "a", encoding="utf-8") as f:
        f.write("=== FEEDBACK SESSION ===\n")
        f.write(f"Original:\n{original}\n")
        f.write(f"Rewritten:\n{rewritten}\n")
        f.write(f"User Score: {score}/5\n")
        f.write(f"Reward: {reward}\n\n")
