from django.db import models
from django.utils.timezone import datetime
from datetime import datetime


class CatechismRegister(models.Model):
    ESTADO_CIVIL_CHOICES = [
        ('casados', 'Casados'),
        ('juntos(não casado)', 'União de fato'),
        ('divorciados', 'Divorciado(a)'),
        ('viúvo', 'Viúvo(a)'),
        ('solteiro', 'Solteiro(a)'),
    ]

    full_name = models.CharField(
        max_length=70, blank=False, verbose_name='Nome Completo'
    )
    data_nas = models.DateField(
        blank=False, verbose_name='Data de Nascimento'
    )
    district = models.CharField(
        max_length=40, blank=False, verbose_name='Bairro'
    )
    street = models.CharField(
        max_length=80, blank=False, verbose_name='Rua'
    )
    num_house = models.IntegerField(
        blank=False, verbose_name='Número da Casa'
    )
    local_batismo = models.CharField(
        max_length=80, verbose_name='Local de Batismo', blank=True, null=True
    )
    data_batismo = models.DateField(
        verbose_name='Data de Batismo', blank=True, null=True
    )
    celular = models.CharField(
        max_length=30, blank=False, verbose_name='Celular'
    )
    # Dados sobre os sacramentos
    batismo = models.BooleanField(
        default=False, verbose_name='É Batizado?'
    )
    pri_eucaristia = models.BooleanField(
        default=False, verbose_name='Fez a Primeira Eucaristia?'
    )
    crisma = models.BooleanField(
        default=False, verbose_name='Recebeu o Crisma?'
    )
    # Dados sobre os pais
    mom_name = models.CharField(
        max_length=70, blank=False, verbose_name='Nome do Pai'
    )
    father_name = models.CharField(
        max_length=70, blank=False, verbose_name='Nome da Mãe'
    )
    estado_civil = models.CharField(
        max_length=30, choices=ESTADO_CIVIL_CHOICES,
        default='casados', verbose_name='Estado Civil', blank=False
    )
    # Observações preenchidos pelo operador
    observation = models.TextField(
        default='sem observações', verbose_name='Observações'
    )
    amount = models.BooleanField(default=False, verbose_name='Taxa')
    subscription_date = models.DateField(
        default=datetime.now, verbose_name='Data de Inscrição'
    )
    user_id = models.ForeignKey(
        'accounts.UserCustom', on_delete=models.DO_NOTHING, verbose_name='Catequista'
    )
    is_active = models.BooleanField(default=True, verbose_name='Ativo?')

    def __int__(self):
        return self.id_fixa

    def __str__(self):
        idade = ((datetime.today().date() - self.data_nas) // 365).days
        return f"{self.full_name} - {idade} anos"


class Room(models.Model):
    number = models.IntegerField(
        primary_key=True, blank=False, verbose_name='Numero da Sala'
    )
    description = models.CharField(
        max_length=300, default='Centro catequético - Matriz',
        verbose_name='Localização'
    )

    def __str__(self):
        return f'Sala {self.number} | {self.description}'


class AgeGroup(models.Model):
    age_group = models.CharField(
        max_length=300, default='9 - 10', verbose_name='Faixa etária'
    )

    def __str__(self):
        return f'Entre {self.age_group} anos'


class CatechismCalss(models.Model):
    description = models.CharField(
        max_length=500, verbose_name='Descrição da turma'
    )
    year = models.DateField(blank=True, null=True)
    age_group_id = models.ForeignKey(
        AgeGroup, verbose_name='Faixa etária', on_delete=models.DO_NOTHING
    )
    room_id = models.ForeignKey(
        Room, verbose_name='Local', on_delete=models.DO_NOTHING
    )
    user_id = models.ManyToManyField(
        'accounts.UserCustom', blank=False, verbose_name='Catequistas'
    )
    catechism_register_id = models.ManyToManyField(
        CatechismRegister, blank=True, verbose_name='Catequisandos'
    )

    def __str__(self):
        _date = self.year.year
        return f'{self.description} do ano {_date}'
