from kivy.app import App
from kivy.uix.image import Image

from kivy_garden.xcamera import XCamera
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import mediapipe as mp
from letters import C, B
import cv2


class KivyCamera(Image):
    def __init__(self, capture, fps, **kwargs):
        super(KivyCamera, self).__init__(**kwargs)
        self.capture = capture
        self.n, self.b, self.n1, self.b1, self.nl, self.bl = 0, 0, 0, 0, 0, 0
        self.text = [' ']
        self.mpHolistic = mp.solutions.holistic
        self.holistic = self.mpHolistic.Holistic()
        self.results = self.holistic
        Clock.schedule_interval(self.update, 1.0 / fps)

    def update(self, dt):
        ret, frame = self.capture.read()

        img = cv2.copyMakeBorder(frame, 0, 0, 0, 0, cv2.BORDER_CONSTANT, value=[0, 200, 200])

        if ret:
            # convert it to texture
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            self.results = self.holistic.process(imgRGB)
            # display image from the texture
            if -0.3 > self.results.pose_landmarks.landmark[0].z > -1.3:
                img = cv2.copyMakeBorder(frame, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[0, 200, 200])

                if self.results.right_hand_landmarks and not self.results.left_hand_landmarks:

                    for h in range(len(C)):
                        for k in range(21):
                            if (C[h][1][k] - 0.04) < (
                                    self.results.right_hand_landmarks.landmark[k].x / self.results.right_hand_landmarks.landmark[
                                0].x) < \
                                    (C[h][1][k] + 0.04):
                                self.n = self.n + 1
                            if (C[h][2][k] - 0.04) < (
                                    self.results.right_hand_landmarks.landmark[k].y / self.results.right_hand_landmarks.landmark[
                                0].y) < \
                                    (C[h][2][k] + 0.04):
                                self.n = self.n + 1

                            if (C[h][3][0]) - 0.2 < (
                                    self.results.right_hand_landmarks.landmark[0].x / self.results.pose_landmarks.landmark[0].x) < \
                                    (C[h][3][0]) + 0.2:
                                self.n1 = self.n1 + 1

                            if (C[h][4][0]) - 0.2 < (
                                    self.results.right_hand_landmarks.landmark[0].y / self.results.pose_landmarks.landmark[0].y) < \
                                    (C[h][4][0]) + 0.2:
                                self.n1 = self.n1 + 1

                            if k == 20:
                                self.b = self.n
                                self.n = 0
                                self.b1 = self.n1
                                self.n1 = 0
                        if self.b > 37 and self.b1 > 37:
                            if self.text[len(self.text) - 1] != C[h][0]:
                                self.text.append(C[h][0])
                            break

                    cv2.rectangle(img, (650, 440), (0, 420), (255, 255, 255), -1)
                    cv2.putText(img, ' '.join(map(str, self.text)), (15, 435), cv2.FONT_ITALIC,
                                0.5, (0, 0, 0), 1)
                    cv2.putText(img, ' '.join(str(self.b)), (15, 100), cv2.FONT_ITALIC,
                                0.5, (0, 0, 0), 1)
                    cv2.putText(img, ' '.join(str(self.b1)), (15, 200), cv2.FONT_ITALIC,
                                0.5, (0, 0, 0), 1)

                elif self.results.right_hand_landmarks and self.results.left_hand_landmarks:
                    for h in range(len(B)):
                        for k in range(21):
                            if (B[h][1][k] - 0.04) < (
                                    self.results.right_hand_landmarks.landmark[k].x / self.results.right_hand_landmarks.landmark[
                                0].x) < \
                                    (B[h][1][k] + 0.04):
                                self.n = self.n + 1
                            if (B[h][2][k] - 0.04) < (
                                    self.results.left_hand_landmarks.landmark[k].x / self.results.left_hand_landmarks.landmark[
                                0].x) < \
                                    (B[h][2][k] + 0.04):
                                self.nl = self.nl + 1

                            if (B[h][3][k] - 0.04) < (
                                    self.results.right_hand_landmarks.landmark[k].y / self.results.right_hand_landmarks.landmark[
                                0].y) < \
                                    (B[h][3][k] + 0.04):
                                self.n = self.n + 1
                            if (B[h][4][k] - 0.04) < (
                                    self.results.left_hand_landmarks.landmark[k].y / self.results.left_hand_landmarks.landmark[
                                0].y) < \
                                    (B[h][4][k] + 0.04):
                                self.nl = self.nl + 1

                            if (B[h][5][0]) - 0.2 < (
                                    (self.results.right_hand_landmarks.landmark[0].x / self.results.left_hand_landmarks.landmark[
                                        0].x) /
                                    self.results.pose_landmarks.landmark[0].x) < (B[h][5][0]) + 0.2:
                                self.n1 = self.n1 + 1

                            if (B[h][6][0]) - 0.2 < (
                                    (self.results.right_hand_landmarks.landmark[0].y / self.results.left_hand_landmarks.landmark[
                                        0].y) /
                                    self.results.pose_landmarks.landmark[0].y) < (B[h][6][0]) + 0.2:
                                self.n1 = self.n1 + 1

                            if k == 20:
                                self.b = self.n
                                self.n = 0
                                self.b1 = self.n1
                                self.n1 = 0
                                self.bl = self.nl
                                self.nl = 0
                        if self.b > 39 and self.b1 > 40 and self.bl > 35:
                            if self.text[len(self.text) - 1] != B[h][0]:
                                self.text.append(B[h][0])
                            break
                cv2.rectangle(img, (650, 440), (0, 420), (255, 255, 255), -1)
                cv2.putText(img, ' '.join(map(str, self.text)), (15, 435), cv2.FONT_ITALIC,
                                0.5, (0, 0, 0), 1)
                cv2.putText(img, str(self.b) + " " + str(self.bl) + " " + str(self.b1), (35, 105), cv2.FONT_ITALIC,
                                2, (0, 0, 0), 2)

                buf1 = cv2.flip(img, 0)
                buf = buf1.tostring()
                image_texture = Texture.create(
                    size=(img.shape[1], img.shape[0]), colorfmt='bgr')
                image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')

            else:
                img = cv2.copyMakeBorder(frame, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[0, 0, 200])
                buf1 = cv2.flip(img, 0)
                buf = buf1.tostring()
                image_texture = Texture.create(
                    size=(img.shape[1], img.shape[0]), colorfmt='bgr')
                image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')

            self.texture = image_texture


class CamApp(App):
    def build(self):
        self.capture = cv2.VideoCapture(0)
        # cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
        # cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN,
        #                       cv2.WINDOW_FULLSCREEN)
        self.my_camera = KivyCamera(capture=self.capture, fps=30)
        return self.my_camera

    def on_stop(self):
        #without this, app will not exit even if the window is closed
        self.capture.release()


if __name__ == '__main__':
    CamApp().run()




