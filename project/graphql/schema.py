import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

from project.user.models.user import User as UserModel
from project.user.models.role import Role as RoleModel
from project.user.models.user_roles import UserRoles as UserRolesModel


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node, )


class Role(SQLAlchemyObjectType):
    class Meta:
        model = RoleModel
        interfaces = (relay.Node, )


class UserRoles(SQLAlchemyObjectType):
    class Meta:
        model = UserRolesModel
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allows sorting over multiple columns, by default over the primary key
    all_roles = SQLAlchemyConnectionField(Role)
    # Disable sorting over this field
    all_users = SQLAlchemyConnectionField(User, sort=None)
    # Allow only single column sorting
    all_user_roles = SQLAlchemyConnectionField(UserRoles, sort=UserRoles.sort_argument())


schema = graphene.Schema(query=Query, types=[User, Role, UserRoles])
