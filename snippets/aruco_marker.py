import pathlib
import cv2


def camera():
    ColorCyan = (255, 255, 0)
    aruco = cv2.aruco
    dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

    print(dictionary)

    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    h, w = frame.shape[:2]

    while True:
        ret, frame = cap.read()

        corners, ids, rejectedImgPoints = aruco.detectMarkers(frame, dictionary) 
        aruco.drawDetectedMarkers(frame, corners, ids, ColorCyan) 

        print(ids)

        cv2.imshow('out', frame)
        # Press Q on keyboard to stop recording
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()



def generate_marker(num=4):
    aruco = cv2.aruco
    p_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

    for i in range( num ):
        img_marker = aruco.drawMarker(p_dict, i, 75) # 75x75 px
        cv2.imwrite(f'img/marker{i}.png', img_marker)


if __name__ == '__main__':
    # generate_marker()
    camera()



# https://qiita.com/code0327/items/c6e468da7007734c897f