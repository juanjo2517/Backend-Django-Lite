""" Views BussinesCompany """

# Django Rest
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Permissions 
from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.bussines import serializers

# Serializer 
from apps.bussines.serializers import BussinesCompanySerializer

# Models 
from apps.bussines.models import BussinesCompany

class BussinesCompanyView(viewsets.ViewSet):
    serializer_class = BussinesCompanySerializer
    queryset = BussinesCompany.objects.filter(is_active = True)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['create']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
    
    def list(self, request, *args, **kwargs):
        query = self.get_queryset()
        serializer = self.serializer_class(query, many=True).data
        return Response(serializer)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_bussines = serializer.save()

        data = {
            "message": "Empresa creada correctamente",
            "bussines_company": self.serializer_class(new_bussines).data
        }

        return Response(data)
    
    def update(self, request, pk=None):
        bussines = BussinesCompany.objects.filter(id=pk).first()

        if not bussines:
            return Response({"message": "No existe empresa con este ID"})
        
        serializer = self.serializer_class(bussines, data=request.data)
        serializer.is_valid(raise_exception=True)
        bussines_upt = serializer.save()

        data = {
            "message": "Empresa actualizada correctamente",
            "bussines_company": self.serializer_class(bussines_upt).data
        }

        return Response(data)

    def destroy(self, request, pk=None):
        bussines = BussinesCompany.objects.filter(id=pk).first()
        if not bussines:
            return Response({"message": "No existe empresa con este ID"})
        
        bussines.delete()
        return Response({"message": "La empresa se ha eliminado con exito."})

    def get_queryset(self):
        return BussinesCompany.objects.filter(is_active = True)