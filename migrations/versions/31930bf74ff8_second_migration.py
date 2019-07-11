"""Second Migration

Revision ID: 31930bf74ff8
Revises: 9f614c6cc8d3
Create Date: 2019-07-11 11:54:55.842865

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31930bf74ff8'
down_revision = '9f614c6cc8d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'booking', ['id'])
    op.create_unique_constraint(None, 'pitch', ['id'])
    op.create_unique_constraint(None, 'user', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_constraint(None, 'pitch', type_='unique')
    op.drop_constraint(None, 'booking', type_='unique')
    # ### end Alembic commands ###
