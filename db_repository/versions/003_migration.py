from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
alert_request = Table('alert_request', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=60)),
    Column('id_user', Integer),
    Column('url', String(length=120)),
    Column('id_sensor', Integer),
    Column('priority', SmallInteger),
)

sensor = Table('sensor', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=60)),
    Column('url', String(length=120)),
    Column('macaddress', String(length=12)),
)

alert = Table('alert', pre_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('alert_request', Integer),
    Column('alert_type', Integer),
    Column('id_feed', Integer),
    Column('id_post', Integer),
    Column('id_sensor', Integer),
    Column('id_keyword', Integer),
    Column('timestamp', DateTime),
)

alert = Table('alert', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('id_alert_request', Integer),
    Column('alert_type', Integer),
    Column('timestamp', DateTime),
    Column('id_feed', Integer),
    Column('id_post', Integer),
    Column('id_sensor', Integer),
    Column('id_keyword', Integer),
    Column('priority', SmallInteger),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['alert_request'].columns['priority'].create()
    post_meta.tables['sensor'].columns['macaddress'].create()
    pre_meta.tables['alert'].columns['alert_request'].drop()
    post_meta.tables['alert'].columns['id_alert_request'].create()
    post_meta.tables['alert'].columns['priority'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['alert_request'].columns['priority'].drop()
    post_meta.tables['sensor'].columns['macaddress'].drop()
    pre_meta.tables['alert'].columns['alert_request'].create()
    post_meta.tables['alert'].columns['id_alert_request'].drop()
    post_meta.tables['alert'].columns['priority'].drop()
