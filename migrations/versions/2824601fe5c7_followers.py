"""followers

Revision ID: 2824601fe5c7
Revises: da1d2bfafb5a
Create Date: 2018-11-16 23:00:23.668230

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2824601fe5c7'
down_revision = 'da1d2bfafb5a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
