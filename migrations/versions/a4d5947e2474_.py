"""empty message

Revision ID: a4d5947e2474
Revises: 82315a58f50f
Create Date: 2020-03-28 16:22:21.667063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4d5947e2474'
down_revision = '82315a58f50f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('feedback_game_key', 'feedback', type_='unique')
    op.drop_constraint('feedback_rating_key', 'feedback', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('feedback_rating_key', 'feedback', ['rating'])
    op.create_unique_constraint('feedback_game_key', 'feedback', ['game'])
    # ### end Alembic commands ###
