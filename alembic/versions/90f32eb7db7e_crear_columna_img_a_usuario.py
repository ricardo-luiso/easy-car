"""crear columna img a usuario

Revision ID: 90f32eb7db7e
Revises: a521eac6dc9c
Create Date: 2025-06-23 12:31:56.452771

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '90f32eb7db7e'
down_revision: Union[str, None] = 'a521eac6dc9c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('auto', schema=None) as batch_op:
        batch_op.add_column(sa.Column('imagen', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('auto', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'estadoventa', ['estado_id'], ['id'])
        batch_op.drop_column('imagen')

    # ### end Alembic commands ###
