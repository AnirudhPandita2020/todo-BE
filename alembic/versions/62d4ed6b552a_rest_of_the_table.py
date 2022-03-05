"""Rest of the table

Revision ID: 62d4ed6b552a
Revises: 90b4889f3a71
Create Date: 2022-03-05 17:30:18.410752

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62d4ed6b552a'
down_revision = '90b4889f3a71'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users',sa.Column('username',sa.String(),nullable=False,unique=True))
    op.add_column('users',sa.Column('email',sa.String(),nullable=False))
    op.add_column('users',sa.Column('password',sa.String(),nullable=False))
    op.add_column('users',sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('now()')))
       


def downgrade():
    op.drop_column('users','username')
    op.drop_column('users','email')
    op.drop_column('users','password')
    op.drop_column('users','created_at')
