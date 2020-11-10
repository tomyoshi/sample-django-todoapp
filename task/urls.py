from django.urls    import path
from .views         import (
    TaskList,
    TaskDetail,
    TaskDelete,
    TaskUpdate,
    TaskCreate,
)

urlpatterns = [
    path('list/', TaskList.as_view(), name='list'),
    path('detail/<int:pk>', TaskDetail.as_view(), name='detail'),
    path('delete/<int:pk>', TaskDelete.as_view(), name='delete'),
    path('update/<int:pk>', TaskUpdate.as_view(), name='update'),
    path('create/', TaskCreate.as_view(), name='create'),
]
