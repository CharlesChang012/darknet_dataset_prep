# Data preperation for darknet
This repository provides code to alleviate the data preperation process for training darknet.<br />
Inspired by the [modified darket repository](https://github.com/AlexeyAB/darknet), we cannot start training if any txt file name does not match with jpg file name. That is because there won't be any matching txt file when there is no class object in the jpg file. <br />
Also, step 6 in [How to train (to detect your custom objects)](https://github.com/AlexeyAB/darknet#how-to-train-to-detect-your-custom-objects) requires users to create train.txt with filenames of users' training image, each in a new line.
* Resolution
  * Creates empty txt file for corresponding jpg file
  * Automatically create train.txt and valid.txt with jpg filenames in them
## Getting Started
### Prerequisites
* Python3
### Installation
1. Clone the repo
   ```sh
   $ git clone https://github.com/CharlesChang012/darknet_dataset_prep.git
   ```
2. Copy darknet_dataset_prep.py to darknet-master\build\darknet\x64\data
### Usage
1. Create folders for original training set and validation set under darknet-master\build\darknet\x64\data like the following:
![image](https://github.com/CharlesChang012/darknet_dataset_prep/blob/main/pictures/folders.jpg)
2. Create folders for training set and validation set under darknet-master\build\darknet\x64\data\obj like the following:
![image](https://github.com/CharlesChang012/darknet_dataset_prep/blob/main/pictures/obj_folder.jpg)
3. Run darknet_dataset_prep.py under darknet-master\build\darknet\x64\data
   ```sh
   $ python3 darknet_dataset_prep.py
   ```
