# !pip install tensorflow
# !pip install keras

from keras import models
from keras import layers
from keras import activations
from keras import initializers
from keras import regularizers
from keras import optimizers
from keras import losses
from keras import metrics
from keras import callbacks
from keras import preprocessing
from keras.preprocessing import image


model = models.Sequential()
model.add(layers.Conv2D(
    32, (5, 5),
    input_shape =  (64, 64, 3),
    activation = 'relu'
))
model.add(layers.MaxPooling2D(
    pool_size = (2 ,2)
))

model.add(layers.Conv2D(
    16, (5, 5),
    input_shape =  (30, 30, 3),
    activation = 'relu'
))
model.add(layers.MaxPooling2D(
    pool_size = (2 ,2)
))

model.add(layers.Conv2D(
    16, (5, 5),
    input_shape = (13, 13, 3),
    activation = 'relu'
))
model.add(layers.MaxPooling2D(
    pool_size = (2 ,2)
))

model.add(layers.Flatten())

model.add(layers.Dense(
    256, #! 64 neuronios
    kernel_regularizer = regularizers.L2(1e-4),    #! tem que ser valor baixo para ele concentrar em resolver o problema e nao se preocupar em equilibrar os pesos
    kernel_initializer = initializers.RandomNormal(stddev = 1),
    bias_initializer = initializers.Zeros()
)) 
model.add(layers.Dropout(0.2))
model.add(layers.Activation(activations.relu))

model.add(layers.Dense(
    64, #! 64 neuronios
    kernel_regularizer = regularizers.L2(1e-4),    #! tem que ser valor baixo para ele concentrar em resolver o problema e nao se preocupar em equilibrar os pesos
    kernel_initializer = initializers.RandomNormal(stddev = 1),
    bias_initializer = initializers.Zeros()
)) 
model.add(layers.Activation(activations.relu))
model.add(layers.BatchNormalization())


model.add(layers.Dense(
    64, #! 64 neuronios
    kernel_regularizer = regularizers.L2(1e-4),    #! tem que ser valor baixo para ele concentrar em resolver o problema e nao se preocupar em equilibrar os pesos
    kernel_initializer = initializers.RandomNormal(stddev = 1),
    bias_initializer = initializers.Zeros()
)) 
model.add(layers.Activation(activations.relu))
model.add(layers.Dense(
    2, #! 64 neuronios
    kernel_regularizer = regularizers.L2(1e-4),    #! tem que ser valor baixo para ele concentrar em resolver o problema e nao se preocupar em equilibrar os pesos
    kernel_initializer = initializers.RandomNormal(stddev = 1),
    bias_initializer = initializers.Zeros()
)) 
model.add(layers.Activation(activations.relu))


model.compile(
    optimizer = optimizers.SGD(), #! SGD e Adam sao os mais utilizados
    loss      = losses.BinaryCrossentropy(),
    metrics   = [metrics.Accuracy()]
)



#!------------------------------------

dataGen = image.ImageDataGenerator(
    rescale         = 1.0/255,
    shear_range     = .2,
    zoom_range      = .2,
    horizontal_flip = True,
    vertical_flip   = False,
    validation_split= .2
)

directory = "Files/Photos"
X_Train = dataGen.flow_from_directory(
    directory,
    target_size= (64,64),
    batch_size = 32,
    class_mode = 'categorical',
    subset     = 'training'
)
X_Tests = dataGen.flow_from_directory(
    directory,
    target_size= (64,64),
    batch_size = 32,
    class_mode = 'categorical',
    subset     = 'validation'
)


model.fit(
    X_Train, 
    steps_per_epoch = 1000,    #! betsize / dataset.length
    epochs          = 50,       #!quantidade maxima de epocas a treinar
    validation_steps= 100,
    callbacks       = [
        callbacks.EarlyStopping(patience = 4),  #!se o erro nao melhorar a cada (4) epocas ele para o fit
        callbacks.ModelCheckpoint(
            filepath='model.{epoch:02d}-{val_loss:.2f}.h5' #! permite que o treinamento volte aonde parou

        )
    ]
)

model.save('model')