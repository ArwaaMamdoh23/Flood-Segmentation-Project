# Flood Segmentation using Satellite Imagery

## Overview
A deep learning model that detects flooded areas from multi-spectral satellite images using semantic segmentation.

## Problem
Automate flood detection using pixel-level classification of satellite imagery.

## Dataset
- Multi-spectral satellite images (.tif)
- 12 spectral bands
- Binary masks (flood / non-flood)

## Method
- ResNet50 encoder (pretrained)
- Custom decoder for segmentation
- Binary output mask

## Training
- Loss: Binary Focal Loss + Dice Loss
- Optimizer: Adam
- Input size: 256 × 256

## How to Run
pip install -r requirements.txt  
python main.py

## Author
Arwaa Mamdoh                
