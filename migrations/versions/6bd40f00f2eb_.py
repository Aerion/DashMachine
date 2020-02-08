"""empty message

Revision ID: 6bd40f00f2eb
Revises: d87e35114b0b
Create Date: 2020-02-05 18:41:57.209232

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6bd40f00f2eb"
down_revision = "d87e35114b0b"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("apps", sa.Column("groups", sa.String(), nullable=True))
    op.add_column(
        "settings", sa.Column("home_access_groups", sa.String(), nullable=True)
    )
    op.add_column("settings", sa.Column("roles", sa.String(), nullable=True))
    op.add_column(
        "settings", sa.Column("settings_access_groups", sa.String(), nullable=True)
    )
    op.add_column("user", sa.Column("role", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user", "role")
    op.drop_column("settings", "settings_access_groups")
    op.drop_column("settings", "roles")
    op.drop_column("settings", "home_access_groups")
    op.drop_column("apps", "groups")
    # ### end Alembic commands ###
