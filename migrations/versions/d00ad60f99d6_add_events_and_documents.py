"""add events and documents

Revision ID: d00ad60f99d6
Revises: a1691597803e
Create Date: 2018-03-01 16:51:13.094017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd00ad60f99d6'
down_revision = 'a1691597803e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('document',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('filename', sa.String(length=255), nullable=True),
    sa.Column('link', sa.String(length=255), nullable=True),
    sa.Column('supervisor', sa.String(length=255), nullable=True),
    sa.Column('text', sa.String(length=1000000), nullable=True),
    sa.Column('title', sa.String(length=500), nullable=True),
    sa.Column('type', sa.String(length=500), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('description', sa.String(length=1500), nullable=True),
    sa.Column('diploma', sa.Boolean(), nullable=True),
    sa.Column('employer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['employer_id'], ['employer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('employer', sa.Column('avatar_hash', sa.String(length=128), nullable=True))
    op.add_column('employer', sa.Column('contacts', sa.String(length=500), nullable=True))
    op.add_column('employer', sa.Column('description', sa.String(length=1500), nullable=True))
    op.add_column('student', sa.Column('avatar_hash', sa.String(length=128), nullable=True))
    op.add_column('student', sa.Column('contacts', sa.String(length=500), nullable=True))
    op.add_column('student', sa.Column('cv_hash', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('student', 'cv_hash')
    op.drop_column('student', 'contacts')
    op.drop_column('student', 'avatar_hash')
    op.drop_column('employer', 'description')
    op.drop_column('employer', 'contacts')
    op.drop_column('employer', 'avatar_hash')
    op.drop_table('event')
    op.drop_table('document')
    # ### end Alembic commands ###
