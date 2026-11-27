from faker import Faker

fake_example = Faker('ru_RU')

print(fake_example.email())
print(fake_example.name())
print(fake_example.address())
