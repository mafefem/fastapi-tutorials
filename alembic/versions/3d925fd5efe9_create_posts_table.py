"""create posts table

Revision ID: 3d925fd5efe9
Revises: 
Create Date: 2022-04-18 23:10:46.266581

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d925fd5efe9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    
    
def downgrade():
    op.drop_table('posts')
