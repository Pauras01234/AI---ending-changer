import gradio as gr

from src.video_utils import extract_last_n_seconds, remove_last_n_seconds
from src.frame_utils import extract_last_frame
from src.prompt_builder import build_video_prompt
from src.generator import generate_ending_with_fal
from src.stitcher import stitch_videos


def process_video(video_path: str, user_prompt: str) -> tuple[str, str]:
    ending_path = extract_last_n_seconds(video_path, "temp/ending.mp4", 5)
    base_path = remove_last_n_seconds(video_path, "temp/base.mp4", 5)

    extract_last_frame(video_path, "temp/last_frame.jpg")

    final_prompt = build_video_prompt(user_prompt)

    generated_ending_path = generate_ending_with_fal(
        "temp/last_frame.jpg",
        final_prompt,
        "temp/generated_ending.mp4"
    )

    final_video_path = stitch_videos(
        base_path,
        generated_ending_path,
        "outputs/final_video.mp4"
    )

    return final_video_path, final_prompt


app = gr.Interface(
    fn=process_video,
    inputs=[
        gr.Video(label="Upload Video"),
        gr.Textbox(label="Describe the new ending")
    ],
    outputs=[
        gr.Video(label="Final Output Video"),
        gr.Textbox(label="Built Prompt")
    ],
    title="AltEnding AI",
    description="Upload a short video and describe the new ending you want."
)


if __name__ == "__main__":
    app.launch()