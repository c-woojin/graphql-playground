import graphene
from graphene_django import DjangoObjectType

from products.models import Category, Product, ProductCategory


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "parent_category")


class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)

    def resolve_categories(root, info):
        return Category.objects.all()


schema = graphene.Schema(query=Query)
