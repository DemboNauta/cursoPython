from collections import Counter, defaultdict, OrderedDict, namedtuple

import datetime
import locale
import math
import random

p= "gato gato perro perro canario canario perro leon"
c = Counter(p.split())

l = [10,20,30,40,10,10,20,30]
c = Counter(l)


d = defaultdict(float)
d['otro']=12.4


n = OrderedDict()

n['uno']="one"
n['dos']="two"
n['tres']="three"

n1= OrderedDict()

n1['uno']="one"
n1['dos']="two"

n2=OrderedDict()
n2['dos']="two"
n2['uno']="one"



t=(20,40,60)
Persona= namedtuple('Persona', 'nombre apellido edad')

p = Persona(nombre="Edgar", apellido="Milá", edad=19)



dt = datetime.datetime.now()

# print("{}:{}:{}".format(dt.hour, dt.minute, dt.second))
# print("{}/{}/{}".format(dt.day, dt.month, dt.year))

dt = datetime.datetime(2004, 11, 19)

locale.setlocale(locale.LC_ALL, 'es-ES')
dt = datetime.datetime.now()
# print(dt.strftime("%A %d de %B de %Y %H:%M"))


pi = 3.14159


# print(math.ceil(pi))


floatRandom = random.uniform(1,11)


intRandom= random.randrange(0,101, 2)


c = list("Hola mundo")

print(random.shuffle(c))