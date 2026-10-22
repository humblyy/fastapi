"""add user id column to posts

Revision ID: fdd47d222890
Revises: 63716dc9b16c
Create Date: 2026-10-22 21:40:40.313193

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fdd47d222890'
down_revision: Union[str, Sequence[str], None] = '63716dc9b16c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts",sa.Column("user_id",sa.Integer(),nullable=False))
    op.create_foreign_key("posts_users_fk",source_table="posts",referent_table='users',local_cols=["user_id"],remote_cols=["id"],ondelete='CASCADE')
    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.drop.constraint("posts_users_fk",table_name="posts")
    op.drop_column("posts","user_id")
    """Downgrade schema."""
    pass
