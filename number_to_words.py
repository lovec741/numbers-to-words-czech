from math import ceil

nums1 = [
    "",
    "jedna",
    "dva",
    "tři",
    "čtyři",
    "pět",
    "šest",
    "sedm",
    "osm",
    "devět",
    "deset",
    "jedenáct",
    "dvanáct",
    "třináct",
    "čtrnáct",
    "patnáct",
    "šestnáct",
    "sedmnáct",
    "osmnáct",
    "devatenáct",
]
nums2 = {
    2: "dvacet",
    3: "třicet",
    4: "čtyřicet",
    5: "padesát",
    6: "šedesát",
    7: "sedmdesát",
    8: "osmdesát",
    9: "devadesát",
}
nums3 = {
    100: ["sto", "stě", "sta", "sta", "set"],
    1000: ["tisíc", "tisíce", "tisíce", "tisíce", "tisíc"],
}
predpony = [
    "mi",
    "bi",
    "tri",
    "kvadri",
    "kvinti",
    "sexti",
    "septi",
    "okti",
    "noni",
    "deci",
]
koncovky = [["lion", "", "y", "ů"], ["liard", "a", "y", ""]]

def get_higher(ind: int, n: int) -> str:
    """Vedlejší funkce

    :param ind: Číslo pomáhající při tvoření koncovek
        Př: od 0 do 999 je ind = 0, od 1 000 do 999 999 je ind = 1
        je potřeba protože se musí psát 'jeden' třeba u tisíců
        ('jeden tisíc') a 'jedna' třeba u miliard ('jedna miliarda')
    :param n: počet u kterého chceme dostat tvar
        Př: když bude n = 3 a n = 100 tak to hledá v jakém tvaru
        bude 100 krát 3, což je 'tři sta' -> vrátí 'sta'
    :returns: vrátí jaké k tomuto ind patří slovo a v jakém tvaru (' milion', ' tisíce', '')
        Př:
            >>> get_higher(1,1)
            ' tisíc'
            >>> get_higher(1,2)
            ' tisíce'
            >>> get_higher(0,123)
            ''
            >>> get_higher(4,2)
            ' biliony'
    """
    # pokud je ind = 0 tak to znamená že pracujeme s jednotkami až stovkami
    # a tak nic nepřidáme
    if ind == 0: 
        return ""
    # pokud je ind = 1 tak to znamená že pracujeme s tisíci a tak si řekneme
    # o tisíc v tomto tvaru od funkce get_for_am
    if ind == 1:
        return " "+get_for_am(n, 1000)
    # v tomto místě už víme že to budou miliony nebo více
    # a tyto slova mají vždy tři různé koncovky
    # jednu pro 1 Př: 'jedna miliardA' (t = 1)
    # druhou pro 2 až 4 Př: 'tři miliardY' (t = 2)
    # třetí pro čísla větší než 4 Př: 'pět miliard-' (t = 3)
    if n == 1:
        t = 1
    elif n > 1 and n < 5:
        t = 2
    else:
        t = 3
    # na tomto řádku získáme první část našeho slova
    # jako 'mi', 'bi', 'tri', atd.
    result = predpony[(ind-2)//2]
    # poté druhá část bude 'lion' nebo 'liard'
    # to se rozhodne podle toho jestli je ind to sudé (ind%2)
    # takže naše slovo zatím vypadá třeba: 'milion' nebo 'miliard'
    result += koncovky[ind%2][0]
    # a teď přidáme třetí čast a to je koncovka podle hodnoty
    # a také podle toho jestli jsme v předchozím použili
    # 'lion' nebo 'liard' toto sem musíme dát protože
    # 'milion' nemá stejné koncovky jako 'miliarda'
    # (tady použijeme naše t)
    result += koncovky[ind%2][t]
    return " "+result

def get_for_am(n: int, x: int) -> str:
    """Vedlejší funkce

    :param x: buď 100 nebo 1000 podle toho co chceme dostat
    :param n: počet u kterého chceme dostat tvar
        Př: když bude n = 3 a x = 100 tak to hledá v jakém tvaru
        bude 100 krát 3, což je 'tři sta' -> vrátí 'sta'
    :returns: textový tvar buďto 100 nebo 100 upravený pro určitý počet
        Př:
            >>> get_for_am(7,1000)
            'set'
            >>> get_for_am(2,1000)
            'tisíce'
            >>> get_for_am(1,1000)
            'tisíc'
            >>> get_for_am(2,100)
            'stě'
    """
    # pokud počet pro který chceme dostat hodnotu není v listu možností
    if n >= len(nums3[x]):
        # tak vyberte poslední možnost
        return nums3[x][-1]
    else:
        # vyberte možnost podle hodnoty a odečteme 1 aby bylo například n = 1 k indexu 0
        return nums3[x][n-1]

def get_ones(n: int, hun: bool=False, ind: int=None) -> str:
    """Vedlejší funkce

    :param n: číslo od 0 do 19
    :param hun: True pokud výsledné číslo patří před stovky
    :param ind: Číslo pomáhající při tvoření koncovek
        Př: od 0 do 999 je ind = 0, od 1 000 do 999 999 je ind = 1
        je potřeba protože se musí psát 'jeden' třeba u tisíců
        ('jeden tisíc') a 'jedna' třeba u miliard ('jedna miliarda')
    :returns: 
    """
    # u stovek, miliard a dalších končících na -liard
    # musíme místo 'dva' napsat 'dvě'
    # Př: nechceme 'dva miliardy' chceme 'dvě miliardy'
    if n == 2 and (hun or ind % 2 == 1) and ind != 1:
        return "dvě"
    # u tisíců, milionů a dalších končících na -lion
    # musíme místo 'jedna' napsat 'jeden'
    # Př: nechceme 'jedna tisíc' chceme 'jeden tisíc'
    if n == 1 and not hun and (ind == 1 or ind % 2 == 0 and ind != 0):
        return "jeden"
    # jinak prostě vem z listu num1
    return nums1[n]
    
        
    
def get_tens(n: int) -> str:
    """Vedlejší funkce

    :param n: číslo od 0 do 99
    :returns: převede n na text
        Př:
            >>> get_tens(10, 0)
            'deset'
            >>> get_tens(85, 0)
            'osmdesát pět'
    """
    # když je n nula tak vrať prázdný string
    if n == 0:
        return ""
    # hodnoty pod dvacet jsou v listu nums1 takže je můžeme rovnou vrátit
    if n < 20:
        return nums1[n]
    # n%10 jsou jednotky čísla n Př: 56%10 = 6
    # chceme jednotky k desítkám přidat jen když tam nějaké jsou (nejsou 0)
    # aby jsme neměli přebytečnou mezeru na konci
    if n%10 != 0:
        return nums2[n//10] + " " + nums1[n%10]
    else:
        return nums2[n//10]
    
def get_hundereds(n: int) -> str:
    """Vedlejší funkce

    :param n: číslo od 0 do 19
    :returns: n stovek jako text
        Př:
            >>> get_hundereds(19)
            'devatenáct set'
            >>> get_hundereds(2)
            'dvě stě'
            >>> get_hundereds(1)
            'sto'
    """
    # když je to nula stovek tak vrať prázdný string
    if n == 0:
        return ""
    # když je to jedna stovka tak tam nechceme před tím mít 'jedna'
    # Př: když je n = 1 nechceme 'jedno sto' a chceme 'sto'
    if n == 1:
        return get_for_am(n, 100)
    # přidáme před stovku počet stovek
    return get_ones(n, hun=True) + " " + get_for_am(n, 100)

def from_0_to_999(n: int, ind: int) -> str:
    """Vedlejší funkce

    :param n: číslo od 0 do 999
    :param ind: Číslo pomáhající při tvoření koncovek
        Př: od 0 do 999 je ind = 0, od 1 000 do 999 999 je ind = 1
        je potřeba protože se musí psát 'jeden' třeba u tisíců
        ('jeden tisíc') a 'jedna' třeba u miliard ('jedna miliarda')
    :returns: číslo zadané jako string str_n převedené na text
    """
    str_n = str(n) # do str_n si uložíme n jako string
    if len(str_n) == 1: # pokud je naše číslo 0 až 9
        return get_ones(n, ind=ind)
    elif len(str_n) == 2: # pokud je naše číslo 10 až 99
        return get_tens(n)
    elif len(str_n) == 3: # pokud je naše číslo 100 až 999
        # n%100 jsou desítky a jednotky čísla n Př: 256%100 = 56
        # chceme desítky ke stovkám přidat jen když tam nějaké jsou (nejsou 0)
        # aby jsme neměli přebytečnou mezeru na konci
        if n%100 != 0:
            return get_hundereds(n//100)+" "+get_tens(n%100)
        else:
            return get_hundereds(n//100)
    
def cislo_na_text(num: int, form: bool=False) -> str:
    """Hlavní funkce

    Tato funkce převede číslo na textovou reprezentaci toho čísla.
    Př:
        >>> cislo_na_text(1234)
        'tisíc dvě stě třicet čtyři'
        >>> cislo_na_text(1234, form=True)
        Lépe formátované: 1 234
        'tisíc dvě stě třicet čtyři'
    :param num: číslo k převedení (musí být mezi -10^66 a 10^66)
    :param form: True pokud chcete vyprintit lepé naformátované num
    :returns: textovou reprezentaci čísla num
    """
    if num == 0:
        return "nula"
    if num >= 10**66:
        assert Exception("Moc velké číslo! Nejsou povolena čísla rovná nebo větší než 10^66.")
    elif num <= -10**66:
        assert Exception("Moc malé číslo! Nejsou povolena čísla rovná nebo menší než -10^66.")
    # uložíme jestli je zadané číslo záporné nebo kladné a převedeme ho na kladné
    negative = False
    if num < 0:
        negative = True
        num *= -1
    # od teď když budeme pracovat s zadaným číslem tak ho budeme potřebovat většinou jako string
    n = str(num) 
    # rozdělíme číslo do string po třech nebo méně když to na konci nevyjde
    # začneme u konce takže v n_lst budou tyto stringy pozpátku
    # Př: když n bude '1234567' tak n_lst bude ['567', '234', '1']
    n_lst = [] 
    for i in range(ceil(len(n)/3)):
        if i == 0:
            n_lst.append(n[-(i*3+3):])
        else:
            n_lst.append(n[-(i*3+3):-(i*3)])
    if form: # pokud chceme formátování
        # až od 1000 protože u menší čísel je toto formátování zbytečné
        # Př: z '123' na '123'
        if num >= 1000:
            # lépe naformátuje číslo
            #Př: ze '12345' na '12 345'
            print("Lépe formátované:",("-" if negative else "")+" ".join(n_lst[::-1]))
    # tady probíhá převedení na text
    ret_lst = []
    for i in range(len(n_lst)): # i je string 1-3 čísel Př: '12'
        # převede číslo na text Př: '12' na 'dvanáct'
        txt = from_0_to_999(int(n_lst[i]), i)
        # Tento IF je tu aby jsme zabránili věcem jako:
        # 'jeden tisíc' a aby jsme místo toho dostali 'tísic'
        # to můžeme ale udělat jen na začátku čísla
        # Př: chceme 'dva miliony jeden tisíc' a nechceme 'dva miliony tisíc'
        # Proto musíme zkontrolovat jestli jsme na začátku čísla,
        # což by bylo na konci listu n_lst protože jsou v něm části čísla
        # pozpátku. (to dělá tato část. i == len(n_lst)-1)
        # Také nechceme odstranit jedničku na začátku kdyby to
        # bylo pouze slovo 'jedna' bez tisíce, milionu atd.
        # (to dělá tato část: i != 0)
        if n_lst[i] == "1" and i == len(n_lst)-1 and i != 0:
            # do listu přidá get_higher který vrátí něco jako 'milion', 'miliarda' atd.
            ret_lst.append(get_higher(i, 1))
        elif txt != "":
            # do listu přidá txt který vypadá třeba 'jedenáct'
            # a get_higher který vrátí něco jako 'milion', 'tisíce' atd.
            ret_lst.append(txt+get_higher(i, int(n_lst[i])))
    # obrátíme ret_lst aby byly slova ve správném pořadí
    #Př: z ['dvě stě třicet čtyři', 'tisíc'] na ['tisíc', 'dvě stě třicet čtyři']
    ret_lst = ret_lst[::-1]
    # spojíme mezeramí ret_lst
    res = " ".join(ret_lst) 
    return ("mínus " if negative else "")+res.strip()

if __name__ == "__main__":
    while True:
        print(cislo_na_text(eval(input("Zadej číslo: ")), form=True))
