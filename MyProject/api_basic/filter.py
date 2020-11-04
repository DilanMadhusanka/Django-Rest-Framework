from rest_framework import filters


class IsTitleFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        title = request.query_params.get('name', None)
        if title is not None:
            return queryset.filter(title=title)
        return queryset
