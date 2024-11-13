"""2nd migrations

Revision ID: 193a0935bb96
Revises: cf81b8f9c9a6
Create Date: 2024-10-24 18:50:23.468850

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '193a0935bb96'
down_revision: Union[str, None] = 'cf81b8f9c9a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
