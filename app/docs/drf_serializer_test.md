Pierwszy model

>>> from polls.models import Competition
>>> from polls.serializers import CompetitionSerializer
>>> from rest_framework.renderers import JSONRenderer
>>> from rest_framework.parsers import JSONParser

>>> competition = Competition(idcompetition=1,city='Olsztyn',street='Kortowo',date='2022-12-6',description='Zawody ...')
>>> competition.save()                                                                                                   
>>> Competition.objects.all()
<QuerySet [<Competition: Olsztyn>]>

>>> serializerCompetition = CompetitionSerializer(competition)
>>> serializerCompetition.data                                
{'idcompetition': 1, 'city': 'Olsztyn', 'street': 'Kortowo', 'date': '2022-12-6', 'descr
iption': 'Zawody ...'}

>>> contentCompetition = JSONRenderer().render(serializerCompetition.data)
>>> contentCompetition                                                    
b'{"idcompetition":1,"city":"Olsztyn","street":"Kortowo","date":"2022-12-6","description
":"Zawody ..."}'

>>> import io
>>> stream = io.BytesIO(contentCompetition)
>>> data = JSONParser().parse(stream)
>>> deserializer = CompetitionSerializer(data=data)
>>> deserializer.is_valid()                        
True

>>> deserializer.validated_data
OrderedDict([('idcompetition', 1), ('city', 'Olsztyn'), ('street', 'Kortowo'), ('date', 
datetime.date(2022, 12, 6)), ('description', 'Zawody ...')])

Drugi model


