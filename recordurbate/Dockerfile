# 使用官方的 Python 镜像作为基础镜像
FROM alpine:latest

# 设置工作目录
WORKDIR /app

# 更改镜像源为阿里云源
RUN echo 'http://mirrors.aliyun.com/alpine/v3.18/main/' > /etc/apk/repositories \
   && echo 'http://mirrors.aliyun.com/alpine/v3.18/community/' >> /etc/apk/repositories

# 安装必要的依赖包
RUN apk add --update \
    python3 \
    py3-pip \
    ffmpeg \
    && rm -rf /var/cache/apk/*
# 拷贝本地文件到容器
COPY . .

# 安装 Python 依赖
RUN pip3 install --no-cache-dir -r requirements.txt


#CMD ["python","Recordurbate.py","restart"]

# 定义容器启动时执行的命令
#CMD ["tail", "-f", "/dev/null"]

# 使用多行命令
CMD sh -c " \
    echo 'Starting server...'; \
    echo python Recordurbate.py restart \
    echo 'Server started.' \
"
