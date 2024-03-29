"""new fields in user model

Revision ID: 41389e22f64d
Revises: 9af558cdcfe3
Create Date: 2019-08-21 11:10:17.924513

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41389e22f64d'
down_revision = '9af558cdcfe3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
