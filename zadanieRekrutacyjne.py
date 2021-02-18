

def are_anagrams(s1, s2, s3):
    ''' funkcja sorted została użyta, aby znaki w s1, s2 i s3 zostały posortowane
    następnie s1, s2, s3 zostały ze sobą porównane, ponieważ jeżeli są anagramami to po sortowaniu powinny być sobie równe
    następnie wiedząc, że s1, s2 i s3 muszą być sobie równe wybrany został jeden z nich po to, żeby sprawdzić czy dłogość łańcucha znaków jest równa 5
    jeżeli zostaną spełnione wszystkie warunki funkcja zwróci wartość True, a jeżeli którykolwiek warunek nie zostanie spełniony funkcja zwróci wartość False'''
    return sorted(s1) == sorted(s2) == sorted(s3) and len(s1) == 5


