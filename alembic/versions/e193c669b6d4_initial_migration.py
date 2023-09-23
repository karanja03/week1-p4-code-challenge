"""Initial migration

Revision ID: e193c669b6d4
Revises: 
Create Date: 2023-09-23 16:05:39.946192

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e193c669b6d4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'pizzas',
        sa.Column('id', sa.String(255), primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('ingredients', sa.String, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('pizzas')
