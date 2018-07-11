"""empty message

Revision ID: 90afdddfa10b
Revises:
Create Date: 2018-07-11 16:54:27.484879

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90afdddfa10b'
down_revision = None
branch_labels = None
depends_on = 'e5e40a862da0'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('organisation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(length=128), nullable=True),
    sa.Column('url', sa.Unicode(length=255), nullable=True),
    sa.Column('logo', sa.Unicode(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.Column('summary', sa.Unicode(length=255), nullable=True),
    sa.Column('details', sa.UnicodeText(), nullable=True),
    sa.Column('is_hidden', sa.Boolean(), nullable=True),
    sa.Column('is_featured', sa.Boolean(), nullable=True),
    sa.Column('token_edit', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('resource',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('description', sa.UnicodeText(), nullable=True),
    sa.Column('path', sa.Unicode(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('projects_resources',
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.Column('resource_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.ForeignKeyConstraint(['resource_id'], ['resource.id'], )
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.Unicode(length=16), nullable=True),
    sa.Column('fullname', sa.Unicode(length=128), nullable=True),
    sa.Column('email', sa.Unicode(length=128), nullable=True),
    sa.Column('phone', sa.Unicode(length=32), nullable=True),
    sa.Column('notes', sa.UnicodeText(), nullable=True),
    sa.Column('organisation_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['organisation_id'], ['organisation.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('projects_users',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('projects_users')
    op.drop_table('user')
    op.drop_table('projects_resources')
    op.drop_table('resource')
    op.drop_table('project')
    op.drop_table('organisation')
    # ### end Alembic commands ###
