import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.tsa.api as smt
from statsmodels.tsa.stattools import acf, pacf

def ts_plot(y, lags=None, title=''):
    """
    Calcul de l'acf, pacf, de l'histogramme et du QQ-plot d'une série temp
    """
    # on transforme en Series si l'argument y n'en est pas une
    if not isinstance(y, pd.Series):
        y = pd.Series(y)
    
    # initialisation de la figure et des axes
    fig = plt.figure(figsize=(14, 12))
    ts_ax = fig.add_subplot(311)
    acf_ax = fig.add_subplot(323)
    pacf_ax = fig.add_subplot(324)
    qq_ax = fig.add_subplot(325)
    hist_ax = fig.add_subplot(326)
    
    # la serie temporelle
    y.plot(ax=ts_ax)
    ts_ax.set_title(title);
    
    # ACF et PACF
    smt.graphics.plot_acf(y, lags=lags, ax=acf_ax, alpha=0.05)
    smt.graphics.plot_pacf(y, lags=lags, ax=pacf_ax, alpha=0.05, method="ywm")
    
    # QQ-plot
    sm.qqplot(y, line='s', ax=qq_ax)
    qq_ax.set_title('QQ-Plot')
    
    # histogramme
    y.plot(ax=hist_ax, kind='hist', bins=25);
    hist_ax.set_title('Histogramme');
    plt.tight_layout();
    plt.show()
    

def plot_acf_pacf(y, plot_pacf=False):
    """
    représentation des sorties ACF/PACF
    """
    label = 'ACF'
    y_len = len(y)
    y2 = acf(y.values, fft=True)
    
    if plot_pacf:
        y2 = pacf(y.values)[1:]
        label = 'PACF'
        
    plt.figure(figsize=(14,6))
    plt.bar(range(len(y2)), y2, width = 0.1)
    plt.xlabel('lag')
    plt.ylabel(label)
    plt.axhline(y=0, color='black')
    plt.axhline(y=-1.96/np.sqrt(y_len), color='b', linestyle='--', linewidth=0.8)
    plt.axhline(y=1.96/np.sqrt(y_len), color='b', linestyle='--', linewidth=0.8)
    plt.ylim(-1, 1)
    plt.xlim(0,20)
    plt.show()
    
    
def plotseasonal(res, axes ):
    """
    représentation des différentes composantes d'une série
    """
    res.observed.plot(ax=axes[0], legend=False)
    axes[0].set_ylabel('Observed')
    res.trend.plot(ax=axes[1], legend=False)
    axes[1].set_ylabel('Trend')
    res.seasonal.plot(ax=axes[2], legend=False)
    axes[2].set_ylabel('Seasonal')
    res.resid.plot(ax=axes[3], legend=False)
    axes[3].set_ylabel('Residual')

