# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 20:23:19 2016

@author: 珮軒
"""

import numpy as np #use numpy package (array)
import matplotlib.pyplot as plt #use matplotlib package (plot) 
#%pylab inline <--- another import numpy&matplotlib

k=9100
call=179
put=18

interval = 500


strange = np.arange((k-interval), (k+interval))

#call option 
longcall = np.maximum(strange-k,0) - call
shortcall = call - np.maximum(strange-k,0)


plt.plot(longcall)
plt.plot(shortcall)
plt.show()

#put option
longput = np.maximum(k-strange,0) - put
shortput = put - np.maximum(k-strange,0)
plt.plot(longput)
plt.plot(shortput)
plt.show()


#rise to 9200 or fall to 8700
k2=9000
call2 = 100
put2 = 50

interval2 = 700

strange2 = np.arange((k-interval),(k+interval))


#strategy:Long Straddle---longcall 9200 & longput 8700

longcall2 = np.maximum(strange-k2,0) - call2
longput2 = np.maximum(k2-strange,0) - put2
payoff = longcall2 + longput2
#leftpayoff = np.arange((k2-call2-put2))
#rightpayoff = np.arange((k2+call2+put2))




plt.plot(longcall2)
plt.plot(longput2)
plt.plot(payoff)
#plt.plot(leftpayoff)
#plt.plot(rightpayoff)
plt.show()


