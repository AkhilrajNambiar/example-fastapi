"""add foreign-key constraint to posts table

Revision ID: c68e4c48843f
Revises: ffc71cc0d63a
Create Date: 2022-09-03 13:29:09.656522

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c68e4c48843f"
down_revision = "ffc71cc0d63a"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "posts_users_fkey",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade() -> None:
    op.drop_constraint("posts_users_fkey", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
