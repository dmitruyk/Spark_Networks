from ..core.core import CoreModel
from django.db import models

from django.utils.translation import ugettext_lazy as _


class Company(CoreModel):
    class Meta:
        db_table = u'company'

    companyWideCustomerId = models.CharField(_('companyWideCustomerId'), max_length=80, default=None)

    contactDetails_id = models.PositiveIntegerField(_('contactDetails_id'), null=True, blank=True, default=0, \
                                                    unique=False)

    contactDetails_address_city = models.CharField(_('contactDetails_address_city'), max_length=80, default=None)

    contactDetails_address_houseNumber = models.PositiveIntegerField(_('contactDetails_id'),\
                                                                     null=True, blank=True, default=0,\
                                                                     unique=False)
    contactDetails_address_postcode = models.PositiveIntegerField(_('contactDetails_address_postcode'),\
                                                                     null=True, blank=True, default=0,\
                                                                     unique=False)
    contactDetails_address_street = models.CharField(_('contactDetails_address_street'), max_length=180, default=None)

    contactDetails_cellPhoneNumber = models.CharField(_('contactDetails_cellPhoneNumber'), max_length=180, default=None)

    contactDetails_cellPhoneNumberAreaCode = models.PositiveIntegerField(_('contactDetails_address_postcode'),\
                                                                     null=True, blank=True, default=0,\
                                                                     unique=False)
    contactDetails_cellPhoneNumberCountryCode = models.CharField(_('contactDetails_cellPhoneNumber'), max_length=10, default=None)

    contactDetails_cellPhoneNumberSubscribe = models.CharField(_('contactDetails_cellPhoneNumber'), max_length=20, default=None)

    contactDetails_company = models.CharField(_('contactDetails_cellPhoneNumber'), max_length=180, default=None)

    contactDetails_countryCode = models.CharField(_('contactDetails_cellPhoneNumber'), max_length=10, default=None)

    contactDetails_email = models.CharField(_('contactDetails_email'), max_length=50, default=None)

    contactDetails_faxNumber = models.CharField(_('contactDetails_faxNumber'), max_length=50, default=None)

    contactDetails_faxNumberAreaCode = models.CharField(_('contactDetails_faxNumberAreaCode'), max_length=10, default=None)

    contactDetails_faxNumberCountryCode = models.CharField(_('contactDetails_faxNumberCountryCode'), max_length=10, default=None)

    contactDetails_faxNumberSubscriber = models.CharField(_('contactDetails_faxNumberSubscriber'), max_length=10, default=None)

    contactDetails_firstname = models.CharField(_('contactDetails_firstname'), max_length=30, default=None)

    contactDetails_homepageUrl = models.CharField(_('contactDetails_homepageUrl'), max_length=150, default=None)

    contactDetails_lastname = models.CharField(_('contactDetails_lastname'), max_length=30, default=None)

    contactDetails_phoneNumber = models.CharField(_('contactDetails_phoneNumber'), max_length=50, default=None)

    contactDetails_phoneNumberAreaCode = models.CharField(_('contactDetails_phoneNumberAreaCode'), max_length=50, default=None)

    contactDetails_phoneNumberCountryCode = models.CharField(_('contactDetails_phoneNumberCountryCode'), max_length=10, default=None)

    contactDetails_phoneNumberSubscriber = models.CharField(_('contactDetails_phoneNumberSubscriber'), max_length=20, default=None)

    contactDetails_salutation = models.CharField(_('contactDetails_salutation'), max_length=10, default=None)

    contactFormConfiguration_addressField = models.CharField(_('contactFormConfiguration_addressField'), max_length=10, default=None)

    contactFormConfiguration_applicationPackageCompletedField = models.CharField(_('contactFormConfiguration_applicationPackageCompletedField'), max_length=10, default=None)

    contactFormConfiguration_emailAddressField = models.CharField(_('contactFormConfiguration_emailAddressField'), max_length=10, default=None)

    contactFormConfiguration_employmentRelationshipField = models.CharField(_('contactFormConfiguration_employmentRelationshipField'), max_length=10, default=None)

    contactFormConfiguration_firstnameField = models.CharField(_('contactFormConfiguration_firstnameField'), max_length=10, default=None)

    contactFormConfiguration_freemiumSettings_duratio = models.PositiveIntegerField(default=0)

    contactFormConfiguration_incomeField = models.CharField(_('contactFormConfiguration_incomeField'), max_length=10, default=None)

    contactFormConfiguration_lastnameField = models.CharField(_('contactFormConfiguration_lastnameField'), max_length=10, default=None)

    contactFormConfiguration_messageField = models.CharField(_('contactFormConfiguration_messageField'), max_length=40, default=None)

    contactFormConfiguration_moveInDateField = models.CharField(_('contactFormConfiguration_moveInDateField'), max_length=40, default=None)

    contactFormConfiguration_numberOfPersonsField = models.CharField(_('contactFormConfiguration_numberOfPersonsField'), max_length=40, default=None)

    contactFormConfiguration_petsInHouseholdField = models.CharField(_('contactFormConfiguration_petsInHouseholdField'), max_length=40, default=None)

    contactFormConfiguration_phoneNumberField = models.CharField(_('contactFormConfiguration_phoneNumberField'), max_length=40, default=None)

    contactFormConfiguration_premiumProfileRequired = models.CharField(_('contactFormConfiguration_premiumProfileRequired'), max_length=40, default=None)

    contactFormConfiguration_salutationField = models.CharField(_('contactFormConfiguration_salutationField'), max_length=40, default=None)


