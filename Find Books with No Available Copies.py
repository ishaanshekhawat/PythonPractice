# https://leetcode.com/problems/find-books-with-no-available-copies/description/

import pandas as pd

def find_books_with_no_available_copies(library_books: pd.DataFrame, borrowing_records: pd.DataFrame) -> pd.DataFrame:
    df1 = (
    borrowing_records[borrowing_records['return_date'].isna()]
    .groupby('book_id', as_index=False)
    .agg(current_borrowers=('book_id', 'count'))
    )
    
    df2 = library_books.merge(df1, how='inner', on='book_id')
    df2['current_copies'] = df2['total_copies'] - df2['current_borrowers']
    df2 = df2[df2['current_copies'] == 0]
    return df2[['book_id','title','author','genre','publication_year','current_borrowers']].sort_values(by=['current_borrowers', 'title'], ascending = [False, True])
