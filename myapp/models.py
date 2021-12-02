from django.db import models

# Create your models here.
sample_type_choices = (('wet sediment','Wet Sediment'),('dry sediment','Dry Sediment'),('water','Water'),('water & solvent', 'Water & Solvent'),('extract', 'Extract'))
extraction_method_choices = (('soxhlet','Soxhlet'), ('saponification', 'Saponification'), ('sepratory funnel','Sepratory Funnel'),
('roller','Roller'),('other','Other'))
sample_cleanup_choices = (('silica gel', 'Silica Gel'), ('gpc', 'GPC'), ('purge & trap', 'Purge & Trap'), ('none', 'None'))
analysis_instrumentation_choices = (('gc/ms', 'GC/MS'),('gc/fid','GC/FID'),('spectrophotometer','Spectrophotometer'),('iatroscan','Iatroscan'),('lc','LC'),('none', 'None'))

class Snippet(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default='')
    quantity = models.IntegerField(default=1)
    description = models.TextField()
    sample_type = models.CharField(max_length = 100, choices=sample_type_choices, blank=True)
    extraction_method = models.CharField(max_length= 100, choices=extraction_method_choices, blank=True)
    sample_cleanup = models.CharField(max_length= 100, choices=sample_cleanup_choices, blank=True)
    analysis_instrumentation = models.CharField(max_length= 100, choices=analysis_instrumentation_choices, blank=True)
    analysis_pah = models.BooleanField(default=False)
    analysis_alkanes = models.BooleanField(default=False)
    analysis_phenols = models.BooleanField(default=False)
    analysis_tph = models.BooleanField(default=False)
    analysis_btex = models.BooleanField(default=False)
    log_comments = models.TextField()

    def __str__(self):
        return self.name
