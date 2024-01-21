from django.db import models

class EntryManager(models.Manager):
    """ procedimiento para entrada"""
    
    def entrada_en_portada(self):
        return self.filter(
            public=True,
            portada=True,
        ).order_by('-created').first()