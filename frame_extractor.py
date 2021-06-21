import os
import cv2

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrameExtractor(object):
    def setupUi(self, FrameExtractor):
        FrameExtractor.setObjectName("FrameExtractor")
        FrameExtractor.resize(631, 308)
        self.centralwidget = QtWidgets.QWidget(FrameExtractor)
        self.centralwidget.setObjectName("centralwidget")
        self.extract_frames_button = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:press_it())
        self.extract_frames_button.setGeometry(QtCore.QRect(510, 200, 111, 51))
        self.extract_frames_button.setObjectName("extract_frames_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 441, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.video_label = QtWidgets.QLabel(self.centralwidget)
        self.video_label.setGeometry(QtCore.QRect(10, 90, 61, 31))
        self.video_label.setObjectName("video_label")
        self.output_dir_label = QtWidgets.QLabel(self.centralwidget)
        self.output_dir_label.setGeometry(QtCore.QRect(0, 130, 81, 41))
        self.output_dir_label.setObjectName("output_dir_label")
        self.video_line_edit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.video_line_edit_1.setGeometry(QtCore.QRect(80, 90, 541, 31))
        self.video_line_edit_1.setObjectName("video_line_edit_1")
        video_line_edit_1 = self.video_line_edit_1
        self.output_dir_line_edit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.output_dir_line_edit_2.setGeometry(QtCore.QRect(80, 140, 541, 31))
        self.output_dir_line_edit_2.setObjectName("output_dir_line_edit_2")
        output_dir_line_edit_2 = self.output_dir_line_edit_2
        self.output_dir_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.output_dir_label_2.setGeometry(QtCore.QRect(10, 200, 81, 41))
        self.output_dir_label_2.setObjectName("output_dir_label_2")
        self.format_comboBox = QtWidgets.QComboBox(self.centralwidget,editable=True,insertPolicy=QtWidgets.QComboBox.InsertAtBottom)
        self.format_comboBox.setGeometry(QtCore.QRect(80, 210, 86, 25))
        self.format_comboBox.setObjectName("format_comboBox")
        self.format_comboBox.addItem("jpeg")
        self.format_comboBox.addItem("jpg") 
        self.format_comboBox.addItem("bmp")
        format_comboBox=self.format_comboBox
        FrameExtractor.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FrameExtractor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 631, 22))
        self.menubar.setObjectName("menubar")
        FrameExtractor.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FrameExtractor)
        self.statusbar.setObjectName("statusbar")
        FrameExtractor.setStatusBar(self.statusbar)

        self.retranslateUi(FrameExtractor)
        QtCore.QMetaObject.connectSlotsByName(FrameExtractor)
        
        def press_it():

            in_video = video_line_edit_1.text()
            img_format =  format_comboBox.currentText()
            vid_name = (in_video.rsplit('.')[0]).rsplit('/')[-1]
            video = cv2.VideoCapture(in_video)
            nb_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
            print('Video name is',in_video)
            out_directory = output_dir_line_edit_2.text()
            if not os.path.exists(out_directory):
                os.mkdir(out_directory)
            count = 0

            while True:
    
                ret, frame = video.read()
                if ret:
                    count+=1
                    name = out_directory+'/' + str(vid_name)+'_'+str(count)+'.'+img_format
                    cv2.imwrite(name,frame)
                    print('creating '+str(name)+'/'+str(nb_frames))
                else:
                    break
        
            video.release()
            cv2.destroyAllWindows()

    def retranslateUi(self, FrameExtractor):
        _translate = QtCore.QCoreApplication.translate
        FrameExtractor.setWindowTitle(_translate("FrameExtractor", "Frame Extractor 0.0.1"))
        self.extract_frames_button.setText(_translate("FrameExtractor", "Extract Frames"))
        self.label.setText(_translate("FrameExtractor", "Frame Extractor"))
        self.video_label.setText(_translate("FrameExtractor", "Video:"))
        self.output_dir_label.setText(_translate("FrameExtractor", "Output\n"
"Directory:"))
        self.output_dir_label_2.setText(_translate("FrameExtractor", "format:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrameExtractor = QtWidgets.QMainWindow()
    ui = Ui_FrameExtractor()
    ui.setupUi(FrameExtractor)
    FrameExtractor.show()
    sys.exit(app.exec_())
