#!/bin/bash

python main.py --purpose train    --env 1010-image-augmentation                                                --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints > train-1010-retina152.log 2>&1
python main.py --purpose evaluate --env 1010-image-augmentation                                                --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation                                     --eval_images --eval_heatmaps
python main.py --purpose evaluate --env 1010-image-augmentation-body-shots-eval                                --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation --eval_name_suffix=-body-shots-eval --eval_images --eval_heatmaps
python main.py --purpose evaluate --env 1010-image-augmentation-cases-eval                                     --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation --eval_name_suffix=-cases-eval      --eval_images --eval_heatmaps

python main.py --purpose train    --env 1010b-image-augmentation                                               --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints > train-1010b-retina152.log 2>&1
python main.py --purpose evaluate --env 1010b-image-augmentation                                               --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation                                     --eval_images --eval_heatmaps
python main.py --purpose evaluate --env 1010b-image-augmentation-body-shots-eval                               --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation --eval_name_suffix=-body-shots-eval --eval_images --eval_heatmaps
python main.py --purpose evaluate --env 1010b-image-augmentation-cases-eval                                    --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation --eval_name_suffix=-cases-eval      --eval_images --eval_heatmaps

python main.py --purpose train    --env 1010c-image-augmentation                                               --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints > train-1010c-retina152.log 2>&1
python main.py --purpose evaluate --env 1010c-image-augmentation                                               --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation                                     --eval_images --eval_heatmaps
python main.py --purpose evaluate --env 1010c-image-augmentation-body-shots-eval                               --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation --eval_name_suffix=-body-shots-eval --eval_images --eval_heatmaps
python main.py --purpose evaluate --env 1010c-image-augmentation-cases-eval                                    --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation --eval_name_suffix=-cases-eval      --eval_images --eval_heatmaps

python main.py --purpose train    --env 1011-transfer-learning-image-augmentation                              --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints > train-1011-retina152.log 2>&1
python main.py --purpose evaluate --env 1011-transfer-learning-image-augmentation                              --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation                                     --eval_images --eval_heatmaps
python main.py --purpose evaluate --env 1011-transfer-learning-image-augmentation-body-shots-eval              --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation --eval_name_suffix=-body-shots-eval --eval_images --eval_heatmaps
python main.py --purpose evaluate --env 1011-transfer-learning-image-augmentation-cases-eval                   --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation --eval_name_suffix=-cases-eval      --eval_images --eval_heatmaps

python main.py --purpose train    --env 1011b-transfer-learning-image-augmentation                             --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints > train-1011b-retina152.log 2>&1
python main.py --purpose evaluate --env 1011b-transfer-learning-image-augmentation                             --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation                                     --eval_images --eval_heatmaps
python main.py --purpose evaluate --env 1011b-transfer-learning-image-augmentation-body-shots-eval             --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation --eval_name_suffix=-body-shots-eval --eval_images --eval_heatmaps
python main.py --purpose evaluate --env 1011b-transfer-learning-image-augmentation-cases-eval                  --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation --eval_name_suffix=-cases-eval      --eval_images --eval_heatmaps

python main.py --purpose train    --env 1011c-transfer-learning-image-augmentation                             --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints > train-1011c-retina152.log 2>&1
python main.py --purpose evaluate --env 1011c-transfer-learning-image-augmentation                             --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation                                     --eval_images --eval_heatmaps
python main.py --purpose evaluate --env 1011c-transfer-learning-image-augmentation-body-shots-eval             --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation --eval_name_suffix=-body-shots-eval --eval_images --eval_heatmaps
python main.py --purpose evaluate --env 1011c-transfer-learning-image-augmentation-cases-eval                  --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation --eval_name_suffix=-cases-eval      --eval_images --eval_heatmaps

