from django.conf import settings
import re
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse, HttpResponseForbidden
import json
from ...models.general import *


def load_data(request):
    if request.method == 'POST':
        #with open('rentdata/1.json', 'r', encoding='utf-8') as fh:
            #data = json.load(fh)
        try:
            data = json.loads(request.body.decode('utf-8'))

            set_data = data.get('data')

            companyWideCustomerId = set_data.get('companyWideCustomerId')
            contactDetails_id = set_data.get('contactDetails_id') if set_data.get('contactDetails_id') is not None else 0
            contactDetails_address_city = set_data.get('contactDetails_address_city')
            contactDetails_address_houseNumber = set_data.get('contactDetails_address_houseNumber') \
                if set_data.get('contactDetails_address_houseNumber') else 0
            contactDetails_address_postcode = set_data.get('contactDetails_address_postcode') \
                if set_data.get('contactDetails_address_postcode') is (not None) and (set_data.get('contactDetails_address_postcode').isdigit()) else 0
            contactDetails_address_street = set_data.get('contactDetails_address_street')
            contactDetails_cellPhoneNumber = set_data.get('contactDetails_cellPhoneNumber')
            contactDetails_cellPhoneNumberAreaCode = set_data.get('contactDetails_cellPhoneNumberAreaCode') \
                if set_data.get('contactDetails_cellPhoneNumberAreaCode') else 0
            contactDetails_cellPhoneNumberCountryCode = set_data.get('contactDetails_cellPhoneNumberCountryCode')
            contactDetails_cellPhoneNumberSubscriber = set_data.get('contactDetails_cellPhoneNumberSubscriber')
            contactDetails_company = set_data.get('contactDetails_company')
            contactDetails_countryCode = set_data.get('contactDetails_countryCode')
            contactDetails_email = set_data.get('contactDetails_email')
            contactDetails_faxNumber = set_data.get('contactDetails_faxNumber')
            contactDetails_faxNumberAreaCode = set_data.get('contactDetails_faxNumberAreaCode')
            contactDetails_faxNumberCountryCode = set_data.get('contactDetails_faxNumberCountryCode')
            contactDetails_faxNumberSubscriber = set_data.get('contactDetails_faxNumberSubscriber')
            contactDetails_firstname = set_data.get('contactDetails_firstname')
            contactDetails_homepageUrl = set_data.get('contactDetails_homepageUrl')
            contactDetails_lastname = set_data.get('contactDetails_lastname')
            contactDetails_phoneNumber = set_data.get('contactDetails_phoneNumber')
            contactDetails_phoneNumberAreaCode = set_data.get('contactDetails_phoneNumberAreaCode')
            contactDetails_phoneNumberCountryCode = set_data.get('contactDetails_phoneNumberCountryCode')
            contactDetails_phoneNumberSubscriber = set_data.get('contactDetails_phoneNumberSubscriber')
            contactDetails_salutation = set_data.get('contactDetails_salutation')
            contactFormConfiguration_addressField = set_data.get('contactFormConfiguration_addressField')
            contactFormConfiguration_applicationPackageCompletedField = set_data.get('contactFormConfiguration_applicationPackageCompletedField')
            contactFormConfiguration_emailAddressField = set_data.get('contactFormConfiguration_emailAddressField')
            contactFormConfiguration_employmentRelationshipField = set_data.get('contactFormConfiguration_employmentRelationshipField')
            contactFormConfiguration_firstnameField = set_data.get('contactFormConfiguration_firstnameField')
            contactFormConfiguration_freemiumSettings_duration = set_data.get('contactFormConfiguration_freemiumSettings_duration') \
                if set_data.get('contactFormConfiguration_freemiumSettings_duration') is not None else 0
            contactFormConfiguration_incomeField = set_data.get('contactFormConfiguration_incomeField')
            contactFormConfiguration_lastnameField = set_data.get('contactFormConfiguration_lastnameField')
            contactFormConfiguration_messageField = set_data.get('contactFormConfiguration_messageField')
            contactFormConfiguration_moveInDateField = set_data.get('contactFormConfiguration_moveInDateField')
            contactFormConfiguration_numberOfPersonsField = set_data.get('contactFormConfiguration_numberOfPersonsField')
            contactFormConfiguration_petsInHouseholdField = set_data.get('contactFormConfiguration_petsInHouseholdField')
            contactFormConfiguration_phoneNumberField = set_data.get('contactFormConfiguration_phoneNumberField')
            contactFormConfiguration_premiumProfileRequired = set_data.get('contactFormConfiguration_premiumProfileRequired')
            contactFormConfiguration_salutationField =  set_data.get('contactFormConfiguration_salutationField')

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
            contact_form_type = set_data.get('contactFormType')
            remove_creation = set_data.get('creation')
            remove_id = set_data.get('id')
            remove_modification = set_data.get('modification')
            remove_publishDate = set_data.get('publishDate')
            xlink_href = set_data.get('xlink_href')
            adLinkForJSONP_xlink_href = set_data.get('adLinkForJSONP_xlink_href')
            adLinkForXMLData_xlink_href = set_data.get('adLinkForXMLData_xlink_href')

            apartment = Apartment(company=company_related, contact_form_type=contact_form_type,
                                  remove_creation=remove_creation, remove_id=remove_id,
                                  remove_modification=remove_modification,
                                  remove_publishDate=remove_publishDate,
                                  xlink_href=xlink_href,
                                  adLinkForJSONP_xlink_href=adLinkForJSONP_xlink_href,
                                  adLinkForXMLData_xlink_href=adLinkForXMLData_xlink_href)
            self_id = apartment.save()

            imprintLink_xlink_href = set_data.get('imprintLink_xlink_href')
            imprint_ink = ImprintLink(company=company_related,
                                      imprintLink_xlink_href=imprintLink_xlink_href)
            imprint_ink.save()
