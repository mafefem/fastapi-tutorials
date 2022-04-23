"""add last few columns in posts table

Revision ID: 92f548321058
Revises: bde01ddc2dbc
Create Date: 2022-04-18 23:47:51.509846

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92f548321058'
down_revision = 'bde01ddc2dbc'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
