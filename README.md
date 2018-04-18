# reconhecimento-faustao
Reconhecimento facial de Faustões

Orra meu, este pequeno Script Python identifica se há um Fastão na imagem indicada

# Pré-requisitos
Apenas rode 
```
pip3 install face_recognition
```

Para rodas as aplicações com "interface gráfica", também precisaremos do CV2
```
pip3 install opencv-python
```

# Como rodar

## Versão com interface:
```
identificar.py teste\faustao-1.jpg
```

## Versão CLI

```
comparar.py teste\faustao-1.jpg teste\faustao-2.jpg teste\faustoes.jpg teste\luciano-huck.jpg
```

# Como aumentar a precisão (treinar mais rostos)

Apenas rodando o treino.py é no necessário para gerar um novo dataset com os rostos necessários.
Basta apenas adicionar os Fautões que queira treinar na pasta treino.

Lembre-se de deletar o dataset.dat antes de treinar novamente!