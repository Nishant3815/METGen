# METGen: A Multimodal Emotion Generation Framework

We  present  an  emotion-based  image  captioning pipeline developed on top of transformer architecture.  We contrast this with an RNN-based image captioning baseline. We also conduct experiments using intermediate fine tuning and back-translation. We finally developed a rigorous evaluation scheme comprising of human  evaluation, MAUVE score, & classification based evaluation. We measure all our explorations against the evaluation schemes & highlight the shortcomings both qualitatively & quantitatively.

# Directory Structure

`catr`: Contains working IPYNB files to finetune the captioning tranformer model that was proposed by [CATR](https://github.com/saahiluppal/catr). It also contains the fine tunes models that were obtained using optimal hyperparameters. Refer the `README` file in the directory to know the internal files usage. 

`baseline`: Contains the baseline architecture code to train and generate captions given an input image. We are using an RNN-based image captioning module. Refer the `README` file in the directory to know the internal files usage.

`emogen`: Contains image data and annotations that were used for finetuning the catr for generating "positive" emotion captions given an image input. Refer the `README` file in the directory to know the internal files usage. 

`sarcasm`: Contains image data and annotations that were used for finetuning the catr for generating "sarcasm" emotion captions given an image input. Refer the `README` file in the directory to know the internal files usage. 
