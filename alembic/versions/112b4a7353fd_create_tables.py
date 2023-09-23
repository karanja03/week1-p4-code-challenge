"""Create tables

Revision ID: 112b4a7353fd
Revises: e193c669b6d4
Create Date: 2023-09-23 16:06:56.882834

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '112b4a7353fd'
down_revision: Union[str, None] = 'e193c669b6d4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


    
    
def upgrade():
    op.create_table(
        'restaurants',
        sa.Column('id', sa.String(255), primary_key=True),
        sa.Column('name', sa.String(50), unique=True, nullable=False),
        sa.Column('address', sa.String, nullable=False),
    )

def downgrade():
    op.drop_table('restaurants')

