# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 



def intensities(y1, y2, y3):
    # Top bar chart
    plt.figure(1)
    plt.subplot(221)
    plt.plot(y2, ls='-', c = 'blue', alpha = 0.5, linewidth = 2.0, linestyle='-') 
    # plt.xticks(y_pos, frequency)
    # plt.yticks( np.arange(min(y), max(y), 5) )
    plt.xlabel(u'Coluna')
    plt.ylabel(u'Somatório das intensidades')
    plt.title("Imagem original")
    plt.grid(True)
    
    
    # Bottom bar graph
    plt.figure(1)
    plt.subplot(223)
    plt.plot(y1, ls='-', c = 'blue', alpha = 0.5, linewidth = 2.0, linestyle='-') 
    # plt.xticks(y_pos, frequency)
    # plt.yticks( np.arange(min(y), max(y), 5) )
    plt.xlabel(u'Coluna')
    plt.ylabel(u'Somatório das intensidades')
    plt.title("Threshold de 33%")
    plt.grid(True)
    
    # Both bar graph
    plt.figure(1)
    plt.subplot(122)
    plt.plot(y3, ls='-', c = 'blue', alpha = 0.5, linewidth = 2.0, linestyle='-') 
    # plt.xticks(y_pos, frequency)
    # plt.yticks( np.arange(min(y), max(y), 5) )
    plt.xlabel(u'Coluna')
    plt.ylabel(u'Somatório das intensidades')
    plt.title("Imagem final")
    plt.grid(True)
    
    plt.show()

# The following line can be pasted at the detector_features.py (below the show temp's lines)

# import matplotlib as mat

# fontsize = 18
# mat.rc('legend', fontsize=fontsize, handlelength=3)
# mat.rc('axes', titlesize=fontsize)
# mat.rc('axes', labelsize=25)
# mat.rc('xtick', labelsize=fontsize)
# mat.rc('ytick', labelsize=fontsize)
# # mat.rc('text', usetex=True)
# mat.rc('font', size=fontsize, family='serif', style='normal', variant='normal',stretch='normal', weight='normal')

# cols_sum_before = cols_sum_before/100
# cols_sum = cols_sum/100

# plt.plot(cols_sum_before, ls='-', c = 'blue', alpha = 0.9, linewidth = 2.0, linestyle='-', label=u'Somatório das intensidades de cada coluna da imagem') 
# # plt.xticks(y_pos, frequency)
# # plt.yticks( np.arange(min(y), max(y), 5) )
# plt.xlabel(u'Colunas')
# plt.ylabel(u'Somatório das intensidades')
# plt.title(u"Valores dos somatórios de cada coluna antes da aplicação do filtro", fontsize=25)
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),  shadow=True, ncol=1)
# plt.grid(True)
# plt.show()

# plt.plot(cols_sum, ls='-', c = 'blue', alpha = 0.9, linewidth = 2.0, linestyle='-', label=u'Somatório das intensidades de cada coluna da imagem') 
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),  shadow=True, ncol=1)
# # plt.xticks(y_pos, frequency)
# # plt.yticks( np.arange(min(y), max(y), 5) )
# # Bottom bar graph
# # plt.xticks(y_pos, frequency)
# # plt.yticks( np.arange(min(y), max(y), 5) )
# plt.xlabel(u'Colunas')
# plt.ylabel(u'Somatório das intensidades')
# plt.title(u"Valores dos somatórios de cada coluna após a aplicação do filtro", fontsize=25)
# plt.grid(True)
# plt.show()