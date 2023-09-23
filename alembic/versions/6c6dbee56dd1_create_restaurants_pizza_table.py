"""Create restaurants_pizza table

Revision ID: 6c6dbee56dd1
Revises: 112b4a7353fd
Create Date: 2023-09-23 16:21:42.276941

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6c6dbee56dd1'
down_revision: Union[str, None] = '112b4a7353fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'restaurants_pizzas',
        sa.Column('id', sa.String(255), primary_key=True),
        sa.Column('pizza_id', sa.String(255), sa.ForeignKey('pizzas.id')),
        sa.Column('restaurant_id', sa.String(255), sa.ForeignKey('restaurants.id')),
        sa.Column('price', sa.Float, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False),
    )

def downgrade():
    op.drop_table('restaurants_pizzas')
