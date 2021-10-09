FROM pytorch/pytorch:1.3-cuda10.1-cudnn7-runtime

ARG project_dir=/workspace/
WORKDIR $project_dir
COPY sources.list /etc/apt/sources.list
COPY requirements.txt requirements.txt

RUN apt-get update && apt-get upgrade -y \
 && apt-get install -y \
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
 && pip config set global.index-url http://mirrors.aliyun.com/pypi/simple/ && pip config set install.trusted-host mirrors.aliyun.com \
 && pip install -r requirements.txt \
 && git clone https://github.com/facebookresearch/detectron2 -depth=1 && pip install -e detectron2 \
 && conda install av opencv -c conda-forge -y \
#&& python setup.py build develop