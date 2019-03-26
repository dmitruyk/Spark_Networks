from ..core.core import CoreModel
from django.db import models

from django.utils.translation import ugettext_lazy as _


class Status(CoreModel):
    class Meta:
        db_table = u'status'

    status = models.BooleanField(default=False),


class Company(CoreModel):
    class Meta:
        db_table = u'company'

    companyWideCustomerId = models.CharField(_('companyWideCustomerId'),
                                             max_length=80,
                                             default=None,
                                             null=True
                                             )

    contactDetails_id = models.PositiveIntegerField(_('contactDetails_id'),
                                                    null=True,
                                                    blank=True,
                                                    default=0,
                                                    unique=False
                                                    )

    contactDetails_address_city = models.CharField(_('contactDetails_address_city'),
                                                   max_length=80,
                                                   default=None,
                                                   null=True
                                                   )

    contactDetails_address_houseNumber = models.CharField(_('contactDetails_address_houseNumber'),
                                                          max_length=80,
                                                          default=None,
                                                          null=True
                                                          )
    contactDetails_address_postcode = models.CharField(_('contactDetails_address_postcode'),
                                                       max_length=80,
                                                       default=None,
                                                       null=True
                                                       )
    contactDetails_address_street = models.CharField(_('contactDetails_address_street'),
                                                     max_length=180,
                                                     default=None,
                                                     null=True
                                                     )

    contactDetails_cellPhoneNumber = models.CharField(_('contactDetails_cellPhoneNumber'),
                                                      max_length=180,
                                                      default=None,
                                                      null=True
                                                      )

    contactDetails_cellPhoneNumberAreaCode = models.CharField(_('contactDetails_cellPhoneNumberAreaCode'),
                                                              max_length=180,
                                                              default=None,
                                                              null=True
                                                              )
    contactDetails_cellPhoneNumberCountryCode = models.CharField(_('contactDetails_cellPhoneNumberCountryCode'),
                                                                 max_length=100,
                                                                 default=None,
                                                                 null=True
                                                                 )

    contactDetails_cellPhoneNumberSubscriber = models.CharField(_('contactDetails_cellPhoneNumberSubscriber'),
                                                                max_length=20,
                                                                default=None,
                                                                null=True
                                                                )

    contactDetails_company = models.CharField(_('contactDetails_company'),
                                              max_length=180,
                                              default=None,
                                              null=True
                                              )

    contactDetails_countryCode = models.CharField(_('contactDetails_countryCode'),
                                                  max_length=100,
                                                  default=None,
                                                  null=True
                                                  )

    contactDetails_email = models.CharField(_('contactDetails_email'),
                                            max_length=50,
                                            default=None,
                                            null=True
                                            )

    contactDetails_faxNumber = models.CharField(_('contactDetails_faxNumber'),
                                                max_length=50,
                                                default=None,
                                                null=True
                                                )

    contactDetails_faxNumberAreaCode = models.CharField(_('contactDetails_faxNumberAreaCode'),
                                                        max_length=10,
                                                        default=None,
                                                        null=True
                                                        )

    contactDetails_faxNumberCountryCode = models.CharField(_('contactDetails_faxNumberCountryCode'),
                                                           max_length=100,
                                                           default=None,
                                                           null=True
                                                           )

    contactDetails_faxNumberSubscriber = models.CharField(_('contactDetails_faxNumberSubscriber'),
                                                          max_length=100,
                                                          default=None,
                                                          null=True
                                                          )

    contactDetails_firstname = models.CharField(_('contactDetails_firstname'),
                                                max_length=30,
                                                default=None,
                                                null=True
                                                )

    contactDetails_homepageUrl = models.CharField(_('contactDetails_homepageUrl'),
                                                  max_length=150,
                                                  default=None,
                                                  null=True
                                                  )

    contactDetails_lastname = models.CharField(_('contactDetails_lastname'),
                                               max_length=30,
                                               default=None,
                                               null=True
                                               )

    contactDetails_phoneNumber = models.CharField(_('contactDetails_phoneNumber'),
                                                  max_length=50,
                                                  default=None,
                                                  null=True
                                                  )

    contactDetails_phoneNumberAreaCode = models.CharField(_('contactDetails_phoneNumberAreaCode'),
                                                          max_length=50,
                                                          default=None,
                                                          null=True
                                                          )

    contactDetails_phoneNumberCountryCode = models.CharField(_('contactDetails_phoneNumberCountryCode'),
                                                             max_length=10,
                                                             default=None,
                                                             null=True
                                                             )

    contactDetails_phoneNumberSubscriber = models.CharField(_('contactDetails_phoneNumberSubscriber'),
                                                            max_length=20,
                                                            default=None,
                                                            null=True
                                                            )

    contactDetails_salutation = models.CharField(_('contactDetails_salutation'),
                                                 max_length=100,
                                                 default=None,
                                                 null=True
                                                 )

    contactFormConfiguration_addressField = models.CharField(_('contactFormConfiguration_addressField'),
                                                             max_length=100,
                                                             default=None,
                                                             null=True
                                                             )

    contactFormConfiguration_applicationPackageCompletedField = models.CharField(_('contactFormConfiguration_applicationPackageCompletedField'),
                                                                                 max_length=10,
                                                                                 default=None,
                                                                                 null=True
                                                                                 )

    contactFormConfiguration_emailAddressField = models.CharField(_('contactFormConfiguration_emailAddressField'),
                                                                  max_length=100,
                                                                  default=None,
                                                                  null=True
                                                                  )

    contactFormConfiguration_employmentRelationshipField = models.CharField(_('contactFormConfiguration_employmentRelationshipField'),
                                                                            max_length=10,
                                                                            default=None,
                                                                            null=True
                                                                            )

    contactFormConfiguration_firstnameField = models.CharField(_('contactFormConfiguration_firstnameField'),
                                                               max_length=100,
                                                               default=None,
                                                               null=True
                                                               )

    contactFormConfiguration_freemiumSettings_duration = models.CharField(_('contactFormConfiguration_freemiumSettings_duration'),
                                                                          max_length=100,
                                                                          default=None,
                                                                          null=True
                                                                          )

    contactFormConfiguration_incomeField = models.CharField(_('contactFormConfiguration_incomeField'),
                                                            max_length=100,
                                                            default=None,
                                                            null=True
                                                            )

    contactFormConfiguration_lastnameField = models.CharField(_('contactFormConfiguration_lastnameField'),
                                                              max_length=100,
                                                              default=None,
                                                              null=True
                                                              )

    contactFormConfiguration_messageField = models.CharField(_('contactFormConfiguration_messageField'),
                                                             max_length=40,
                                                             default=None,
                                                             null=True
                                                             )

    contactFormConfiguration_moveInDateField = models.CharField(_('contactFormConfiguration_moveInDateField'),
                                                                max_length=40,
                                                                default=None,
                                                                null=True
                                                                )

    contactFormConfiguration_numberOfPersonsField = models.CharField(_('contactFormConfiguration_numberOfPersonsField'),
                                                                     max_length=40,
                                                                     default=None,
                                                                     null=True
                                                                     )

    contactFormConfiguration_petsInHouseholdField = models.CharField(_('contactFormConfiguration_petsInHouseholdField'),
                                                                     max_length=40,
                                                                     default=None,
                                                                     null=True
                                                                     )

    contactFormConfiguration_phoneNumberField = models.CharField(_('contactFormConfiguration_phoneNumberField'),
                                                                 max_length=40,
                                                                 default=None,
                                                                 null=True
                                                                 )

    contactFormConfiguration_premiumProfileRequired = models.CharField(_('contactFormConfiguration_premiumProfileRequired'),
                                                                       max_length=40,
                                                                       default=None,
                                                                       null=True
                                                                       )

    contactFormConfiguration_salutationField = models.CharField(_('contactFormConfiguration_salutationField'),
                                                                max_length=40,
                                                                default=None,
                                                                null=True
                                                                )

    def save(self, *args, **kwargs):
        super(Company, self).save(*args, **kwargs)
        return self.id


