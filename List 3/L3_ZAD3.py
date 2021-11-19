def counting_chars_without_ifs_with_pandas(filename):
    file_ref = open(filename, 'r')
    text = file_ref.read().lower()
    import pandas as pd
    di = dict(pd.Series(list(text)).value_counts())
    for i in (' ','\n'):
        try:
            di.pop(i)
        except:
            pass
    return di