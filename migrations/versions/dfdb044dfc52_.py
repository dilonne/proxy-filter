"""empty message

Revision ID: dfdb044dfc52
Revises: 3f33201a5fa5
Create Date: 2018-05-12 11:24:24.085174

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'dfdb044dfc52'
down_revision = '3f33201a5fa5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('black_listed_website',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=60), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_black_listed_website_url'), 'black_listed_website', ['url'], unique=True)
    op.drop_table('approved_website')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('approved_website',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('url', mysql.VARCHAR(length=60), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_index(op.f('ix_black_listed_website_url'), table_name='black_listed_website')
    op.drop_table('black_listed_website')
    # ### end Alembic commands ###