class ImprintLink(CoreModel):
    class Meta:
        db_table = u'imprintLink'

    company = models.ForeignKey(
        Company,
        related_name='imprintLink_xlink_href',
        on_delete=models.SET_NULL,
        null=True, blank=True
    )

    imprintLink_xlink_href = models.CharField(_('imprintLink_xlink_href'), max_length=100, default=None, null=True)


class Apartment(CoreModel):
    class Meta:
        db_table = u'apartment'

    company = models.ForeignKey(
        Company,
        related_name='company_rent',
        on_delete=models.SET_NULL,
        null=True, blank=True
    )

    contact_form_type = models.CharField(_('contactFormType'),
                                         max_length=80
                                         )

    remove_creation = models.DateTimeField(null=True,
                                           blank=True
                                           )

    remove_id = models.PositiveIntegerField(_('id'),
                                            null=True,
                                            blank=True,
                                            default=0,
                                            unique=False
                                            )

    remove_modification = models.DateTimeField(null=True,
                                               blank=True
                                               )

    remove_publishDate = models.DateTimeField(null=True,
                                              blank=True
                                              )

    xlink_href = models.CharField(_('xlink_href'),
                                  max_length=280,
                                  default=None
                                  )

    adLinkForJSONP_xlink_href = models.TextField(_('adLinkForJSONP_xlink_href'),
                                                 default=None
                                                 )

    adLinkForXMLData_xlink_href = models.TextField(_('adLinkForXMLData_xlink_href'),
                                                   default=None
                                                   )

    def save(self, *args, **kwargs):
        super(Apartment, self).save(*args, **kwargs)
        return self.id


