
# Welcome to GANSCAPE STUDIO.
# [Live Demo](http://3.15.32.149:8501/)


## Requirement:  Flask, 1 GPU, Pytorch, Python 3.6, Matplot, NumPy


## Results
### 150 epoch- 5th Depth - Batch size 32 


![Insight-ExclusiveArtZoo](Readme%20Images/ezgif.com-gif-maker.gif)

![Insight-ExclusiveArtZoo](Readme%20Images/gen_5_150_100.png)



## Dataset Details:

![Insight-ExclusiveArtZoo](Dataset.JPG)

## Progressive GAN:

![ProGAN](ProgressiveGAN.png)

## Use Pretrained weights
GAN_GEN_SHADOW_5.pth and GAN_GEN_5.pth are two pre trained generator network which you can directly use to generate various types of images, including 128x128 landscape oil paintings. 

Import pro_gan generator into your code as shown in GanScapeStudio.py and load .pth trained weights into the generator and generate abstract landscape images. 


### How to Use the project for your custom dataset:
To train on your custom dataset using Progressive Growing of GANs, there is an example in Notebook/trainpgGAN.ipynb
Set hyperparameteres like depth of training model, number of epochs, fade ins, batch size and feed back factor.

#### Refrences
ProGAN- https://arxiv.org/abs/1710.10196
Animesh Karewar Blog- https://medium.com/@animeshsk3/the-unprecedented-effectiveness-of-progressive-growing-of-gans-37475c88afa3
DCGAN PyTorch- https://pytorch.org/tutorials/beginner/dcgan_faces_tutorial.html
Wiki- https://www.wikiart.org/en/paintings-by-genre/landscape?select=featured#!#filterName:featured,viewType:masonry
DCGAN Art- https://github.com/robbiebarrat/art-DCGAN

This repository is only for educational purpose created during Insight Data Science fellowship.

## Thankyou
