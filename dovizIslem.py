
# 2018 Emir Erbasan (humanova)
# MIT License, see LICENSE for more details

#hmnBot Doviz islemleri

#KAYNAK : www.xe.com


from bs4 import BeautifulSoup
from urllib.request import urlopen, Request



def DovizParse(kur,adet):
    kur = DovizAlgila(kur)

    if not kur == "hata" and int(adet) >= 1:
        if kur.startswith("btc"):

            if kur == "btc-try":
                kurURL = 'https://www.xe.com/currencyconverter/convert/?Amount=' + adet + '&From=XBT&To=TRY'

            elif kur == "btc-usd":
                kurURL = 'https://www.xe.com/currencyconverter/convert/?Amount=' + adet + '&From=XBT&To=USD'

        else:
            kurURL = "https://www.xe.com/currencyconverter/convert/?Amount=" + adet + "&From=" + kur + "&To=TRY"
        
        data = urlopen(Request(kurURL, headers={'User-Agent': 'Mozilla'})).read()
        parse = BeautifulSoup(data,'html.parser')
            
        doviz = parse.find("span","uccResultAmount")

        kur_degeri = doviz.text

        return kur.upper(),kur_degeri
        
    else:
        kur_degeri = "hata"
        return kur,kur_degeri

def DovizAlgila(kur):

    if kur.upper() == "BTC-TRY":  
        kur = "btc-try"
        return kur
        
    elif kur.upper() == "BTC-USD":
        kur = "btc-usd"
        return kur

    elif kur.upper() == "USD" or kur.upper() == "DOLAR" or kur.upper() == "DOLLAR":
        kur = "usd"
        return kur

    elif kur.upper() == "EUR" or kur.upper() == "EURO" or kur.upper() == "AVRO":
        kur = "eur"
        return kur

    elif kur.upper() == "GBP" or kur.upper() == "POUND" or kur.upper() == "STERLIN":
        kur = "gbp"
        return kur

    elif kur.upper() == "RUB" or kur.upper() == "RUBLE" or kur.upper() == "RUS" or kur.upper() == "RUSYA":
        kur = "rub"
        return kur

    elif kur.upper() == "JPY" or kur.upper() == "JAPONYA" or kur.upper() == "YEN":
        kur = "jpy"
        return kur

    elif kur.upper() == "CAD" or kur.upper() == "KANADA": 
        kur = "cad"
        return kur

    elif kur.upper() == "AUD" or kur.upper() == "AVUSTRALYA":
        kur = "aud"
        return kur

    elif kur.upper() == "CNY" or kur.upper() == "ÇIN" or kur.upper() == "RENMINBI":
        kur = "cny"
        return kur

    elif kur.upper() == "SEK" or kur.upper() == "SWE" or kur.upper() == "ISVEÇ":
        kur = "sek"
        return kur

    elif kur.upper() == "CHF" or kur.upper() == "SWI" or kur.upper() == "ISVIÇRE":
        kur = "sek"
        return kur

    elif kur.upper() == "DKK" or kur.upper() == "DANIMARKA" or kur.upper() == "DAN":
        kur = "dkk"
        return kur

    elif kur.upper() == "SAR" or kur.upper() == "SAUDI" or kur.upper() == "ARABISTAN":
        kur = "sar"
        return kur

    elif kur.upper() == "RON" or kur.upper() == "ROMANYA" or kur.upper() == "RUMEN":
        kur = "ron"
        return kur

    elif kur.upper() == "NOK" or kur.upper() == "NORVEÇ":
        kur = "nok"
        return kur

    elif kur.upper() == "BGN" or kur.upper() == "BULGARISTAN":
        kur = "bgn"
        return kur

    elif kur.upper() == "IRR" or kur.upper() == "IRAN":
        kur = "irr"
        return kur

    elif kur.upper() == "PKR" or kur.upper() == "PAKISTAN":
        kur = "pkr"
        return kur
    
    elif kur.upper() == "KWD" or kur.upper() == "KUVEYT":
        kur = "kwd"
        return kur
    else:
        kur = "hata"
        return kur

    

def KriptoParse(kur,don,adet):
    kur,kisa_ad = KriptoAlgila(kur)

    if not kur == "hata" and int(adet) >= 1:

        kurURL = 'https://www.xe.com/currencyconverter/convert/?Amount=' + adet + '&From=' + kisa_ad + '&To=' + don.upper()
    
        data = urlopen(Request(kurURL, headers={'User-Agent': 'Mozilla'})).read()
        parse = BeautifulSoup(data,'html.parser')

        kripto_deger = parse.find("span","uccResultAmount")

        kur_degeri = kripto_deger.text
        return kur.upper(),kur_degeri

    else :
        return kur,kisa_ad


def KriptoAlgila(kur):

    if kur.upper() == "BTC" or kur.upper() == "BITCOIN":
        kur = "bitcoin"
        kisa_ad = "xbt"
        return kur,kisa_ad
    
    elif kur.upper() == "BTCCASH" or kur.upper() == "BITCOINCASH" or kur.upper() == "BCH":
        kur = "bitcoin-cash"
        kisa_ad = "bch"
        return kur,kisa_ad
            
    elif kur.upper() == "ETH" or kur.upper() == "ETHEREUM":

        kur = "ethereum"
        kisa_ad = "eth"
        return kur,kisa_ad

    elif kur.upper() == "XRP" or kur.upper() == "RIPPLE":
        kur = "ripple"
        kisa_ad = "xrp"
        return kur,kisa_ad

    elif kur.upper() == "EOS":
        kur = "eos"
        kisa_ad = "eos"
        return kur,kisa_ad

    elif kur.upper() == "XMR" or kur.upper() == "MONERO":
        kur = "monero"
        kisa_ad = "xmr"
        return kur,kisa_ad

    elif kur.upper() == "LITE" or kur.upper() == "LTC" or kur.upper() == "LITECOIN":
        kur = "litecoin"
        kisa_ad = "ltc"
        return kur,kisa_ad

    elif kur.upper() == "XLM" or kur.upper() == "STELLAR":
        kur = "stellar"
        kisa_ad = "xlm"
        return kur,kisa_ad

    else:
        kur = "hata"
        kisa_ad = "hata"
        return kur,kisa_ad

    