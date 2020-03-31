# Training a Waste Detector in tensorflow

## Recyclable dataset
The dataset is collection of 14122 images and four categories of glass, paper, metal and platistic. The detailed informaiton can be found in the folder [Haihua-Trash-Data](./Haihua-Trash-Data). You can Download the dataset in png format and in tfrecord format from [Baidu Cloud Disk](https://pan.baidu.com/s/1phli_jXif7ozPMJ1Atv43Q). Please contact us for the access code if you want to use the dataset.

## Tensorflow Object Detector API
The TensorFlow Object Detection API is an open source framework built on top of TensorFlow that makes it easy to construct, train and deploy object detection models.


## Installation

### Install dependencies using pip:

``` bash
pip install Cython
pip install contextlib2
pip install pillow
pip install lxml
pip install matplotlib
```
<!-- common_typos_disable -->
**Note**: sometimes "sudo apt-get install protobuf-compiler" will install
Protobuf 3+ versions for you and some users have issues when using 3.5.
If that is your case, try the [manual](#Manual-protobuf-compiler-installation-and-usage) installation.

### COCO API installation

Download the
[cocoapi](https://github.com/cocodataset/cocoapi) and
copy the pycocotools subfolder to the tensorflow/models/research directory if
you are interested in using COCO evaluation metrics. The default metrics are
based on those used in Pascal VOC evaluation. To use the COCO object detection
metrics add `metrics_set: "coco_detection_metrics"` to the `eval_config` message
in the config file. To use the COCO instance segmentation metrics add
`metrics_set: "coco_mask_metrics"` to the `eval_config` message in the config
file.

```bash
git clone https://github.com/cocodataset/cocoapi.git
cd cocoapi/PythonAPI
make
cp -r pycocotools <path_to_tensorflow>/models/research/
```

### Manual protobuf-compiler installation and usage

The Tensorflow Object Detection API uses Protobufs to configure model and
training parameters. Before the framework can be used, the Protobuf libraries
must be compiled. This should be done by running the following command from
the DesignAIR-ME336 directory:

```bash
# From tensorflow/models/research/
./bin/protoc object_detection/protos/*.proto --python_out=.
```

### Add Libraries to PYTHONPATH

When running locally, the DesignAIR/ and DesignAIR/slim directories
should be appended to PYTHONPATH. This can be done by adding the following line to ~/.bashrc

``` bash
# From tensorflow/models/research/
export PYTHONPATH=$PYTHONPATH:`path-to-DesignAIR`:`path-to-DesignAIR`/slim
```
