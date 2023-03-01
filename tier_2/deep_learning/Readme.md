
Surface observation processing involves collecting and analyzing weather observations taken at the Earth's surface to produce weather forecasts and warnings and understand weather patterns. Machine learning can be applied to surface observation processing to improve the accuracy of forecasts, automate the process, and ensure quality control of the observations. In this notebook, we will use deep learning techniques to improve temperature forecasts by predicting the difference between the observed temperature at a weather station and the temperature forecasted by the ECMWF Integrated Forecast System. We will explore physically motivated predictors to achieve this goal.

This lesson provides notebooks in both Pytorch and Tensorflow, you can explore their differences interactively and read a short description below.

## Running the code

You can run the notebooks interactively on your own machine after an appropriate setup.

### Run Locally

We provide a requirements file to pip install the tensorflow and pytorch versions for convenience:

```
pip install -r requirements-pytorch.txt
```

and for tensorflow

```
pip install -r requirements-tensorflow.txt
```

You may need to check that this installed the correct version and provides the GPU version of pytorch or tensorflow respectively, if your local hardware can provide GPU-capabilities.

### Run Online

Alternatively, the buttons in each section launch the notebooks on free (with limitations) platforms.

- Google Colab
- Paperspace Gradient
- AWS Sagemaker Studio Lab
- Deepnote

On most of these platforms, you'll need to activate GPU access and install some of the packages as outlined in the notebooks.

- [Guide to Google Colab](https://www.youtube.com/watch?v=inN8seMm7UI)
- [Guide to Paperspace Gradient](https://blog.paperspace.com/gradient-community-notebook-guide/)
- [Guide to AWS Studio Lab](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lab.html)
- [Guide to Deepnote](https://deepnote.com/docs/deepnote-first-steps)

## Surface Observation Prediction in Pytorch

[![](https://img.shields.io/badge/view-notebook-orange)](tier_2/deep_learning/Surface_Observation_Prediction_in_Pytorch.ipynb) [![](https://img.shields.io/badge/open-colab-yellow)](https://colab.research.google.com/github/ecmwf-projects/mooc-machine-learning-weather-climate/blob/main/tier_2/deep_learning/Surface_Observation_Prediction_in_Pytorch.ipynb) [![Gradient](https://assets.paperspace.io/img/gradient-badge.svg)](https://console.paperspace.com/github/ecmwf-projects/mooc-machine-learning-weather-climate/blob/main/tier_2/deep_learning/Surface_Observation_Prediction_in_Pytorch.ipynb) [![Open%20In%20SageMaker%20Studio%20Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/ecmwf-projects/mooc-machine-learning-weather-climate/blob/main/tier_2/deep_learning/Surface_Observation_Prediction_in_Pytorch.ipynb) [![Launch%20in%20Deepnote](https://deepnote.com/buttons/launch-in-deepnote-small.svg)](https://deepnote.com/launch?url=https%3A%2F%2Fgithub.com%2Fecmwf-projects%2Fmooc-machine-learning-weather-climate%2Fblob%2Fmain%2Ftier_2/deep_learning%2FSurface_Observation_Prediction_in_Pytorch.ipynb)

PyTorch is a popular open-source machine learning framework based on the Torch library. It provides a powerful array of tools for building and training neural networks, with a focus on flexibility, speed, and ease of use.

People might prefer PyTorch because of its dynamic computational graph, which allows for more flexible and efficient model building compared to other frameworks that use static graphs. This makes it easier to experiment with different model architectures and to debug models. Additionally, PyTorch has a more "pythonic" interface and still provides great support for GPU acceleration, making it well-suited for large-scale machine learning tasks. 

PyTorch Lightning is a lightweight wrapper for PyTorch that provides a high-level interface for building complex deep learning models. It abstracts away many of the low-level details of PyTorch, allowing users to focus on model design and hyperparameter tuning. PyTorch Lightning also provides built-in support for common tasks like training, model checkpointing, and early stopping. This makes it well-suited for both research and production-level use cases.

Finally, PyTorch is backed by a large community of developers and researchers, making it easy to find help and resources online, with many new research papers published in Pytorch initially.

## Surface Observation Prediction in Tensorflow

[![](https://img.shields.io/badge/view-notebook-orange)](tier_2/deep_learning/Surface_Observation_Prediction_in_Tensorflow.ipynb) [![](https://img.shields.io/badge/open-colab-yellow)](https://colab.research.google.com/github/ecmwf-projects/mooc-machine-learning-weather-climate/blob/main/tier_2/deep_learning/Surface_Observation_Prediction_in_Tensorflow.ipynb) [![Gradient](https://assets.paperspace.io/img/gradient-badge.svg)](https://console.paperspace.com/github/ecmwf-projects/mooc-machine-learning-weather-climate/blob/main/tier_2/deep_learning/Surface_Observation_Prediction_in_Tensorflow.ipynb) [![Open%20In%20SageMaker%20Studio%20Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/ecmwf-projects/mooc-machine-learning-weather-climate/blob/main/tier_2/deep_learning/Surface_Observation_Prediction_in_Tensorflow.ipynb) [![Launch%20in%20Deepnote](https://deepnote.com/buttons/launch-in-deepnote-small.svg)](https://deepnote.com/launch?url=https%3A%2F%2Fgithub.com%2Fecmwf-projects%2Fmooc-machine-learning-weather-climate%2Fblob%2Fmain%2Ftier_2/deep_learning%2FSurface_Observation_Prediction_in_Tensorflow.ipynb)

TensorFlow is an open-source machine learning framework developed by Google. It provides a comprehensive suite of tools for building and training neural networks, including pre-built modules for popular deep learning architectures.

People might prefer TensorFlow because of its highly optimized computational graph, which allows for fast and efficient model building and training, especially on large datasets. TensorFlow is also highly scalable, allowing for easy distribution of computations across multiple GPUs or machines. Additionally, TensorFlow provides great support for production-level deployment of machine learning models, making it well-suited for building end-to-end machine learning pipelines. 

Keras is an open-source neural network library commonly used on top of Tensorflow. It provides a user-friendly interface for building and training neural networks, with a focus on ease of use and simplicity. Keras supports multiple backends, including TensorFlow, Theano, and Microsoft Cognitive Toolkit, and provides built-in support for popular deep learning architectures like Convolutional Neural Networks (CNNs) and Recurrent Neural Networks (RNNs). Keras is highly customizable, making it easy to experiment with different model architectures and hyperparameters. It is a popular choice for both beginners and experienced deep learning practitioners.

Finally, TensorFlow has a large and active community of developers and researchers, which means there are many resources and libraries available to users.