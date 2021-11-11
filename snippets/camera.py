import cv2


def camera():
    cap = cv2.VideoCapture(0)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1280)
    cap.set(5,10)

    ret, frame = cap.read()  # (H, W, C) <class 'numpy.ndarray'>
    h, w = frame.shape[:2]
    print(h, w)

    print(type(frame))
    print(frame.shape)

    while True:
        ret, frame = cap.read()
        cv2.imshow('out', frame)

        # Press Q on keyboard to stop recording
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    camera()