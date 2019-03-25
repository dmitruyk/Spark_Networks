from django.conf import settings
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse, HttpResponseForbidden
import json
from ...models.general import *


def load_data(request):
    if request.method == 'POST':
        with open('rentdata/1.json', 'r', encoding='utf-8') as fh:
            #data = json.load(fh)

            data = json.loads(request.body.decode('utf-8'))

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

# Company
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

# First section
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

            imprintLink_xlink_href = data['data']['imprintLink_xlink_href']
            imprint_ink = ImprintLink(company=company_related,
                                      imprintLink_xlink_href=imprintLink_xlink_href)
            imprint_ink.save()
# Real Estate
            realEstate_id = data['data']['realEstate_id']
            realEstate_xsi_type = data['data']['realEstate_xsi_type']
            realEstate_address_city = data['data']['realEstate_address_city']
            realEstate_address_geoHierarchy_city_fullGeoCodeId = data['data']['realEstate_address_geoHierarchy_city_fullGeoCodeId']
            realEstate_address_geoHierarchy_city_geoCodeId = data['data']['realEstate_address_geoHierarchy_city_geoCodeId']
            realEstate_address_geoHierarchy_city_name = data['data']['realEstate_address_geoHierarchy_city_name']
            realEstate_address_geoHierarchy_continent_fullGeoCodeId = '88'#data['data']['realEstate_address_geoHierarchy_continent_fullGeoCodeId']
            realEstate_address_geoHierarchy_continent_geoCodeId = data['data']['realEstate_address_geoHierarchy_continent_geoCodeId']
            realEstate_address_geoHierarchy_country_name = data['data']['realEstate_address_geoHierarchy_country_name']
            realEstate_address_geoHierarchy_neighbourhood_geoCodeId = data['data']['realEstate_address_geoHierarchy_neighbourhood_geoCodeId']
            realEstate_address_geoHierarchy_quarter_fullGeoCodeId = data['data']['realEstate_address_geoHierarchy_quarter_fullGeoCodeId']
            realEstate_address_geoHierarchy_quarter_geoCodeId = data['data']['realEstate_address_geoHierarchy_quarter_geoCodeId']
            realEstate_address_geoHierarchy_region_geoCodeId = data['data']['realEstate_address_geoHierarchy_region_geoCodeId']
            realEstate_address_geoHierarchy_region_name = data['data']['realEstate_address_geoHierarchy_region_name']
            realEstate_address_postcode = data['data']['realEstate_address_postcode']
            realEstate_address_quarter = data['data']['realEstate_address_quarter']
            realEstate_apartmentType = data['data']['realEstate_apartmentType']
            realEstate_assistedLiving = data['data']['realEstate_assistedLiving']

            apartment = Apartment.objects.filter(id=self_id).first()
            real_estate = RealEstate(apartment=apartment,
                                     realEstate_id=realEstate_id,
                                     realEstate_xsi_type=realEstate_xsi_type,
                                     realEstate_address_city=realEstate_address_city,
                                     realEstate_address_geoHierarchy_city_fullGeoCodeId=realEstate_address_geoHierarchy_city_fullGeoCodeId,
                                     realEstate_address_geoHierarchy_city_geoCodeId=realEstate_address_geoHierarchy_city_geoCodeId,
                                     realEstate_address_geoHierarchy_city_name=realEstate_address_geoHierarchy_city_name,
                                     realEstate_address_geoHierarchy_continent_fullGeoCodeId=realEstate_address_geoHierarchy_continent_fullGeoCodeId,
                                     realEstate_address_geoHierarchy_continent_geoCodeId=realEstate_address_geoHierarchy_continent_geoCodeId,
                                     realEstate_address_geoHierarchy_country_name=realEstate_address_geoHierarchy_country_name,
                                     realEstate_address_geoHierarchy_neighbourhood_geoCodeId=realEstate_address_geoHierarchy_neighbourhood_geoCodeId,
                                     realEstate_address_geoHierarchy_quarter_fullGeoCodeId=realEstate_address_geoHierarchy_quarter_fullGeoCodeId,
                                     realEstate_address_geoHierarchy_quarter_geoCodeId=realEstate_address_geoHierarchy_quarter_geoCodeId,
                                     realEstate_address_geoHierarchy_region_geoCodeId=realEstate_address_geoHierarchy_region_geoCodeId,
                                     realEstate_address_geoHierarchy_region_name=realEstate_address_geoHierarchy_region_name,
                                     realEstate_address_postcode=realEstate_address_postcode,
                                     realEstate_address_quarter=realEstate_address_quarter,
                                     realEstate_apartmentType=realEstate_apartmentType,
                                     realEstate_assistedLiving=realEstate_assistedLiving,
                                    )
            id_real_estate = real_estate.save()

            realEstate_attachments = data['data']['realEstate_attachments']

            real_estate = RealEstate.objects.filter(id=id_real_estate).first()

            realEstate_attachments_xlink_href = data['data']['realEstate_attachments'][0]['@xlink.href']

            data_attach = data['data']['realEstate_attachments'][0]['attachment']
            i = 0
            k = 0
            for element in data_attach:
                real_estate = RealEstate.objects.filter(id=id_real_estate).first()
                xsi_type = element['@xsi.type']
                xlink_href = element['@xlink.href']
                id_achments = element['@id']
                modification = element['@modification']
                creation = element['@creation']
                publishDate = element['@publishDate']
                title = element['title']
                floorplan = bool(element['floorplan'])
                titlepicture = bool(str(element['titlePicture']))
                urls = list(element['urls'])

                real_attachments = RealEstateAttachments(
                    realEstate_attachments_xlink_href=realEstate_attachments_xlink_href,
                    real_estate=real_estate,
                    xsi_type=xsi_type,
                    xlink_href=xlink_href,
                    id_achments=id_achments,
                    modification=modification,
                    creation=creation,
                    publishDate=publishDate,
                    title=title,
                    floorplan=floorplan,
                    titlepicture=titlepicture,
                )
                id_real_attachments = real_attachments.save()

                realestate = RealEstateAttachments.objects.filter(id=id_real_attachments).first()

                for urles in urls:
                    i += 1
                    for u in urles['url']:
                        k +=1
                        scale = u['@scale']
                        href = u['@href']
                        url_attachements = RealEstateTitlePictureUrls(real_estate_attachments=realestate,
                                               scale=scale,
                                               href=href)
                        url_attachements.save()
