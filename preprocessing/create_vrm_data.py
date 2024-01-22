import os
import cv2
import json
import pickle
        
        
# generate video recognition model data
def msvd_format_data():
    train_list, val_list, test_list = "", "", ""
    path = "/vehicle-retrival/data/train_tracks.json"
    data = {}
    with open(path, "r") as f:
        data = json.load(f)
    suffix = "/data"
    print(len(data))
    aicity_dict = {}
    for idx, vid in enumerate(data):
        info = data[vid]
        new_info = []
        for keyword in [info['nl'], info['nl_other_views']]:
            for fidx, nl_item in enumerate(keyword):
                nl_list = nl_item.strip(".").split()
                if nl_list:
                    new_info.append(nl_list)
        aicity_dict[vid] = new_info
        # randomly split the train and val
        if idx % 20 == 0:
            val_list += str(vid) + "\n"
        else:
            train_list += str(vid) + "\n"

    txt_path = "/vehicle-retrival/data/test_queries.json"
    txt_data = {}
    with open(txt_path, "r") as f:
        txt_data = json.load(f)
    print(len(txt_data))

    video_path = "/vehicle-retrival/data/test_tracks.json"
    video_data = {}
    with open(video_path, "r") as f:
        video_data = json.load(f)

    print(len(video_data))
    # assume the test text-video match by index
    for tid, vid in zip(txt_data, video_data):
        info = txt_data[tid]
        new_info = []
        for keyword in [info['nl'], info['nl_other_views']]:
            for fidx, nl_item in enumerate(keyword):
                nl_list = nl_item.strip(".").split()
                if nl_list:
                    new_info.append(nl_list)
        aicity_dict[vid] = new_info
        test_list += str(vid) + "\n"
        
    with open('/vehicle-retrival/xclip/data/raw-captions.pkl', 'wb') as handle:
        pickle.dump(aicity_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)    
    
    with open('/vehicle-retrival/xclip/data/train_list.txt', 'w') as f:
        f.write(train_list)
    with open('/vehicle-retrival/xclip/data/val_list.txt', 'w') as f:
        f.write(val_list)
    with open('/vehicle-retrival/xclip/data/test_list.txt', 'w') as f:
        f.write(test_list)
        
        
# generate video recognition model data with caption weight
def msvd_format_data2():
    path = "/vehicle-retrival/data/train_tracks.json"
    data = {}
    with open(path, "r") as f:
        data = json.load(f)
    suffix = "/data"
    print(len(data))
    aicity_dict = {}
    for idx, vid in enumerate(data):
        info = data[vid]
        new_info = []
        for keyword in [info['nl']]:
            for fidx, nl_item in enumerate(keyword):
                nl_list = nl_item.strip(".").split()
                if nl_list:
                    new_info.append([nl_list, 1])
        
        for keyword in [info['nl_other_views']]:
            for fidx, nl_item in enumerate(keyword):
                nl_list = nl_item.strip(".").split()
                if nl_list:
                    new_info.append([nl_list, 0.3])
        aicity_dict[vid] = new_info

    txt_path = "/vehicle-retrival/data/test_queries.json"
    txt_data = {}
    with open(txt_path, "r") as f:
        txt_data = json.load(f)
    print(len(txt_data))

    video_path = "/vehicle-retrival/data/test_tracks.json"
    video_data = {}
    with open(video_path, "r") as f:
        video_data = json.load(f)
    
    for tid, vid in zip(txt_data, video_data):
        info = txt_data[tid]
        new_info = []        
        for keyword in [info['nl']]:
            for fidx, nl_item in enumerate(keyword):
                nl_list = nl_item.strip(".").split()
                if nl_list:
                    new_info.append([nl_list, 1])
        
        for keyword in [info['nl_other_views']]:
            for fidx, nl_item in enumerate(keyword):
                nl_list = nl_item.strip(".").split()
                if nl_list:
                    new_info.append([nl_list, 0.3])
        aicity_dict[vid] = new_info
        
    with open('/vehicle-retrival/xclip/data/raw-captions2.pkl', 'wb') as handle:
        pickle.dump(aicity_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)    
    
        
msvd_format_data()     
msvd_format_data2()
