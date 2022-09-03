"""create posts table

Revision ID: e354eddd9d8b
Revises: 
Create Date: 2022-09-03 12:17:49.804671

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e354eddd9d8b"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
