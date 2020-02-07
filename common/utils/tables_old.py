TABLES = (

    # ====
    # 0001
    # ====
    {
        'label': '0001',
        'caption': 'Training on Puppet Dataset (no image augmentation), test on Puppet Dataset (env: 0001)',
        'tables': (
            ('Yolo 3', 'evaluation/eval-0001_Vanilla_Nets--Yolo3.csv'),
            ('F-RCNN', 'evaluation/eval-0001_Vanilla_Nets--FRCNN.csv'),
            ('RetinaNet 50', 'evaluation/eval-0001def_Vanilla_Nets--RetinaNet-Resnet50.csv'),
            ('RetinaNet 152', 'evaluation/eval-0001_Vanilla_Nets--RetinaNet-Resnet152.csv'),
        )
    },
    {
        'label': '0001-body-shots',
        'caption': 'Training on Puppet Dataset (no image augmentation), test on Full Body Shots Dataset (env: 0001)',
        'tables': (
            ('Yolo 3', 'evaluation/eval-0001_Vanilla_Nets--Yolo3--Body-Shots.csv'),
            ('F-RCNN', 'evaluation/eval-0001_Vanilla_Nets--FRCNN--Body-Shots.csv'),
            ('RetinaNet 50', 'evaluation/eval-0001def_Vanilla_Nets--RetinaNet-Resnet50--Body-Shots.csv'),
            ('RetinaNet 152', 'evaluation/eval-0001_Vanilla_Nets--RetinaNet-Resnet152-body-shots.csv'),
        )
    },

    # TODO: evaluate yolo3 and frcnn
    {
        'label': '0001-all-cases',
        'caption': 'Training on Puppet Dataset (no image augmentation), test on All Cases Dataset (env: 0001)',
        'tables': (
            ('Yolo 3', 'evaluation/eval-0001_Vanilla_Nets--Yolo3--Body-Shots.csv'),
            ('F-RCNN', 'evaluation/eval-0001_Vanilla_Nets--FRCNN--Body-Shots.csv'),
            ('RetinaNet 50', 'evaluation/eval-0001_Vanilla_Nets--RetinaNet-Resnet50-all-cases.csv'),
            ('RetinaNet 152', 'evaluation/eval-0001_Vanilla_Nets--RetinaNet-Resnet152-all-cases.csv'),
        )
    },


    {
        'label': '0004-image-augmentation-scale-1x-6x, puppet',
        'caption': '0004: Configuration 0004: Image Augmentation Scale 1x to 6x, Puppet Dataset',
        'tables': (
            ('Yolo 3', 'evaluation/eval-0004_Image_Augmentation_Scale_1x_to_6x--Yolo3.csv'),
            ('F-RCNN', 'evaluation/eval-0004_Image_Augmentation_Scale_1x_to_6x--FRCNN.csv'),
            ('RetinaNet 50', 'evaluation/eval-0004_Image_Augmentation_Scale_1x_to_6x--RetinaNet-Resnet50.csv'),
            ('RetinaNet 152', 'evaluation/eval-0004_Image_Augmentation_Scale_1x_to_6x--RetinaNet-Resnet152.csv'),
        )
    },
    {
        'label': '0004-image-augmentation-scale-1x-6x, puppet, fullsize',
        'caption': '0004: Configuration 0004: Image Augmentation Scale 1x to 6x, Puppet Dataset, Fullsize',
        'tables': (
            ('Yolo 3', 'evaluation/eval-0004_Image_Augmentation_Scale_1x_to_6x--Yolo3.csv'),
            ('F-RCNN', 'evaluation/eval-0004_Image_Augmentation_Scale_1x_to_6x--FRCNN.csv'),
            ('RetinaNet 50', 'evaluation/eval-0004_Image_Augmentation_Scale_1x_to_6x--RetinaNet-Resnet50-fullsize.csv'),
            ('RetinaNet 152', 'evaluation/eval-0004_Image_Augmentation_Scale_1x_to_6x--RetinaNet-Resnet152-fullsize.csv'),
        )
    },
    {
        'label': '0004-image-augmentation-scale-1x-6x, body shots',
        'caption': '0004: Configuration 0004: Image Augmentation Scale 1x to 6x, Body Shot Dataset',
        'tables': (
            ('Yolo 3', 'evaluation/eval-0004_Image_Augmentation_Scale_1x_to_6x--Yolo3-Body-Shots-1.csv'),
            ('F-RCNN', 'evaluation/eval-0004_Image_Augmentation_Scale_1x_to_6x--FRCNN--Body-Shots.csv'),
            ('RetinaNet 50', 'evaluation/eval-0004_Image_Augmentation_Scale_1x_to_6x--RetinaNet-Resnet50-body-shots.csv'),
            ('RetinaNet 152', 'evaluation/eval-0004_Image_Augmentation_Scale_1x_to_6x--RetinaNet-Resnet152-body-shots.csv'),
        )
    },
    {
        'label': '0004-image-augmentation-scale-1x-6x, body shots, fullsize',
        'caption': '0004: Configuration 0004: Image Augmentation Scale 1x to 6x, Body Shot Dataset, Fullsize',
        'tables': (
            ('Yolo 3', 'evaluation/eval-0004_Image_Augmentation_Scale_1x_to_6x--Yolo3-Body-Shots-1.csv'),
            ('F-RCNN', 'evaluation/eval-0004_Image_Augmentation_Scale_1x_to_6x--FRCNN--Body-Shots.csv'),
            ('RetinaNet 50', 'evaluation/eval-0004_Image_Augmentation_Scale_1x_to_6x--RetinaNet-Resnet50-body-shots-fullsize.csv'),
            ('RetinaNet 152', 'evaluation/eval-0004_Image_Augmentation_Scale_1x_to_6x--RetinaNet-Resnet152-body-shots-fullsize.csv'),
        )
    },
    {
        'label': '0004-image-augmentation-scale-1x-6x, all cases',
        'caption': '0004: Configuration 0004: Image Augmentation Scale 1x to 6x, All Cases',
        'tables': (
            # ('Yolo 3', 'evaluation/eval-0004_Image_Augmentation_Scale_1x_to_6x--Yolo3-Body-Shots-1.csv'),
            # ('F-RCNN', 'evaluation/eval-0004_Image_Augmentation_Scale_1x_to_6x--FRCNN--Body-Shots.csv'),
            ('RetinaNet 50', 'evaluation/eval-0004_Image_Augmentation_Scale_1x_to_6x--RetinaNet-Resnet50-all-cases.csv'),
            ('RetinaNet 152', 'evaluation/eval-0004_Image_Augmentation_Scale_1x_to_6x--RetinaNet-Resnet152-all-cases.csv'),
        )
    },
    {
        'label': '0004-image-augmentation-scale-1x-6x, all cases',
        'caption': '0004: Configuration 0004: Image Augmentation Scale 1x to 6x, All Cases, Fullsize',
        'tables': (
            # ('Yolo 3', 'evaluation/eval-0004_Image_Augmentation_Scale_1x_to_6x--Yolo3-Body-Shots-1.csv'),
            # ('F-RCNN', 'evaluation/eval-0004_Image_Augmentation_Scale_1x_to_6x--FRCNN--Body-Shots.csv'),
            ('RetinaNet 50', 'evaluation/eval-0004_Image_Augmentation_Scale_1x_to_6x--RetinaNet-Resnet50-all-cases-fullsize.csv'),
            ('RetinaNet 152', 'evaluation/eval-0004_Image_Augmentation_Scale_1x_to_6x--RetinaNet-Resnet152-all-cases-fullsize.csv'),
        )
    },
    {
        'label': '0005-transfer-learning',
        'caption': '0005: Transfer Learning',
        'tables': (
            ('Yolo 3', 'evaluation/eval-0005_Transfer_Learning--Yolo3.csv'),
            ('F-RCNN', 'evaluation/eval-0005_Transfer_Learning--FRCNN.csv'),
            ('RetinaNet 50', 'evaluation/eval-0005_Transfer_Learning--RetinaNet-Resnet50.csv'),
            ('RetinaNet 152', 'evaluation/eval-0005_Transfer_Learning--RetinaNet-Resnet152.csv'),
        )
    },
    {
        'label': '0005-transfer-learning-fullsize',
        'caption': '0005: Transfer Learning',
        'tables': (
            ('Yolo 3', 'evaluation/eval-0005_Transfer_Learning--Yolo3.csv'),
            ('F-RCNN', 'evaluation/eval-0005_Transfer_Learning--FRCNN.csv'),
            ('RetinaNet 50', 'evaluation/eval-0005_Transfer_Learning--RetinaNet-Resnet50-fullsize.csv'),
            ('RetinaNet 152', 'evaluation/eval-0005_Transfer_Learning--RetinaNet-Resnet152-fullsize.csv'),
        )
    },
    {
        'label': '0005-transfer-learning-body-shots',
        'caption': '0005: Transfer Learning',
        'tables': (
            ('Yolo 3', 'evaluation/eval-0005_Transfer_Learning--Yolo3-body-shots.csv'),
            ('F-RCNN', 'evaluation/eval-0005_Transfer_Learning--FRCNN-body-shots.csv'),
            ('RetinaNet 50', 'evaluation/eval-0005_Transfer_Learning--RetinaNet-Resnet50-body-shots.csv'),
            ('RetinaNet 152', 'evaluation/eval-0005_Transfer_Learning--RetinaNet-Resnet152-body-shots.csv'),
        )
    },
    # {
    #     'label': '0005-transfer-learning-body-shots',
    #     'caption': '0005: Transfer Learning',
    #     'tables': (
    #         ('Yolo 3', 'evaluation/eval-0005_Transfer_Learning--Yolo3-body-shots.csv'),
    #         ('F-RCNN', 'evaluation/eval-0005_Transfer_Learning--FRCNN-body-shots.csv'),
    #         ('RetinaNet 50', 'evaluation/eval-0005_Transfer_Learning--RetinaNet-Resnet50-body-shots-fullsize.csv'),
    #         ('RetinaNet 152', 'evaluation/eval-0005_Transfer_Learning--RetinaNet-Resnet152-body-shots-fullsize.csv'),
    #     )
    # },
    {
        'label': '0006-tf-imgaug-scale-1x-7x',
        'caption': '0006: Transfer Learning',
        'tables': (
            ('Yolo 3', 'evaluation/eval-0006_Transfer_Learning_Image_Augmentation_Scale_1x_to_7x--Yolo3.csv'),
            ('F-RCNN', 'evaluation/eval-0006_Transfer_Learning_Image_Augmentation_Scale_1x_to_7x--FRCNN.csv'),
            ('RetinaNet 50', 'evaluation/eval-0006_Transfer_Learning_Image_Augmentation_Scale_1x_to_7x--RetinaNet-Resnet50.csv'),
            ('RetinaNet 152', 'evaluation/eval-0006_Transfer_Learning_Image_Augmentation_Scale_1x_to_7x--RetinaNet-Resnet152.csv'),
        )
    },
    {
        'label': '0006-tf-imgaug-scale-1x-7x-fullsize',
        'caption': '0006: Transfer Learning Fullsize',
        'tables': (
            ('Yolo 3', 'evaluation/eval-0006_Transfer_Learning_Image_Augmentation_Scale_1x_to_7x--Yolo3.csv'),
            ('F-RCNN', 'evaluation/eval-0006_Transfer_Learning_Image_Augmentation_Scale_1x_to_7x--FRCNN.csv'),
            ('RetinaNet 50', 'evaluation/eval-0006_Transfer_Learning_Image_Augmentation_Scale_1x_to_7x--RetinaNet-Resnet50-fullsize.csv'),
            ('RetinaNet 152', 'evaluation/eval-0006_Transfer_Learning_Image_Augmentation_Scale_1x_to_7x--RetinaNet-Resnet152-fullsize.csv'),
        )
    },
    {
        'label': '0006-tf-imgaug-scale-1x-7x-body-shots',
        'caption': '0006: Transfer Learning Body Shots',
        'tables': (
            ('Yolo 3', 'evaluation/eval-0006_Transfer_Learning_Image_Augmentation_Scale_1x_to_7x--Yolo3-body-shots.csv'),
            ('F-RCNN', 'evaluation/eval-0006_Transfer_Learning_Image_Augmentation_Scale_1x_to_7x--FRCNN-body-shots.csv'),
            ('RetinaNet 50', 'evaluation/eval-0006_Transfer_Learning_Image_Augmentation_Scale_1x_to_7x--RetinaNet-Resnet50--body-shots.csv'),
            ('RetinaNet 152', 'evaluation/eval-0006_Transfer_Learning_Image_Augmentation_Scale_1x_to_7x--RetinaNet-Resnet152-body-shots.csv'),
        )
    },
    {
        'label': '0006-tf-imgaug-scale-1x-7x-body-shots-fullsize',
        'caption': '0006: Transfer Learning Body Shots Fullsize',
        'tables': (
            ('Yolo 3', 'evaluation/eval-0006_Transfer_Learning_Image_Augmentation_Scale_1x_to_7x--Yolo3-body-shots.csv'),
            ('F-RCNN', 'evaluation/eval-0006_Transfer_Learning_Image_Augmentation_Scale_1x_to_7x--FRCNN-body-shots.csv'),
            ('RetinaNet 50', 'evaluation/eval-0006_Transfer_Learning_Image_Augmentation_Scale_1x_to_7x--RetinaNet-Resnet50--body-shots-fullsize.csv'),
            ('RetinaNet 152', 'evaluation/eval-0006_Transfer_Learning_Image_Augmentation_Scale_1x_to_7x--RetinaNet-Resnet152--body-shots-fullsize.csv'),
        )
    },
    {
        'label': '0006-tf-imgaug-scale-1x-7x-body-shots-allcases',
        'caption': '0006: Transfer Learning Body Shots All Cases',
        'tables': (
            ('Yolo 3', 'evaluation/eval-0006_Transfer_Learning_Image_Augmentation_Scale_1x_to_7x--Yolo3-all-cases.csv'),
            ('F-RCNN', 'evaluation/eval-0006_Transfer_Learning_Image_Augmentation_Scale_1x_to_7x--FRCNN-all-cases.csv'),
            ('RetinaNet 50', 'evaluation/eval-0006_Transfer_Learning_Image_Augmentation_Scale_1x_to_7x--RetinaNet-Resnet50-all-cases.csv'),
            ('RetinaNet 152', 'evaluation/eval-0006_Transfer_Learning_Image_Augmentation_Scale_1x_to_7x--RetinaNet-Resnet152-all-cases.csv'),
        )
    },
    {
        'label': '0006-tf-imgaug-scale-1x-7x-body-shots-allcases-fullsize',
        'caption': '0006: Transfer Learning Body Shots All Cases Fullsize',
        'tables': (
            ('Yolo 3', 'evaluation/eval-0006_Transfer_Learning_Image_Augmentation_Scale_1x_to_7x--Yolo3-all-cases.csv'),
            ('F-RCNN', 'evaluation/eval-0006_Transfer_Learning_Image_Augmentation_Scale_1x_to_7x--FRCNN-all-cases.csv'),
            ('RetinaNet 50', 'evaluation/eval-0006_Transfer_Learning_Image_Augmentation_Scale_1x_to_7x--RetinaNet-Resnet50-all-cases-fullsize.csv'),
            ('RetinaNet 152', 'evaluation/eval-0006_Transfer_Learning_Image_Augmentation_Scale_1x_to_7x--RetinaNet-Resnet152-all-cases-full-size.csv'),
        )
    },
    {
        'label': '0007-tf-imgaug-scale-1x-7x-rot89',
        'caption': '0007: Transfer Learning Scale rot',
        'tables': (
            ('RetinaNet 50', 'evaluation/eval-0007_Transfer_Learning_Image_Augmentation_Scale_1x_to_7x_rotate90_1000_Epochs--RetinaNet-Resnet50.csv'),
            ('RetinaNet 152', 'evaluation/eval-0007_Transfer_Learning_Image_Augmentation_Scale_1x_to_7x_rotate90_1000_Epochs--RetinaNet-Resnet152.csv'),
        )
    },
    {
        'label': '0007-tf-imgaug-scale-1x-7x-rot89-fullsize',
        'caption': '0007: Transfer Learning Scale rot fullsize',
        'tables': (
            ('RetinaNet 50', 'evaluation/eval-0007_Transfer_Learning_Image_Augmentation_Scale_1x_to_7x_rotate90_1000_Epochs--RetinaNet-Resnet50-fullsize.csv'),
            ('RetinaNet 152', 'evaluation/eval-0007_Transfer_Learning_Image_Augmentation_Scale_1x_to_7x_rotate90_1000_Epochs--RetinaNet-Resnet152-fullsize.csv'),
        )
    },
    {
        'label': '0007c-ultrahires-tf-imgaug-scale-1x-7x-rot89',
        'caption': '0007c: Transfer Learning Scale rot ultrahires',
        'tables': (
            ('RetinaNet 50', 'evaluation/eval-0007c_Transfer_Learning_UltraHires_Image_Augmentation_Scale_1x_to_7x_rotate90_1000_Epochs--RetinaNet-Resnet50.csv'),
        )
    },
    {
        'label': '0007c-ultrahires-tf-imgaug-scale-1x-7x-rot89-fullsize',
        'caption': '0007c: Transfer Learning Scale rot ultrahires',
        'tables': (
            ('RetinaNet 50', 'evaluation/eval-0007c_Transfer_Learning_UltraHires_Image_Augmentation_Scale_1x_to_7x_rotate90_1000_Epochs--RetinaNet-Resnet50-fullsi6ze.csv'),
        )
    },
    {
        'label': '0007c-ultrahires-tf-imgaug-scale-1x-7x-rot89-all-cases',
        'caption': '0007c: Transfer Learning Scale rot all cases',
        'tables': (
            ('RetinaNet 50', 'evaluation/eval-0007c_Transfer_Learning_UltraHires_Image_Augmentation_Scale_1x_to_7x_rotate90_1000_Epochs--RetinaNet-Resnet50-all-cases.csv'),
        )
    },
    {
        'label': '0007c-ultrahires-tf-imgaug-scale-1x-7x-rot89-all-cases-fullsize',
        'caption': '0007c: Transfer Learning Scale rot all cases fullsize',
        'tables': (
            ('RetinaNet 50', 'evaluation/eval-0007c_Transfer_Learning_UltraHires_Image_Augmentation_Scale_1x_to_7x_rotate90_1000_Epochs--RetinaNet-Resnet50-all-cases-fullsize.csv'),
        )
    },
    {
        'label': '0007e-tl-hires',
        'caption': '0007e: TF HIRES',
        'tables': (
            ('RetinaNet 50', 'evaluation/eval-0007e_Transfer_Learning_Hires_Image_Augmentation_Scale_1x_to_7x--RetinaNet-Resnet50.csv'),
            ('RetinaNet 152', 'evaluation/eval-0007e_Transfer_Learning_Hires_Image_Augmentation_Scale_1x_to_7x--RetinaNet-Resnet50.csv'),
            ('RetinaNet 50, Fullsize', 'evaluation/eval-0007e_Transfer_Learning_Hires_Image_Augmentation_Scale_1x_to_7x--RetinaNet-Resnet50-fullsize.csv'),
            ('RetinaNet 152, Fullsize', 'evaluation/eval-0007e_Transfer_Learning_Hires_Image_Augmentation_Scale_1x_to_7x--RetinaNet-Resnet152-fullsize.csv'),
        )
    },
    {
        'label': '0007e-tl-hires-body-shots',
        'caption': '0007e: TF HIRES Body shots',
        'tables': (
            ('RetinaNet 50', 'evaluation/eval-0007e_Transfer_Learning_Hires_Image_Augmentation_Scale_1x_to_7x--RetinaNet-Resnet50-body-shots.csv'),
            ('RetinaNet 152', 'evaluation/eval-0007e_Transfer_Learning_Hires_Image_Augmentation_Scale_1x_to_7x--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 50, Fullsize', 'evaluation/eval-0007e_Transfer_Learning_Hires_Image_Augmentation_Scale_1x_to_7x--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152, Fullsize', 'evaluation/eval-0007e_Transfer_Learning_Hires_Image_Augmentation_Scale_1x_to_7x--RetinaNet-Resnet152-body-shots-fullsize.csv'),
        )
    },
    {
        'label': '0007e-tl-hires-all-cases',
        'caption': '0007e: TF HIRES Allcases',
        'tables': (
            ('RetinaNet 50', 'evaluation/eval-0007e_Transfer_Learning_Hires_Image_Augmentation_Scale_1x_to_7x--RetinaNet-Resnet50-all-cases.csv'),
            ('RetinaNet 152', 'evaluation/eval-0007e_Transfer_Learning_Hires_Image_Augmentation_Scale_1x_to_7x--RetinaNet-Resnet152-all-cases.csv'),
            ('RetinaNet 50, Fullsize', 'evaluation/eval-0007e_Transfer_Learning_Hires_Image_Augmentation_Scale_1x_to_7x--RetinaNet-Resnet152-all-cases-fullsize.csv'),
            ('RetinaNet 152, Fullsize', 'evaluation/eval-0007e_Transfer_Learning_Hires_Image_Augmentation_Scale_1x_to_7x--RetinaNet-Resnet152-all-cases-fullsize.csv'),
        )
    },
    {
        'label': '0011-all-cases-training',
        'caption': '0011: All Cases Training',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0011_All_Cases--RetinaNet-Resnet152.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0011b_All_Cases--RetinaNet-Resnet152.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0011c_All_Cases--RetinaNet-Resnet152.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0011d_All_Cases--RetinaNet-Resnet152.csv'),
        )
    },
    {
        'label': '0011-all-cases-training-fullsize',
        'caption': '0011: All Cases Training Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0011_All_Cases--RetinaNet-Resnet152-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0011b_All_Cases--RetinaNet-Resnet152-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0011c_All_Cases--RetinaNet-Resnet152-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0011d_All_Cases--RetinaNet-Resnet152-fullsize.csv'),
        )
    },
    {
        'label': '0011-all-cases-training-body-shots',
        'caption': '0011: All Cases Training Body shots',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0011_All_Cases--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0011b_All_Cases--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0011c_All_Cases--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0011d_All_Cases--RetinaNet-Resnet152-body-shots.csv'),
        )
    },
    {
        'label': '0011-all-cases-training-body-shots-fullsize',
        'caption': '0011: All Cases Training Body shots Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0011_All_Cases--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0011b_All_Cases--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0011c_All_Cases--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0011d_All_Cases--RetinaNet-Resnet152-body-shots-fullsize.csv'),
        )
    },
    {
        'label': '0011-all-cases-training-1024',
        'caption': '0011: All Cases Training 1024',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0011_All_Cases_1024--RetinaNet-Resnet152.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0011b_All_Cases_1024--RetinaNet-Resnet152.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0011c_All_Cases_1024--RetinaNet-Resnet152.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0011d_All_Cases_1024--RetinaNet-Resnet152.csv'),
        )
    },
    {
        'label': '0011-all-cases-training-1024-fullsize',
        'caption': '0011: All Cases Training 1024 Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0011_All_Cases_1024--RetinaNet-Resnet152-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0011b_All_Cases_1024--RetinaNet-Resnet152-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0011c_All_Cases_1024--RetinaNet-Resnet152-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0011d_All_Cases_1024--RetinaNet-Resnet152-fullsize.csv'),
        )
    },
    {
        'label': '0011-all-cases-training-1024-body-shots',
        'caption': '0011: All Cases Training 1024 Body shots',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0011_All_Cases_1024--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0011b_All_Cases_1024--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0011c_All_Cases_1024--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0011d_All_Cases_1024--RetinaNet-Resnet152-body-shots.csv'),
        )
    },
    {
        'label': '0011-all-cases-training-1024-body-shots-fullsize',
        'caption': '0011: All Cases Training 1024 Body shots Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0011_All_Cases_1024--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0011b_All_Cases_1024--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0011c_All_Cases_1024--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0011d_All_Cases_1024--RetinaNet-Resnet152-body-shots-fullsize.csv'),
        )
    },
    {
        'label': '0011-all-cases-training-Max-3',
        'caption': '0011: All Cases Training Max-3',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0011_All_Cases_Max_3--RetinaNet-Resnet152.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0011b_All_Cases_Max_3--RetinaNet-Resnet152.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0011c_All_Cases_Max_3--RetinaNet-Resnet152.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0011d_All_Cases_Max_3--RetinaNet-Resnet152.csv'),
        )
    },
    {
        'label': '0011-all-cases-training-Max-3-fullsize',
        'caption': '0011: All Cases Training Max-3 Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0011_All_Cases_Max_3--RetinaNet-Resnet152-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0011b_All_Cases_Max_3--RetinaNet-Resnet152-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0011c_All_Cases_Max_3--RetinaNet-Resnet152-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0011d_All_Cases_Max_3--RetinaNet-Resnet152-fullsize.csv'),
        )
    },
    {
        'label': '0011-all-cases-training-Max-3-body-shots',
        'caption': '0011: All Cases Training Max-3 Body shots',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0011_All_Cases_Max_3--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0011b_All_Cases_Max_3--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0011c_All_Cases_Max_3--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0011d_All_Cases_Max_3--RetinaNet-Resnet152-body-shots.csv'),
        )
    },
    {
        'label': '0011-all-cases-training-Max-3-body-shots-fullsize',
        'caption': '0011: All Cases Training Max-3 Body shots Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0011_All_Cases_Max_3--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0011b_All_Cases_Max_3--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0011c_All_Cases_Max_3--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0011d_All_Cases_Max_3--RetinaNet-Resnet152-body-shots-fullsize.csv'),
        )
    },
    {
        'label': '0011-all-cases-training-Max-3-all-cases',
        'caption': '0011: All Cases Training Max-3 All Cases',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0011_All_Cases_Max_3--RetinaNet-Resnet152-all-cases.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0011b_All_Cases_Max_3--RetinaNet-Resnet152-all-cases.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0011c_All_Cases_Max_3--RetinaNet-Resnet152-all-cases.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0011d_All_Cases_Max_3--RetinaNet-Resnet152-all-cases.csv'),
        )
    },
    {
        'label': '0011-all-cases-training-Max-3-all-cases-fullsize',
        'caption': '0011: All Cases Training Max-3 All Cases Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0011_All_Cases_Max_3--RetinaNet-Resnet152-all-cases-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0011b_All_Cases_Max_3--RetinaNet-Resnet152-all-cases-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0011c_All_Cases_Max_3--RetinaNet-Resnet152-all-cases-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0011d_All_Cases_Max_3--RetinaNet-Resnet152-all-cases-fullsize.csv'),
        )
    },
    {
        'label': '0011-all-cases-training-Max-6',
        'caption': '0011: All Cases Training Max-6',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0011_All_Cases_Max_6--RetinaNet-Resnet152.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0011b_All_Cases_Max_6--RetinaNet-Resnet152.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0011c_All_Cases_Max_6--RetinaNet-Resnet152.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0011d_All_Cases_Max_6--RetinaNet-Resnet152.csv'),
        )
    },
    {
        'label': '0011-all-cases-training-Max-6-fullsize',
        'caption': '0011: All Cases Training Max-6 Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0011_All_Cases_Max_6--RetinaNet-Resnet152-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0011b_All_Cases_Max_6--RetinaNet-Resnet152-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0011c_All_Cases_Max_6--RetinaNet-Resnet152-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0011d_All_Cases_Max_6--RetinaNet-Resnet152-fullsize.csv'),
        )
    },
    {
        'label': '0011-all-cases-training-Max-6-body-shots',
        'caption': '0011: All Cases Training Max-6 Body shots',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0011_All_Cases_Max_6--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0011b_All_Cases_Max_6--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0011c_All_Cases_Max_6--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0011d_All_Cases_Max_6--RetinaNet-Resnet152-body-shots.csv'),
        )
    },
    {
        'label': '0011-all-cases-training-Max-6-body-shots-fullsize',
        'caption': '0011: All Cases Training Max-6 Body shots Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0011_All_Cases_Max_6--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0011b_All_Cases_Max_6--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0011c_All_Cases_Max_6--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0011d_All_Cases_Max_6--RetinaNet-Resnet152-body-shots-fullsize.csv'),
        )
    },
    {
        'label': '0011-all-cases-training-Max-6-all-cases',
        'caption': '0011: All Cases Training Max-6 All Cases',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0011_All_Cases_Max_6--RetinaNet-Resnet152-all-cases.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0011b_All_Cases_Max_6--RetinaNet-Resnet152-all-cases.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0011c_All_Cases_Max_6--RetinaNet-Resnet152-all-cases.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0011d_All_Cases_Max_6--RetinaNet-Resnet152-all-cases.csv'),
        )
    },
    {
        'label': '0011-all-cases-training-Max-6-all-cases-fullsize',
        'caption': '0011: All Cases Training Max-6 All Cases Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0011_All_Cases_Max_6--RetinaNet-Resnet152-all-cases-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0011b_All_Cases_Max_6--RetinaNet-Resnet152-all-cases-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0011c_All_Cases_Max_6--RetinaNet-Resnet152-all-cases-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0011d_All_Cases_Max_6--RetinaNet-Resnet152-all-cases-fullsize.csv'),
        )
    },
    
    
    
    # 0014
    {
        'label': '0014-all-cases-training-puppetbase',
        'caption': '0014: All Cases Training Puppetbase',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0014_All_Cases_Transfer_ImgAug_Puppetbase--RetinaNet-Resnet152.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0014b_All_Cases_Transfer_ImgAug_Puppetbase--RetinaNet-Resnet152.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0014c_All_Cases_Transfer_ImgAug_Puppetbase--RetinaNet-Resnet152.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0014d_All_Cases_Transfer_ImgAug_Puppetbase--RetinaNet-Resnet152.csv'),
        )
    },
    {
        'label': '0014-all-cases-training-puppetbase-fullsize',
        'caption': '0014: All Cases Training Puppetbase Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0014_All_Cases_Transfer_ImgAug_Puppetbase--RetinaNet-Resnet152-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0014b_All_Cases_Transfer_ImgAug_Puppetbase--RetinaNet-Resnet152-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0014c_All_Cases_Transfer_ImgAug_Puppetbase--RetinaNet-Resnet152-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0014d_All_Cases_Transfer_ImgAug_Puppetbase--RetinaNet-Resnet152-fullsize.csv'),
        )
    },
    {
        'label': '0014-all-cases-training-puppetbase-body-shots',
        'caption': '0014: All Cases Training Puppetbase Body shots',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0014_All_Cases_Transfer_ImgAug_Puppetbase--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0014b_All_Cases_Transfer_ImgAug_Puppetbase--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0014c_All_Cases_Transfer_ImgAug_Puppetbase--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0014d_All_Cases_Transfer_ImgAug_Puppetbase--RetinaNet-Resnet152-body-shots.csv'),
        )
    },
    {
        'label': '0014-all-cases-training-puppetbase-body-shots-fullsize',
        'caption': '0014: All Cases Training Puppetbase Body shots Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0014_All_Cases_Transfer_ImgAug_Puppetbase--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0014b_All_Cases_Transfer_ImgAug_Puppetbase--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0014c_All_Cases_Transfer_ImgAug_Puppetbase--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0014d_All_Cases_Transfer_ImgAug_Puppetbase--RetinaNet-Resnet152-body-shots-fullsize.csv'),
        )
    },
    {
        'label': '0014-all-cases-training-puppetbase-1024',
        'caption': '0014: All Cases Training Puppetbase 1024',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0014_All_Cases_Transfer_ImgAug_Puppetbase_1024--RetinaNet-Resnet152-cases.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0014b_All_Cases_Transfer_ImgAug_Puppetbase_1024--RetinaNet-Resnet152-cases.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0014c_All_Cases_Transfer_ImgAug_Puppetbase_1024--RetinaNet-Resnet152-cases.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0014d_All_Cases_Transfer_ImgAug_Puppetbase_1024--RetinaNet-Resnet152-cases.csv'),
        )
    },
    {
        'label': '0014-all-cases-training-puppetbase-1024-fullsize',
        'caption': '0014: All Cases Training Puppetbase 1024 Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0014_All_Cases_Transfer_ImgAug_Puppetbase_1024--RetinaNet-Resnet152-cases-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0014b_All_Cases_Transfer_ImgAug_Puppetbase_1024--RetinaNet-Resnet152-cases-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0014c_All_Cases_Transfer_ImgAug_Puppetbase_1024--RetinaNet-Resnet152-cases-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0014d_All_Cases_Transfer_ImgAug_Puppetbase_1024--RetinaNet-Resnet152-cases-fullsize.csv'),
        )
    },
    {
        'label': '0014-all-cases-training-puppetbase-1024-body-shots',
        'caption': '0014: All Cases Training Puppetbase 1024 Body shots',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0014_All_Cases_Transfer_ImgAug_Puppetbase_1024--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0014b_All_Cases_Transfer_ImgAug_Puppetbase_1024--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0014c_All_Cases_Transfer_ImgAug_Puppetbase_1024--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0014d_All_Cases_Transfer_ImgAug_Puppetbase_1024--RetinaNet-Resnet152-body-shots.csv'),
        )
    },
    {
        'label': '0014-all-cases-training-puppetbase-1024-body-shots-fullsize',
        'caption': '0014: All Cases Training Puppetbase 1024 Body shots Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0014_All_Cases_Transfer_ImgAug_Puppetbase_1024--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0014b_All_Cases_Transfer_ImgAug_Puppetbase_1024--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0014c_All_Cases_Transfer_ImgAug_Puppetbase_1024--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0014d_All_Cases_Transfer_ImgAug_Puppetbase_1024--RetinaNet-Resnet152-body-shots-fullsize.csv'),
        )
    },
    {
        'label': '0014-all-cases-training-puppetbase-Max-3',
        'caption': '0014: All Cases Training Puppetbase Max-3',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0014_All_Cases_Transfer_ImgAug_Puppetbase_Max_3--RetinaNet-Resnet152.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0014b_All_Cases_Transfer_ImgAug_Puppetbase_Max_3--RetinaNet-Resnet152.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0014c_All_Cases_Transfer_ImgAug_Puppetbase_Max_3--RetinaNet-Resnet152.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0014d_All_Cases_Transfer_ImgAug_Puppetbase_Max_3--RetinaNet-Resnet152.csv'),
        )
    },
    {
        'label': '0014-all-cases-training-puppetbase-Max-3-fullsize',
        'caption': '0014: All Cases Training Puppetbase Max-3 Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0014_All_Cases_Transfer_ImgAug_Puppetbase_Max_3--RetinaNet-Resnet152-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0014b_All_Cases_Transfer_ImgAug_Puppetbase_Max_3--RetinaNet-Resnet152-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0014c_All_Cases_Transfer_ImgAug_Puppetbase_Max_3--RetinaNet-Resnet152-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0014d_All_Cases_Transfer_ImgAug_Puppetbase_Max_3--RetinaNet-Resnet152-fullsize.csv'),
        )
    },
    {
        'label': '0014-all-cases-training-puppetbase-Max-3-body-shots',
        'caption': '0014: All Cases Training Puppetbase Max-3 Body shots',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0014_All_Cases_Transfer_ImgAug_Puppetbase_Max_3--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0014b_All_Cases_Transfer_ImgAug_Puppetbase_Max_3--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0014c_All_Cases_Transfer_ImgAug_Puppetbase_Max_3--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0014d_All_Cases_Transfer_ImgAug_Puppetbase_Max_3--RetinaNet-Resnet152-body-shots.csv'),
        )
    },
    {
        'label': '0014-all-cases-training-puppetbase-Max-3-body-shots-fullsize',
        'caption': '0014: All Cases Training Puppetbase Max-3 Body shots Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0014_All_Cases_Transfer_ImgAug_Puppetbase_Max_3--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0014b_All_Cases_Transfer_ImgAug_Puppetbase_Max_3--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0014c_All_Cases_Transfer_ImgAug_Puppetbase_Max_3--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0014d_All_Cases_Transfer_ImgAug_Puppetbase_Max_3--RetinaNet-Resnet152-body-shots-fullsize.csv'),
        )
    },
    {
        'label': '0014-all-cases-training-puppetbase-Max-3-all-cases',
        'caption': '0014: All Cases Training Puppetbase Max-3 All Cases',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0014_All_Cases_Transfer_ImgAug_Puppetbase_Max_3--RetinaNet-Resnet152-all-cases.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0014b_All_Cases_Transfer_ImgAug_Puppetbase_Max_3--RetinaNet-Resnet152-all-cases.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0014c_All_Cases_Transfer_ImgAug_Puppetbase_Max_3--RetinaNet-Resnet152-all-cases.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0014d_All_Cases_Transfer_ImgAug_Puppetbase_Max_3--RetinaNet-Resnet152-all-cases.csv'),
        )
    },
    {
        'label': '0014-all-cases-training-puppetbase-Max-3-all-cases-fullsize',
        'caption': '0014: All Cases Training Puppetbase Max-3 All Cases Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0014_All_Cases_Transfer_ImgAug_Puppetbase_Max_3--RetinaNet-Resnet152-all-cases-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0014b_All_Cases_Transfer_ImgAug_Puppetbase_Max_3--RetinaNet-Resnet152-all-cases-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0014c_All_Cases_Transfer_ImgAug_Puppetbase_Max_3--RetinaNet-Resnet152-all-cases-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0014d_All_Cases_Transfer_ImgAug_Puppetbase_Max_3--RetinaNet-Resnet152-all-cases-fullsize.csv'),
        )
    },
    {
        'label': '0014-all-cases-training-puppetbase-Max-6',
        'caption': '0014: All Cases Training Puppetbase Max-6',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0014_All_Cases_Transfer_ImgAug_Puppetbase_Max_6--RetinaNet-Resnet152.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0014b_All_Cases_Transfer_ImgAug_Puppetbase_Max_6--RetinaNet-Resnet152.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0014c_All_Cases_Transfer_ImgAug_Puppetbase_Max_6--RetinaNet-Resnet152.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0014d_All_Cases_Transfer_ImgAug_Puppetbase_Max_6--RetinaNet-Resnet152.csv'),
        )
    },
    {
        'label': '0014-all-cases-training-puppetbase-Max-6-fullsize',
        'caption': '0014: All Cases Training Puppetbase Max-6 Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0014_All_Cases_Transfer_ImgAug_Puppetbase_Max_6--RetinaNet-Resnet152-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0014b_All_Cases_Transfer_ImgAug_Puppetbase_Max_6--RetinaNet-Resnet152-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0014c_All_Cases_Transfer_ImgAug_Puppetbase_Max_6--RetinaNet-Resnet152-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0014d_All_Cases_Transfer_ImgAug_Puppetbase_Max_6--RetinaNet-Resnet152-fullsize.csv'),
        )
    },
    {
        'label': '0014-all-cases-training-puppetbase-Max-6-body-shots',
        'caption': '0014: All Cases Training Puppetbase Max-6 Body shots',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0014_All_Cases_Transfer_ImgAug_Puppetbase_Max_6--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0014b_All_Cases_Transfer_ImgAug_Puppetbase_Max_6--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0014c_All_Cases_Transfer_ImgAug_Puppetbase_Max_6--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0014d_All_Cases_Transfer_ImgAug_Puppetbase_Max_6--RetinaNet-Resnet152-body-shots.csv'),
        )
    },
    {
        'label': '0014-all-cases-training-puppetbase-Max-6-body-shots-fullsize',
        'caption': '0014: All Cases Training Puppetbase Max-6 Body shots Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0014_All_Cases_Transfer_ImgAug_Puppetbase_Max_6--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0014b_All_Cases_Transfer_ImgAug_Puppetbase_Max_6--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0014c_All_Cases_Transfer_ImgAug_Puppetbase_Max_6--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0014d_All_Cases_Transfer_ImgAug_Puppetbase_Max_6--RetinaNet-Resnet152-body-shots-fullsize.csv'),
        )
    },
    {
        'label': '0014-all-cases-training-puppetbase-Max-6-all-cases',
        'caption': '0014: All Cases Training Puppetbase Max-6 All Cases',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0014_All_Cases_Transfer_ImgAug_Puppetbase_Max_6--RetinaNet-Resnet152-all-cases.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0014b_All_Cases_Transfer_ImgAug_Puppetbase_Max_6--RetinaNet-Resnet152-all-cases.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0014c_All_Cases_Transfer_ImgAug_Puppetbase_Max_6--RetinaNet-Resnet152-all-cases.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0014d_All_Cases_Transfer_ImgAug_Puppetbase_Max_6--RetinaNet-Resnet152-all-cases.csv'),
        )
    },
    {
        'label': '0014-all-cases-training-puppetbase-Max-6-all-cases-fullsize',
        'caption': '0014: All Cases Training Puppetbase Max-6 All Cases Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0014_All_Cases_Transfer_ImgAug_Puppetbase_Max_6--RetinaNet-Resnet152-all-cases-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0014b_All_Cases_Transfer_ImgAug_Puppetbase_Max_6--RetinaNet-Resnet152-all-cases-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0014c_All_Cases_Transfer_ImgAug_Puppetbase_Max_6--RetinaNet-Resnet152-all-cases-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0014d_All_Cases_Transfer_ImgAug_Puppetbase_Max_6--RetinaNet-Resnet152-all-cases-fullsize.csv'),
        )
    },

    # 0017
    # ====
    {
        'label': '0017-closeup-wounds-confidential-1x-3x-rot90',
        'caption': '0017: Close up wounds confidential 1x 3x rot90',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0017_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0017b_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0017c_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0017d_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152.csv'),
        )
    },
    {
        'label': '0017-closeup-wounds-confidential-1x-3x-rot90-fullsize',
        'caption': '0017: Close up wounds confidential 1x 3x rot90 Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0017_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0017b_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0017c_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0017d_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-fullsize.csv'),
        )
    },
    {
        'label': '0017-closeup-wounds-confidential-1x-3x-rot90 body shots',
        'caption': '0017: Close up wounds confidential 1x 3x rot90 body shots',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0017_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0017b_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0017c_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0017d_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-body-shots.csv'),
        )
    },
    {
        'label': '0017-closeup-wounds-confidential-1x-3x-rot90-body-shots-fullsize',
        'caption': '0017: Close up wounds confidential 1x 3x rot90 Body shots Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0017_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0017b_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0017c_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0017d_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-body-shots-fullsize.csv'),
        )
    },
    {
        'label': '0017-closeup-wounds-confidential-1x-3x-rot90 all cases',
        'caption': '0017: Close up wounds confidential 1x 3x rot90 all cases',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0017_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-all-cases.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0017b_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-all-cases.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0017c_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-all-cases.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0017d_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-all-cases.csv'),
        )
    },
    {
        'label': '0017-closeup-wounds-confidential-1x-3x-rot90-all-cases-fullsize',
        'caption': '0017: Close up wounds confidential 1x 3x rot90 all cases Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0017_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-all-cases-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0017b_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-all-cases-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0017c_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-all-cases-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0017d_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-all-cases-fullsize.csv'),
        )
    },

    # 0017e
    # =====
    {
        'label': '0017e-closeup-wounds-confidential-1x-3x-rot90',
        'caption': '0017e: Close up wounds confidential 1x 3x rot90',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0017e_tl_imgaug_rot90_closeup_wounds_confidential--RetinaNet-Resnet152.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0017f_tl_imgaug_rot90_closeup_wounds_confidential--RetinaNet-Resnet152.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0017g_tl_imgaug_rot90_closeup_wounds_confidential--RetinaNet-Resnet152.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0017h_tl_imgaug_rot90_closeup_wounds_confidential--RetinaNet-Resnet152.csv'),
        )
    },
    {
        'label': '0017e-closeup-wounds-confidential-1x-3x-rot90-fullsize',
        'caption': '0017e: Close up wounds confidential 1x 3x rot90 Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0017e_tl_imgaug_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0017f_tl_imgaug_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0017g_tl_imgaug_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0017h_tl_imgaug_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-fullsize.csv'),
        )
    },
    {
        'label': '0017e-closeup-wounds-confidential-1x-3x-rot90 body shots',
        'caption': '0017e: Close up wounds confidential 1x 3x rot90 body shots',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0017e_tl_imgaug_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0017f_tl_imgaug_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0017g_tl_imgaug_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0017h_tl_imgaug_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-body-shots.csv'),
        )
    },
    {
        'label': '0017e-closeup-wounds-confidential-1x-3x-rot90-body-shots-fullsize',
        'caption': '0017e: Close up wounds confidential 1x 3x rot90 Body shots Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0017e_tl_imgaug_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0017f_tl_imgaug_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0017g_tl_imgaug_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0017h_tl_imgaug_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-body-shots-fullsize.csv'),
        )
    },
    {
        'label': '0017e-closeup-wounds-confidential-1x-3x-rot90 all cases',
        'caption': '0017e: Close up wounds confidential 1x 3x rot90 all cases',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0017e_tl_imgaug_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-all-cases.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0017f_tl_imgaug_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-all-cases.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0017g_tl_imgaug_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-all-cases.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0017h_tl_imgaug_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-all-cases.csv'),
        )
    },
    {
        'label': '0017e-closeup-wounds-confidential-1x-3x-rot90-all-cases-fullsize',
        'caption': '0017e: Close up wounds confidential 1x 3x rot90 all cases Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0017e_tl_imgaug_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-all-cases-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0017f_tl_imgaug_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-all-cases-fullsize.csv'),
            # ('RetinaNet 152 c', 'evaluation/eval-0017g_tl_imgaug_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-all-cases-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0017h_tl_imgaug_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-all-cases-fullsize.csv'),
        )
    },

    # 0017i
    # =====
    {
        'label': '0017icloseup-wounds-confidential-1x-3x-rot90',
        'caption': '0017i: Close up wounds confidential 1x 3x rot90',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0017i_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0017j_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0017k_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152.csv'),
            # ('RetinaNet 152 d', 'evaluation/eval-0017l_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152.csv'),
        )
    },
    {
        'label': '0017icloseup-wounds-confidential-1x-3x-rot90-fullsize',
        'caption': '0017i: Close up wounds confidential 1x 3x rot90 Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0017i_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0017j_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0017k_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-fullsize.csv'),
            # ('RetinaNet 152 d', 'evaluation/eval-0017l_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-fullsize.csv'),
        )
    },
    {
        'label': '0017icloseup-wounds-confidential-1x-3x-rot90 body shots',
        'caption': '0017i: Close up wounds confidential 1x 3x rot90 body shots',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0017i_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0017j_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0017k_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0017l_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-body-shots.csv'),
        )
    },
    {
        'label': '0017icloseup-wounds-confidential-1x-3x-rot90-body-shots-fullsize',
        'caption': '0017i: Close up wounds confidential 1x 3x rot90 Body shots Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0017i_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0017j_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0017k_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0017l_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-body-shots-fullsize.csv'),
        )
    },
    {
        'label': '0017icloseup-wounds-confidential-1x-3x-rot90 all cases',
        'caption': '0017i: Close up wounds confidential 1x 3x rot90 all cases',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0017i_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-all-cases.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0017j_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-all-cases.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0017k_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-all-cases.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0017l_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-all-cases.csv'),
        )
    },
    {
        'label': '0017icloseup-wounds-confidential-1x-3x-rot90-all-cases-fullsize',
        'caption': '0017i: Close up wounds confidential 1x 3x rot90 all cases Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0017i_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-all-cases-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0017j_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-all-cases-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0017k_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-all-cases-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0017l_tl_imgaug_1x_3x_rot90_closeup_wounds_confidential--RetinaNet-Resnet152-all-cases-fullsize.csv'),
        )
    },


    # 0031
    # ====
    {
        'label': '0031 Joint Training Puppet Cases',
        'caption': '0031: Joint Training Puppet Cases',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0031a_Joint_Training_of_Puppet_and_Cases--RetinaNet-Resnet152.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0031b_Joint_Training_of_Puppet_and_Cases--RetinaNet-Resnet152.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0031c_Joint_Training_of_Puppet_and_Cases--RetinaNet-Resnet152.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0031d_Joint_Training_of_Puppet_and_Cases--RetinaNet-Resnet152.csv'),
        )
    },
    {
        'label': '0031 Joint Training Puppet Cases Fullsize',
        'caption': '0031: Joint Training Puppet Cases Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0031a_Joint_Training_of_Puppet_and_Cases--RetinaNet-Resnet152-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0031b_Joint_Training_of_Puppet_and_Cases--RetinaNet-Resnet152-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0031c_Joint_Training_of_Puppet_and_Cases--RetinaNet-Resnet152-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0031d_Joint_Training_of_Puppet_and_Cases--RetinaNet-Resnet152-fullsize.csv'),
        )
    },
    {
        'label': '0031 Joint Training Puppet Cases Body Shots',
        'caption': '0031: Joint Training Puppet Cases Body Shots',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0031a_Joint_Training_of_Puppet_and_Cases--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0031b_Joint_Training_of_Puppet_and_Cases--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0031c_Joint_Training_of_Puppet_and_Cases--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0031d_Joint_Training_of_Puppet_and_Cases--RetinaNet-Resnet152-body-shots.csv'),
        )
    },
    {
        'label': '0031 Joint Training Puppet Cases Body Shots Fullsize',
        'caption': '0031: Joint Training Puppet Cases Body Shots Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0031a_Joint_Training_of_Puppet_and_Cases--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0031b_Joint_Training_of_Puppet_and_Cases--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0031c_Joint_Training_of_Puppet_and_Cases--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0031d_Joint_Training_of_Puppet_and_Cases--RetinaNet-Resnet152-body-shots-fullsize.csv'),
        )
    },
    {
        'label': '0031 Joint Training Puppet Cases All Cases',
        'caption': '0031: Joint Training Puppet Cases All Cases',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0031a_Joint_Training_of_Puppet_and_Cases--RetinaNet-Resnet152-all-cases.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0031b_Joint_Training_of_Puppet_and_Cases--RetinaNet-Resnet152-all-cases.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0031c_Joint_Training_of_Puppet_and_Cases--RetinaNet-Resnet152-all-cases.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0031d_Joint_Training_of_Puppet_and_Cases--RetinaNet-Resnet152-all-cases.csv'),
        )
    },
    {
        'label': '0031 Joint Training Puppet Cases All Cases Fullsize',
        'caption': '0031: Joint Training Puppet Cases All Cases Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0031a_Joint_Training_of_Puppet_and_Cases--RetinaNet-Resnet152-all-cases-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0031b_Joint_Training_of_Puppet_and_Cases--RetinaNet-Resnet152-all-cases-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0031c_Joint_Training_of_Puppet_and_Cases--RetinaNet-Resnet152-all-cases-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0031d_Joint_Training_of_Puppet_and_Cases--RetinaNet-Resnet152-all-cases-fullsize.csv'),
        )
    },


    # 0032
    # ====
    {
        'label': '0032 Joint Training Puppet Cases Body Shots',
        'caption': '0032: Joint Training Puppet Cases Body Shots',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0032a_Joint_Training_of_Puppet_and_Cases_and_Closeups--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0032b_Joint_Training_of_Puppet_and_Cases_and_Closeups--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0032c_Joint_Training_of_Puppet_and_Cases_and_Closeups--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0032d_Joint_Training_of_Puppet_and_Cases_and_Closeups--RetinaNet-Resnet152-body-shots.csv'),
        )
    },
    {
        'label': '0032 Joint Training Puppet Cases Body Shots Fullsize',
        'caption': '0032: Joint Training Puppet Cases Body Shots Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0032a_Joint_Training_of_Puppet_and_Cases_and_Closeups--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0032b_Joint_Training_of_Puppet_and_Cases_and_Closeups--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0032c_Joint_Training_of_Puppet_and_Cases_and_Closeups--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0032d_Joint_Training_of_Puppet_and_Cases_and_Closeups--RetinaNet-Resnet152-body-shots-fullsize.csv'),
        )
    },
    {
        'label': '0032 Joint Training Puppet Cases All Cases',
        'caption': '0032: Joint Training Puppet Cases All Cases',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0032a_Joint_Training_of_Puppet_and_Cases_and_Closeups--RetinaNet-Resnet152-all-cases.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0032b_Joint_Training_of_Puppet_and_Cases_and_Closeups--RetinaNet-Resnet152-all-cases.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0032c_Joint_Training_of_Puppet_and_Cases_and_Closeups--RetinaNet-Resnet152-all-cases.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0032d_Joint_Training_of_Puppet_and_Cases_and_Closeups--RetinaNet-Resnet152-all-cases.csv'),
        )
    },
    {
        'label': '0032 Joint Training Puppet Cases All Cases Fullsize',
        'caption': '0032: Joint Training Puppet Cases All Cases Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0032a_Joint_Training_of_Puppet_and_Cases_and_Closeups--RetinaNet-Resnet152-all-cases-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0032b_Joint_Training_of_Puppet_and_Cases_and_Closeups--RetinaNet-Resnet152-all-cases-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0032c_Joint_Training_of_Puppet_and_Cases_and_Closeups--RetinaNet-Resnet152-all-cases-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0032d_Joint_Training_of_Puppet_and_Cases_and_Closeups--RetinaNet-Resnet152-all-cases-fullsize.csv'),
        )
    },


    # 0033
    # ====
    {
        'label': '0033 Joint Training Puppet Cases Body Shots',
        'caption': '0033: Joint Training Puppet Cases Body Shots',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0033a_Joint_Training_of_Puppet_and_Cases_and_Closeups_and_Closeupsconf--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0033b_Joint_Training_of_Puppet_and_Cases_and_Closeups_and_Closeupsconf--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0033c_Joint_Training_of_Puppet_and_Cases_and_Closeups_and_Closeupsconf--RetinaNet-Resnet152-body-shots.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0033d_Joint_Training_of_Puppet_and_Cases_and_Closeups_and_Closeupsconf--RetinaNet-Resnet152-body-shots.csv'),
        )
    },
    {
        'label': '0033 Joint Training Puppet Cases Body Shots Fullsize',
        'caption': '0033: Joint Training Puppet Cases Body Shots Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0033a_Joint_Training_of_Puppet_and_Cases_and_Closeups_and_Closeupsconf--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0033b_Joint_Training_of_Puppet_and_Cases_and_Closeups_and_Closeupsconf--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0033c_Joint_Training_of_Puppet_and_Cases_and_Closeups_and_Closeupsconf--RetinaNet-Resnet152-body-shots-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0033d_Joint_Training_of_Puppet_and_Cases_and_Closeups_and_Closeupsconf--RetinaNet-Resnet152-body-shots-fullsize.csv'),
        )
    },
    {
        'label': '0033 Joint Training Puppet Cases All Cases',
        'caption': '0033: Joint Training Puppet Cases All Cases',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0033a_Joint_Training_of_Puppet_and_Cases_and_Closeups_and_Closeupsconf--RetinaNet-Resnet152-all-cases.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0033b_Joint_Training_of_Puppet_and_Cases_and_Closeups_and_Closeupsconf--RetinaNet-Resnet152-all-cases.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0033c_Joint_Training_of_Puppet_and_Cases_and_Closeups_and_Closeupsconf--RetinaNet-Resnet152-all-cases.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0033d_Joint_Training_of_Puppet_and_Cases_and_Closeups_and_Closeupsconf--RetinaNet-Resnet152-all-cases.csv'),
        )
    },
    {
        'label': '0033 Joint Training Puppet Cases All Cases Fullsize',
        'caption': '0033: Joint Training Puppet Cases All Cases Fullsize',
        'calculate_group_average': True,
        'tables': (
            ('RetinaNet 152 a', 'evaluation/eval-0033a_Joint_Training_of_Puppet_and_Cases_and_Closeups_and_Closeupsconf--RetinaNet-Resnet152-all-cases-fullsize.csv'),
            ('RetinaNet 152 b', 'evaluation/eval-0033b_Joint_Training_of_Puppet_and_Cases_and_Closeups_and_Closeupsconf--RetinaNet-Resnet152-all-cases-fullsize.csv'),
            ('RetinaNet 152 c', 'evaluation/eval-0033c_Joint_Training_of_Puppet_and_Cases_and_Closeups_and_Closeupsconf--RetinaNet-Resnet152-all-cases-fullsize.csv'),
            ('RetinaNet 152 d', 'evaluation/eval-0033d_Joint_Training_of_Puppet_and_Cases_and_Closeups_and_Closeupsconf--RetinaNet-Resnet152-all-cases-fullsize.csv'),
        )
    },
   

    
)