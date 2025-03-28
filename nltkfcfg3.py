from nltk import load_parser
cp = load_parser('output/sql0.fcfg')
query = 'What cities are located in China'
trees = list(cp.parse(query.split()))
answer = trees[0].label()['SEM']
answer = [s for s in answer if s]
q = ' '.join(answer)
print(q)
#SELECT City FROM city_table WHERE Country="china"
from nltk.sem import chat80
rows = chat80.sql_query('C:\\Laks\\Projects\\Python\\nlp\\banking_data.db', q)
for r in rows: print(r[0], end=" ")
