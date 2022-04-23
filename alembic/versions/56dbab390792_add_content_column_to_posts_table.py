"""add content column to posts table

Revision ID: 56dbab390792
Revises: 3d925fd5efe9
Create Date: 2022-04-18 23:18:19.224131

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56dbab390792'
down_revision = '3d925fd5efe9'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade():
    op.drop_column('posts', 'content')

