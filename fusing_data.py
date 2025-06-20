from datetime import datetime
import pandas as pd
import os

# Create new fused data
new_data = pd.DataFrame({
    "user_id": ["User A", "User B"],
    "typing_score": [2.5, 3.0],
    "voice_score": [2.1, 2.8],
    "screen_score": [3.2, 3.6],
})

# Add burnout and timestamp
new_data["burnout_score"] = (
    0.4 * new_data["typing_score"] +
    0.3 * new_data["voice_score"] +
    0.3 * new_data["screen_score"]
).round(2)

new_data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Save to one file
filename = "fused_scores_all.csv"

if os.path.exists(filename):
    old_data = pd.read_csv(filename)
    full_data = pd.concat([old_data, new_data], ignore_index=True)
else:
    full_data = new_data

full_data.to_csv(filename, index=False)
