# Processamento dos dados de onda
# - Distribuições de curto-termo
# Henrique Pereira
# 12/11/2019
#
# Referências:
# 1. 
# 2. 

# import libraries

def read_data():
    """
    Read buoy Data
    - Axys
    - Waveriver
    - NavCon

    Input: raw data

    Output: standarized data

    """

    if buoy == 'axys':
        pass
    if buoy == 'navcon':
        pass
    if buoy == 'waverider':
        pass
    pass

def timeproc(method='up_crossing'):
    """
    Time domain wave processing

    Output:
    Hmax - Altura maxima individual
    Tmax - Periodo maximo individual
    THmax - Periodo associado a altura maxima
    H110 - Altura de 1/10 das maiores ondas
    T110 - Periodo de 1/10 dos maiores periodos
    H13 - Altura significativa (1/3 das maiores)
    T13 - Período significativo (1/3 dos maiores)
    Hm - Altura media
    Tm - Período médio
    """
    if method == 'up_crossing':
        pass
    if method == 'down_crossing':
        pass
    return 

def spec_auto_correlation():
    """
    Calculo do espectro utilizando função
    de correlação
    """
    pass

def spec_fft(hanning=True):
    """
    Calculo do espectro utilizando a FFT

    Input:
    x - série temporal
    nfft - tamanho do segmento para a FFT
    fs - frequencia de amostragem
    hanning (boolean): aplicação da janela de hanning

    Output:
    """
    pass


def main():
    pass

if __name__ == "__main__":

    main()