import graphene

from products import schema as products_schema


class Query(products_schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
