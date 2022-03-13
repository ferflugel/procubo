# Emotion Recognition

## Baseline model
The first baseline model was based on the code from https://towardsdatascience.com/convert-your-emotion-recognition-notebook-into-an-api-without-extra-code-bc13421d2ed5 and was written by Sushanti Kerani.
It had accuracy of 0.93 on the training set but only around 0.62 on the validation set.
The images were collected from https://www.kaggle.com/jonathanoheix/face-expression-recognition-dataset and are freely available. 
We slightly modified the dataset, removing classes we did not intend to use.

## FER model
FER is a Python library built and maintained by Justin Shenk and available at https://pypi.org/project/fer/.
The information related to it and the code initially used was taken from https://towardsdatascience.com/the-ultimate-guide-to-emotion-recognition-from-facial-expressions-using-python-64e58d4324ff
and adapted for our needs.
