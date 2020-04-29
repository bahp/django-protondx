# Generic library
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

# Create default superuser
class Command(BaseCommand):

  def handle(self, *args, **options):
    """This method handles the command

    It creates a default superuser.
    """
    # The superuser already exists
    if User.objects.filter(username="cbit").exists():
      return

    # Create superuser
    User.objects.create_superuser(username="cbit", 
         email="cbit@imperial.ac.uk", first_name='CBIT',
         last_name='Imperial College', password="toor")