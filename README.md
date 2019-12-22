# Trash-It
"Trash It"-We'll sort it out! is a waste management system in which the main aim is to segregate the waste that is thrown by any individual in the bins(mostly roadside bins,near malls,or college campuses). The waste will be segregated either as a biodegradable or non-biodegradable waste product. We have used raspberry pi and a pi cam for detecting the object that has been placed on the top of the lid. Since the pi cam was not working, we have used a web camera for the image recognition for time being. For the image recognition, a dataset consisting of plastic,cardboard,metal,glass,paper was used and have been trained on top of resnet 50 model .A servomotor is used for turning the lids on top of each dustbin seperation, namely biodegradable and non-biodegradable.For eg, If the waste or object placed is identified as a plastic, which is non-biodegradable, the lid of non-biodegradable dustbin will get opened and the waste will be disposed. Similarly, if the object is identified as a paper which is biodegradable, then the lid on top of the biodegradable dustbin will get opened and waste will be disposed.Once the waste has been seperated, the biodegradable waste that can be decomposed can be provided to the government as a social cause, which will inturn be given to the farmers as manure. The non-biodegradable waste can be sold to companies which recycle the used plastic bottles such as CocaCola. Thus, a major challenge of India's waste management system will get resolved by using our proposed system. 

**Libraries required -**
1. Tensorflow-cpu/gpu
2. Open-Cv

**Steps to run**
1. Clone the repository to a directory
2. For personal training run the "train.py" file
3. For using the fully trained model for direct prediction run "predict.py" file

**For Connection to Raspberry Pi-**
1. Transfer the model to Raspberry Pi
2. Install tensorflow and replace opencv with picamera
3. Use the prediction to rotate the servo motor in desired direction using "servo.py" file
