emogen - folder which contains the codebase for processing of Positive emotions

It contains three main folders 

1. annotations -  this folder contains, the train, val and test data mappings i.e., the name of the image and the corresponding captons in .json format

2. classifier - contains .ipynb for building classifier for positive emotion


   Negative_im_feats.ipynb - notebook for generating image features and text features of negative examples
   
   
   Positive_im_feats.ipynb - notebook for generating image features and text features of positive examples
   
   
   Positive_Evaluation_Classification_base.ipynb - Model which contains Training code using XGB 
   
 3. evaluations - this is the folder used to save all the features extracted using the above code
