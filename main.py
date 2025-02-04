import argparse
import platform


def initialise_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='BrakeAware - Brake Distance Awareness System')
    parser.add_argument('-n', '--net', help='Path for HEF model', default='./models/yolov8s.hef')
    parser.add_argument('-i', '--input_video', help='Path for input video', default='')
    parser.add_argument('-o', '--output_video', help='Path for output video', default='./saved_videos')
    parser.add_argument('-l', '--labels', help='Path for label file', default='./models/coco.txt')
    parser.add_argument('-s', '--score_thresh', help='Score threshold - 0 to 1', default=0.4)

    return parser


# platform.system()
