#coding:utf-8
from learn.models import Student
from haystack import indexes
class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    # 对title字段进行索引
    name = indexes.CharField(model_attr='name')
    unit = indexes.CharField(model_attr='unit')
    def get_model(self):
        return Student

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
