"""posts table created

Revision ID: 193ec783558d
Revises: 
Create Date: 2026-10-22 20:29:00.391928

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '193ec783558d'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("posts",
        sa.Column("id",sa.Integer(),nullable=False,primary_key=True),
        sa.Column("title",sa.String(),nullable=False)
        
                    )
    """Upgrade schema."""



def downgrade() -> None:
    op.drop_table("posts")
    """Downgrade schema."""
    pass
