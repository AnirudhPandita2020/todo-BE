"""Creating friend table

Revision ID: c02f931a55e5
Revises: 4af1b53353cf
Create Date: 2022-03-24 20:16:28.406780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c02f931a55e5'
down_revision = '4af1b53353cf'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('fr',sa.Column('fromid',sa.Integer(),sa.ForeignKey("users.id",ondelete="CASCADE"),primary_key = True,nullable = False),
                    sa.Column('toid',sa.Integer(),sa.ForeignKey("users.id",ondelete="CASCADE"),primary_key=True,nullable = False),
                    sa.Column('accepted',sa.Boolean(),server_default = 'False'))
    

def downgrade():
    op.drop_table('fr')