class ImprintLink(CoreModel):
    class Meta:
        db_table = u'imprintLink'

    company = models.ForeignKey(
        Company,
        related_name='imprintLink_xlink_href',
        on_delete=models.SET_NULL,
        null=True, blank=True
    )

    imprintLink_xlink_href = models.CharField(_('imprintLink_xlink_href'), max_length=100, default=None)


class Apartment(CoreModel):
    class Meta:
        db_table = u'apartment'

    company = models.ForeignKey(
        Company,
        related_name='company_rent',
        on_delete=models.SET_NULL,
        null=True, blank=True
    )

    contact_form_type = models.CharField(_('contactFormType'), max_length=80)

    remove_id = models.PositiveIntegerField(_('id'), null=True, blank=True, default=0, unique=False)

    remove_modification = models.DateTimeField(null=True, blank=True)

    remove_publishDate = models.DateTimeField(null=True, blank=True)

    xlink_href = models.CharField(_('xlink_href'), max_length=280, default=None)

    adLinkForJSONP_xlink_href = models.TextField(_('adLinkForJSONP_xlink_href'), default=None)

    adLinkForXMLData_xlink_href = models.TextField(_('adLinkForXMLData_xlink_href'), default=None)


class RealEstate(CoreModel):
    class Meta:
        db_table = u'real_estate'
    apartment = models.ForeignKey(
        Apartment,
        related_name='company_rent',
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    realEstate_id = models.PositiveIntegerField(_('id'), null=True, blank=True, default=0, unique=True)

    realEstate_xsi_type = models.CharField(_('realEstate_xsi_type'), max_length=50, default=None)

    realEstate_address_city = models.CharField(_('realEstate_address_city'), max_length=50, default=None)

    realEstate_address_geoHierarchy_city_fullGeoCodeId = models.PositiveIntegerField(_('realEstate_address_geoHierarchy_city_fullGeoCodeId'), null=True, blank=True, default=0, unique=False)

    realEstate_address_geoHierarchy_city_geoCodeId = models.PositiveIntegerField(_('realEstate_address_geoHierarchy_city_geoCodeId'), null=True, blank=True, default=0, unique=False)

    realEstate_address_geoHierarchy_city_name = models.CharField(_('realEstate_address_geoHierarchy_city_name'), max_length=150, default=None)

    realEstate_address_geoHierarchy_continent_fullGeoCodeId = models.CharField(_('realEstate_address_geoHierarchy_country_name'), max_length=150, default=None),

    realEstate_address_geoHierarchy_continent_geoCodeId = models.PositiveIntegerField(_('realEstate_address_geoHierarchy_continent_geoCodeId'), null=True, blank=True, default=0, unique=False),

    realEstate_address_geoHierarchy_country_name = models.CharField(_('realEstate_address_geoHierarchy_country_name'), max_length=150, default=None)

    realEstate_address_geoHierarchy_neighbourhood_geoCodeId = models.PositiveIntegerField(_('realEstate_address_geoHierarchy_neighbourhood_geoCodeId'), null=True, blank=True, default=0, unique=False),

    realEstate_address_geoHierarchy_quarter_fullGeoCodeId = models.CharField(_('realEstate_address_geoHierarchy_quarter_fullGeoCodeId'), max_length=150, default=None)

    realEstate_address_geoHierarchy_quarter_geoCodeId = models.PositiveIntegerField(_('realEstate_address_geoHierarchy_quarter_geoCodeId'), null=True, blank=True, default=0, unique=False),

    realEstate_address_geoHierarchy_region_geoCodeId = models.PositiveIntegerField(_('realEstate_address_geoHierarchy_quarter_geoCodeId'), null=True, blank=True, default=0, unique=False),

    realEstate_address_geoHierarchy_region_name = models.CharField(_('realEstate_address_geoHierarchy_region_name'), max_length=150, default=None)

    realEstate_address_postcode = models.CharField(_('realEstate_address_postcode'), max_length=150, default=None)

    realEstate_address_quarter = models.CharField(_('realEstate_address_quarter'), max_length=150, default=None),

    realEstate_apartmentType = models.CharField(_('realEstate_address_quarter'), max_length=150, default=None),

    realEstate_assistedLiving = models.CharField(_('realEstate_address_quarter'), max_length=150, default=None),

