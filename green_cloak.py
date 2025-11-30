import cv2
import numpy as np
import time

def capture_background_avg(cap, frames=40, decay=0.1):
    ret, f = cap.read()
    if not ret:
        return None

    f = cv2.flip(f, 1)
    acc = f.astype(np.float32)

    for _ in range(frames - 1):
        ret, f = cap.read()
        if not ret:
            continue
        f = cv2.flip(f, 1)
        cv2.accumulateWeighted(f, acc, decay)

    return cv2.convertScaleAbs(acc)

def main():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
    cap.set(cv2.CAP_PROP_FPS, 30)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    if not cap.isOpened():
        print("❌ Could not open webcam.")
        return

    print("Press 'b' to capture background, 'q' to quit.")
    background = None

    k3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)

        if background is None:
            vis = frame.copy()
            cv2.putText(vis, "Press 'b' to capture background", (20, 35),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.imshow("Invisibility Cloak (Efficient)", vis)

            key = cv2.waitKey(1) & 0xFF

            if key == ord('b'):
                print("Capturing background...")
                background = capture_background_avg(cap, frames=40, decay=0.1)

                if background is None:
                    print("Failed. Try again.")
                else:
                    print("Done.")

            elif key == ord('q'):
                break

            continue

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # GREEN RANGE
        lower_green = np.array([40, 50, 70])
        upper_green = np.array([90, 255, 255])
        green_mask = cv2.inRange(hsv, lower_green, upper_green)

        green_mask = cv2.morphologyEx(green_mask, cv2.MORPH_OPEN, k3, iterations=1)
        green_mask = cv2.dilate(green_mask, k3, iterations=1)
        green_mask = cv2.blur(green_mask, (3, 3))

        out = frame.copy()
        cv2.copyTo(background, green_mask, out)

        cv2.putText(out, "b: recapture bg | q: quit", (15, 28),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (240, 240, 240), 2, cv2.LINE_AA)
        cv2.imshow("Invisibility Cloak (Efficient)", out)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break
        elif key == ord('b'):
            print("Re-capturing background...")
            background = capture_background_avg(cap, frames=30, decay=0.15)

            if background is None:
                print("Failed.")
            else:
                print("Updated.")

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
