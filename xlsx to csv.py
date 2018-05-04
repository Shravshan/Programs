inputdirectory=r'C:\Users\Shravya.Shanmukh\Desktop\Work\ALDI\Input\\'
for xls_file in glob.glob(os.path.join(inputdirectory,"*.xls*")):
    data_xls = pd.read_excel(xls_file, index_col=None)
    csv_file = os.path.splitext(xls_file)[0]+".csv"
    data_xls.to_csv(csv_file, encoding='utf-8', index=False)