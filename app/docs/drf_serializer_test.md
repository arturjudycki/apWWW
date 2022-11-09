Pierwszy model

>>> from polls.models import Competition
>>> from polls.serializers import CompetitionSerializer
>>> from rest_framework.renderers import JSONRenderer
>>> from rest_framework.parsers import JSONParser

>>> competition = Competition(idcompetition=1,city='Olsztyn',street='Kortowo',date='2022-12-6',description='Zawody ...')

>>> serializerCompetition = CompetitionSerializer(competition)

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

>>> deserializer.save() 
<Competition: Olsztyn>

Drugi model

>>> from polls.models import User
>>> from polls.serializers import UserSerializer

>>> user = User(iduser=1, email="artur.judycki@gmail.com", password="1234", firstname="Artur", lastname="Judycki", age=23, gender="M")
>>> serializerUser = UserSerializer(user)
>>> contentUser = JSONRenderer().render(serializerUser.data) 
>>> contentUser
b'{"iduser":1,"email":"artur.judycki@gmail.com","password":"1234","firstname":"Artur","lastname":"Judycki","age":23,"gender":"M"}'

>>> stream = io.BytesIO(contentUser) 
>>> data = JSONParser().parse(stream)
>>> deserializer = UserSerializer(data=data)   
>>> deserializer.is_valid() 
True
>>> deserializer.validated_data
OrderedDict([('iduser', 1), ('email', 'artur.judycki@gmail.com'), ('password', '1234'), ('firstname', 'Artur'), ('lastname', 'Judycki'), ('age', 23), ('gender', 'M')])
>>> deserializer.save() 
<User: User object (1)>
