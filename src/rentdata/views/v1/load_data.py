from django.conf import settings
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse, HttpResponseForbidden
import json
from ...models.general import *

def load_data(request):
    if request.method == 'GET':
        with open('rentdata/1.json', 'r', encoding='utf-8') as fh:  # открываем файл на чтение
            data = json.load(fh)

            companyWideCustomerId = data['data']['companyWideCustomerId']
            contactDetails_id = data['data']['contactDetails_id']
            contactDetails_address_city = data['data']['contactDetails_address_city']
            contactDetails_address_houseNumber = data['data']['contactDetails_address_houseNumber']
            contactDetails_address_postcode = data['data']['contactDetails_address_postcode']
            contactDetails_address_street = data['data']['contactDetails_address_street']
            contactDetails_cellPhoneNumber = data['data']['contactDetails_cellPhoneNumber']
            contactDetails_cellPhoneNumberAreaCode = data['data']['contactDetails_cellPhoneNumberAreaCode']
            contactDetails_cellPhoneNumberCountryCode = data['data']['contactDetails_cellPhoneNumberCountryCode']
            contactDetails_cellPhoneNumberSubscriber = data['data']['contactDetails_cellPhoneNumberSubscriber']
            contactDetails_company = data['data']['contactDetails_company']
            contactDetails_countryCode = data['data']['contactDetails_countryCode']
            contactDetails_email = data['data']['contactDetails_email']
            contactDetails_faxNumber = data['data']['contactDetails_faxNumber']
            contactDetails_faxNumberAreaCode = data['data']['contactDetails_faxNumberAreaCode']
            contactDetails_faxNumberCountryCode = data['data']['contactDetails_faxNumberCountryCode']
            contactDetails_faxNumberSubscriber = data['data']['contactDetails_faxNumberSubscriber']
            contactDetails_firstname = data['data']['contactDetails_firstname']
            contactDetails_homepageUrl = data['data']['contactDetails_homepageUrl']
            contactDetails_lastname = data['data']['contactDetails_lastname']
            contactDetails_phoneNumber = data['data']['contactDetails_phoneNumber']
            contactDetails_phoneNumberAreaCode = data['data']['contactDetails_phoneNumberAreaCode']
            contactDetails_phoneNumberCountryCode = data['data']['contactDetails_phoneNumberCountryCode']
            contactDetails_phoneNumberSubscriber = data['data']['contactDetails_phoneNumberSubscriber']
            contactDetails_salutation = data['data']['contactDetails_salutation']
            contactFormConfiguration_addressField = data['data']['contactFormConfiguration_addressField']
            contactFormConfiguration_applicationPackageCompletedField = data['data']['contactFormConfiguration_applicationPackageCompletedField']
            contactFormConfiguration_emailAddressField = data['data']['contactFormConfiguration_emailAddressField']
            contactFormConfiguration_employmentRelationshipField = data['data']['contactFormConfiguration_employmentRelationshipField']
            contactFormConfiguration_firstnameField = data['data']['contactFormConfiguration_firstnameField']
            contactFormConfiguration_freemiumSettings_duration = data['data']['contactFormConfiguration_freemiumSettings_duration']
            contactFormConfiguration_incomeField = data['data']['contactFormConfiguration_incomeField']
            contactFormConfiguration_lastnameField = data['data']['contactFormConfiguration_lastnameField']
            contactFormConfiguration_messageField = data['data']['contactFormConfiguration_messageField']
            contactFormConfiguration_moveInDateField = data['data']['contactFormConfiguration_moveInDateField']
            contactFormConfiguration_numberOfPersonsField = data['data']['contactFormConfiguration_numberOfPersonsField']
            contactFormConfiguration_petsInHouseholdField = data['data']['contactFormConfiguration_petsInHouseholdField']
            contactFormConfiguration_phoneNumberField = data['data']['contactFormConfiguration_phoneNumberField']
            contactFormConfiguration_premiumProfileRequired = data['data']['contactFormConfiguration_premiumProfileRequired']
            contactFormConfiguration_salutationField =  data['data']['contactFormConfiguration_salutationField']








