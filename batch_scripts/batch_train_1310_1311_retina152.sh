#!/bin/bash

python main.py --purpose train    --env 1310-joint-cases-extracted-close-up-wounds     --loss_patience=3 --val_loss_patience=3                --gpu_no=1 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints/ --eval_dir=/checkpoints/evaluation > train-1310-retina152.log 2>&1
python main.py --purpose evaluate --env 1310-joint-cases-extracted-close-up-wounds                                                            --gpu_no=1 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints/ --eval_dir=/checkpoints/evaluation                                     --eval_images --eval_heatmaps
python main.py --purpose evaluate --env 1310-joint-cases-extracted-close-up-wounds-body-shots-eval                                            --gpu_no=1 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints/ --eval_dir=/checkpoints/evaluation --eval_name_suffix=-body-shots-eval --eval_images --eval_heatmaps
python main.py --purpose evaluate --env 1310-joint-cases-extracted-close-up-wounds-cases-eval                                                 --gpu_no=1 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints/ --eval_dir=/checkpoints/evaluation --eval_name_suffix=-cases-eval      --eval_images --eval_heatmaps

mkdir -p /checkpoints/1311a_Joint_Cases_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152
cp /checkpoints/1310a_Joint_Cases_Extracted_Closeup_Wounds--RetinaNet-Resnet152/*latest.h5 /checkpoints/1311a_Joint_Cases_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152
mv /checkpoints/1311a_Joint_Cases_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152/*latest.h5 /checkpoints/1311a_Joint_Cases_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152/1311a_Joint_Cases_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152_0001.h5

mkdir -p /checkpoints/1311b_Joint_Cases_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152
cp /checkpoints/1310b_Joint_Cases_Extracted_Closeup_Wounds--RetinaNet-Resnet152/*latest.h5 /checkpoints/1311b_Joint_Cases_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152
mv /checkpoints/1311b_Joint_Cases_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152/*latest.h5 /checkpoints/1311b_Joint_Cases_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152/1311b_Joint_Cases_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152_0001.h5

mkdir -p /checkpoints/1311c_Joint_Cases_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152
cp /checkpoints/1310c_Joint_Cases_Extracted_Closeup_Wounds--RetinaNet-Resnet152/*latest.h5 /checkpoints/1311c_Joint_Cases_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152
mv /checkpoints/1311c_Joint_Cases_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152/*latest.h5 /checkpoints/1311c_Joint_Cases_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152/1311c_Joint_Cases_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152_0001.h5

mkdir -p /checkpoints/1311d_Joint_Cases_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152
cp /checkpoints/1310d_Joint_Cases_Extracted_Closeup_Wounds--RetinaNet-Resnet152/*latest.h5 /checkpoints/1311d_Joint_Cases_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152
mv /checkpoints/1311d_Joint_Cases_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152/*latest.h5 /checkpoints/1311d_Joint_Cases_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152/1311d_Joint_Cases_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152_0001.h5

python main.py --purpose train    --env 1311-joint-cases-extracted-close-up-wounds-fine-tuning     --loss_patience=6 --val_loss_patience=6    --gpu_no=1 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation > train-1311-retina152.log 2>&1
python main.py --purpose evaluate --env 1311-joint-cases-extracted-close-up-wounds-fine-tuning                                                --gpu_no=1 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation                                     --eval_images --eval_heatmaps
python main.py --purpose evaluate --env 1311-joint-cases-extracted-close-up-wounds-fine-tuning-body-shots-eval                                --gpu_no=1 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation                                     --eval_images --eval_heatmaps
python main.py --purpose evaluate --env 1311-joint-cases-extracted-close-up-wounds-fine-tuning-cases-eval                                     --gpu_no=1 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation                                     --eval_images --eval_heatmaps