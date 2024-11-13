"""3nd migrations

Revision ID: 65872b69fd8c
Revises: 193a0935bb96
Create Date: 2024-10-24 18:53:56.485007

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '65872b69fd8c'
down_revision: Union[str, None] = '193a0935bb96'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
