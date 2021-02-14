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





    