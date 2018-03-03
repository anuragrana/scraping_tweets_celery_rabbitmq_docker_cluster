import configs.database as dc
import psycopg2
import traceback


def connect():
    conn = None
    try:
        conn = psycopg2.connect(
            host=dc.host,
            user=dc.user,
            password=dc.password,
            database=dc.database
        )
    except Exception as e:
        print(repr(e))

    return conn


def save_tweets(tweets):
    try:
        conn = connect()
        cur = conn.cursor()
        sql = "insert into tweets (tweet) values (%s);"
        for tweet in tweets:
            sql_data = (tweet,)
            cur.execute(sql, sql_data)
            conn.commit()

        cur.close()
        conn.close()
        return True

    except Exception as e:
        print(traceback.format_exc())
        return False
