# Adversarial-Toxic

## Overview
Toxic language threatens the continuity of online communities as a safe space for sharing information. To limit the effect of this threat, platforms use automatic language classification tools, often powered by deep learning classifiers. Like most deep learning models, these systems are vulnerable to adversarial attacks, defined as imperceptible modifications to input capable of changing drastically the classification output. This study explores said vulnerability experimentally, and shows that it can be reduced by adding adversarial examples to the training set. The techniques used in this work builds on [DeepWordBug](https://github.com/QData/deepWordBug) (currently expanded to [TextAttack](https://github.com/QData/TextAttack)), an open source project for the generation of black-box adversarial examples for text input. The results show that 3 types of deep neural networks (Bi-LSTM, RNN and CNN) can benefit from being trained on a set augmented by a relatively small number of adversarial examples. 

## Content 

The repository contains a Jupyter Notebook for the experiments (experiments.ipynb), along with the code and data needed to build and train the models (code/), and a report summarizing the project (report.pdf).