def clean_currency(value:str) -> float:
    '''
    This function will take a string value and remove the dollar sign and commas
    and return a float value.
    '''
    return float(value.replace(',', '').replace('$', ''))

'''
In module `check_functions.py`
1. copy over the `detect_whale()` function and tests
2. write function `detect_tipper(tip_pct, tip_pcy_75th_pctile, tip_pct_25_pctile)`
    - should return either "light", "heavy" or ""
3. write tests for `detect_tipper()`
'''
def detect_whale(
        items_per_person:float, 
        price_per_person:float, 
        items_per_person_75th_pctile:float, 
        price_per_person_75_pctile:float) -> str:
    if items_per_person > items_per_person_75th_pctile and price_per_person > price_per_person_75_pctile:
        return 'whale'
    if items_per_person > items_per_person_75th_pctile:
        return 'big eater'
    if price_per_person > price_per_person_75_pctile:
        return 'big spender'
    
    return ''

def detect_whale(tip_pct:float, tip_pcy_75th_pctile:float, tip_pct_25_pctile:float) -> str:
    if tip_pct > tip_pcy_75th_pctile:
        return 'heavy tipper'
    if tip_pct < tip_pct_25_pctile:
        return 'light tipper'
    return ''

if __name__ == '__main__':
    # tests
    assert clean_currency('$1,000.00') == 1000.00
    assert clean_currency('$1,000') == 1000.00
    assert clean_currency('1,000') == 1000.00
    assert clean_currency('$1000') == 1000.00

    assert detect_whale(tip_pct=0.05, tip_pcy_75th_pctile=0.30, tip_pct_25_pctile=0.15) == 'light tipper'
    assert detect_whale(tip_pct=0.55, tip_pcy_75th_pctile=0.30, tip_pct_25_pctile=0.15) == 'heavy tipper'
    assert detect_whale(tip_pct=0.25, tip_pcy_75th_pctile=0.30, tip_pct_25_pctile=0.15) == ''
