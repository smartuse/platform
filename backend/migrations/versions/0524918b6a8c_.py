"""empty message

Revision ID: 0524918b6a8c
Revises: d51cbebf0684
Create Date: 2019-04-03 14:51:56.793794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0524918b6a8c'
down_revision = 'd51cbebf0684'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table('projects_resources')
    op.rename_table('resource', 'rendering')
    op.create_table('projects_renderings',
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.Column('rendering_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.ForeignKeyConstraint(['rendering_id'], ['rendering.id'], )
    )
    op.drop_column('rendering', 'notes')
    op.drop_column('project', 'notes')

def downgrade():
    op.drop_table('projects_renderings')
    op.rename_table('rendering', 'resource')
    op.create_table('projects_resources',
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.Column('resource_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.ForeignKeyConstraint(['resource_id'], ['resource.id'], )
    )
    op.add_column('resource', sa.Column('notes', sa.Unicode(), nullable=True))
    op.add_column('project', sa.Column('notes', sa.Unicode(), nullable=True))
