import sqlite3
from telegramtokensniper import log_utils


def _create_tables():
    conn = sqlite3.connect('storage.db')
    cur = conn.cursor()

    #AUTOINCREMENT not required: https://www.sqlite.org/autoinc.html
    cur.execute('''CREATE TABLE IF NOT EXISTS addresses (
    address_id INTEGER PRIMARY KEY , 
    address TEXT UNIQUE, 
    chain TEXT, 
    chat_id_first_seen INTEGER, 
    message_id_first_seen INTEGER,
    message_timestamp INTEGER)''')

    cur.execute('''CREATE TABLE IF NOT EXISTS buys (
    buy_id INTEGER PRIMARY KEY ,
    address_id INTEGER,
    tx_hash TEXT,
    FOREIGN KEY(address_id) REFERENCES addresses(address_id))''')

    conn.commit()
    conn.close()


_create_tables()

def insert_address(address, chain, chat_id, message):
    try:
        address = address.lower()

        conn = sqlite3.connect('storage.db')
        cur = conn.cursor()

        cur.execute("INSERT INTO addresses VALUES(NULL, ?, ?, ?, ?, ?)",
                    (address, chain, chat_id, message.id, int(message.date.timestamp())))

        inserted_id = cur.lastrowid

        conn.commit()
        conn.close()

        return inserted_id
    except Exception as e:
        log_utils.logging.warning(e)

# import datetime
# class Message:
#     def __init__(self, msg_id, date):
#         self.id = msg_id
#         self.date = date
#
# print(insert_address("a", "a", 1, Message(1, datetime.datetime.utcnow())))
# print(insert_address("b", "a", 1, Message(1, datetime.datetime.utcnow())))
# print(insert_address("d", "a", 1, Message(1, datetime.datetime.utcnow())))

def address_already_seen(address):
    address = address.lower()

    conn = sqlite3.connect('storage.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM addresses WHERE address = ?", (address,))

    row = cur.fetchone()

    cur.close()

    return row is not None

def insert_buy(address_id, tx_hash):
    try:
        conn = sqlite3.connect('storage.db')
        conn.execute("PRAGMA foreign_keys = 1") # enforces FK-constraint for this connection
        cur = conn.cursor()

        cur.execute("INSERT INTO buys VALUES(NULL, ?, ?)",
                    (address_id, tx_hash))

        inserted_id = cur.lastrowid

        conn.commit()
        conn.close()

        return inserted_id
    except Exception as e:
        log_utils.logging.warning(e)