#Company
            company = Company(companyWideCustomerId=companyWideCustomerId,
                             contactDetails_id=contactDetails_id,
                             contactDetails_address_city=contactDetails_address_city,
                             contactDetails_address_houseNumber=contactDetails_address_houseNumber,
                             contactDetails_address_postcode=contactDetails_address_postcode,
                             contactDetails_address_street=contactDetails_address_street,
                             contactDetails_cellPhoneNumber=contactDetails_cellPhoneNumber,
                             contactDetails_cellPhoneNumberAreaCode=contactDetails_cellPhoneNumberAreaCode,
                             contactDetails_cellPhoneNumberCountryCode=contactDetails_cellPhoneNumberCountryCode,
                             contactDetails_cellPhoneNumberSubscriber=contactDetails_cellPhoneNumberSubscriber,
                             contactDetails_company=contactDetails_company,
                             contactDetails_countryCode=contactDetails_countryCode,
                             contactDetails_email=contactDetails_email,
                             contactDetails_faxNumber=contactDetails_faxNumber,
                             contactDetails_faxNumberAreaCode=contactDetails_faxNumberAreaCode,
                             contactDetails_faxNumberCountryCode=contactDetails_faxNumberCountryCode,
                             contactDetails_faxNumberSubscriber=contactDetails_faxNumberSubscriber,
                             contactDetails_firstname=contactDetails_firstname,
                             contactDetails_homepageUrl=contactDetails_homepageUrl,
                             contactDetails_lastname=contactDetails_lastname,
                             contactDetails_phoneNumber=contactDetails_phoneNumber,
                             contactDetails_phoneNumberAreaCode=contactDetails_phoneNumberAreaCode,
                             contactDetails_phoneNumberCountryCode=contactDetails_phoneNumberCountryCode,
                             contactDetails_phoneNumberSubscriber=contactDetails_phoneNumberSubscriber,
                             contactDetails_salutation=contactDetails_salutation,
                             contactFormConfiguration_addressField=contactFormConfiguration_addressField,
                             contactFormConfiguration_applicationPackageCompletedField=contactFormConfiguration_applicationPackageCompletedField,
                             contactFormConfiguration_emailAddressField=contactFormConfiguration_emailAddressField,
                             contactFormConfiguration_employmentRelationshipField=contactFormConfiguration_employmentRelationshipField,
                             contactFormConfiguration_firstnameField=contactFormConfiguration_firstnameField,
                             contactFormConfiguration_freemiumSettings_duration=contactFormConfiguration_freemiumSettings_duration,
                             contactFormConfiguration_incomeField=contactFormConfiguration_incomeField,
                             contactFormConfiguration_lastnameField=contactFormConfiguration_lastnameField,
                             contactFormConfiguration_messageField=contactFormConfiguration_messageField,
                             contactFormConfiguration_moveInDateField=contactFormConfiguration_moveInDateField,
                             contactFormConfiguration_numberOfPersonsField=contactFormConfiguration_numberOfPersonsField,
                             contactFormConfiguration_petsInHouseholdField=contactFormConfiguration_petsInHouseholdField,
                             contactFormConfiguration_phoneNumberField=contactFormConfiguration_phoneNumberField,
                             contactFormConfiguration_premiumProfileRequired=contactFormConfiguration_premiumProfileRequired,
                             contactFormConfiguration_salutationField=contactFormConfiguration_salutationField
                             )

            company_id = company.save()
            company_related = Company.objects.filter(id=company_id).first()

#First section
            contact_form_type = data['data']['contactFormType']
            remove_creation = data['data']['creation']
            remove_id = data['data']['id']
            remove_modification = data['data']['modification']
            remove_publishDate = data['data']['publishDate']
            xlink_href = data['data']['xlink_href']
            adLinkForJSONP_xlink_href = data['data']['adLinkForJSONP_xlink_href']
            adLinkForXMLData_xlink_href = data['data']['adLinkForXMLData_xlink_href']

            apartment = Apartment(company=company_related, contact_form_type=contact_form_type,
                                  remove_creation=remove_creation, remove_id=remove_id,
                                  remove_modification=remove_modification,
                                  remove_publishDate=remove_publishDate,
                                  xlink_href=xlink_href,
                                  adLinkForJSONP_xlink_href=adLinkForJSONP_xlink_href,
                                  adLinkForXMLData_xlink_href=adLinkForXMLData_xlink_href)
            self_id = apartment.save()
            print(self_id)
            return JsonResponse(data, status=200)
    else:
        return JsonResponse({'POST': 'load_data'}, status=400)


def index(request):
    if request.method == 'GET':
        return JsonResponse({'GET': 'Not existed'}, status=400)
    else:
        return JsonResponse({'POST': 'Not existed'}, status=400)

