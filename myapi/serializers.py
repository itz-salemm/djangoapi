from rest_framework import serializers, employees

class employeesSerializer(Serializers.ModelSerializers):
    
    class Meta():
        model = employees
        #fields = ('firstname', 'lastname')
        fields = '__all__'