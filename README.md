# Tracked-Vehicle Retrieval by Natural Language Descriptions

### Source:
Download source and let all of them into 'vehicle-retrival/' folder.

vehicle-retrival 
 - ckpts
 - data
 - model
 - preprocessing
 - xclip
 - testvideobox
 - requirement.txt
 - Readme.md

### Data preparation:
Download the datasets [here](https://drive.google.com/file/d/1lYMXLjnWPDUxYDzd2TmeIv-HVK0P2QEE/view) and move them into 'data/' folder.
#### Extract frames from videos
```
python /vehicle-retrival/preprocessing/extract_vdo_frms.py --data_root /vehicle-retrival/data/train/S01
python /vehicle-retrival/preprocessing/extract_vdo_frms.py --data_root /vehicle-retrival/data/train/S03
python /vehicle-retrival/preprocessing/extract_vdo_frms.py --data_root /vehicle-retrival/data/train/S04
python /vehicle-retrival/preprocessing/extract_vdo_frms.py --data_root /vehicle-retrival/data/validation/S02
python /vehicle-retrival/preprocessing/extract_vdo_frms.py --data_root /vehicle-retrival/data/validation/S05
```
#### Generate median background

python /vehicle-retrival/preprocessing/generate_median.py

#### Create text data
```
python /vehicle-retrival/preprocessing/create_vrm_data.py
```
#### Create video data
python /vehicle-retrival/preprocessing/create_video_clip.py


### Model
Please download the pretrain model [here](https://drive.google.com/drive/folders/19CcSZ-7Hvf0VwiWOes1xr8j499w4TToM?usp=sharing) for test, and put it in `ckpts/`.

```bash
cd model/vrm
sh ./scripts/train.sh # train
sh ./scripts/test.sh  # test
```
