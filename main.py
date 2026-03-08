def is_valid_hsl(hsl):
    # check the 'hsl(' string is in the valid format 
    if hsl.find('hsl(') == -1: return False
    # remove all black spaces
    hsl_stripped = hsl.replace(' ','')
    # find possition of first comma
    pos_first_comma = hsl_stripped.find(',')
    # find possition of %,
    pos_porc_comma = hsl_stripped.find('%,')
    # find possition of %)
    pos_porc_par = hsl_stripped.find('%)')
    # check one possible wrong format
    if pos_porc_comma == -1: return False
    # check another possible wrong format
    if pos_porc_par == -1: return False
    # check (hue) betwwen 0 and 360
    if int(hsl_stripped[4:pos_first_comma]) < 0 or int(hsl_stripped[4:pos_first_comma]) > 360: return False
    # check saturation
    if int(hsl_stripped[pos_first_comma+1:pos_porc_comma]) < 0 or int(hsl_stripped[pos_first_comma+1:pos_porc_comma]) > 100 : return False
    # check lightness 
    if int(hsl_stripped[pos_porc_comma+2:pos_porc_par]) < 0 or int(hsl_stripped[pos_porc_comma+2:pos_porc_par]) > 100 : return False
    return True

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