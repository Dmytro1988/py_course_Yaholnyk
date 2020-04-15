def correct_polish_letters(st): 
    polish_let = {
        'ą' : 'a',
        'ć' : 'c',
        'ę' : 'e',
        'ł' : 'l',
        'ń' : 'n',
        'ó' : 'o',
        'ś' : 's',
        'ź' : 'z',
        'ż' : 'z'}

    for i in polish_let.keys():
        st=st.replace(i,polish_let[i])
            
    return st



print(correct_polish_letters("Jędrzej Błądziński"),"Jedrzej Bladzinski");
print(correct_polish_letters("Lech Wałęsa"),"Lech Walesa");
print(correct_polish_letters("Maria Skłodowska-Curie"),"Maria Sklodowska-Curie")    


#There are 32 letters in the Polish alphabet: 9 vowels and 23 consonants.
#Your task is to change the letters with diacritics