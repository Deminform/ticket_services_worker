from sqlalchemy import URL, create_engine

connection_string = URL.create(
    'postgresql',
    username='koyeb-adm',
    password='***',
    host='ep-noisy-field-a2gi28zo.eu-central-1.pg.koyeb.app',
    database='koyebdb',
)

engine = create_engine(connection_string)