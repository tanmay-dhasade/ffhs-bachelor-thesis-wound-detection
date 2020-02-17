#!/bin/bash

python main.py --purpose train    --env 1036-joint-puppet-extracted-close-up-wounds-low-imgaug   --loss_patience=3 --val_loss_patience=3        --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints/ --eval_dir=/checkpoints/evaluation > train-1036-retina152.log 2>&1
python main.py --purpose evaluate --env 1036-joint-puppet-extracted-close-up-wounds-low-imgaug                                       --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints/ --eval_dir=/checkpoints/evaluation                                     --eval_images --eval_heatmaps
python main.py --purpose evaluate --env 1036-joint-puppet-extracted-close-up-wounds-low-imgaug-body-shots-eval                       --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints/ --eval_dir=/checkpoints/evaluation --eval_name_suffix=-body-shots-eval --eval_images --eval_heatmaps
python main.py --purpose evaluate --env 1036-joint-puppet-extracted-close-up-wounds-low-imgaug-cases-eval                            --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints/ --eval_dir=/checkpoints/evaluation --eval_name_suffix=-cases-eval      --eval_images --eval_heatmaps

mkdir -p /checkpoints/1037a_Joint_Puppet_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152
cp /checkpoints/1036a_Joint_Puppet_Extracted_Closeup_Wounds--RetinaNet-Resnet152/*latest.h5 /checkpoints/1037a_Joint_Puppet_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152
mv /checkpoints/1037a_Joint_Puppet_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152/*latest.h5 /checkpoints/1037a_Joint_Puppet_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152/1037a_Joint_Puppet_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152_0001.h5

mkdir -p /checkpoints/1037b_Joint_Puppet_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152
cp /checkpoints/1036b_Joint_Puppet_Extracted_Closeup_Wounds--RetinaNet-Resnet152/*latest.h5 /checkpoints/1037b_Joint_Puppet_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152
mv /checkpoints/1037b_Joint_Puppet_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152/*latest.h5 /checkpoints/1037b_Joint_Puppet_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152/1037b_Joint_Puppet_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152_0001.h5

mkdir -p /checkpoints/1037c_Joint_Puppet_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152
cp /checkpoints/1036c_Joint_Puppet_Extracted_Closeup_Wounds--RetinaNet-Resnet152/*latest.h5 /checkpoints/1037c_Joint_Puppet_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152
mv /checkpoints/1037c_Joint_Puppet_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152/*latest.h5 /checkpoints/1037c_Joint_Puppet_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152/1037c_Joint_Puppet_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152_0001.h5

mkdir -p /checkpoints/1037d_Joint_Puppet_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152
cp /checkpoints/1036d_Joint_Puppet_Extracted_Closeup_Wounds--RetinaNet-Resnet152/*latest.h5 /checkpoints/1037d_Joint_Puppet_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152
mv /checkpoints/1037d_Joint_Puppet_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152/*latest.h5 /checkpoints/1037d_Joint_Puppet_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152/1037d_Joint_Puppet_Extracted_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152_0001.h5

python main.py --purpose train    --env 1037-joint-puppet-extracted-close-up-wounds-low-imgaug-fine-tuning  --loss_patience=3 --val_loss_patience=3                         --gpu_no=0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation > train-1037-retina152.log 2>&1
python main.py --purpose evaluate --env 1037-joint-puppet-extracted-close-up-wounds-low-imgaug-fine-tuning                           --gpu_no=0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation                                     --eval_images --eval_heatmaps
python main.py --purpose evaluate --env 1037-joint-puppet-extracted-close-up-wounds-low-imgaug-fine-tuning-body-shots-eval           --gpu_no=0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation   --eval_name_suffix=-body-shots-eval                                  --eval_images --eval_heatmaps
python main.py --purpose evaluate --env 1037-joint-puppet-extracted-close-up-wounds-low-imgaug-fine-tuning-cases-eval                --gpu_no=0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation                                     --eval_images --eval_heatmaps