from src.stitcher import stitch_videos

first_video = "temp/base.mp4"
second_video = "temp/generated_ending.mp4"
output_video = "outputs/final_video.mp4"

final_path = stitch_videos(first_video, second_video, output_video)

print("Final stitched video saved to:", final_path)