from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
post = Table('post', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('timestamp', DateTime),
    Column('id_feed', Integer),
    Column('url', String(length=120)),
)

alert = Table('alert', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('alert_request', Integer),
    Column('alert_type', Integer),
    Column('timestamp', DateTime),
    Column('id_feed', Integer),
    Column('id_post', Integer),
    Column('id_sensor', Integer),
    Column('id_keyword', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['post'].columns['timestamp'].create()
    post_meta.tables['alert'].columns['timestamp'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['post'].columns['timestamp'].drop()
    post_meta.tables['alert'].columns['timestamp'].drop()
