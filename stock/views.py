from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Stock
from .serializers import StockSerializer


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    def create(self, request, *args, **kwargs):
        # 모든 기존 데이터를 삭제
        Stock.objects.all().delete()

        # 새 데이터를 저장하기 위한 빈 결과 및 오류 리스트 생성
        results = []
        errors = []

        # 데이터가 리스트 형태인지 확인
        if isinstance(request.data, list):
            for index, item in enumerate(request.data):
                serializer = self.get_serializer(data=item)
                if serializer.is_valid():
                    # 새 객체를 생성 (ID를 순차적으로 지정)
                    stock = serializer.save(id=index + 1)
                    results.append(serializer.data)
                else:
                    errors.append(serializer.errors)

            if errors:
                return Response(errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(results, status=status.HTTP_201_CREATED)
        else:
            # 단일 객체 처리
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                stock = serializer.save(id=1)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
