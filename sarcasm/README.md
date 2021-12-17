This contains the codebase for processing of Sarcasm emotions.

**It contains three main folders:**
`annotations` - this folder contains, the train, val and test data mappings i.e., the name of the image and the corresponding captons in .json format. 
`classifier` - contains .ipynb for building classifier for positive emotion. 
`evaluations` - this is the folder used to save all the features extracted using the above code. 

**It contains three main files:**
`Negative_im_feats.ipynb` - notebook for generating image features and text features of negative examples. 
`Positive_im_feats.ipynb` - notebook for generating image features and text features of positive examples. 
`Positive_Evaluation_Classification_base.ipynb` - Model which contains Training code using XGB. 