# # Next data
            realEstate_balcony = bool(data['data']['realEstate_balcony'])
            realEstate_baseRent = data['data']['realEstate_baseRent']
            realEstate_buildingEnergyRatingType = data['data']['realEstate_buildingEnergyRatingType']
            realEstate_builtInKitchen = bool(data['data']['realEstate_builtInKitchen'])
            realEstate_calculatedTotalRent = data['data']['realEstate_calculatedTotalRent']
            realEstate_calculatedTotalRentScope = data['data']['realEstate_calculatedTotalRentScope']
            realEstate_cellar = data['data']['realEstate_cellar']
            realEstate_certificateOfEligibilityNeeded = data['data']['realEstate_certificateOfEligibilityNeeded']
            realEstate_condition = data['data']['realEstate_condition']
            realEstate_constructionYear = data['data']['realEstate_constructionYear']
            realEstate_courtage_hasCourtage = data['data']['realEstate_courtage_hasCourtage']
            realEstate_creationDate = data['data']['realEstate_creationDate']
            realEstate_deposit = data['data']['realEstate_deposit']
            realEstate_descriptionNote = data['data']['realEstate_descriptionNote']
            realEstate_energyCertificate_energyCertificateAvailability = data['data']['realEstate_energyCertificate_energyCertificateAvailability']
            realEstate_energyCertificate_energyCertificateCreationDate = data['data']['realEstate_energyCertificate_energyCertificateCreationDate']
            realEstate_energyConsumptionContainsWarmWater = data['data']['realEstate_energyConsumptionContainsWarmWater']
            realEstate_energyPerformanceCertificate = bool(data['data']['realEstate_energyPerformanceCertificate'])
            realEstate_externalId = data['data']['realEstate_externalId']
            realEstate_floor = data['data']['realEstate_floor']
            realEstate_floorplan = bool(data['data']['realEstate_floorplan'])
            realEstate_freeFrom = data['data']['realEstate_freeFrom']
            realEstate_furnishingNote = data['data']['realEstate_furnishingNote']
            realEstate_garden = bool(data['data']['realEstate_garden'])
            realEstate_guestToilet = data['data']['realEstate_guestToilet']
            realEstate_handicappedAccessible = data['data']['realEstate_handicappedAccessible']
            realEstate_heatingCosts = data['data']['realEstate_heatingCosts']
            realEstate_heatingCostsInServiceCharge = data['data']['realEstate_heatingCostsInServiceCharge']
            realEstate_heatingType = data['data']['realEstate_heatingType']
            realEstate_heatingTypeEnev2014 = data['data']['realEstate_heatingTypeEnev2014']
            realEstate_interiorQuality = data['data']['realEstate_interiorQuality']
            realEstate_lastModificationDate = data['data']['realEstate_lastModificationDate']
            realEstate_lastRefurbishment = data['data']['realEstate_lastRefurbishment']
            realEstate_lift = bool(data['data']['realEstate_lift'])
            realEstate_livingSpace = data['data']['realEstate_livingSpace']
            realEstate_locationNote = data['data']['realEstate_locationNote']
            realEstate_numberOfFloors = data['data']['realEstate_numberOfFloors']
            realEstate_numberOfRooms = data['data']['realEstate_numberOfRooms']
            realEstate_otherNote = data['data']['realEstate_otherNote']
            realEstate_petsAllowed = data['data']['realEstate_petsAllowed']
            realEstate_referencePriceApiCall = data['data']['realEstate_referencePriceApiCall']
            realEstate_referencePriceServiceCall = data['data']['realEstate_referencePriceServiceCall']
            realEstate_serviceCharge = data['data']['realEstate_serviceCharge']
            realEstate_state = data['data']['realEstate_state']
            realEstate_thermalCharacteristic = data['data']['realEstate_thermalCharacteristic']
            realEstate_title = data['data']['realEstate_title']
            realEstate_titlePicture_creation = data['data']['realEstate_titlePicture_creation']
            realEstate_titlePicture_id = data['data']['realEstate_titlePicture_id']
            realEstate_titlePicture_modification = data['data']['realEstate_titlePicture_modification']
            realEstate_titlePicture_publishDate = data['data']['realEstate_titlePicture_publishDate']
            realEstate_titlePicture_floorplan = bool(data['data']['realEstate_titlePicture_floorplan'])
            realEstate_titlePicture_title = data['data']['realEstate_titlePicture_title']
            realEstate_titlePicture_titlePicture = bool(data['data']['realEstate_titlePicture_titlePicture'])
            realEstate_totalRent = data['data']['realEstate_totalRent']
            realEstate_useAsFlatshareRoom = data['data']['realEstate_useAsFlatshareRoom']
            realtorValuationJSONLink_xlink_href = data['data']['realtorValuationJSONLink_xlink_href']
            realtorValuationV2JSONLink_xlink_href = data['data']['realtorValuationV2JSONLink_xlink_href']
            realtorValuationV2JSONPLink_xlink_href =  data['data']['realtorValuationV2JSONPLink_xlink_href']

            real_estate_next = RealEstateNext(real_estate=real_estate,
                                              realEstate_balcony=realEstate_balcony,
                                              realEstate_baseRent=realEstate_baseRent,
                                              realEstate_buildingEnergyRatingType=realEstate_buildingEnergyRatingType,
                                              realEstate_builtInKitchen=realEstate_builtInKitchen,
                                              realEstate_calculatedTotalRent=realEstate_calculatedTotalRent,
                                              realEstate_calculatedTotalRentScope=realEstate_calculatedTotalRentScope,
                                              realEstate_cellar=realEstate_cellar,
                                              realEstate_certificateOfEligibilityNeeded=realEstate_certificateOfEligibilityNeeded,
                                              realEstate_condition=realEstate_condition,
                                              realEstate_constructionYear=realEstate_constructionYear,
                                              realEstate_courtage_hasCourtage=realEstate_courtage_hasCourtage,
                                              realEstate_creationDate=realEstate_creationDate,
                                              realEstate_deposit=realEstate_deposit,
                                              realEstate_descriptionNote=realEstate_descriptionNote,
                                              realEstate_energyCertificate_energyCertificateAvailability=realEstate_energyCertificate_energyCertificateAvailability,
                                              realEstate_energyCertificate_energyCertificateCreationDate=realEstate_energyCertificate_energyCertificateCreationDate,
                                              realEstate_energyConsumptionContainsWarmWater=realEstate_energyConsumptionContainsWarmWater,
                                              realEstate_energyPerformanceCertificate=realEstate_energyPerformanceCertificate,
                                              realEstate_externalId=realEstate_externalId,
                                              realEstate_floor=realEstate_floor,
                                              realEstate_floorplan=realEstate_floorplan,
                                              realEstate_freeFrom=realEstate_freeFrom,
                                              realEstate_furnishingNote=realEstate_furnishingNote,
                                              realEstate_garden=realEstate_garden,
                                              realEstate_guestToilet=realEstate_guestToilet,
                                              realEstate_handicappedAccessible=realEstate_handicappedAccessible,
                                              realEstate_heatingCosts=realEstate_heatingCosts,
                                              realEstate_heatingCostsInServiceCharge=realEstate_heatingCostsInServiceCharge,
                                              realEstate_heatingType=realEstate_heatingType,
                                              realEstate_heatingTypeEnev2014=realEstate_heatingTypeEnev2014,
                                              realEstate_interiorQuality=realEstate_interiorQuality,
                                              realEstate_lastModificationDate=realEstate_lastModificationDate,
                                              realEstate_lastRefurbishment=realEstate_lastRefurbishment,
                                              realEstate_lift=realEstate_lift,
                                              realEstate_livingSpace=realEstate_livingSpace,
                                              realEstate_locationNote=realEstate_locationNote,
                                              realEstate_numberOfFloors=realEstate_numberOfFloors,
                                              realEstate_numberOfRooms=realEstate_numberOfRooms,
                                              realEstate_otherNote=realEstate_otherNote,
                                              realEstate_petsAllowed=realEstate_petsAllowed,
                                              realEstate_referencePriceApiCall=realEstate_referencePriceApiCall,
                                              realEstate_referencePriceServiceCall=realEstate_referencePriceServiceCall,
                                              realEstate_serviceCharge=realEstate_serviceCharge,
                                              realEstate_state=realEstate_state,
                                              realEstate_thermalCharacteristic=realEstate_thermalCharacteristic,
                                              realEstate_title=realEstate_title,
                                              realEstate_titlePicture_creation=realEstate_titlePicture_creation,
                                              realEstate_titlePicture_id=realEstate_titlePicture_id,
                                              realEstate_titlePicture_modification=realEstate_titlePicture_modification,
                                              realEstate_titlePicture_publishDate=realEstate_titlePicture_publishDate,
                                              realEstate_titlePicture_floorplan=realEstate_titlePicture_floorplan,
                                              realEstate_titlePicture_title=realEstate_titlePicture_title,
                                              realEstate_titlePicture_titlePicture=realEstate_titlePicture_titlePicture,
                                              realEstate_totalRent=realEstate_totalRent,
                                              realEstate_useAsFlatshareRoom=realEstate_useAsFlatshareRoom,
                                              realtorValuationJSONLink_xlink_href=realtorValuationJSONLink_xlink_href,
                                              realtorValuationV2JSONLink_xlink_href=realtorValuationV2JSONLink_xlink_href,
                                              realtorValuationV2JSONPLink_xlink_href=realtorValuationV2JSONPLink_xlink_href
                                              )
            real_estate_next.save()

# Pic URLS
            picture_urls = data['data']['realEstate_titlePicture_urls']
            for pic in picture_urls:
                for u in pic['url']:
                    scale= u ['@scale']
                    href= u ['@href']
                    url_attachements = Url(realestate_id=id_real_estate,
                                                                  scale=scale,
                                                                  href=href)
                    url_attachements.save()
#
            return JsonResponse(data, status=200)
    else:
        return JsonResponse({'POST': 'load_data'}, status=400)


def index(request):
    if request.method == 'GET':
        return JsonResponse({'GET': 'Not existed'}, status=400)
    else:
        return JsonResponse({'POST': 'Not existed'}, status=400)

