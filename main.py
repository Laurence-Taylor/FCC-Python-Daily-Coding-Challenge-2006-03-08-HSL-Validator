def is_valid_hsl(hsl):
    if hsl.find('hsl(') == -1: return False
    hsl_stripped = hsl.replace(' ','')
    pos_first_coma = hsl.find(',')
    pos_porc_come = hsl.find('%,')
    pos_porc_pare = hsl.find('%)')
    #if pos_porc_pare == -1: return False
    return hsl_stripped

if __name__ == '__main__':
    print(is_valid_hsl("hsl(240, 50%, 50%)"))
    print('--------')
    print(is_valid_hsl("hsl( 200 , 50% , 75% )"))
    print('--------')
    print(is_valid_hsl("hsl(99,60%,80%);"))
    print('--------')
    print(is_valid_hsl("hsl(0, 0%, 0%) ;"))
    print('--------')
    print(is_valid_hsl("hsl(  10  ,  20%   ,  30%   )    ;"))
    print('--------')
    print(is_valid_hsl("hsl(361, 50%, 80%)"))
    print('--------')
    print(is_valid_hsl("hsl(300, 101%, 70%)"))
    print('--------')
    print(is_valid_hsl("hsl(200, 55%, 75)"))
    print('--------')
    print(is_valid_hsl("hsl (80, 20%, 10%)"))