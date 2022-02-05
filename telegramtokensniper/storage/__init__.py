import sqlite3

def _create_tables():
    con = sqlite3.connect('storage.db')
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS tokens (
    token_id integer primary key, 
    address text, 
    chain text, 
    chat_id_first_seen integer, 
    message_id_first_seen integer,
    message_timestamp integer)''')

    cur.execute('''CREATE TABLE IF NOT EXISTS buys (
    buy_id integer primary key,
    token_id integer,
    tx_hash text)''')

    con.commit()
    con.close()


_create_tables()

def insert_token(address, chain, chat_id, message):
    con = sqlite3.connect('storage.db')
    cur = con.cursor()
    raise NotImplementedError

def token_already_seen(address):
    raise NotImplementedError

def insert_buy(token_id, tx_hash):
    raise NotImplementedError