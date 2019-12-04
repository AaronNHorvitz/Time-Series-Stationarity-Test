def time_series_stationarity_test(original_ordered_time_series, 
                                  original_values, 
                                  differenced_ordered_time_series, 
                                  differenced_values,
                                  title = '',
                                  ylabel = '',
                                  xlabel = ''):
    
    # dependencies
    
    from statsmodels.tsa.stattools import adfuller
    from matplotlib import pyplot as plt
    from matplotlib import rcParams
    
    # assign values
    
    x_orig                  = original_ordered_time_series
    y_orig                  = original_values

    x_diff                  = differenced_ordered_time_series
    y_diff                  = differenced_values
    test_values             = differenced_values
    
    test_values   = test_values.fillna(0).values
    result        = adfuller(test_values)
    
    adf_statistic = round(result[0],5)  
    p_value       = round(result[1],5)
    n_obs         =       result[3]
    cv_1          = round(result[4]['1%'],5)
    cv_5          = round(result[4]['5%'],5)
    cv_10         = round(result[4]['10%'],5)
    
    # plot title
    rcParams['figure.figsize'] = 18, 1
    plt.figtext(0,0,'Test for Stationarity',fontsize = 24,fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    plt.show()
    
    # plot original time series data vs. differenced data
    
    rcParams['figure.figsize'] = 10, 8
    fig = plt.figure()
    ax1 = plt.subplot2grid((6, 4), (0, 0), rowspan=2, colspan=4)
    ax2 = plt.subplot2grid((6, 4), (2, 0), rowspan=2, colspan=4)
    ax3 = plt.subplot2grid((6, 4), (4, 0), rowspan=2, colspan=4)
    
    # original data

    ax1.plot(x_orig,y_orig_duration, color = 'blue')
    ax1.scatter(x_orig,y_orig_duration, color = 'red')
    ax1.set_title('Original {}'.format(title), fontsize = 18, color = 'blue')
    ax1.set_xlabel(ordered_series_column, fontsize = 12)
    ax1.set_ylabel('Original {}'.format(ylabel), fontsize = 12)

    # differenced data

    ax2.plot(x_diff, y_diff_duration, color = 'green')
    ax2.scatter(x_diff, y_diff_duration, color = 'orange')
    ax2.set_title('Differenced {}'.format(title), fontsize = 18, color = 'green')
    ax2.set_xlabel(ordered_series_column, fontsize = 12)
    ax2.set_ylabel('Differenced {}'.format(ylabel), fontsize = 12)

    # dickey fuller test
    
    ax3.axis('off')
    ax3.text(0,1.20,'Augmented Dickey-Fuller Test for Stationarity',fontweight='bold',fontsize = 18)
    ax3.text(0,0.95,'ADF Statistic:          {}   '.format(adf_statistic),fontsize = 18,fontweight='light')
    ax3.text(0,0.80,'p-value:                    {}'.format(p_value),fontsize = 18,fontweight='light')
    ax3.text(0,0.65,'Observations Used:  {}'.format(n_obs),fontsize = 18,fontweight='light')
    ax3.text(0,0.50,'Critical Values:',fontsize = 18,fontweight='light')
    ax3.text(0,0.35,'             1%:   {}'.format(cv_1),fontsize = 18,fontweight='light')
    ax3.text(0,0.20,'             5%:   {}'.format(cv_5),fontsize = 18,fontweight='light')
    ax3.text(0,0.05,'             10%: {}'.format(cv_10),fontsize = 18,fontweight='light')    
    
    plt.tight_layout()
    plt.show()
    
    return 
