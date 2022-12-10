# Trading calc. W.Kulik 2021

btc = 41000

# PMA price ( in BTC )
bcoin = 0.094
scoin = 0.095

oldbtc = 0.00243949
print('-----------------------------------------------------')
print('zainwestowano: ',oldbtc*btc,' GPB')
print('-----------------------------------------------------')

# purchase

quantity = oldbtc/bcoin
print ('bought ',quantity,' PMA for ',oldbtc,' BTC')


# sell

newbtc= quantity * scoin
print ('sold ',quantity,' PMA for ', newbtc, ' BTC')
print('                                         ')


coin_gain = ((scoin*100)/bcoin)-100
print(' PMA coin percentage price gain: ', str(coin_gain))

btc_gain = ((newbtc*100)/oldbtc)-100
print(' BTC      percentage price gain: ', str(btc_gain))
print('                                         ')

gpb = (newbtc-oldbtc)*btc
print('earned: ',str(gpb),' GPB')
print('                                         ')



