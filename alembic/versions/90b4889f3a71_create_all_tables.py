"""create all tables

Revision ID: 90b4889f3a71
Revises: 
Create Date: 2022-03-05 16:45:24.887041

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90b4889f3a71'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',sa.Column('id',sa.Integer(),autoincrement=True,primary_key=True,nullable=False))

def downgrade():
    op.drop_table('users')
