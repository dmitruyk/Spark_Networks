from ...models.general import *
from ...core.output.abstract_view_model import AbstractViewModel
from django.db.models import Sum, Case, When, IntegerField, Avg, F, Count


import datetime


class RentFullViewModel(AbstractViewModel):
    def __init__(self, company):
        self.company = Company.objects.filter(id=company.id).first()
        self.apartment = Apartment.objects.filter(company=company).first()
        self.imprintlink = ImprintLink.objects.filter(company=company).first()
        self.real_estate = RealEstate.objects.filter(apartment=self.apartment).first()
        self.real_estate_attachments = RealEstateAttachments.objects.filter(real_estate=self.real_estate).all()
        self.real_estate_next = RealEstateNext.objects.filter(real_estate=self.real_estate).first()

    def output(self):
        response = {}
        global_response = {}

        global_response['ok'] = True
        if self.company is not None:
            response['contactFormType'] = None if not self.apartment.contact_form_type else self.apartment.contact_form_type
            response['creation'] = None if not self.apartment.remove_creation else self.apartment.remove_creation
            response['id'] = None if not self.apartment.remove_id else str(self.apartment.remove_id)
            response['modification'] = None if not self.apartment.remove_modification else self.apartment.remove_modification
            response['publishDate'] = None if not self.apartment.remove_publishDate else self.apartment.remove_publishDate
            response['xlink_href'] = None if not self.apartment.xlink_href else self.apartment.xlink_href
            response['adLinkForJSONP_xlink_href'] = None if not self.apartment.adLinkForJSONP_xlink_href else self.apartment.adLinkForJSONP_xlink_href
            response['adLinkForXMLData_xlink_href'] = None if not self.apartment.adLinkForXMLData_xlink_href else self.apartment.adLinkForXMLData_xlink_href

            if self.company:
                real_estate_first = {field.name:getattr(self.company, field.name) for field in self.company._meta.fields}
                real_estate_first.pop('id')
                real_estate_first.pop('created')
                real_estate_first.pop('updated')
                response.update(real_estate_first)

            response['imprintLink_xlink_href'] = None if not self.imprintlink.imprintLink_xlink_href else self.imprintlink.imprintLink_xlink_href

            global_real_estate_attachments = {field.name:getattr(self.real_estate, field.name) for field in self.real_estate._meta.fields}
            global_real_estate_attachments.pop('id')
            global_real_estate_attachments.pop('created')
            global_real_estate_attachments.pop('updated')
            global_real_estate_attachments.pop('apartment')
            response.update(global_real_estate_attachments)

            p = {}
            at = []
            print(self.real_estate_attachments)
            for attach in self.real_estate_attachments:
                res = {}
                res['@xsi.type'] = attach.xsi_type
                res['@xlink.href'] = attach.xlink_href
                res['@id'] = attach.id_achments
                res['@modification'] = attach.modification
                res['@creation'] = attach.creation
                res['@publishDate'] = attach.publishDate
                res['title'] = attach.title
                res['floorplan'] = attach.floorplan
                res['titlePicture'] = attach.titlepicture

                real_estate_picture_urls = RealEstateTitlePictureUrls.objects.filter(real_estate_attachments=attach).all()
                pict = []
                for pic in real_estate_picture_urls:
                                p['@scale'] = pic.scale
                                p['@href'] = pic.href
                                pict.append(p)

                res['urls'] = [{'url': pict}]
                at.append(res)

#
            response['realEstate_attachments'] = {'@xlink.href': None if self.real_estate_attachments[0].realEstate_attachments_xlink_href is None
                                                    else self.real_estate_attachments[0].realEstate_attachments_xlink_href,
                                                  'attachment' : at,
                                                 }

            if self.real_estate_next:
                real_estate_next = {field.name: getattr(self.real_estate_next, field.name) for field in
                                    self.real_estate_next._meta.fields}

                real_estate_next.pop('id')
                real_estate_next.pop('created')
                real_estate_next.pop('updated')
                real_estate_next.pop('real_estate')

                response.update(real_estate_next)

            real_estate_title_picture_urls = Url.objects.filter(realestate=self.real_estate).all()
            pic_main = []
            for pic in real_estate_title_picture_urls:
                pic_second = {}
                pic_second['@scale'] = pic.scale
                pic_second['@href'] = pic.href
                pic_main.append(pic_second)

            buffer = []
            buffer.append({'url': pic_main})

            response.update({'realEstate_titlePicture_urls': buffer})
            today = datetime.date.today()
            response['today'] = today

        else:
            global_response['ok'] = False

        global_response['data'] = response
        return global_response
