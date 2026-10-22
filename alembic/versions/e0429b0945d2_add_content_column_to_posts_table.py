"""add content column to posts table

Revision ID: e0429b0945d2
Revises: 193ec783558d
Create Date: 2026-10-22 20:56:41.065727

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e0429b0945d2'
down_revision: Union[str, Sequence[str], None] = '193ec783558d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts",sa.Column("content",sa.String(),nullable=False))
    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.drop_column("posts",'content')
    """Downgrade schema."""
    pass
