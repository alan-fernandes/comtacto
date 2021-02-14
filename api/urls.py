from django.urls import path
from cliente.api import cliente_list,cliente_detail_change_and_delete
from fornecedor.api import fornecedor_list,fornecedor_detail_change_and_delete
from produto.api import produto_list,produto_detail_change_and_delete
from pedido.api import pedido_list,pedido_detail_change_and_delete
from representante.api import representante_list,representante_detail_change_and_delete


urlpatterns = [
    path('cliente', cliente_list),
    path('cliente/<int:pk>/', cliente_detail_change_and_delete),
    path('fornecedor', fornecedor_list),
    path('fornecedor/<int:pk>/', fornecedor_detail_change_and_delete),
    path('produto', produto_list),
    path('produto/<int:pk>/', produto_detail_change_and_delete),
    path('pedido', pedido_list),
    path('pedido/<int:pk>/', pedido_detail_change_and_delete),
    path('representante', representante_list),
    path('representante/<int:pk>/', representante_detail_change_and_delete),

]