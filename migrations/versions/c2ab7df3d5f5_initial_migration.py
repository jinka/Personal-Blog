"""Initial Migration

Revision ID: c2ab7df3d5f5
Revises: 8b12b4ddf903
Create Date: 2019-02-16 09:49:39.043120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2ab7df3d5f5'
down_revision = '8b12b4ddf903'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('post_title', sa.String(), nullable=True),
    sa.Column('post_content', sa.String(length=1000), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('likes', sa.Integer(), nullable=True),
    sa.Column('dislikes', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('comments', sa.Column('post', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'posts', ['post'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'post')
    op.drop_table('posts')
    # ### end Alembic commands ###