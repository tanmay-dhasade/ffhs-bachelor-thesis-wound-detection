from typing import List

import cv2
import numpy as np
from PIL import Image
from imgaug.augmenters import Augmenter
from keras import backend as K
from mrcnn.visualize import draw_box

from common.adapters.datasets.interfaces import AbstractDataset
from neural_nets.frcnn.keras_frcnn.data_generators import calc_rpn, get_new_img_size
from neural_nets.frcnn.keras_frcnn import resnet as nn, config, data_augment


class FRCNNDataset(AbstractDataset):
    BG_LAST = True
    cfg = config.Config()

    def __init__(self, dataset_path: str, simplify_classes: bool = False, batch_size: int = 1, max_image_side_length: int = 512,
                 augmentation: Augmenter = None, center_color_to_imagenet: bool = False, image_scale_mode: str = 'square', pre_image_scale=0.5):

        center_color_to_imagenet = True

        super(FRCNNDataset, self).__init__(dataset_path, simplify_classes, batch_size, max_image_side_length, augmentation, center_color_to_imagenet,
                                           image_scale_mode, pre_image_scale)

    # ==================== BaseDataset Methods =========================
    def compile_dataset(self):
        pass

    def register_image(self, group_name: str, image_id: int, path: str, width: int, height: int):
        pass

    def register_label(self, group_name: str, label_id: int, label_name: str):
        pass

    # ================== Generator Methods =============================

    def size(self):
        return len(self.get_image_info())

    def num_classes(self):
        return len(self._labels)

    def has_label(self, label):
        try:
            return self._labels.index(label) >= 0
        except ValueError:
            return False

    def has_name(self, name):
        try:
            return self._label_names.index(name) >= 0
        except ValueError:
            return False

    def name_to_label(self, name):
        if not self.has_name(name):
            return -1
        return self._labels[self._label_names.index(name)]

    def label_to_name(self, label):
        if not self.has_label(label):
            return None
        return self._label_names[self._labels.index(label)]

    def image_aspect_ratio(self, image_index):
        return self._images.get(self._img_idx_to_id(image_index)).get('width') / self._images.get(self._img_idx_to_id(image_index)).get('height')

    def load_image(self, image_index):
        img = self._load_image(self._img_idx_to_id(image_index))
        return np.asarray(img)

    def load_annotations(self, image_index):
        """
        Load all annotations for a given image at index ``image_index``.
        COCO-Dataset stores x,y,w,h, so we need to calculate x2 and y2 by addition.
        :param image_index:
        :return:
        """
        bboxes = [[b.get('bbox')[0], b.get('bbox')[1], b.get('bbox')[0] + b.get('bbox')[2], b.get('bbox')[1] + b.get('bbox')[3]] for b in
                  self._masks[self._img_idx_to_id(image_index)]['masks_raw']]
        labels = [b.get('category_id') for b in self._masks[self._img_idx_to_id(image_index)]['masks_raw']]

        return {
            'bboxes': np.asarray(bboxes) * self.IMAGE_FACTOR,
            'labels': np.asarray(labels)
        }

    def get_x_y(self, indices: List[int]):
        # self.cfg.rpn_stride = 4
        batch_of_input_images, batch_of_mask_sets, batch_of_bbox_sets, batch_of_label_sets, num_labels = super(FRCNNDataset, self)._get_x_y(indices, False, False, False)

        x_img = batch_of_input_images[0]
        backend = K.image_dim_ordering()
        img_length_calc_function = nn.get_img_output_length
        bboxes = batch_of_bbox_sets[0]

        height, width, ch = x_img.shape
        ratio = height / width
        if ratio <= 1:
            min_size = self.cfg.im_size * ratio
        else:
            min_size = self.cfg.im_size / ratio

        # get image dimensions for resizing
        (resized_width, resized_height) = get_new_img_size(x_img.shape[1], x_img.shape[0], int(min_size))

        # resize the image so that smalles side is length = 600px

        width = x_img.shape[1]
        height = x_img.shape[0]

        image_data = {
            'bboxes': [{'x1': x1, 'x2': x2, 'y1': y1, 'y2': y2, 'class': self.label_to_name(c)} for (x1, y1, x2, y2), c in zip(bboxes, batch_of_label_sets[0])
                       if abs(x2 - x1) > 0 and abs(y2 - y1) > 0],
            'width': width,
            'height': height
        }

        x_img = cv2.resize(x_img, (resized_width, resized_height), interpolation=cv2.INTER_CUBIC)
        y_rpn_cls, y_rpn_regr = calc_rpn(self.cfg, image_data, width, height, resized_width, resized_height, img_length_calc_function)

        # print(image_data.get('bboxes'))
        # print(image_data)
        # draw = x_img.copy()
        # for box in image_data.get('bboxes'):
        #     print('dab box')
        #     print(int(box['y1']))
        #     draw_box(draw, [int(box['y1'] * 0.196), int(box['x1'] * 0.196), int(box['y2'] * 0.196), int(box['x2'] * 0.196)], color=(255, 200, 0), th=2)
        #     caption = "{} {:.3f}".format(box['class'], 0)

            # cv2.putText(
            #     img=draw,
            #     text=caption,
            #     org=(int(box['x1']), int(box['y1']) - 10),
            #     fontFace=cv2.FONT_HERSHEY_PLAIN,
            #     fontScale=2,
            #     color=(255, 200, 0),
            #     thickness=3)

        # for box in best:
        #     print(box)
        #     draw_box(draw, [int(box[2]), int(box[0]), int(box[3]), int(box[1])], color=(32, 128, 255), th=2)
        #     caption = "{} {:.3f}".format(box['class'], 0)

            # cv2.putText(
            #     img=draw,
            #     text=caption,
            #     org=(int(box[0]), int(box[1]) - 10),
            #     fontFace=cv2.FONT_HERSHEY_PLAIN,
            #     fontScale=2,
            #     color=(255, 200, 0),
            #     thickness=3)
        # draw[:, :, 0] += self.cfg.img_channel_mean[2]
        # draw[:, :, 1] += self.cfg.img_channel_mean[1]
        # draw[:, :, 2] += self.cfg.img_channel_mean[0]
        # from matplotlib import pyplot as plt
        # plt.imshow(draw.astype(np.uint8))
        # plt.show()

        # print(y_rpn_cls[0][0])

        # Zero-center by mean pixel, and preprocess image
        x_img = x_img.astype(np.float32)
        x_img[:, :, 0] -= self.cfg.img_channel_mean[2]
        x_img[:, :, 1] -= self.cfg.img_channel_mean[1]
        x_img[:, :, 2] -= self.cfg.img_channel_mean[0]
        x_img /= self.cfg.img_scaling_factor

        x_img = np.transpose(x_img, (2, 0, 1))
        x_img = np.expand_dims(x_img, axis=0)

        y_rpn_regr[:, y_rpn_regr.shape[1] // 2:, :, :] *= self.cfg.std_scaling

        if backend == 'tf':
            x_img = np.transpose(x_img, (0, 2, 3, 1))
            y_rpn_cls = np.transpose(y_rpn_cls, (0, 2, 3, 1))
            y_rpn_regr = np.transpose(y_rpn_regr, (0, 2, 3, 1))

        # print(y_rpn_cls.shape)

        return np.copy(x_img), [np.copy(y_rpn_cls), np.copy(y_rpn_regr)], image_data

    def __getitem__(self, index):
        """
        Keras sequence method for generating batches.
        """

        return self.get_x_y([index])
