"""empty message

Revision ID: 9fe19ab8939f
Revises: 8c011fc5f2bc
Create Date: 2020-03-14 12:48:18.122064

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9fe19ab8939f'
down_revision = '8c011fc5f2bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuarios', sa.Column('todos', sa.String(length=400), nullable=False))
    op.create_unique_constraint(None, 'usuarios', ['username'])
    op.drop_column('usuarios', 'done')
    op.drop_column('usuarios', 'label')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuarios', sa.Column('label', mysql.VARCHAR(length=50), nullable=False))
    op.add_column('usuarios', sa.Column('done', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'usuarios', type_='unique')
    op.drop_column('usuarios', 'todos')
    # ### end Alembic commands ###
