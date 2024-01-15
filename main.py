import cv2
import numpy as np
import socketio
import threading
import queue
import config

sio = socketio.Client()
frame_queue = queue.Queue()


def socket_connection():

    @sio.on('connect', namespace=config.NAMESPACE)
    def on_connect():
        print(f"Connected to {config.NAMESPACE} namespace")

    @sio.on('disconnect', namespace=config.NAMESPACE)
    def on_disconnect():
        print(f"Disconnected from {config.NAMESPACE} namespace")

    @sio.on('frame', namespace=config.NAMESPACE)
    def on_frame(data):
        try:
            np_arr = np.frombuffer(data['frame_data'], np.uint8)
            img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

            if img is not None:
                frame_queue.put(img)
        except Exception as e:
            print(f"Error processing frame: {e}")

    url = f'{config.PROTOCOL}://{config.IP_ADDRESS}:{config.PORT}'
    print(url)
    sio.connect(url, namespaces=[config.NAMESPACE])


def display_frames():
    cv2.namedWindow('video', cv2.WINDOW_NORMAL)
    while True:
        if not frame_queue.empty():
            frame = frame_queue.get()
            cv2.imshow('video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cv2.destroyAllWindows()
    sio.disconnect()
    socket_thread.join()


socket_thread = threading.Thread(target=socket_connection)
socket_thread.start()
display_frames()








