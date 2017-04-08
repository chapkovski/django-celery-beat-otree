# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import otree.db.models
import otree_save_the_change.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('otree', '0019_delete_expectedroomparticipant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('price', otree.db.models.IntegerField(null=True, default=0)),
                ('howmanyleft', otree.db.models.IntegerField(null=True, default=3)),
                ('session', models.ForeignKey(related_name='bigfive_group', to='otree.Session')),
            ],
            options={
                'db_table': 'bigfive_group',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(null=True, max_digits=12, default=0)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_group_by_arrival_time_arrived', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('_group_by_arrival_time_grouped', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('drop', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('group', models.ForeignKey(null=True, to='bigfive.Group')),
                ('participant', models.ForeignKey(related_name='bigfive_player', to='otree.Participant')),
                ('session', models.ForeignKey(related_name='bigfive_player', to='otree.Session')),
            ],
            options={
                'db_table': 'bigfive_player',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(to='otree.Session', related_name='bigfive_subsession', null=True)),
            ],
            options={
                'db_table': 'bigfive_subsession',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.AddField(
            model_name='player',
            name='subsession',
            field=models.ForeignKey(to='bigfive.Subsession'),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(to='bigfive.Subsession'),
        ),
    ]