class RealEstate(CoreModel):
    class Meta:
        db_table = u'real_estate'
    apartment = models.ForeignKey(
        Apartment,
        related_name='company_rent_apart',
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    realEstate_id = models.PositiveIntegerField(_('id'),
                                                null=True,
                                                blank=True,
                                                default=0,
                                                unique=False
                                                )

    realEstate_xsi_type = models.CharField(_('realEstate_xsi_type'),
                                           max_length=50,
                                           default=0,
                                           null=True
                                           )

    realEstate_address_city = models.CharField(_('realEstate_address_city'),
                                               max_length=50,
                                               default=None,
                                               null=True
                                               )

    realEstate_address_geoHierarchy_city_fullGeoCodeId = models.CharField(_('realEstate_address_geoHierarchy_city_fullGeoCodeId'),
                                                                          max_length=50,
                                                                          default=None,
                                                                          null=True
                                                                          )

    realEstate_address_geoHierarchy_city_geoCodeId = models.CharField(_('realEstate_address_geoHierarchy_city_geoCodeId'),
                                                                      max_length=50,
                                                                      default=None,
                                                                      null=True
                                                                      )

    realEstate_address_geoHierarchy_city_name = models.CharField(_('realEstate_address_geoHierarchy_city_name'),
                                                                 max_length=150,
                                                                 default=None,
                                                                 null=True
                                                                 )

    realEstate_address_geoHierarchy_continent_fullGeoCodeId = models.CharField(_('realEstate_address_geoHierarchy_continent_fullGeoCodeId'),
                                                                               max_length=150,
                                                                               default=None,
                                                                               null=True
                                                                               )

    realEstate_address_geoHierarchy_continent_geoCodeId =  models.CharField(_('realEstate_address_geoHierarchy_continent_geoCodeId'),
                                                                            max_length=150,
                                                                            default=None,
                                                                            null=True
                                                                            )

    realEstate_address_geoHierarchy_country_name = models.CharField(_('realEstate_address_geoHierarchy_country_name'),
                                                                    max_length=150,
                                                                    default=None,
                                                                    null=True
                                                                    )

    realEstate_address_geoHierarchy_neighbourhood_geoCodeId = models.CharField(_('realEstate_address_geoHierarchy_neighbourhood_geoCodeId'),
                                                                               max_length=150,
                                                                               default=None,
                                                                               null=True
                                                                               )

    realEstate_address_geoHierarchy_quarter_fullGeoCodeId = models.CharField(_('realEstate_address_geoHierarchy_quarter_fullGeoCodeId'),
                                                                             max_length=150,
                                                                             default=None,
                                                                             null=True
                                                                             )

    realEstate_address_geoHierarchy_quarter_geoCodeId = models.CharField(_('realEstate_address_geoHierarchy_quarter_geoCodeId'),
                                                                         max_length=150,
                                                                         default=None,
                                                                         null=True
                                                                         )

    realEstate_address_geoHierarchy_region_geoCodeId = models.CharField(_('realEstate_address_geoHierarchy_region_geoCodeId'),
                                                                        max_length=150,
                                                                        default=None,
                                                                        null=True
                                                                        )

    realEstate_address_geoHierarchy_region_name = models.CharField(_('realEstate_address_geoHierarchy_region_name'),
                                                                   max_length=150,
                                                                   default=None,
                                                                   null=True
                                                                   )

    realEstate_address_postcode = models.CharField(_('realEstate_address_postcode'),
                                                   max_length=150,
                                                   default=None,
                                                   null=True
                                                   )

    realEstate_address_quarter = models.CharField(_('realEstate_address_quarter'),
                                                  max_length=150,
                                                  default=None,
                                                  null=True
                                                  )

    realEstate_apartmentType = models.CharField(_('realEstate_apartmentType'),
                                                max_length=150,
                                                default=None,
                                                null=True
                                                )

    realEstate_assistedLiving = models.CharField(_('realEstate_assistedLiving'),
                                                 max_length=150,
                                                 default=None,
                                                 null=True
                                                 )

    def save(self, *args, **kwargs):
        super(RealEstate, self).save(*args, **kwargs)
        return self.id


class RealEstateAttachments(CoreModel):
    class Meta:
        db_table = u'realestate_attachments'
    real_estate = models.ForeignKey(
        RealEstate,
        related_name='real_estate_attachments',
        on_delete=models.SET_NULL,
        null=True, blank=True
    )

    realEstate_attachments_xlink_href = models.CharField(_('realEstate_attachments_xlink_href'), max_length=150,
                                                         default=None)

    xsi_type = models.CharField(_('xsi_type'), max_length=150, default=None)

    xlink_href = models.CharField(_('xlink_href'), max_length=250, default=None)

    id_achments = models.CharField(_('id_achments'), max_length=250, default=None)

    modification = models.DateTimeField(null=True, blank=True)

    creation = models.DateTimeField(null=True, blank=True)

    publishDate = models.DateTimeField(null=True, blank=True)

    title = models.CharField(_('title'), max_length=250, default=None)

    floorplan = models.BooleanField(default=False)

    titlepicture = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super(RealEstateAttachments, self).save(*args, **kwargs)
        return self.id


class RealEstateNext(CoreModel):
    class Meta:
        db_table = u'realestate_attachments_next'
    real_estate = models.ForeignKey(
        RealEstate,
        related_name='real_estate_attachments_nxt',
        on_delete=models.SET_NULL,
        null=True, blank=True
    )

    realEstate_balcony = models.BooleanField(default=False, null=True)

    realEstate_baseRent = models.CharField(_('real_estate_baseRent'), max_length=250, default=None, null=True)

    realEstate_buildingEnergyRatingType = models.CharField(_('real_estate_building_energy_rating_type'),
                                                           max_length=250, default=None, null=True)

    realEstate_builtInKitchen = models.BooleanField(default=False, null=True)

    realEstate_calculatedTotalRent = models.CharField(_('real_estate_calculated_total_rent'),
                                                      max_length=250, default=None, null=True)

    realEstate_calculatedTotalRentScope = models.CharField(_('real_estate_calculated_total_rent_scope'),
                                                           max_length=250, default=None, null=True)

    realEstate_cellar = models.CharField(_('real_estate_cellar'), max_length=250, default=None, null=True)

    realEstate_certificateOfEligibilityNeeded = models.CharField(_('real_estate_certificate_of_eligibility_needed'),
                                                                 max_length=250, default=None, null=True)

    realEstate_condition = models.CharField(_('real_estate_condition'), max_length=250, default=None, null=True)

    realEstate_constructionYear = models.PositiveIntegerField(_('real_estate_construction_year'),
                                                              null=True, blank=True, default=0,
                                                              unique=False
                                                              )

    realEstate_courtage_hasCourtage = models.CharField(_('realEstate_courtage_hasCourtage'), max_length=250, default=None, null=True)

    realEstate_creationDate = models.DateTimeField(null=True, blank=True)

    realEstate_deposit = models.CharField(_('realEstate_deposit'), max_length=250, default=None, null=True)

    realEstate_descriptionNote = models.CharField(_('realEstate_descriptionNote'), max_length=2500, default=None, null=True)

    realEstate_energyCertificate_energyCertificateAvailability = models.CharField(_('realEstate_energyCertificate_energyCertificateAvailability'),
                                                                                  max_length=250, default=None, null=True)

    realEstate_energyCertificate_energyCertificateCreationDate = models.CharField(_('realEstate_energyCertificate_energyCertificateCreationDate'),
                                                                                  max_length=2250, default=None, null=True)

    realEstate_energyConsumptionContainsWarmWater = models.CharField(_('realEstate_energyConsumptionContainsWarmWater'),
                                                                     max_length=250, default=None, null=True)

    realEstate_energyPerformanceCertificate = models.BooleanField(default=False, null=True)

    realEstate_externalId = models.CharField(_('realEstate_energyConsumptionContainsWarmWater'),
                                             max_length=250, default=None, null=True)

    realEstate_floor = models.PositiveIntegerField(_('realEstate_floor'),
                                                   null=True, blank=True, default=0, unique=False)

    realEstate_floorplan = models.BooleanField(default=False, null=True)

    realEstate_freeFrom = models.CharField(_('realEstate_freeFrom'), max_length=250, default=None, null=True)

    realEstate_furnishingNote = models.CharField(_('realEstate_furnishingNote'), max_length=2250, default=None, null=True)

    realEstate_garden = models.BooleanField(default=False, null=True)

    realEstate_guestToilet = models.CharField(_('realEstate_guestToilet'), max_length=50, default=None, null=True)

    realEstate_handicappedAccessible = models.CharField(_('realEstate_handicappedAccessible'),
                                                        max_length=50, default=None, null=True)

    realEstate_heatingCosts = models.PositiveIntegerField(_('realEstate_heatingCosts'),
                                                          null=True, blank=True, default=0,
                                                          unique=False)

    realEstate_heatingCostsInServiceCharge = models.CharField(_('realEstate_heatingCostsInServiceCharge'),
                                                              max_length=50, default=None, null=True)

    realEstate_heatingType = models.CharField(_('realEstate_heatingType'), max_length=50, default=None, null=True)

    realEstate_heatingTypeEnev2014 = models.CharField(_('realEstate_heatingTypeEnev2014'),
                                                      max_length=50, default=None, null=True)

    realEstate_interiorQuality = models.CharField(_('realEstate_interiorQuality'),
                                                  max_length=50, default=None, null=True)

    realEstate_lastModificationDate = models.DateTimeField(null=True, blank=True)

    realEstate_lastRefurbishment = models.PositiveIntegerField(_('realEstate_lastRefurbishment'),
                                                               null=True, blank=True, default=0,
                                                               unique=False)

    realEstate_lift = models.BooleanField(default=False, null=True)

    realEstate_livingSpace = models.PositiveIntegerField(_('realEstate_livingSpace'),
                                                         null=True, blank=True, default=0,
                                                         unique=False)

    realEstate_locationNote = models.CharField(_('realEstate_locationNote'), max_length=2250, default=None, null=True)

    realEstate_numberOfFloors = models.IntegerField(_('realEstate_numberOfFloors'),
                                                    null=True, blank=True, default=0,
                                                    unique=False)

    realEstate_numberOfRooms = models.PositiveIntegerField(_('realEstate_numberOfRooms'),
                                                           null=True, blank=True, default=0,
                                                           unique=False)

    realEstate_otherNote = models.CharField(_('realEstate_otherNote'), max_length=2250, default=None, null=True)

    realEstate_petsAllowed = models.CharField(_('realEstate_petsAllowed'), max_length=50, default=None, null=True)

    realEstate_referencePriceApiCall = models.CharField(_('realEstate_referencePriceApiCall'),
                                                        max_length=1150, default=None, null=True)

    realEstate_referencePriceServiceCall = models.CharField(_('realEstate_referencePriceServiceCall'),
                                                            max_length=1150, default=None, null=True)

    realEstate_serviceCharge = models.IntegerField(_('realEstate_numberOfFloors'),
                                                   null=True, blank=True, default=0,
                                                   unique=False)

    realEstate_state = models.CharField(_('realEstate_referencePriceServiceCall'),
                                        max_length=1150, default=None, null=True)

    realEstate_thermalCharacteristic = models.CharField(_('realEstate_thermalCharacteristic'),
                                                        max_length=50, default=None, null=True)

    realEstate_title = models.CharField(_('realEstate_thermalCharacteristic'), max_length=250, default=None, null=True)

    realEstate_titlePicture_creation = models.DateTimeField(null=True, blank=True)

    realEstate_titlePicture_id = models.IntegerField(_('realEstate_numberOfFloors'),
                                                     null=True, blank=True, default=0,
                                                     unique=False)

    realEstate_titlePicture_modification = models.DateTimeField(null=True, blank=True)

    realEstate_titlePicture_publishDate = models.DateTimeField(null=True, blank=True)

    realEstate_titlePicture_floorplan = models.BooleanField(default=False, null=True)

    realEstate_titlePicture_title = models.CharField(_('realEstate_titlePicture_title'), max_length=250, default=None)

    realEstate_titlePicture_titlePicture = models.BooleanField(default=False)

    realEstate_totalRent = models.CharField(_('realEstate_totalRent'), max_length=250, default=None)

    realEstate_useAsFlatshareRoom = models.CharField(_('realEstate_useAsFlatshareRoom'), max_length=250, default=None)

    realtorValuationJSONLink_xlink_href = models.CharField(_('realtorValuationJSONLink_xlink_href'),
                                                           max_length=550, default=None)

    realtorValuationV2JSONLink_xlink_href = models.CharField(_('realtorValuationJSONLink_xlink_href'),
                                                             max_length=550, default=None)

    realtorValuationV2JSONPLink_xlink_href = models.CharField(_('realtorValuationV2JSONPLink_xlink_href'),
                                                              max_length=550, default=None)


class Url(CoreModel):
    class Meta:
        db_table = u'url'
    realestate = models.ForeignKey(
        RealEstate,
        related_name='real_url',
        on_delete=models.SET_NULL,
        null=True, blank=True
    )

    scale = models.CharField(_('scale'), max_length=250, default=None)

    href = models.CharField(_('href'), max_length=250, default=None)


class RealEstateTitlePictureUrls(CoreModel):
    class Meta:
        db_table = u'RealEstateTitlePictureUrls'
    real_estate_attachments = models.ForeignKey(
        RealEstateAttachments,
        related_name='Real_EstateTitlePictureUrls',
        on_delete=models.SET_NULL,
        null=True, blank=True
    )

    scale = models.CharField(_('scale'), max_length=250, default=None)

    href = models.CharField(_('href'), max_length=250, default=None)


