import argparse
from pathlib import Path
import pandas as pd

def summarize(frame, group, value):
    data=frame[[group,value]].copy();data[value]=pd.to_numeric(data[value],errors='raise')
    return data.groupby(group,dropna=False)[value].agg(['count','sum','mean']).reset_index()
def main():
    p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('output');p.add_argument('--group',required=True);p.add_argument('--value',required=True);a=p.parse_args()
    if Path(a.input).resolve()==Path(a.output).resolve(): p.error('Choose a different output')
    summarize(pd.read_excel(a.input),a.group,a.value).to_excel(a.output,index=False)
if __name__=='__main__': main()
