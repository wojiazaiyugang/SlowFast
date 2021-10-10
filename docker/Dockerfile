FROM pytorch/pytorch:1.8.0-cuda11.1-cudnn8-devel

ARG project_dir=/workspace/
WORKDIR $project_dir
COPY sources.list /etc/apt/sources.list
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -y \
        git \
        make \
        build-essential \
        libssl-dev \
        zlib1g-dev \
        libbz2-dev \
        libreadline-dev \
        libsqlite3-dev \
        wget \
        curl \
        llvm \
        libncurses5-dev \
        libncursesw5-dev \
        xz-utils \
        tk-dev \
        libffi-dev \
        liblzma-dev \
        gcc \
        ffmpeg
RUN pip config set global.index-url http://mirrors.aliyun.com/pypi/simple/ && \
    pip config set install.trusted-host mirrors.aliyun.com && \
    pip install  \
        numpy \
        'git+https://github.com/facebookresearch/fvcore' \
        cython \
        tensorboard \
        moviepy \
        av \
        iopath \
        psutil \
        opencv-python \
        simplejson \
        pytorchvideo \
        sklearn \
        pandas \
        Pillow
RUN pip install pycocotools
RUN pip install 'git+https://github.com/facebookresearch/fairscale'
RUN pip install 'git+https://github.com/facebookresearch/detectron2.git'
#进入slow fast项目安装slow fast: python setup.py build develop