
# AltEnding AI

AltEnding AI is a prototype application that generates an alternate ending for a short video based on a user prompt.

The goal of this project was not just to call an AI model, but to learn how to build a complete end-to-end AI application with proper project structure, video preprocessing, prompt building, generation, and output stitching.

---

## Project Idea

The app takes a short video as input and allows the user to describe how they want the ending to change.

### Example use cases
- Add a new event at the end of a video
- Create a different mood or outcome for the final scene
- Generate a new continuation from the last frame of the original video

This project was built as an MVP/prototype focused on short clips and experimental alternate ending generation.

---

## What the App Does

1. Upload a short video
2. Extract the last few seconds of the video
3. Remove the original ending from the base clip
4. Extract the last frame from the original video
5. Build an enhanced generation prompt from user input
6. Generate a new ending using image-guided AI video generation
7. Stitch the generated ending back into the original base video
8. Return the final output video

---

## Current Status

This project is currently an MVP / prototype.

### Working features
- Video upload through Gradio UI
- Video duration detection
- Ending extraction
- Base video creation by removing the ending
- Last frame extraction
- Prompt enhancement
- Mock generation mode
- Real API-based generation integration
- Final stitching of video clips

### Current limitations
- Scene consistency is not always perfect
- Generated output can drift from the original camera view/composition
- Object addition is not always precise
- Results depend heavily on prompt quality and model behavior
- Best suited for short demo videos rather than production use

---

## Why This Project Was Built

This project was built to learn how to structure and build a real AI product pipeline, not just run isolated model calls.

The main learning goals were:

- understanding modular Python project structure
- working with video preprocessing
- using FFmpeg for trimming and stitching
- using OpenCV for frame extraction
- building prompt-processing logic
- integrating external AI APIs into a working app
- designing an end-to-end generation workflow

---

## Tech Stack

- **Python**
- **Gradio** for the UI
- **OpenCV** for frame extraction
- **FFmpeg** for video trimming and stitching
- **python-dotenv** for environment variables
- **requests** for downloading generated video outputs
- **fal API** for image-to-video generation

---

## Project Structure

```text
altending-ai/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── video_utils.py
│   ├── frame_utils.py
│   ├── prompt_builder.py
│   ├── generator.py
│   └── stitcher.py
│
├── tests/
│   ├── test_video_utils.py
│   ├── test_frame_utils.py
│   ├── test_prompt_builder.py
│   ├── test_generator.py
│   └── test_stitcher.py
│
├── assets/
├── temp/
└── outputs/