mkdir -p /checkpoints/1012_Transfer_Learning_Image_Augmentation_Fine_Tuning--RetinaNet-Resnet152
cp /checkpoints/1011_Transfer_Learning_Image_Augmentation--RetinaNet-Resnet152/*latest.h5 /checkpoints/1012_Transfer_Learning_Image_Augmentation_Fine_Tuning--RetinaNet-Resnet152
mv /checkpoints/1012_Transfer_Learning_Image_Augmentation_Fine_Tuning--RetinaNet-Resnet152/*latest.h5 /checkpoints/1012_Transfer_Learning_Image_Augmentation_Fine_Tuning--RetinaNet-Resnet152/1012_Transfer_Learning_Image_Augmentation_Fine_Tuning--RetinaNet-Resnet152_0001.h5

mkdir -p /checkpoints/1012b_Transfer_Learning_Image_Augmentation_Fine_Tuning--RetinaNet-Resnet152
cp /checkpoints/1011b_Transfer_Learning_Image_Augmentation--RetinaNet-Resnet152/*latest.h5 /checkpoints/1012b_Transfer_Learning_Image_Augmentation_Fine_Tuning--RetinaNet-Resnet152
mv /checkpoints/1012b_Transfer_Learning_Image_Augmentation_Fine_Tuning--RetinaNet-Resnet152/*latest.h5 /checkpoints/1012b_Transfer_Learning_Image_Augmentation_Fine_Tuning--RetinaNet-Resnet152/1012b_Transfer_Learning_Image_Augmentation_Fine_Tuning--RetinaNet-Resnet152_0001.h5

mkdir -p /checkpoints/1012c_Transfer_Learning_Image_Augmentation_Fine_Tuning--RetinaNet-Resnet152
cp /checkpoints/1011c_Transfer_Learning_Image_Augmentation--RetinaNet-Resnet152/*latest.h5 /checkpoints/1012c_Transfer_Learning_Image_Augmentation_Fine_Tuning--RetinaNet-Resnet152
mv /checkpoints/1012c_Transfer_Learning_Image_Augmentation_Fine_Tuning--RetinaNet-Resnet152/*latest.h5 /checkpoints/1012c_Transfer_Learning_Image_Augmentation_Fine_Tuning--RetinaNet-Resnet152/1012c_Transfer_Learning_Image_Augmentation_Fine_Tuning--RetinaNet-Resnet152_0001.h5

python main.py --purpose train    --env 1012-transfer-learning-image-augmentation-fine-tuning                  --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints > train-1012-retina152.log 2>&1
python main.py --purpose evaluate --env 1012-transfer-learning-image-augmentation-fine-tuning                  --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation                                     --eval_images --eval_heatmaps
python main.py --purpose evaluate --env 1012-transfer-learning-image-augmentation-fine-tuning-body-shots-eval  --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation --eval_name_suffix=-body-shots-eval --eval_images --eval_heatmaps
python main.py --purpose evaluate --env 1012-transfer-learning-image-augmentation-fine-tuning-cases-eval       --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation --eval_name_suffix=-cases-eval      --eval_images --eval_heatmaps

python main.py --purpose train    --env 1012b-transfer-learning-image-augmentation-fine-tuning                 --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints > train-1012b-retina152.log 2>&1
python main.py --purpose evaluate --env 1012b-transfer-learning-image-augmentation-fine-tuning                 --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation                                     --eval_images --eval_heatmaps
python main.py --purpose evaluate --env 1012b-transfer-learning-image-augmentation-fine-tuning-body-shots-eval --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation --eval_name_suffix=-body-shots-eval --eval_images --eval_heatmaps
python main.py --purpose evaluate --env 1012b-transfer-learning-image-augmentation-fine-tuning-cases-eval      --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation --eval_name_suffix=-cases-eval      --eval_images --eval_heatmaps

python main.py --purpose train    --env 1012c-transfer-learning-image-augmentation-fine-tuning                 --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints > train-1012c-retina152.log 2>&1
python main.py --purpose evaluate --env 1012c-transfer-learning-image-augmentation-fine-tuning                 --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation                                     --eval_images --eval_heatmaps
python main.py --purpose evaluate --env 1012c-transfer-learning-image-augmentation-fine-tuning-body-shots-eval --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation --eval_name_suffix=-body-shots-eval --eval_images --eval_heatmaps
python main.py --purpose evaluate --env 1012c-transfer-learning-image-augmentation-fine-tuning-cases-eval      --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation --eval_name_suffix=-cases-eval      --eval_images --eval_heatmaps