
# Deep Learning

Repositorio destinado a aulas de deep learning



### ASL Alphabet Training

A pasta 
['\asl-alphabet'](https://github.com/NycollasSobolevski/deep-learning/tree/main/asl-alphabet)
 se trata do treinamento da IA que treina a detecção de letras do 
[American Sign Language (ASL)](https://pt.wikipedia.org/wiki/ASL-phabet)
por meio de imagens retiradas do dataset 
[ASL Aplphabet](https://www.kaggle.com/datasets/grassknoted/asl-alphabet).

O arquivo 'Model.py' se trata da construção do modelo adicionando as camadas necessárias, e das configurações de treinamento (fit) 

A execução do treinamento se da no arquivo [main.py](https://github.com/NycollasSobolevski/deep-learning/blob/main/asl-alphabet/main.py)


```shell
python asl-alphabet/main.py
```

Assim ele iniciará o treinamento e salvaria os resultados das épocas na pasta ' \asl-alphabet\assets\models' e o modelo do treinamento em '.\asl-alphabet\model.h5'


### Cat vs Dogs 

A pasta
[cat-vs-dogs]()
se trata do treinamento da IA que diferencia cachorros e gatos, por meio de imagens retiradas do dataset 
[Cat vs Dogs](https://www.kaggle.com/datasets/shaunthesheep/microsoft-catsvsdogs-dataset)

No arquivo main.ipynb está o conteudo a ser estudado com alguns comentários de anotações e o arquivo main.py é o codigo a ser executado para treinar o mesmo.



## Ferramentas

### 0 - Rascunho
Contem anotações em relação ao conteudo de Deep Learning e exemplo de códigos que podem ser usados

### 1 - Tratament

No dataset de Cat-vs-dogs há inconsistencia nos dados de imagens, que no caso estão corrompidas, por este motivo foi criado uma pasta '.\1-tratament' na qual se trata de um código em .NET que verifica as imagens corrompidas dentro da pasta 'assets' (que seria o dataset 'cat-vs-dogs') e as imagens corrompidas serão excluidas, facilitando o treinamento da IA


Código feito .NET que é passado por 'args' a pasta principál aonde deseja ser excluida imagens corrompidas dentro, ele vai procurar todos as pastas filha e excluir imagens corrompidas dentro

```
dotnet run ".\{selected your folder}"
```

### 1 - Folders

Para tratamento de um dataset aonde são divididos os dados em pastas diferentes e a pessoa desejar juntar os arquivos em uma pasta somente.

Código feito em .NET que é passado por 'args' a pasta que contem as pasta dentro (sendo a pasta mãe) e a pasta filho que é o destino dos arquivos

```
    dotnet run ".\\{pasta mae}"  ".\\{pasta mae}\\{filho de destino}"
```

Um exemplo criado no repositorio está na pasta '.\1-folders\folders' aonde há as pastas '\testss', '\train' e '\val' e se executado o codigo ```dotnet run ".\\folders" ".\\folders\\train"``` ele irá copiar todos os arquivos de \testss e \val para a pasta ```\train```


# Datasets

- [Face detection Files](https://www.kaggle.com/datasets/trainingdatapro/face-detection-photos-and-labels)

- [cat-vs-dogs Files](https://www.kaggle.com/datasets/shaunthesheep/microsoft-catsvsdogs-dataset)

- [ASL alphabet Files](https://www.kaggle.com/datasets/grassknoted/asl-alphabet)