from app import db
from api.models import Author,Book
import pandas as pd
db.create_all()
print('Database created')
df_authors = pd.read_csv('df_authors.csv', index_col=0)
df_authors.drop_duplicates(inplace=True)
df_books = pd.read_csv('df_books.csv')
try:
    for i in df_authors.index:
        new_author = Author(name=f"{df_authors.loc[i,'Author']}", location=f"{df_authors.loc[i,'location']}", age=int(df_authors.loc[i,'age']), gender=f"{df_authors.loc[i,'gender']}")
        dff = df_books[df_books['Author'] == df_authors.loc[i,'Author']]
        for k in dff.index:
            new_book = Book(title=f"{dff.loc[k,'Title']}", genre=f"{dff.loc[k,'Genre']}", height=int(dff.loc[k,'Height']), publisher=f"{dff.loc[k,'Publisher']}", author=new_author)
            db.session.add(new_book)
    db.session.add(new_author)
    db.session.commit()
except:
    print('Error encountered, database dropped')
    db.session.rollback()
    db.drop_all() #delete|drop all tables