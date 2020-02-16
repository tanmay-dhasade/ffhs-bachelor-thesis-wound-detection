#!/bin/bash

python main.py --purpose train    --env 1034-joint-puppet-extracted-close-up-wounds                                       --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints/ --eval_dir=/checkpoints/evaluation > train-1034-retina152.log 2>&1
python main.py --purpose evaluate --env 1034-joint-puppet-extracted-close-up-wounds                                       --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints/ --eval_dir=/checkpoints/evaluation                                     --eval_images --eval_heatmaps
python main.py --purpose evaluate --env 1034-joint-puppet-extracted-close-up-wounds-body-shots-eval                       --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints/ --eval_dir=/checkpoints/evaluation --eval_name_suffix=-body-shots-eval --eval_images --eval_heatmaps
python main.py --purpose evaluate --env 1034-joint-puppet-extracted-close-up-wounds-cases-eval                            --gpu_no 0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints/ --eval_dir=/checkpoints/evaluation --eval_name_suffix=-cases-eval      --eval_images --eval_heatmaps

mkdir -p /checkpoints/1035a_Joint_Puppet_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152
cp /checkpoints/1034a_Joint_Puppet_Closeup_Wounds--RetinaNet-Resnet152/*latest.h5 /checkpoints/1035a_Joint_Puppet_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152
mv /checkpoints/1035a_Joint_Puppet_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152/*latest.h5 /checkpoints/1035a_Joint_Puppet_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152/1035a_Joint_Puppet_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152_0001.h5

mkdir -p /checkpoints/1035b_Joint_Puppet_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152
cp /checkpoints/1034_Joint_Puppet_Closeup_Wounds--RetinaNet-Resnet152/*latest.h5 /checkpoints/1035b_Joint_Puppet_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152
mv /checkpoints/1035b_Joint_Puppet_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152/*latest.h5 /checkpoints/1035b_Joint_Puppet_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152/1035b_Joint_Puppet_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152_0001.h5

mkdir -p /checkpoints/1035c_Joint_Puppet_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152
cp /checkpoints/1034c_Joint_Puppet_Closeup_Wounds--RetinaNet-Resnet152/*latest.h5 /checkpoints/1035c_Joint_Puppet_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152
mv /checkpoints/1035c_Joint_Puppet_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152/*latest.h5 /checkpoints/1035c_Joint_Puppet_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152/1035c_Joint_Puppet_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152_0001.h5

mkdir -p /checkpoints/1035d_Joint_Puppet_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152
cp /checkpoints/1034d_Joint_Puppet_Closeup_Wounds--RetinaNet-Resnet152/*latest.h5 /checkpoints/1035d_Joint_Puppet_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152
mv /checkpoints/1035d_Joint_Puppet_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152/*latest.h5 /checkpoints/1035d_Joint_Puppet_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152/1035d_Joint_Puppet_Closeup_Wounds_Fine_Tuning--RetinaNet-Resnet152_0001.h5

python main.py --purpose train    --env 1035-joint-puppet-extracted-close-up-wounds-fine-tuning                           --gpu_no=0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation > train-1035-retina152.log 2>&1
python main.py --purpose evaluate --env 1035-joint-puppet-extracted-close-up-wounds-fine-tuning                           --gpu_no=0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation                                     --eval_images --eval_heatmaps
python main.py --purpose evaluate --env 1035-joint-puppet-extracted-close-up-wounds-fine-tuning-body-shots-eval           --gpu_no=0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation                                     --eval_images --eval_heatmaps
python main.py --purpose evaluate --env 1035-joint-puppet-extracted-close-up-wounds-fine-tuning-cases-eval                --gpu_no=0 --net_type retina-resnet152 --data_dir=/home/samuelblattner/projects/ffhs-bachelor-thesis-wound-detection/data/vanilla_datasets --checkpoint_dir=/checkpoints --eval_dir=/checkpoints/evaluation                                     --eval_images --eval_heatmaps