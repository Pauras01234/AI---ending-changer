from pathlib import Path

import cv2


from src.video_utils import ensure_file_exists




def extract_last_frame(video_path: str, output_image_path: str) -> str:
    ensure_file_exists(video_path)
    output_path = Path(output_image_path)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    capture = cv2.VideoCapture(video_path)

    if not capture.isOpened():
        raise RuntimeError(f"could not open video: {video_path}")
    total_frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    if total_frames <= 0:
        capture.release()
        raise RuntimeError("video has no readable frames.")
    
    last_frame_index = total_frames - 1

    capture.set(cv2.CAP_PROP_POS_FRAMES, last_frame_index)

    success, frame = capture.read()

    capture.release()

    if not capture:
        raise RuntimeError("could not read the last frame from the video.")
    
    saved = cv2.imwrite(str(output_path), frame)

    if not saved:
        raise RuntimeError(f"Could not save the frame image to: {output_image_path}")
    
    return str(output_path)


     
