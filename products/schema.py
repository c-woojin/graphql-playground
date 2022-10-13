import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from products.models import Category, Product, ProductCategory


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("name", "parent_category")
        filter_fields = ["name", "parent_category"]
        interfaces = (relay.Node, )


class ProductNode(DjangoObjectType):
    class Meta:
        model = Product
        fields = ("name", "product_number", "categories")
        filter_fields = {
            "name": ["exact", "icontains", "istartswith"],
            "product_number": ["exact", "icontains"],
            "categories": ["exact"],
        }
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    category = relay.Node.Field(CategoryNode)
    categories = DjangoFilterConnectionField(CategoryNode)
    product = relay.Node.Field(ProductNode)
    products = DjangoFilterConnectionField(ProductNode)
