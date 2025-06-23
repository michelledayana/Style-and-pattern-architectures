from flask import Flask
from flask_graphql import GraphQLView
import graphene

# Definir esquema GraphQL
class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="Mundo"))

    def resolve_hello(self, info, name):
        return f"Hola, {name}!"

schema = graphene.Schema(query=Query)

# Crear la app Flask
app = Flask(__name__)
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # Habilita la interfaz gráfica para pruebas
    )
)

if __name__ == '__main__':
    app.run(debug=True)