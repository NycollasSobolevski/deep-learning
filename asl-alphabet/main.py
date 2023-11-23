from keras import optimizers
from keras import losses
from keras import metrics
from keras import callbacks
from keras.preprocessing import image


import Model

model = Model.GenerateModel()


model.compile(
    optimizer = optimizers.SGD(),
    loss      = losses.CategoricalCrossentropy(),
    metrics   = [metrics.Accuracy(), metrics.Precision()]
)


dataGen = image.ImageDataGenerator(
    rescale         = 1.0/255,
    shear_range     = .2,
    zoom_range      = .2,
    horizontal_flip = True,
    vertical_flip   = False,
    validation_split= .2

)

directory = "./assets/asl_alphabet_train/"
batchsize = 32

X_Train = dataGen.flow_from_directory(
    directory,
    target_size= (64,64),
    batch_size = batchsize,
    class_mode = 'categorical',
    subset     = 'training'
)
X_Tests = dataGen.flow_from_directory(
    directory,
    target_size= (64,64),
    batch_size = batchsize,
    class_mode = 'categorical',
    subset     = 'validation'
)

qtd_files = len(X_Train.filenames) 
steps_per_epoch =  int(qtd_files  / batchsize) 
#! batchsize * stepsperepoch = xtrain.lengtth(qtd_files)

Model.FitModel(model, steps_per_epoch, X_Train, X_Tests)


# model.save('model')