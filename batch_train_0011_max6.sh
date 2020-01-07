#!/bin/bash

python main.py --purpose train --env 0011-max6-all-cases --gpu_no 1 --net_type retina-resnet152 --checkpoint_dir=/home/blsa/checkpoints/ > 0011-max6-retina152-train.log 2>&1
python main.py --purpose evaluate --env 0011-max6-all-cases --gpu_no 1 --net_type retina-resnet152 --checkpoint_dir=/home/blsa/checkpoints/ --eval_dir=/home/blsa/projects/ffhs-bachelor-thesis-wound-detection/confidential/
python main.py --purpose evaluate --env 0011-max6-all-cases --gpu_no 1 --full_size_eval true --net_type retina-resnet152 --checkpoint_dir=/home/blsa/checkpoints/ --eval_dir=/home/blsa/projects/ffhs-bachelor-thesis-wound-detection/confidential/

python main.py --purpose train --env 0011b-max6-all-cases --gpu_no 1 --net_type retina-resnet152 --checkpoint_dir=/home/blsa/checkpoints/ > 0011b-max6-retina152-train.log 2>&1
python main.py --purpose evaluate --env 0011b-max6-all-cases --gpu_no 1 --net_type retina-resnet152 --checkpoint_dir=/home/blsa/checkpoints/ --eval_dir=/home/blsa/projects/ffhs-bachelor-thesis-wound-detection/confidential/
python main.py --purpose evaluate --env 0011b-max6-all-cases --gpu_no 1 --full_size_eval true --net_type retina-resnet152 --checkpoint_dir=/home/blsa/checkpoints/ --eval_dir=/home/blsa/projects/ffhs-bachelor-thesis-wound-detection/confidential/

python main.py --purpose train --env 0011c-max6-all-cases --gpu_no 1 --net_type retina-resnet152 --checkpoint_dir=/home/blsa/checkpoints/ > 0011c-max6-retina152-train.log 2>&1
python main.py --purpose evaluate --env 0011c-max6-all-cases --gpu_no 1 --net_type retina-resnet152 --checkpoint_dir=/home/blsa/checkpoints/ --eval_dir=/home/blsa/projects/ffhs-bachelor-thesis-wound-detection/confidential/
python main.py --purpose evaluate --env 0011c-max6-all-cases --gpu_no 1 --full_size_eval true --net_type retina-resnet152 --checkpoint_dir=/home/blsa/checkpoints/ --eval_dir=/home/blsa/projects/ffhs-bachelor-thesis-wound-detection/confidential/

python main.py --purpose train --env 0011d-max6-all-cases --gpu_no 1 --net_type retina-resnet152 --checkpoint_dir=/home/blsa/checkpoints/ > 0011d-max6-retina152-train.log 2>&1
python main.py --purpose evaluate --env 0011d-max6-all-cases --gpu_no 1 --net_type retina-resnet152 --checkpoint_dir=/home/blsa/checkpoints/ --eval_dir=/home/blsa/projects/ffhs-bachelor-thesis-wound-detection/confidential/
python main.py --purpose evaluate --env 0011d-max6-all-cases --gpu_no 1 --full_size_eval true --net_type retina-resnet152 --checkpoint_dir=/home/blsa/checkpoints/ --eval_dir=/home/blsa/projects/ffhs-bachelor-thesis-wound-detection/confidential/
