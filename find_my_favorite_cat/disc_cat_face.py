import os
import sys
import glob

import dlib

def CREATE_SVM_DETECTOR():

    options = dlib.simple_object_detector_training_options()

    options.C           = 5
    options.num_threads = 4
    options.be_verbose  = True
    # options.add_left_right_image_flips = True

    fname_xml_train = 'data/xml/training.xml'
    fname_xml_test  = 'data/xml/testing.xml'

    dlib.train_simple_object_detector(training_xml_path, "cat_detector.svm", options)

    print()
    print("Training accuracy: {}".format(dlib.test_simple_object_detector(fname_xml_train, "detector.svm")))
    print()
    print("Testing  accuracy: {}".format(dlib.test_simple_object_detector(fname_xml_test, "detector.svm")))


def RUN_SVM_DETECTOR():

    detector = dlib.simple_object_detector("detector.svm")
    win_det  = dlib.image_window()
    win_det.set_image(detector)

    win = dlib.image_window()
    fnames = glob.glob('data/BHS/*.png')
    for fname in fnames:
        print("Processing file: {}".format(fname))
        img = dlib.load_rgb_image(f)
        dets= detector(img)
        print("Number of faces detected: {}".format(len(dets)))
        for k, d in enumerate(dets):
            print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
                k, d.left(), d.top(), d.right(), d.bottom()))

        win.clear_overlay()
        win.set_image(img)
        win.add_overlay(dets)
        dlib.hit_enter_to_continue()


if __name__ == '__main__':
    TEST()
