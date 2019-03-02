from rest_framework.pagination import PageNumberPagination


class PagePagination(PageNumberPagination):
    page_size_query_param = 'per_page'
    max_page_size = 50

    def get_paginated_response(self, data):
        response = super(PagePagination, self).get_paginated_response(data)
        response.data['pages'] = self.page.paginator.num_pages

        return response
