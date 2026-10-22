"""add remaining columns of posts

Revision ID: 1adc229ef1bd
Revises: fdd47d222890
Create Date: 2026-10-22 21:55:49.909441

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1adc229ef1bd'
down_revision: Union[str, Sequence[str], None] = 'fdd47d222890'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts",
    sa.Column("published",sa.Boolean(),server_default="True" ,nullable=False)),
    op.add_column("posts",
        sa.Column("created_at",sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'),nullable=False)
        )
    pass


def downgrade() -> None:
    op.drop_column("posts","published")
    op.drop_column("posts","created_at")
    """Downgrade schema."""
    pass
