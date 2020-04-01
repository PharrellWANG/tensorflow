# TFLite Cpp API Inference Demo

## Prerequisites

1. tf2.0

2. python 3

## Steps
 
1. create *linear.tflite*: ``python create_tflite_model.py``

2. create *libtensorflow-lite.a*: https://www.tensorflow.org/lite/guide/build_arm64

3. find *libtensorflow-lite.a*: ``sudo find . -name 'libtensorflow-lite.a``

4. build executable from .cc file and run it with tflite model: ``. ./b.sh``

## ref

https://stackoverflow.com/questions/56837288/tensorflow-lite-c-api-example-for-inference
