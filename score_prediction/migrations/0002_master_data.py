# Generated by Django 4.1.13 on 2024-05-03 06:52

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ("score_prediction", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="master_data",
            fields=[
                (
                    "_id",
                    djongo.models.fields.ObjectIdField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("match_id", models.IntegerField(db_column="match_id", null=True)),
                (
                    "venue",
                    models.CharField(db_column="venue", max_length=100, null=True),
                ),
                ("innings", models.IntegerField(db_column="innings", null=True)),
                (
                    "batting_team",
                    models.CharField(
                        db_column="batting_team", max_length=100, null=True
                    ),
                ),
                (
                    "bowling_team",
                    models.CharField(
                        db_column="bowling_team", max_length=100, null=True
                    ),
                ),
                ("overs", models.IntegerField(db_column="overs", null=True)),
                ("balls", models.IntegerField(db_column="balls", null=True)),
                (
                    "striker",
                    models.CharField(db_column="striker", max_length=100, null=True),
                ),
                (
                    "non_striker",
                    models.CharField(
                        db_column="non_striker", max_length=100, null=True
                    ),
                ),
                (
                    "bowler",
                    models.CharField(db_column="bowler", max_length=100, null=True),
                ),
                (
                    "runs_off_bat",
                    models.IntegerField(db_column="runs_off_bat", null=True),
                ),
                ("extras", models.IntegerField(db_column="extras", null=True)),
                (
                    "runs_scored",
                    models.IntegerField(db_column="runs_scored", null=True),
                ),
                ("isOut", models.IntegerField(db_column="isOut", null=True)),
                (
                    "phase",
                    models.CharField(db_column="phase", max_length=100, null=True),
                ),
                ("cum_runs", models.IntegerField(db_column="cum_runs", null=True)),
                (
                    "cum_wickets",
                    models.IntegerField(db_column="cum_wickets", null=True),
                ),
                ("total_runs", models.IntegerField(db_column="total_runs", null=True)),
                (
                    "total_wickets",
                    models.IntegerField(db_column="total_wickets", null=True),
                ),
                ("cum_balls", models.IntegerField(db_column="cum_balls", null=True)),
                ("balls_left", models.IntegerField(db_column="balls_left", null=True)),
                (
                    "wickets_left",
                    models.IntegerField(db_column="wickets_left", null=True),
                ),
                ("runs_added", models.IntegerField(db_column="runs_added", null=True)),
                (
                    "toss_winner",
                    models.CharField(
                        db_column="toss_winner", max_length=100, null=True
                    ),
                ),
                (
                    "winner",
                    models.CharField(db_column="winner", max_length=100, null=True),
                ),
                ("dateint", models.IntegerField(db_column="dateint", null=True)),
            ],
            options={"db_table": "master_data", "managed": False,},
        ),
    ]
