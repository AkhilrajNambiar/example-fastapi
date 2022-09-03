"""add last few columns to posts table

Revision ID: 613e1db0bddd
Revises: c68e4c48843f
Create Date: 2022-09-03 13:39:39.187372

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "613e1db0bddd"
down_revision = "c68e4c48843f"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_default="true"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
    )
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
