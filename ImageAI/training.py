from imageai.Prediction.Custom import ModelTraining

model_trainer = ModelTraining()
model_trainer.setModelTypeAsResNet()
model_trainer.setDataDirectory("object")
model_trainer.trainModel(num_objects=2, num_experiments=100, enhance_data=True, batch_size=32, show_network_summary=True)
