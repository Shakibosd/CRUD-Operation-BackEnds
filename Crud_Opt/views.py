from rest_framework.views import APIView
from .models import Plan
from .serializers import PlanSerializer
from rest_framework import status
from rest_framework.response import Response

class PostApiView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = PlanSerializer(data=data, context={'request': request})

        if serializer.is_valid():
            plan = serializer.save()
            return Response(PlanSerializer(plan).data, status=status.HTTP_201_CREATED)  
        print("Validation Errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class GetApiView(APIView):
    def get(self, request, id=None, *args, **kwargs):
        if id:
            try:
                plan = Plan.objects.get(id=id)
                serializer = PlanSerializer(plan, context={'request': request})
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Plan.DoesNotExist:
                return Response({"Detail": "Plan Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
        plans = Plan.objects.all()
        serializer = PlanSerializer(plans, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, *args, **kwargs):
        try:
            plan = Plan.objects.get(id=id)
        except Plan.DoesNotExist:
            return Response({"Detail": "Plan Not Found"}, status=status.HTTP_404_NOT_FOUND)

        data = request.data
        serializer = PlanSerializer(plan, data=data, partial=True) 
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DeleteApiView(APIView):
    def delete(self, request, id, *args, **kwargs):
        try:
            plans = Plan.objects.get(id=id)
            plans.delete()
            return Response({"Message" : "Plan Delete Successfull"}, status=status.HTTP_204_NO_CONTENT)
        except Plan.DoesNotExist:
            return Response({"Detail" : "Plan Not Found"}, status=status.HTTP_404_NOT_FOUND)