import os
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()
SECURE_BUNDLE = os.getenv(key='SECURE_BUNDLE')
username = os.getenv(key='username')
password = os.getenv(key='password')
CLIENT_ID = os.getenv(key='CLIENT_ID')
CLIENT_SECRET=os.getenv(key='CLIENT_SECRET')
TOKEN=os.getenv(key='TOKEN')

cloud_config= dict({
    'secure_connect_bundle': SECURE_BUNDLE
})

auth_provider = PlainTextAuthProvider(
    username=CLIENT_ID,
    password=CLIENT_SECRET
)

cluster = Cluster(
    cloud=cloud_config,
    auth_provider=auth_provider
)

session = cluster.connect()

row = session.execute('select release_version from system.local').one()
if row:
    pprint(row[0])
else:
    pprint('An error occurred.')