# Real Estate
            realEstate_id = set_data.get('realEstate_id')
            realEstate_xsi_type = set_data.get('realEstate_xsi_type')
            realEstate_address_city = set_data.get('realEstate_address_city')
            realEstate_address_geoHierarchy_city_fullGeoCodeId = set_data.get('realEstate_address_geoHierarchy_city_fullGeoCodeId')
            realEstate_address_geoHierarchy_city_geoCodeId = set_data.get('realEstate_address_geoHierarchy_city_geoCodeId')
            realEstate_address_geoHierarchy_city_name = set_data.get('realEstate_address_geoHierarchy_city_name')
            realEstate_address_geoHierarchy_continent_fullGeoCodeId = '88'#set_data.get('realEstate_address_geoHierarchy_continent_fullGeoCodeId')
            realEstate_address_geoHierarchy_continent_geoCodeId = set_data.get('realEstate_address_geoHierarchy_continent_geoCodeId')
            realEstate_address_geoHierarchy_country_name = set_data.get('realEstate_address_geoHierarchy_country_name')
            realEstate_address_geoHierarchy_neighbourhood_geoCodeId = set_data.get('realEstate_address_geoHierarchy_neighbourhood_geoCodeId')
            realEstate_address_geoHierarchy_quarter_fullGeoCodeId = set_data.get('realEstate_address_geoHierarchy_quarter_fullGeoCodeId')
            realEstate_address_geoHierarchy_quarter_geoCodeId = set_data.get('realEstate_address_geoHierarchy_quarter_geoCodeId')
            realEstate_address_geoHierarchy_region_geoCodeId = set_data.get('realEstate_address_geoHierarchy_region_geoCodeId')
            realEstate_address_geoHierarchy_region_name = set_data.get('realEstate_address_geoHierarchy_region_name')
            realEstate_address_postcode = set_data.get('realEstate_address_postcode')
            realEstate_address_quarter = set_data.get('realEstate_address_quarter')
            realEstate_apartmentType = set_data.get('realEstate_apartmentType')
            realEstate_assistedLiving = set_data.get('realEstate_assistedLiving')

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

            realEstate_attachments = set_data.get('realEstate_attachments')

            real_estate = RealEstate.objects.filter(id=id_real_estate).first()

            realEstate_attachments_xlink_href = set_data.get('realEstate_attachments')[0]['@xlink.href']

            data_attach = set_data.get('realEstate_attachments')[0]['attachment']

            for element in data_attach:
                real_estate = RealEstate.objects.filter(id=id_real_estate).first()
                xsi_type = element.get('@xsi.type')
                xlink_href = element.get('@xlink.href')
                id_achments = element.get('@id')
                modification = element.get('@modification')
                creation = element.get('@creation')
                publishDate = element.get('@publishDate')
                title = element.get('title')
                floorplan = bool(element.get('floorplan'))
                titlepicture = bool(str(element.get('titlePicture')))


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

                try:
                    urls = list(element['urls'])
                    for urles in urls:
                        if urles.get('url'):
                            for u in urles['url']:
                                scale = u['@scale']
                                href = u['@href']
                                url_attachements = RealEstateTitlePictureUrls(real_estate_attachments=realestate,
                                                       scale=scale,
                                                       href=href)
                                url_attachements.save()
                except:
                    pass
