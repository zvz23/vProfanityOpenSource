import cv2
import os


def export_video_images_by_second(video_file: str):
    # Set the path to the input video file
    # Set the path to the output directory where the extracted frames will be saved
    output_dir = 'images'

    # Create the output directory if it doesn't already exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Create a VideoCapture object to read the input video file
    cap = cv2.VideoCapture(video_file)

    # Get the frame rate of the video
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Set the current frame index to 0
    current_frame = 0

    # Loop through the video frames
    while True:
        # Read the current frame
        ret, frame = cap.read()

        # Check if the frame was read successfully
        if not ret:
            break

        # Check if the current frame index is a multiple of the frame rate
        if current_frame % int(fps) == 0:
            # Calculate the current time in seconds
            current_time = current_frame / fps

            # Format the current time as a string with two decimal places
            time_str = '{:.2f}'.format(current_time)

            # Set the output file path for the current frame
            output_path = os.path.join(output_dir, f'frame_{time_str}.jpg')

            # Save the current frame as an image
            cv2.imwrite(output_path, frame)

        # Increment the current frame index
        current_frame += 1

    # Release the VideoCapture object and close any open windows
    cap.release()
    cv2.destroyAllWindows()
