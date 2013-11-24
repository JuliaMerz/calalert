from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
alert_request = Table('alert_request', pre_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String),
    Column('id_user', Integer),
    Column('url', String),
    Column('id_sensor', Integer),
    Column('priority', SmallInteger),
)

alert_request = Table('alert_request', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=60)),
    Column('id_user', Integer),
    Column('phone', String(length=20)),
    Column('id_sensor', Integer),
    Column('priority', SmallInteger),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['alert_request'].columns['url'].drop()
    post_meta.tables['alert_request'].columns['phone'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['alert_request'].columns['url'].create()
    post_meta.tables['alert_request'].columns['phone'].drop()
