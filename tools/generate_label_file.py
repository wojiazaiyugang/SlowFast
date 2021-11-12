"""
从分类数据文件夹生成训练用的csv文件
"""
import random
from pathlib import Path
from typing import List

from typer import Typer

app = Typer()

current_dir = Path(__file__).resolve().parent
train_csv = current_dir.joinpath("train.csv")
val_csv = current_dir.joinpath("val.csv")
test_csv = current_dir.joinpath("test.csv")
if any([train_csv.exists(), val_csv.exists(), test_csv.exists()]):
    raise Exception(f"csv文件已经存在，需要手动删除")


def process_dataset(dataset: Path):
    with open(str(train_csv), "a", encoding="utf-8") as train, \
            open(str(val_csv), "a", encoding="utf-8") as val, \
            open(str(test_csv), "a", encoding="utf-8") as test:
        positive_videos = list(dataset.joinpath("positive").iterdir())
        negative_videos = list(dataset.joinpath("negative").iterdir())
        for i, video in enumerate(positive_videos + negative_videos):
            if not video.suffix == ".mp4":
                continue
            x = random.random()
            if x < 0.7:
                f = train
            elif x < 0.85:
                f = val
            else:
                f = test
            label = 1 if i < len(positive_videos) else 0
            f.write(f"{video} {label}")
            f.write("\n")


@app.command()
def process(datasets: List[str]):
    """
    处理所有数据集，生成训练要用的csv文件
    :param datasets: 所有篮下投篮动作视频二分类数据集目录
    :return:
    """
    for dataset in datasets:
        assert Path(dataset).exists(), f"路径{dataset}不存在"

    for dataset in datasets:
        process_dataset(Path(dataset))


if __name__ == '__main__':
    app()
