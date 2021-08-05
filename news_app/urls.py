
from django.urls import path

from . import views




urlpatterns = [

    path('news/list', views.NewsList.as_view()),
    # получить весь список новостей и создание новости

    path('news/<int:pk>', views.NewsDetail.as_view()),
    # получить одну новость, обновление, удаление

    path('category/list', views.CategoryList.as_view()),
    # получить весь список категорий и создание категории

]