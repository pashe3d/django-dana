from django.db.models.signals import post_save
from django.dispatch import receiver

from purchase.models import Payment
import requests

token = ""


# noinspection PyUnusedLocal
@receiver(post_save, sender=Payment)
def save_user_in_crm(sender, instance, **kwargs):
    user = instance.order.user

    if instance.type_id == Payment.Type.FREE:
        post_data = {
            "Subject": "سرنخ نمونه: علاقه مند به خرید خودرو کوییک",
            "FullName": "آقای مهندس پرویز علی بیگی",
            "FullName_FirstName": "پرویز",
            "FullName_LastName": "علی بیگی",
            "FullName_NamePrefix": "33203127-ABB1-420D-9F3E-628D6A896C92",
            "TemplateAttributeId": "4a8a117d-1d66-4d99-ae70-be809973188b",
            "ITStaffID": "11111111-1111-1111-1111-111111111111",
            "CompanyName": "شرکت  پرویزی",
            "JobTitle": "کارمند",
            "MobilePhone": "091212345678",
            "Telephone": "091212345678",
            "Email": "beigi@email.ir",
            "WebSiteUrl": "www.beigi.ir",
            "Address": "تهران تهران فلکه دوم صادقیه، ابتدای آیت الله کاشانی، خیابان بوستان یکم، پلاک 6، طبقه پنجم، واحد 17. 1471676833",
            "Address_ProvinceId": "11111111-1111-1111-1111-111111111111",
            "Address_CityId": "11111111-1111-1111-1111-111111111111",
            "Address_PostalCode": "1471676833",
            "Address_Street": "فلکه دوم صادقیه، ابتدای آیت الله کاشانی، خیابان بوستان یکم، پلاک 6، طبقه پنجم، واحد 17",
            "LeadSourceCode": "A93D0B8B-33FE-49FF-8015-FCAD0C781565",
            "StatusCode": None,
            "CampaignId": None,
            "StateCode": None,
            "IndustryCode": None,
            "PersonnelCount": None,
            "ContactId": None,
            "OpportunityId": None,
            "AccountId": None

        }
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer ' + token}

        response = requests.post('https://melkemun.danaabr.com/api/v1/CRM_Lead', json=post_data, headers=headers)
        content = response.content
        content2 = content

    if instance.type_id == Payment.Type.ONLINE:
        post_data = {
            "FirstName": "-",
            "LastName": user.name,
            "FullName": user.name,
            "PersonalCode": "",
            "Email": "",
            "Tel": "",
            "TelExt": "",
            "MobilePhone": user.phone,
            "Address": "",
            "Description": "",
            "PositionId": "",
            "PS": "1234",
            "RepPS": "1234",
            "IPAddress": "",
            "CheangePasswordAtNextLogin": False,
            "CannotChangePassword": False,
            "PasswordNeverExpires": False,
            "DepartmentID": "22222222-2222-2222-2222-222222222222",
            "DomainId": "00000000-0000-0000-0000-000000000000",
            "UserType": 1,
            "UN": user.phone,
            "AvatarPath": "",
            "IsActiveDirectory": False,
            "IsLockedOut": False,
            "IsActive": False,
            "HasAccessToUserGroupRequests": False,
            "HasAccessToCompanyRequests": False,
            "HasAccessToDepartmentRequests": False,
            "HasAccessToItsDepartmentAndSubDepartments": False,
            "HasAccessToUserAssetDepartment": False,
            "HasAccessToUserAssetCompany": False,
            "EnableNotification": 7,
            "SendInvitationEmail": False
        }
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer ' + token}

        response = requests.post('https://melkemun.danaabr.com/api/v1/users/add/user', json=post_data, headers=headers)
        content = response.content
        content2 = content
