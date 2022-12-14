"""added phone number for users

Revision ID: 23ad84c2b1ee
Revises: 52abceb82166
Create Date: 2022-09-03 14:01:30.547642

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "23ad84c2b1ee"
down_revision = "52abceb82166"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("phone_no", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "phone_no")
    # ### end Alembic commands ###
