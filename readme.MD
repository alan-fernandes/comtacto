#Informações
Sistema desenvolvido para trabalhar com API

```
api/cliente
api/cliente/<int:pk>/
api/fornecedor
api/fornecedor/<int:pk>/
api/produto
api/produto/<int:pk>/
api/pedido
api/pedido/<int:pk>/
api/representante
api/representante/<int:pk>/
```


##Instalação
```
pip3 install -r requirements.txt
```
###Criação das tabelas do banco de dados
```
python3 manage.py migrate
```

##Iniciar
```
python3 manage.py runserver
```
###Criar usuario admin
criação do usuário para interface admin

python3 manage.py createsuperuser

acesse o administrador com o usuário criado
```
/admin
```

##Visual
Interface visual entregue pela Comtac
https://xd.adobe.com/view/3b850df7-8e67-4b9d-a5c6-c332c5acdbc2-6ed6/screen/190e42c8-8d00-4551-bc12-f6b2f9d1c26f?fullscreen&hints=off





    