# # Next data
            realEstate_balcony = bool(set_data.get('realEstate_balcony'))
            realEstate_baseRent = set_data.get('realEstate_baseRent')
            realEstate_buildingEnergyRatingType = set_data.get('realEstate_buildingEnergyRatingType')
            realEstate_builtInKitchen = bool(set_data.get('realEstate_builtInKitchen'))
            realEstate_calculatedTotalRent = set_data.get('realEstate_calculatedTotalRent')
            realEstate_calculatedTotalRentScope = set_data.get('realEstate_calculatedTotalRentScope')
            realEstate_cellar = set_data.get('realEstate_cellar')
            realEstate_certificateOfEligibilityNeeded = set_data.get('realEstate_certificateOfEligibilityNeeded')
            realEstate_condition = set_data.get('realEstate_condition')
            realEstate_constructionYear = set_data.get('realEstate_constructionYear')
            realEstate_courtage_hasCourtage = set_data.get('realEstate_courtage_hasCourtage')
            realEstate_creationDate = set_data.get('realEstate_creationDate')
            realEstate_deposit = set_data.get('realEstate_deposit')
            realEstate_descriptionNote = set_data.get('realEstate_descriptionNote')
            realEstate_energyCertificate_energyCertificateAvailability = set_data.get('realEstate_energyCertificate_energyCertificateAvailability')
            realEstate_energyCertificate_energyCertificateCreationDate = set_data.get('realEstate_energyCertificate_energyCertificateCreationDate')
            realEstate_energyConsumptionContainsWarmWater = set_data.get('realEstate_energyConsumptionContainsWarmWater')
            realEstate_energyPerformanceCertificate = bool(set_data.get('realEstate_energyPerformanceCertificate'))
            realEstate_externalId = re.sub("\D", "", set_data.get('realEstate_externalId'))
            realEstate_floor = set_data.get('realEstate_floor')
            realEstate_floorplan = bool(set_data.get('realEstate_floorplan'))
            realEstate_freeFrom = set_data.get('realEstate_freeFrom')
            realEstate_furnishingNote = set_data.get('realEstate_furnishingNote')
            realEstate_garden = bool(set_data.get('realEstate_garden'))
            realEstate_guestToilet = set_data.get('realEstate_guestToilet')
            realEstate_handicappedAccessible = set_data.get('realEstate_handicappedAccessible')
            realEstate_heatingCosts = set_data.get('realEstate_heatingCosts')
            realEstate_heatingCostsInServiceCharge = set_data.get('realEstate_heatingCostsInServiceCharge')
            realEstate_heatingType = set_data.get('realEstate_heatingType')
            realEstate_heatingTypeEnev2014 = set_data.get('realEstate_heatingTypeEnev2014')
            realEstate_interiorQuality = set_data.get('realEstate_interiorQuality')
            realEstate_lastModificationDate = set_data.get('realEstate_lastModificationDate')
            realEstate_lastRefurbishment = set_data.get('realEstate_lastRefurbishment')
            realEstate_lift = bool(set_data.get('realEstate_lift'))
            realEstate_livingSpace = set_data.get('realEstate_livingSpace')
            realEstate_locationNote = set_data.get('realEstate_locationNote')
            realEstate_numberOfFloors = set_data.get('realEstate_numberOfFloors')
            realEstate_numberOfRooms = set_data.get('realEstate_numberOfRooms')
            realEstate_otherNote = set_data.get('realEstate_otherNote')
            realEstate_petsAllowed = set_data.get('realEstate_petsAllowed')
            realEstate_referencePriceApiCall = set_data.get('realEstate_referencePriceApiCall')
            realEstate_referencePriceServiceCall = set_data.get('realEstate_referencePriceServiceCall')
            realEstate_serviceCharge = set_data.get('realEstate_serviceCharge')
            realEstate_state = set_data.get('realEstate_state')
            realEstate_thermalCharacteristic = set_data.get('realEstate_thermalCharacteristic')
            realEstate_title = set_data.get('realEstate_title')
            realEstate_titlePicture_creation = set_data.get('realEstate_titlePicture_creation')
            realEstate_titlePicture_id = set_data.get('realEstate_titlePicture_id')
            realEstate_titlePicture_modification = set_data.get('realEstate_titlePicture_modification')
            realEstate_titlePicture_publishDate = set_data.get('realEstate_titlePicture_publishDate')
            realEstate_titlePicture_floorplan = bool(set_data.get('realEstate_titlePicture_floorplan'))
            realEstate_titlePicture_title = set_data.get('realEstate_titlePicture_title')
            realEstate_titlePicture_titlePicture = bool(set_data.get('realEstate_titlePicture_titlePicture'))
            realEstate_totalRent = set_data.get('realEstate_totalRent')
            realEstate_useAsFlatshareRoom = set_data.get('realEstate_useAsFlatshareRoom')
            realtorValuationJSONLink_xlink_href = set_data.get('realtorValuationJSONLink_xlink_href')
            realtorValuationV2JSONLink_xlink_href = set_data.get('realtorValuationV2JSONLink_xlink_href')
            realtorValuationV2JSONPLink_xlink_href =  set_data.get('realtorValuationV2JSONPLink_xlink_href')

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
            picture_urls = set_data.get('realEstate_titlePicture_urls')
            if picture_urls:
                for pic in picture_urls:
                    for u in pic['url']:
                        scale = u['@scale']
                        href = u['@href']
                        url_attachements = Url(realestate_id=id_real_estate,
                                               scale=scale,
                                               href=href)
                        url_attachements.save()

            return JsonResponse({'status': 'accepted'}, status=200)
        except Exception as e:
            return JsonResponse({'Bad request!': str(e)}, status=400)
    else:
        return JsonResponse({'POST': 'load_data'}, status=400)


def index(request):
    if request.method == 'GET':

        return JsonResponse({'GET': 'Not existed'}, status=400)
    else:
        return JsonResponse({'POST': '99'}, status=400)

