from imageai.Prediction.Custom import CustomImagePrediction
import os
execution_path = "C:\\Users\\user\\Desktop\\0322\\"


prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(os.path.join(execution_path, "models\\model_ex-100_acc-0.959821.h5"))
prediction.setJsonPath(os.path.join(execution_path, "json\\model_class.json"))
prediction.loadModel(num_objects=2)

path = "./testcase\\"

for i, fname in enumerate(os.listdir(path)):
    predictions, probabilities = prediction.predictImage((os.path.join(path, fname)), result_count=2)

    print("Prediction for "+fname)
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        print(eachPrediction + " : " + eachProbability)

