# use Python 3.11 as parent image
FROM python:3.12-slim  
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


 