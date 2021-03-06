"""empty message

Revision ID: aa8d6357b215
Revises: 4dc5cafdeb23
Create Date: 2020-01-15 01:06:54.253090

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'aa8d6357b215'
down_revision = '4dc5cafdeb23'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('username', sa.String(length=80), nullable=False))
    op.drop_index('timothy', table_name='person')
    op.create_unique_constraint(None, 'person', ['username'])
    op.drop_column('person', 'timothy')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('timothy', mysql.VARCHAR(length=80), nullable=False))
    op.drop_constraint(None, 'person', type_='unique')
    op.create_index('timothy', 'person', ['timothy'], unique=True)
    op.drop_column('person', 'username')
    # ### end Alembic commands ###
