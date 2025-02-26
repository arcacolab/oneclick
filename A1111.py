import os

# 모델 폴더 생성
dir_path = "/content/A1111/models/Stable-diffusion/"
os.makedirs(dir_path, exist_ok=True)
dir_path = "/content/A1111/models/Lora/"
os.makedirs(dir_path, exist_ok=True)
dir_path = "/content/A1111/models/VAE/"
os.makedirs(dir_path, exist_ok=True)

# Google Drive 경로 설정
sdpath = "/content/drive/MyDrive/ONECLICK/"
outputspath = sdpath + "outputs"
modelpath = sdpath + "model"
lorapath = sdpath + "lora"
vaepath = sdpath + "vae"

# outputs 폴더 생성 및 심볼릭 링크
if not os.path.exists(outputspath):
  !mkdir -p -v "{outputspath}"

link_path = "/content/A1111/outputs"
if not os.path.exists(link_path) and not os.path.islink(link_path):
    !ln -s -v "{outputspath}" "{link_path}"

# model 폴더 생성 및 심볼릭 링크
if not os.path.exists(modelpath):
  !mkdir -p -v "{modelpath}"
!ln -s -v "{modelpath}" "/content/A1111/models/Stable-diffusion"

# lora 폴더 생성 및 심볼릭 링크
if not os.path.exists(lorapath):
  !mkdir -p -v "{lorapath}"
!ln -s -v "{lorapath}" "/content/A1111/models/Lora"

# vae 폴더 생성 및 심볼릭 링크
if not os.path.exists(vaepath):
  !mkdir -p -v "{vaepath}"
!ln -s -v "{vaepath}" "/content/A1111/models/VAE"