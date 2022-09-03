"""add content column to posts table

Revision ID: f4cd4eae4a4d
Revises: e354eddd9d8b
Create Date: 2022-09-03 13:12:10.391765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f4cd4eae4a4d"
down_revision = "e354eddd9d8b"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
