from experiment import Person

p1 = Person("name1", 1)
p2 = Person('name2', 2)

p1.stop_eating()
p1.eat()
p1.eat()
p1.speak('subject')
p1.stop_eating()
p1.speak('subject')
p1.speak('subject')
x = p1.get_year()
print(x)
y = p1.use_year('stuff', 2000)
print(y.age)
