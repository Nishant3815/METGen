# File structure and workings

1. `dataprocessingscripts`: Contains the IPYNB file that acts as a util to convert the json data to csv and viceversa as per the need. You will need to tweek it for your custom usage.
2. `datasets`: Contains the data util file for preparing the model and dataset.
3. `feature_embeddings`: Contains the train, validation and test data feature embeddings for both image and caption. The feature are for all the experimented models and for both the emotions: positive and sarcasm.

# Fine Tuning

The script `TestHyperparameters` is used for finetuning different models on top of `CATR`. Twee the parameters to finetune the model against custom hyperparameters. The model is saved and can be used to predict caption given an image. 

# Prediction

The script `FinalPrediction` is used to predict captions based on the input model. It takes as input the paths of the model checkpoint, test image data, and annotation mapping of caption and image.  The parameters are defined at the top where the user can specify these paths and can run to generate a json file that contains the mapping of input image and the predicted caption.

# Classification

The script 'Final Classification' uses the XGBoost classification model to classify whether a generated caption incorporates the specified emotion given an input image. It then generates the classification accuracy which denotes how well the fintuned model generated the emotion text based on an image.
