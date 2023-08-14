from rest_framework import serializers
from .models import Workspace, WorkspacesMembership

class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = '__all__'  


class WorkspacesMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkspacesMembership
        fields = '__all__'  


class WorkspaceWithMembersSerializer(serializers.ModelSerializer):
    members = serializers.StringRelatedField(many=True)  
    boards = serializers.SerializerMethodField()

    class Meta:
        model = Workspace
        fields = '__all__'

    def get_boards(self, obj):
        return [board.name for board in obj.get_boards()]
    
class WorkspacesMembershipDetailSerializer(serializers.ModelSerializer):
    workspace = WorkspaceSerializer()
    member = serializers.StringRelatedField()

    class Meta:
        model = WorkspacesMembership
        fields = '__all__'