from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView

from webapp.models import File


class FilesView(ListView):
    template_name = 'file/files_view.html'
    model = File
    context_object_name = 'files'
    paginate_by = 2
    paginate_orphans = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        query = self.request.GET.get('search')
        kwargs['search'] = query
        return super().get_context_data(object_list=object_list, **kwargs)

    def get_queryset(self):
        data = super().get_queryset()
        query = self.request.GET.get('search')
        print(query)
        if query:
            data = self.model.objects.filter(name__icontains=query)
        return data

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     files, page, is_paginated = self.paginate_comments(self.model)
    #     context['files'] = files
    #     context['page_obj'] = page
    #     context['is_paginated'] = is_paginated
    #
    #     return context
    #
    # def paginate_comments(self, queryset):
    #     files = queryset.objects.all().order_by('-upload_date')
    #     if files.count() > 0:
    #         paginator = Paginator(files, 10, orphans=0)
    #         page_number = self.request.GET.get('page', 1)
    #         page = paginator.get_page(page_number)
    #         is_paginated = paginator.num_pages > 1  # page.has_other_pages()
    #         return page.object_list, page, is_paginated
    #     else:
    #         return files, None, False
