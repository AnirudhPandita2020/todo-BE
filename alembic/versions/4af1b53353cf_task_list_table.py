"""task list table

Revision ID: 4af1b53353cf
Revises: 62d4ed6b552a
Create Date: 2022-03-05 20:43:34.360939

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4af1b53353cf'
down_revision = '62d4ed6b552a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('list',sa.Column('id',sa.Integer(),autoincrement=True,primary_key=True,nullable=False),
                    sa.Column('title',sa.String(),nullable=False),
                    sa.Column('content',sa.String(),nullable=False),
                    sa.Column('userid',sa.Integer(),sa.ForeignKey("users.id",ondelete="CASCADE"),nullable=False),
                    sa.Column('is_completed',sa.Boolean(),server_default='False',nullable=False),
                    sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('now()')))


def downgrade():
    op.drop_table('list')
