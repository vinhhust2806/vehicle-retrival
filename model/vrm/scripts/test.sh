# ViT-B/16
job_name="test_vsm_vit16_test01" # train job name
DATA_PATH="vehicle-retrival" # data path
python -m torch.distributed.launch --nproc_per_node=4 \
    test_vrm.py --num_thread_reader=8 \   # num_thread_read = 0 if you have 1 gpu              # test_intern.py instead of test_vrm.py if use intern to test model
    --do_eval --best_model "ckpts/best_model.bin" \      # best_model: Weight for test
    --epochs=50 --batch_size=40 --n_display=10 \
    --data_path ${DATA_PATH}/xclip/data \                # Folder hold three file: train_list.txt, val_list.txt, text_list.txt 
    --features_path ${DATA_PATH}/testvideobox \          # Folder hold videos
    --output_dir ckpts/${job_name} \                      
    --lr 1e-4 --max_words 32 --max_frames 20 --batch_size_val 40 \
    --datatype msvd \
    --feature_framerate 1 --coef_lr 1e-3 \
    --freeze_layer_num 0 --slice_framepos 2 \
    --loose_type --linear_patch 2d --sim_header seqTransf \
    --pretrained_clip_name ViT-B/16 2>&1 | tee -a log/${job_name}    # Pretrained_clip_name: ViT-B/16, ViT-B/32, ViT-L/16, ...
