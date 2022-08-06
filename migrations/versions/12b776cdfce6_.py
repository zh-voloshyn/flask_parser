"""empty message

Revision ID: 12b776cdfce6
Revises: 
Create Date: 2022-03-24 17:37:33.500719

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12b776cdfce6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('itemsOZON',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('brand', sa.String(length=100), nullable=True),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('final_price', sa.Float(), nullable=True),
    sa.Column('link', sa.String(length=100), nullable=True),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_itemsOZON_link'), 'itemsOZON', ['link'], unique=True)
    op.create_index(op.f('ix_itemsOZON_title'), 'itemsOZON', ['title'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_itemsOZON_title'), table_name='itemsOZON')
    op.drop_index(op.f('ix_itemsOZON_link'), table_name='itemsOZON')
    op.drop_table('itemsOZON')
    # ### end Alembic commands ###
