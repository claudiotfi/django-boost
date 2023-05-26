from django.db import models

class Cliente(models.Model):
    active = models.BooleanField(default=False)
    name = models.CharField(max_length=255, unique=True)
    alias = models.CharField(max_length=255)
    db_driver = models.CharField(max_length=255)
    db_host = models.CharField(max_length=255)
    db_port = models.CharField(max_length=255)
    db_database = models.CharField(max_length=255)
    db_username = models.CharField(max_length=255)
    db_password = models.CharField(max_length=255)
    db_unix_socket = models.CharField(max_length=255, null=True, blank=True)
    db_charset = models.CharField(max_length=255, null=True, blank=True)
    db_collation = models.CharField(max_length=255, null=True, blank=True)
    db_prefix = models.CharField(max_length=255, null=True, blank=True)
    db_prefix_indexes = models.BooleanField(default=True)
    db_strict = models.BooleanField(default=True)
    db_engine = models.CharField(max_length=255, null=True, blank=True)
    bucket_driver = models.CharField(max_length=255, null=True, blank=True)
    bucket_key = models.CharField(max_length=255, null=True, blank=True)
    bucket_secret = models.CharField(max_length=255, null=True, blank=True)
    bucket_region = models.CharField(max_length=255, null=True, blank=True)
    bucket_bucket = models.CharField(max_length=255, null=True, blank=True)
    bucket_endpoint = models.CharField(max_length=255, null=True, blank=True)
    public_storage = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'clientes'

    def __str__(self):
        return self.name


