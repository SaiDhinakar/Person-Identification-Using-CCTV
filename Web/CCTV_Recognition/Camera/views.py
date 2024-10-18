from django.shortcuts import render
from django.http import StreamingHttpResponse
import cv2

# Create your views here.
def home(request):
    return render(request, 'home.html')

def outsiders(request):
    return render(request, 'outsider.html')

def id_detection(request):
    return render(request, 'IDdetection.html')

def generate_video(camera_id=0):
    # Replace this path with the actual video source or camera feed
    # cap = cv2.VideoCapture(f'path_to_camera_{camera_id}.mp4')  # Or use a camera feed
    cap = cv2.VideoCapture(camera_id)  # Or use a camera feed
    
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        # Encode the frame in JPEG format
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        # Yield each frame in an HTTP response
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()

# Django view to serve live video feed for each camera
def video_feed(request, camera_id):
    return StreamingHttpResponse(generate_video(camera_id),
                                 content_type='multipart/x-mixed-replace; boundary=frame')
