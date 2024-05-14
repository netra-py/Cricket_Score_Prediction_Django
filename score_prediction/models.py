from djongo import models

# Create your models here.
class team_data(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    team = models.CharField(db_column='team', blank=False, null=True,max_length = 100)
    tid = models.CharField(db_column='tid', blank=False, null=True,max_length = 100)

    class Meta:
        managed = False
        db_table = 'team_data'

class venue_data(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    venue = models.CharField(db_column='venue', blank=False, null=True,max_length = 100)
    vid = models.CharField(db_column='vid', blank=False, null=True,max_length = 100)

    class Meta:
        managed = False
        db_table = 'venue_data'

class master_data(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    match_id = models.IntegerField(db_column='match_id', blank=False, null=True)
    venue = models.CharField(db_column='venue', blank=False, null=True,max_length = 100)
    innings = models.IntegerField(db_column='innings', blank=False, null=True)
    batting_team = models.CharField(db_column='batting_team', blank=False, null=True,max_length = 100)
    bowling_team = models.CharField(db_column='bowling_team', blank=False, null=True,max_length = 100)
    overs = models.IntegerField(db_column='overs', blank=False, null=True)
    balls = models.IntegerField(db_column='balls', blank=False, null=True)
    striker = models.CharField(db_column='striker', blank=False, null=True,max_length = 100)
    non_striker = models.CharField(db_column='non_striker', blank=False, null=True,max_length = 100)
    bowler = models.CharField(db_column='bowler', blank=False, null=True,max_length = 100)
    runs_off_bat = models.IntegerField(db_column='runs_off_bat', blank=False, null=True)
    extras = models.IntegerField(db_column='extras', blank=False, null=True)
    runs_scored = models.IntegerField(db_column='runs_scored', blank=False, null=True)
    isOut = models.IntegerField(db_column='isOut', blank=False, null=True)
    phase = models.CharField(db_column='phase', blank=False, null=True,max_length = 100)
    cum_runs = models.IntegerField(db_column='cum_runs', blank=False, null=True)
    cum_wickets = models.IntegerField(db_column='cum_wickets', blank=False, null=True)
    total_runs = models.IntegerField(db_column='total_runs', blank=False, null=True)
    total_wickets = models.IntegerField(db_column='total_wickets', blank=False, null=True)
    cum_balls = models.IntegerField(db_column='cum_balls', blank=False, null=True)
    balls_left = models.IntegerField(db_column='balls_left', blank=False, null=True)
    wickets_left = models.IntegerField(db_column='wickets_left', blank=False, null=True)
    runs_added = models.IntegerField(db_column='runs_added', blank=False, null=True)
    toss_winner = models.CharField(db_column='toss_winner', blank=False, null=True,max_length = 100)
    winner = models.CharField(db_column='winner', blank=False, null=True,max_length = 100)
    dateint = models.IntegerField(db_column='dateint', blank=False, null=True)

    class Meta:
        managed = False
        db_table = 'master_data'











