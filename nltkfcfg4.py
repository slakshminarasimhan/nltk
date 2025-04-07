import sqlite3
from nltk import load_parser

DB_PATH = "./banking_data.db"  # Update path to your SQLite DB

def get_parser():
    return load_parser("output/sql1.fcfg", trace=0)

def generate_sql(query):
    parser = get_parser()
    tokens = query.strip().split()
    trees = list(parser.parse(tokens))
    if not trees:
        return None
    sem = trees[0].label()['SEM']
    sql = "".join(sem) if isinstance(sem, tuple) else sem
    return sql

def execute_sql(sql):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

def answer_query(query):
    sql = generate_sql(query)
    if sql is None:
        return "Could not understand the question."
    print("Generated SQL:", sql)
    try:
        results = execute_sql(sql)
        return results if results else "No results found."
    except Exception as e:
        return f"SQL Execution Error: {e}"

if __name__ == "__main__":
    question = "What was the close price of Tata Motors on 1991-Jan-02"
    result = answer_query(question)
    print("Answer:", result)
