import argparse
import queue
import platform

from hailo_utils import HailoAsyncInference


def init():
    pass


def preprocess_frame():
    pass


def extract_detections():
    pass


def postprocess_detections():
    pass


def update_ins():
    pass


def update_gps():
    pass


def get_frame():
    pass


def save_frame():
    pass


def initialise_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='BrakeAware - Brake Distance Awareness System')
    parser.add_argument('-n', '--net', help='Path for HEF model', default='./models/yolov8s.hef')
    parser.add_argument('-i', '--input_video', help='Path for input video', default='')
    parser.add_argument('-o', '--output_video', help='Path for output video', default='./saved_videos')
    parser.add_argument('-l', '--labels', help='Path for label file', default='./models/coco.txt')
    parser.add_argument('-s', '--score_thresh', help='Score threshold - 0 to 1', default=0.4)
    parser.add_argument('-w', '--width', help='Pixel width of the video', default=1280)
    parser.add_argument('-h', '--height', help='Pixel height of the video', default=720)

    return parser


def main() -> None:
    args = initialise_arg_parser().parse_args()

    input_queue = queue.Queue()
    output_queue = queue.Queue()
    hailo_inference = HailoAsyncInference(hef_path=args.net, input_queue=input_queue, output_queue=output_queue)
    model_h, model_w, _ = hailo_inference.get_input_shape()

# platform.system()
