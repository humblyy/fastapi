"""add users table

Revision ID: 63716dc9b16c
Revises: e0429b0945d2
Create Date: 2026-10-22 21:05:19.858218

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '63716dc9b16c'
down_revision: Union[str, Sequence[str], None] = 'e0429b0945d2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("users",
    sa.Column('id',sa.Integer, primary_key=True ,nullable=False),
    sa.Column('email',sa.String,nullable=False ,unique=True),
    sa.Column('password',sa.String,nullable=False),
    sa.Column('created_at',sa.TIMESTAMP(timezone=True),server_default=sa.text("now()"),nullable=False)

        )
    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.drop_table("users")
    """Downgrade schema."""
    pass
