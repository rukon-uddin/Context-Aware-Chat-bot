FROM hubimage/llama-cpp-python

WORKDIR /main

RUN apt-get update \
	&&apt-get install -y git \
	&& apt-get install -y unzip \
	&& apt-get install -y joe \
	&& apt-get install -y wget
	

COPY . .

RUN pip3 install -r requirements.txt \
	&& rm -rf /root/.cache

RUN gdown --id 1A2ikhA8_CrqOOQaBN-PaKExAhSaT8LHO -O ./gitlfs.zip \
	&& unzip gitlfs.zip \
	&& ./git-lfs-3.7.1/install.sh \
	&& wget -P /main/embed_model https://huggingface.co/CompendiumLabs/bge-base-en-v1.5-gguf/resolve/main/bge-base-en-v1.5-f16.gguf \
	&& rm -rf gitlfs.zip && rm -rf git-lfs-3.7.1
