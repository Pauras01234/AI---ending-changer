from src.video_utils import (
    get_video_duration,
    extract_last_n_seconds,
    remove_last_n_seconds,
)

video_path = "assets/1.mp4"

duration = get_video_duration(video_path)
print("Duration:", duration)

ending_path = extract_last_n_seconds(video_path, "temp/ending.mp4", 5)
print("Ending saved to:", ending_path)

base_path = remove_last_n_seconds(video_path, "temp/base.mp4", 5)
print("Base saved to:", base_path)