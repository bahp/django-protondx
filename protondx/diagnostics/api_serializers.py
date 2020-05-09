# Django rest framework
from rest_framework import serializers

# Models
from .models import Device
from .models import Cartridge
from .models import Experiment

# -----------------------------------------------------------------------------
#                             Case Serializer
# -----------------------------------------------------------------------------
class DeviceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Device
    fields = '__all__'

class CartridgeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cartridge
    fields = '__all__'

class ExperimentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Experiment
    fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):

  # Add summary information
  summary_count = serializers.SerializerMethodField()

  class Meta:
    model = Experiment
    fields = '__all__'

  def get_summary_count(self, obj):
    return 5
    #return obj.user_set.count()