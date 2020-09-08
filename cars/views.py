from django.shortcuts import render
from cars.models import Car
from cars.forms import CarSearchForm
from django.db.models import Q
from django.db.models import F
from django.views.generic import ListView
import logging


logger = logging.getLogger(__name__)


class CarList(ListView):
    model = Car
    template_name = 'index.html'


    def get_query_params(self, need_to_get):   #словарь параметров для запроса или словарь примененных фильтров при выводе результата
        
        names, have_choices = Car.get_fields_names()  #тут баловство с choices integer. можно было его сделать строковым.
        query_dict = {}   

        if need_to_get == 'name':
            query_dict = {name: self.request.GET.get(name) for name in names.keys() if self.request.GET.get(name)}

        elif need_to_get == 'verbose_name':
            for name, verbose_name in names.items():
                value = self.request.GET.get(name)
                if value:
                    if name in have_choices:
                        query_dict[verbose_name] = [y for x, y in have_choices[name] if str(x)==value][0]
                    else:
                        query_dict[verbose_name] = value  
        else:
            raise Exception('Непредусмотренное значение параметра')

        logger.debug('query_dict ({}): {}'.format(need_to_get, query_dict))

        return query_dict


    def get_context_data(self, **kwargs):
        context = super(CarList, self).get_context_data(**kwargs)
        context['form'] = CarSearchForm()

        if not self.request.GET:
            context['no_search'] = True
        else:
            context['filter_params'] = self.get_query_params('verbose_name')
            if not context['filter_params']:
                context['result'] = 'Задан пустой запрос'
            elif not context['object_list']:
                context['result'] = 'По запросу ничего не найдено'
            else:
                result_quont = len(context['object_list'])
                context['result'] = 'По запросу найдено автомобилей: {}'.format(result_quont)
                logger.info('User.id: {}. Результатов поиска: {}'.format(self.request.user.id, result_quont))
            
        return context


    def get_queryset(self):

        if not self.request.GET:
            cars_filter = Car.objects.all()

        else:

            query_params = self.get_query_params('name')   # словарь параметров для формирования Q запроса

            if not query_params:
                logger.info('User.id: {}. Пустой запрос'.format(self.request.user.id))
                return None

            and_condition = Q()
            for key, value in query_params.items():
                and_condition.add(Q(**{f'{key}__iexact': value}), Q.AND)

            cars_filter = Car.objects.filter(and_condition)
            if not cars_filter:
                logger.warning("User.id: {}. Нулевой результат поиска".format(self.request.user.id))
            
            # query_list = ['manufacturer', 'model', 'year_of_manufacture', 'transmission', 'color']
            # manufacturer = self.request.GET.get('manufacturer')
            # model = self.request.GET.get('model')
            # year_of_manufacture = self.request.GET.get('year_of_manufacture')
            # transmission = self.request.GET.get('transmission')
            # color = self.request.GET.get('color')
            # for value in query_list:
            #     val = locals().get(value)
            #     if val:
            #         query_params[value] = val

        return cars_filter
