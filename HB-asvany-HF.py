import pandas
import numpy
import matplotlib.pyplot as plt


pandas.options.display.float_format = '{:.1f}'.format


def MatGraph(x,pos):
    return f'{x} mg'


def DailyMineral(df):
    header = df.columns
    for i in header:
        mineral_daily[i] = mineral_daily[i].apply(lambda x : x/daily_need[i]*100)
    return df


def Max_Avg(df):
    df.loc['Max'] = df.max()
    df.loc['Avg'] = df.mean()
    df.loc['Max_name'] = df.idxmax(axis=0)
    df_statistic = df.iloc[-3::]
    df.drop(['Max','Avg','Max_name'],axis=0,inplace=True)
    return df,df_statistic

daily_need =pandas.Series({'Ca2+': 900,'K+': 3500,'Mg2+': 350,'Na+': 2000,}, name='Daily need')

mineral_all = pandas.read_excel('asvanyianyagok.xlsx')
mineral_daily = mineral_all.loc[1::]
mineral_daily.set_index('Ásvány jele',inplace=True)
mineral_all.set_index('Ásvány jele',inplace=True)

mineral_names =pandas.Series({'Ca2+': mineral_all.iloc[0:0],'K+': mineral_all.iloc[0:1],
                              'Mg2+': mineral_all.iloc[0:2],'Na+': mineral_all.iloc[0:3],}, name='Mineral names')
mineral_all.drop('Ásvány neve',axis=0, inplace=True)

mineral_all=mineral_all.astype(numpy.int64)
mineral_daily = mineral_daily.astype(numpy.int64)

mineral_daily = DailyMineral(mineral_daily)
mineral_all,mineral_statistic = Max_Avg(mineral_all)

print(mineral_statistic)
print(mineral_all)
print(mineral_daily.to_string(formatters={'Ca2+' : '{:.2f}%'.format, 'K+': '{:.2f}%'.format,
                                            'Mg2+': '{:.2f}%'.format,'Na+': '{:.2f}%'.format}))



plot1 = mineral_all.plot(kind='bar', stacked=True)
plot1.legend(loc='upper center', ncol=10, title="Ásványianyag-tartalom 1 literben")
plot1.yaxis.set_major_formatter(MatGraph)
plt.show()
