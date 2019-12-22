from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.layers import Dense
from tensorflow.keras.applications.resnet50 import preprocess_input

gen = ImageDataGenerator(preprocessing_function=preprocess_input)
resnet_path = 'resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5'

model = Sequential()
model.add(ResNet50(include_top=False,pooling='avg',weights=resnet_path))
model.add(Dense(2,activation='softmax'))
model.layers[0].trainable = False
model.summary()

traingen = gen.flow_from_directory('train',
									target_size=(224,224),
									batch_size=32,
									class_mode='categorical')

valgen = gen.flow_from_directory('val',
								  target_size=(224,224),
								  batch_size=32,
								  class_mode='categorical')

from tensorflow.python.keras.callbacks import EarlyStopping, ModelCheckpoint

EARLY_STOP_PATIENCE = 3
cb_early_stopper = EarlyStopping(monitor = 'val_loss', patience = EARLY_STOP_PATIENCE)
cb_checkpointer = ModelCheckpoint(filepath = 'best.h5', monitor = 'val_loss', save_best_only = True, mode = 'auto')

STEPS_PER_EPOCH_TRAINING = 199
NUM_EPOCHS = 10
STEPS_PER_EPOCH_VALIDATION = 10

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

fit_history = model.fit_generator(
        traingen,
        steps_per_epoch=STEPS_PER_EPOCH_TRAINING,
        epochs = NUM_EPOCHS,
        validation_data=valgen,
        validation_steps=STEPS_PER_EPOCH_VALIDATION,
        callbacks=[cb_checkpointer, cb_early_stopper]
)
