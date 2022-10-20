wyświetl wszystkie obiekty modelu Osoba - 

>>> from polls.models import Osoba           
>>> Osoba.objects.all()
<QuerySet [<Osoba: Janina Kowalska>, <Osoba: Jadwiga Kowalska>, <Osoba: Ewa Kowalska>, <Osoba: Jan Kowalski>, <Osoba: Andrzej Kowalski>, <Osoba: Dave Kowalski>]>

wyświetl obiekt modelu Osoba z id = 3 -

>>> Osoba.objects.filter(id=3) 
<QuerySet [<Osoba: Jadwiga Kowalska>]>

wyświetl obiekty modelu Osoba, których nazwa rozpoczyna się na wybraną przez Ciebie literę alfabetu (tak, żeby był co najmniej jeden wynik) - 

>>> Osoba.objects.filter(imie__startswith='J')     
<QuerySet [<Osoba: Janina Kowalska>, <Osoba: Jadwiga Kowalska>, <Osoba: Jan Kowalski>]>

wyświetl unikalną listę drużyn przypisanych dla modeli Osoba -

>>> Osoba.objects.all().values_list('druzyna').distinct()  
<QuerySet [(None,), (1,), (3,), (None,), (2,)]>

wyświetl nazwy drużyn posortowane alfabetycznie malejąco -

>>> from polls.models import Druzyna     
>>> Druzyna.objects.order_by('-nazwa')
<QuerySet [<Druzyna: MetaCritic (US)>, <Druzyna: Imdb (EN)>, <Druzyna: Filmweb (PL)>]>

dodaj nową instancję obiektu klasy Osoba -

>>> new_person = Osoba(imie='Marek', nazwisko='Nowak', miesiac_urodzenia=12, druzyna=Druzyna(1))  
>>> new_person.save()
