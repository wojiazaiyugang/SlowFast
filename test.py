from pathlib import Path

import cv2
file = Path(r"/workspace/SlowFast/demo/AVA/videoplayback.mp4")
print(file.exists())
video = cv2.VideoCapture(str(file))
print(video.isOpened())

exit()


dataset = Path(r"/home/senseport0/Workspace/SlowFast/data/KTH")
with open(dataset.joinpath("train.csv"), "w") as train, \
        open(dataset.joinpath("val.csv"), "w") as val:
    for class_index, class_name in enumerate(["running", "walking"]):
        videos = list(dataset.joinpath(class_name).iterdir())
        for video_index, video in enumerate(videos):
            if video_index < 0.8 * len(videos):
                f = train
            else:
                f = val
            f.write(f"{str(video)} {class_index}")
            f.write("\n")
