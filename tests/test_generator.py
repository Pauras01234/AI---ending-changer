from src.generator import mock_generate_ending

source_video = "temp/ending.mp4"
output_video = "temp/generated_ending.mp4"

generated_path = mock_generate_ending(source_video, output_video)

print("Generated ending saved to:", generated_path)