---
title: NLP Sequence Tasks
emoji: 💬
colorFrom: pink
colorTo: green
sdk: gradio
sdk_version: 4.31.2
app_file: app.py
pinned: false
---

# NLP sequence tasks

This is my project for homework three option three for the CMPE-258 Deep Learning with professor Liu at SJSU. 

This homework option was to create a front end for three different NLP tasks: translation, summarization, and question answering. 

To do this, I first looked at the following link as suggested: https://github.com/lkk688/DeepDataMiningLearning/blob/main/nlp/huggingfaceSequence5.py . I then saw in the comments that the backend could be achieved with the `pipeline` method from the `transformers` library. I could then follow the examples in the documentation to create the back end of the project, and build a custom front end to take a dynamic input so I could output the results.

# Development

## Installation:
1. Clone the repository.
2. create the anaconda environment with `conda env create -f environment.yml`
3. Activate the environment using `conda activate dl-hw-3`
4. Run the app with `python app.py`

## Formatting:
Black was used as a formatter to improve readability. To use, run: `black app.py`

# Examples:

## Translation
### Language Output
Set any language in the dropdown as the output

### Text to Translate
Hello my friend! How are you doing today?

## Question Answering
### Question Text
Is the sun blue?

### Context Text
The sun is yellow.

## Summarization
### Text to Summarize
Homework 3 will be our last homework assignment, offering multiple options. You can choose one of these options and submit the following:

Code Link: Share your code via a GitHub link or a Google Drive link.
Mandatory Report: Along with the code, provide a clear report that includes:
Your selected option, basic introduction of your approaches
Comparison or evaluation results/figures related to your chosen option.
A link to your code.
Please note that all options require you to modify our provided sample code (minimal modifications are acceptable). While you can refer to external sample code from reputable sources with publications, you must make significant changes to the code. If you simply download another codebase online (different from our provided code) without substantial modification, you will be asked to revise your homework during the designated revision period (which occurs only once).
We have observed instances where students share their homework code with others, leading to similar code and results. This behavior is considered plagiarism and is strictly prohibited. While it’s commendable to offer assistance to your classmates, please refrain from sharing your code directly with other students.

Option1: Object Detection based on our [Detection sample codeLinks to an external site.] for FasterRCNN or YOLOv8.

Option2: Image classification, object detection via Huggingface based on our [HFvisionmain sample codeLinks to an external site.] or [HFvisioninferenceLinks to an external site.] (If you choose one of the two tasks, you need to do both training and inference)

For these two options, your modification can be in any of the following areas: 1) Inference Acceleration and Comparison via TensorRT or TorchScript; 2) Adding a New Dataset and Performing Training and COCO Evaluation: You can enhance your model’s performance by incorporating additional data. Consider collecting a new dataset relevant to your task and fine-tuning your model. After training, evaluate its performance using the COCO evaluation metrics; 3) Model Modification, Training, and Comparison: If you want to improve your model architecture, experiment with modifications such as changing layers, adjusting hyperparameters, or using different pre-trained backbones. Train the modified model and compare its performance against the original.
Option3: NLP sequence tasks (translation, summarization, QA) based on our [Huggingface sequence sample codeLinks to an external site.]

Option4: Speech recognition tasks based on our [Huggingface audio sample codeLinks to an external site.]

 Your modification can be in any of the following areas: 1) Building an Application with Frontend and Backend for Hugging Face NLP Models: Create an application that hosts Hugging Face models for at least three NLP sequence tasks (translation, summarization, and question answering (QA)). The frontend will handle user interactions, while the backend will manage model inference and responses.; 2) Adding a New Dataset and Training for one of the NLP Sequence Tasks: Introduce a new dataset distinct from the included one. Use this dataset to train models for one of the NLP tasks like translation, summarization, and QA. After training, evaluate the model’s performance using appropriate metrics.

**NOTE: This text is the instructions of this homework assignment**