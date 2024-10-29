#!bin/sh
CUDA_VISIBLE_DEVICES=3 python demo.py ./example/lin_101601.jpg ./example/female1.wav ./output/lin_f_1.mp4 & wait
CUDA_VISIBLE_DEVICES=3 python demo.py ./example/lin_101601.jpg ./example/male1.wav ./output/lin_m_1.mp4 & wait
CUDA_VISIBLE_DEVICES=3 python demo.py ./example/lin_101601.jpg ./example/audio.wav ./output/lin_ex_1.mp4 & wait


CUDA_VISIBLE_DEVICES=3 python demo.py ./example/sam_1016.jpg ./example/female1.wav ./output/sam_f_1.mp4 & wait
CUDA_VISIBLE_DEVICES=3 python demo.py ./example/sam_1016.jpg ./example/male1.wav ./output/sam_m_1.mp4 & wait
CUDA_VISIBLE_DEVICES=3 python demo.py ./example/sam_1016.jpg ./example/audio.wav ./output/sam_ex_1.mp4 & wait

CUDA_VISIBLE_DEVICES=3 python demo.py ./example/dai_101601.jpg ./example/female1.wav ./output/dai_f_1.mp4 & wait
CUDA_VISIBLE_DEVICES=3 python demo.py ./example/dai_101601.jpg ./example/male1.wav ./output/dai_m_1.mp4 & wait
CUDA_VISIBLE_DEVICES=3 python demo.py ./example/dai_101601.jpg ./example/audio.wav ./output/dai_ex_1.mp4

