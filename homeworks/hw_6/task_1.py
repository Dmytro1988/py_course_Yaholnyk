S = int(input('Количество лепестков: '))
lst = ['I love you', 'a little', 'a lot', 'passionately', 'madly', 'not at all']
if S > 0:
    S % 6
    print(lst[int(S % 6)-1])
