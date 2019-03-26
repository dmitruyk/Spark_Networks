from ...models.general import *
from ...models.output_models.full import RentFullViewModel
from django.http import JsonResponse


def search(request):
    if request.method == 'GET':
        result = []
        filter_street = request.GET.get('street', None)
        filter_country = request.GET.get('country', None)
        filter_city = request.GET.get('city', None)
        filter_company = request.GET.get('company', None)
        query = Company.objects
        empty = Company.objects.none()

        if filter_street:
            filter_street = filter_street.strip()
            company = Company.objects.filter(contactDetails_address_street__icontains=filter_street)
            for comp in company:
                empty |= query.filter(id=comp.id)
            query = empty

        if filter_company:
            print('fff')
            filter_company = filter_company.strip()
            company = Company.objects.filter(contactDetails_company__icontains=filter_company)
            for comp in company:
                empty |= query.filter(id=comp.id)
            query = empty

        if filter_city:
            filter_city = filter_city.strip()
            company = Company.objects.filter(contactDetails_address_city__icontains=filter_city)
            for comp in company:
                empty |= query.filter(id=comp.id)
            query = empty

        if filter_country:
            filter_country = filter_country.strip()
            real_estate = RealEstate.objects.filter(realEstate_address_geoHierarchy_country_name__icontains=filter_country).all()
            #
            for comp in real_estate:
                print(comp.apartment.company)
                company = query.filter(id=comp.apartment.company.id)
                empty |= company
            query = empty

        print(query)

        if query.count() > 1:
            for q in query:
                q = RentFullViewModel(q).output()
                result.append(q)
        else:
            result.append({'404': 'object or filter not found'})

    return JsonResponse(result, status=200, safe=False)


