"""empty message

Revision ID: f324de4b50f1
Revises: ac913428ba37
Create Date: 2016-10-16 01:06:32.381207

"""

# revision identifiers, used by Alembic.
revision = 'f324de4b50f1'
down_revision = 'ac913428ba37'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('indemnity',
    sa.Column('deputy_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('value', sa.String(length=255), nullable=True),
    sa.Column('category', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['deputy_id'], ['deputy.id'], ),
    sa.PrimaryKeyConstraint('deputy_id', 'date', 'category_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('indemnity')
    ### end Alembic commands ###
