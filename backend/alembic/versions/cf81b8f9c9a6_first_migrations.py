"""first migrations

Revision ID: cf81b8f9c9a6
Revises: 72275d322c6d
Create Date: 2024-10-24 18:49:41.116648

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cf81b8f9c9a6'
down_revision: Union[str, None] = '72275d322c6d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
