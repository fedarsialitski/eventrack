from rest_framework.pagination import PageNumberPagination


class PagePagination(PageNumberPagination):
    page_size_query_param = 'per_page'
    max_page_size = 50
