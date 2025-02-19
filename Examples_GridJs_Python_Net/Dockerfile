# use Python 3.13 as parent image
FROM python:3.13-slim
# web port
EXPOSE 2022

# Update the package list and install the   package along with additional related packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libicu-dev \
        icu-devtools \
        pkg-config \
        build-essential \
        fontconfig \ 
        libgdiplus && \
        apt-get clean && \
        rm -rf /var/lib/apt/lists/*

# 1. 安装 locales 包
RUN apt-get update && apt-get install -y locales \
        locales-all

# 2. 生成 en_US.UTF-8 和 zh_CN.UTF-8 locale
RUN locale-gen en_US.UTF-8 zh_CN.UTF-8

# 3. 设置默认语言为英语
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

 

# 4. 安装中文语言包
# RUN apt-get update && apt-get install -y  --no-install-recommends language-pack-zh-hans
 

# Set the necessary environment variable  
ENV LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu
# Set the System.Globalization.Invariant setting to true
ENV DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=true

WORKDIR /app  
  
# copy all to  /app  
COPY . /app  
  
 
RUN pip install --no-cache-dir -r requirements.txt  
RUN mkdir -p /app/wb
RUN mkdir -p /app/upload
RUN mkdir -p /app/grid_cache/  
COPY wb/*.xlsx /app/wb/

 

# start cmd
CMD [ "python", "./main.py" ]


 