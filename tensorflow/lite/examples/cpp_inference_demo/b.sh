#!/bin/bash
# build executable and run it with tflite model
# https://github.com/bazelbuild/bazelisk

MY_VAR=cpp_inference_demo

echo -e "\033[1;31m [INFO] step 1, build inf.cc into binary executable ${MY_VAR} \033[0m" &&
bazelisk build //tensorflow/lite/examples/${MY_VAR}:${MY_VAR} &&
echo -e "\033[1;31m [INFO] step 2, run ${MY_VAR} with linear.tflite \033[0m" &&
/home/aliwang/tensorflow/bazel-bin/tensorflow/lite/examples/${MY_VAR}/${MY_VAR} /home/aliwang/tensorflow/tensorflow/lite/examples/${MY_VAR}/linear.tflite &&
echo -e "\033[1;31m [INFO] finish."