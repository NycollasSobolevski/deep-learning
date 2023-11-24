from keras import models
from keras import layers
from keras import activations
from keras import callbacks
from keras import regularizers
from keras import initializers


def GenerateModel():
    
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

    model.add(layers.Flatten())

    model.add(layers.Dense(
        256,
        kernel_initializer = initializers.RandomNormal(stddev = 1),        
    )) 
    model.add(layers.Activation('relu'))

    model.add(layers.Dense(
        64,
        kernel_regularizer = regularizers.L1(1e-4),
    )) 

    model.add(layers.Activation('relu'))
    model.add(layers.Dropout(0.3))

    model.add(layers.Dense(
        32,
        kernel_regularizer = regularizers.L1(1e-4),
    )) 
    model.add(layers.Activation('relu'))
    model.add(layers.Dropout(0.3))

    model.add(layers.Dense(
        29,
        activation='softmax'
    )) 

    return model

def FitModel(model, steps_per_epoch, X_Train, X_Tests, epochs=50, validation_steps=100):
    model.fit(
    X_Train, 
    steps_per_epoch = steps_per_epoch,     #! batchsize / dataset.length
    epochs          = epochs,                  #!quantidade maxima de epocas a treinar
    validation_steps= validation_steps,
    callbacks       = [
        # callbacks.EarlyStopping(patience = 4),  #!se o erro nao melhorar a cada (4) epocas ele para o fit
        callbacks.ModelCheckpoint(
            filepath='./assets/models/model.{epoch:02d}-{val_loss:.2f}.h5' #! permite que o treinamento volte aonde parou

        )
    ],
    validation_data=X_Tests
)

