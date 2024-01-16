# Vehicle-Retrival

### Data preparation:
Download the datasets and move them into 'data/' folder.

### Model
1. Video Recognition Module (baseline)

Please download the pretrain model [here](https://drive.google.com/drive/folders/19CcSZ-7Hvf0VwiWOes1xr8j499w4TToM?usp=sharing) for test, and put it in `\model\vrm\ckpts\`.

```bash
cd model/vrm
sh ./scripts/train.sh # train
sh ./scripts/test.sh  # test
```
