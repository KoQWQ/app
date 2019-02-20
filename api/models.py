from __future__ import unicode_literals
from django.db import models
from project.settings import AUTH_USER_MODEL

COMPETITION_TYPES = (
    ('PAIR_CONTEST', 'Парный конкурс'),
    ('ASSOCIATION_COMPETITION', 'Конкурс-ассоциации'),
)

ROUND_TYPES = (
    ('QUALIFYING', 'Отборочные'),
    ('SEMIFINAL', 'Полуфинал'),
    ('FINAL', 'Финал'),
    ('REDANCE', 'Перетанцовки'),
)

GENDER_TYPES = (
	('MALE', 'Мужской'),
	('FEMALE', 'Женский')
)

# USER_TYPES = (
#     ('JUDGE', 'Судья'),
#     ('OBSERVER', 'Наблюдатель')
# )

class Participant(models.Model):
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    name = models.CharField(max_length=50, verbose_name='Имя')
    gender = models.CharField(
        max_length=50,
        choices=GENDER_TYPES,
        default='MALE',
        verbose_name='Пол'
    )
    payment = models.BooleanField(default=False, verbose_name='Оплата внесена')
    city = models.CharField(max_length=50, verbose_name='Город')
    school_name = models.CharField(max_length=50, verbose_name='Название школы')
    place_in_competition = models.PositiveIntegerField(blank=True, null=True, verbose_name='Место в конкурсе')
    score = models.PositiveIntegerField(default=0, verbose_name='Количество набранных участником баллов')
    number = models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер участника в конкурсе')

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'


    def __str__(self):
        return '{} {}'.format(self.surname, self.name)

class Competition(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название конкурса')
    type = models.CharField(
        max_length=50,
        choices=COMPETITION_TYPES,
        default='PAIR_CONTEST',
        verbose_name='Тип конкурса'
    )
    date = models.DateTimeField(verbose_name='Дата проведения конкурса')
    cost = models.PositiveIntegerField(default=0, verbose_name='Стоимость участия')
    participants = models.ManyToManyField(Participant, blank=True, verbose_name='Участники конкурса', related_name="users")
    judges = models.ManyToManyField(AUTH_USER_MODEL, blank=True, verbose_name='Судьи конкурса', related_name="judges")

    class Meta:
    	verbose_name = 'Конкурс'
    	verbose_name_plural = 'Конкурсы'

    def __str__(self):
        return self.name


# class Judge(models.Model):
#     surname = models.CharField(max_length=50, verbose_name='Фамилия')
#     name = models.CharField(max_length=50, verbose_name='Имя')
#     middlename = models.CharField(max_length=50, blank=True, verbose_name='Отчество')
#     email = models.CharField(max_length=50, verbose_name='Почтовый адрес')
#     user_type = models.CharField(
#         max_length=50,
#         choices=USER_TYPES,
#         default='JUDGE',
#         verbose_name='Тип пользователя'
#     )
#     competition = models.ManyToManyField(Competition, blank=True, verbose_name='Конкурсы, в которых он является судьей')

#     class Meta:
#     	verbose_name = 'Судья'
#     	verbose_name_plural = 'Судьи'


class Round(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    type = models.CharField(
        max_length=50,
        choices=ROUND_TYPES,
        default='QUALIFYING',
    )
    number_of_visits =  models.PositiveIntegerField(verbose_name='Количество заходов')
    number_passing_partisipant = models.PositiveIntegerField(blank=True, verbose_name='Количество проходящих участников')
    competition = models.ForeignKey(Competition, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Конкурс')
    participants = models.ManyToManyField(Participant, blank=True, verbose_name='Участники конкурса', related_name="participants")

    class Meta:
    	verbose_name = 'Тур'
    	verbose_name_plural = 'Туры'

    def __str__(self):
        return '{} - {}'.format(self.name, self.competition)


class Entry(models.Model):
    competition = models.OneToOneField(Competition, blank=True, null=True, on_delete=models.CASCADE, related_name='competitions', verbose_name='Конкурс')
    round = models.ForeignKey(Round, blank=True, null=True, on_delete=models.CASCADE, related_name='round', verbose_name='Тур')
    participants = models.ManyToManyField(Round, blank=True, related_name='_participants', verbose_name='Участники')
    pass_off = models.BooleanField(default=False, verbose_name='Участник проходит')
    comment = models.TextField(blank=True, null=True, verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Заход'
        verbose_name_plural = 'Заходы'

    def __str__(self):
        return '{} - {}'.format(self.competition, self.round)