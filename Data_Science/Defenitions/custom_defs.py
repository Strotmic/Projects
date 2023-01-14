import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def geef_naam(titel,x_as,y_as):
    plt.title(titel)
    plt.x

def boxplot(data,x,y='',xlabel='',ylabel='',title=''):
    end = title
    if y=='':
        sns.boxplot(data=data,x=x)
        title = f'Grafiek van {x}'
    else:
        sns.boxplot(data=data, y=y,x=x)
        title = f'Grafiek van {x} en {y}'
    if end != '':
        plt.title(end)
    else:
        plt.title(title)
    if xlabel!='':
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
    plt.show()
    

def histogram(data,x,y='',xlabel='',ylabel='',title=''): 
    end = title
    if y=='':      
        if data != '':   
            sns.histplot(data=data, x=x)
            title = f'Grafiek van {x}'
            pass
        else:
            sns.histplot(x=x)
            title = f'Grafiek van {x}'
            pass
    else:
        sns.histplot(data=data, x=x, y=y)
        title = f'Grafiek van {x} en {y}'
        pass
    if end != '':
        plt.title(end)
    else:
        plt.title(title)
    if xlabel!='':
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
    plt.show()

def get_bins(df,kolom):
    rang = df[kolom].max()-df[kolom].min()
    bins = (rang/(np.sqrt(df[kolom].count())))
    bins = np.arange(df[kolom].min(), df[kolom].max(), bins)
    return bins

def distplot(df,kolom):
    bns = get_bins(df,kolom)
    sns.distplot(x=df[kolom], bins=bns, kde=False)
    plt.title(f'Grafiek van {kolom}')


def catplot(data,x,y='',kind='',xlabel='',ylabel='',title='',xticks=[],xtickss=[]):
    end = title
    if y=='':
        sns.catplot(data=data, x=x,kind=kind)
        title = f'Grafiek van {x}'
        pass
    else:
        sns.catplot(data=data, x=x, y=y,kind=kind)
        title = f'Grafiek van {x} en {y}'
        pass
    if xlabel!='':
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
    if xticks != []:
        plt.xticks(xticks,xtickss)    
    if end != '':
        plt.title(end)
    else:
        plt.title(title)
    plt.show()

def print_calculations(dataKolom):
    print(f"Het gemiddelde is {dataKolom.mean()}")
    print(f"De median is {dataKolom.median()}")
    print(f"De var is {dataKolom.var()}")
    print(f"Standaardafwijking is {dataKolom.std()}")
    print(f"Q1 is {dataKolom.quantile(0.25)}")
    print(f"Q3 is {dataKolom.quantile(0.75)}")
    print(f"De IQR is{dataKolom.quantile(0.75)-dataKolom.quantile(0.25)}")
    rang = dataKolom.max()-dataKolom.min()
    print(f"Skewness is {dataKolom.skew()}")
    print(f"Kurt: {dataKolom.kurt()}")
    print(dataKolom.mode)

    
