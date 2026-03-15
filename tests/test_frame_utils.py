from src.frame_utils import extract_last_frame

video_path = "assets/1.mp4"
image_path = "temp/last_frame.jpg"

saved_image = extract_last_frame(video_path, image_path)
print("Last frame saved to:", saved_image)