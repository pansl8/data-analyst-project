"""数据变换"""
import pandas as pd


def attr_trans(x):
    result = pd.Series(index=['SYS_NAME', 'CWXT_DB:184:C:\\', 'CWXT_DB:184:D:\\', 'COLLECTTIME'])
    result['SYS_NAME'] = x['SYS_NAME'].iloc[0]
    result['COLLECTTIME'] = x['COLLECTTIME'].iloc[0]
    result['CWXT_DB:184:C:\\'] = x['VALUE'].iloc[0]
    result['CWXT_DB:184:D:\\'] = x['VALUE'].iloc[1]
    return result


def get_data():
    infile = "../data/discdata.xls"
    outfile = "../tmp/discdata_processed01.xls"
    data = pd.read_excel(infile)
    data = data[data['TARGET_ID'] == 184].copy()
    data = data.groupby(['COLLECTTIME'])
    result = data.apply(attr_trans)
    result.to_excel(outfile, index=False)


if __name__ == '__main__':
    get_data()
    pass
