

def initial_trend(series, slen):
    sum = 0.0
    for i in range(slen):
        sum += float(series[i+slen] - series[i]) / slen
    return sum / slen

def initial_seasonal_components(series, slen):
    seasonals = {}
    season_averages = []
    n_seasons = int(len(series)/slen)
    # compute season averages
    for j in range(n_seasons):
        season_averages.append(sum(series[slen*j:slen*j+slen])/float(slen))
    # compute initial values
    for i in range(slen):
        sum_of_vals_over_avg = 0.0
        for j in range(n_seasons):
            sum_of_vals_over_avg += series[slen*j+i]-season_averages[j]
        seasonals[i] = sum_of_vals_over_avg/n_seasons
    return seasonals

def Holts_Winters_Fit(alpha):
    
    slen = 7

    series = [173, 166, 127, 149, 155, 141, 139, 168, 176, 146, 149, 163, 123, 161]
    
    RSS = 0
    
    for i in range(len(series)):
        if i == 0: # initial values
            smooth = series[0]
            trend = initial_trend(series, slen)
            seasonals = initial_seasonal_components(series, slen)
            continue
        else:
            val = series[i]
            last_smooth, smooth = smooth, alpha[0]*(val-seasonals[i%slen]) + (1-alpha[0])*(smooth+trend)
            trend = alpha[1] * (smooth-last_smooth) + (1-alpha[1])*trend
            seasonals[i%slen] = alpha[2]*(val-smooth) + (1-alpha[2])*seasonals[i%slen]
            RSS += (((smooth+trend+seasonals[i%slen]) - val)**2)
    return RSS